from django.shortcuts import render
from gear.models import Item
from heroes.models import Hero, Rarity
from .models import Drop, Chapter, Stage
import copy
import json
import urllib

def index(request, max_chapter = 0, ingredients_raw = '', candidates_raw = ''):
	chapters = Chapter.objects.all().order_by('-number')
	heroes = Hero.objects.all().prefetch_related(
		'rarities__gear1',
		'rarities__gear2',
		'rarities__gear3',
		'rarities__gear4',
		'rarities__gear5',
		'rarities__gear6',
		'quests'
	)
	next_steps = ''
	failed = False
	ingredients = ''
	candidates = ''
	drops = ''
	if('' != ingredients_raw and '' != candidates_raw):
		sets = ingredients_raw.split('_')
		ingredients = {}
		for pair in sets:
			values = pair.split(':');
			ingredients[values[0]] = { 'item_id' : int(values[0]), 'quantity' : int(values[1]) }
		sets = candidates_raw.split('#')
		candidates = []
		for pair in sets:
			values = pair.split(':');
			candidates.append({ 'hero' : Hero.objects.filter(id=int(values[0])), 'item' : Item.objects.filter(id=int(values[1])), 'unique_id' : values[2] })
		json_data = urllib.request.urlopen('http://dragonsoul.s3.amazonaws.com/items.json').read()
		items = json.loads(json_data.decode('utf-8').replace('items = ', '').replace(';', ''))
		winners = copy.deepcopy(candidates)
		if 1 != len(winners):
			new_winners = {}
			most = 0
			for candidate in winners:
				points = 0
				for stat in candidate.item.stats:
					if stat.id == candidate.hero.primary:
						points = points + 4
					else:
						for recc in candidate.hero.stat_users:
							if stat.id == recc.stat.id:
								if True == recc.recommended:
									points = points + 3
								elif True == recc.stat.primary:
									points = points + 2
								else:
									points = points + 1
								break
						if points not in new_winners:
							new_winners[points] = []
						new_winners[points].append(candidate)
						if points > most:
							most = points
						break
			winners = copy.deepcopy(new_winners[most])
			if 1 != len(winners):
				new_winners = {}
				most = 0
				for candidate in winners:
					points = 0
					for stat in candidate.item.stats:
						if stat.id == candidate.hero.primary:
							points = points + (4 * stat.quantity)
						else:
							for recc in candidate.hero.stat_users:
								if stat.id == recc.stat.id:
									if True == recc.recommended:
										points = points + (3 * stat.quantity)
									elif True == recc.stat.primary:
										points = points + (2 * stat.quantity)
									else:
										points = points + (1 * stat.quantity)
									break
							if points not in new_winners:
								new_winners[points] = []
							new_winners[points].append(candidate)
							if points > most:
								most = points
							break
				winners = copy.deepcopy(new_winners[most])
				if 1 != len(winners):
					new_winners = {}
					least = 9999999999999999
					for candidate in winners:
						count = 0
						item = items[candidate.unique_id]
						for scrap in item:
							count = count + scrap.total
						if count not in new_winners:
							new_winners[count] = []
						new_winners[count].append(candidate)
						if count < least:
							least = count
					winners = copy.deepcopy(new_winners[least])
		winner = winners[0]	
		covered = []
		needed = items[winner['unique_id']]
		needed_ids = list(needed.keys())
		stages = []
		for item_id in needed_ids:
			if item_id not in covered and ingredients[item_id]['quantity'] < needed[item_id]['total']:
				drops = Drop.objects.filter(item = item_id).filter(stage__chapter__id__lte = max_chapter).order_by('-id').prefetch_related('stage__drops')
				if 0 < len(drops):
					if 1 != len(drops):
						for ingredient in ingredients:
							drops_new = []
							for drop in drops:
								for dropped_item in drop.stage.drops.all():
									if dropped_item.item.id == int(ingredient):
										drops_new.append(drop)
										break
							if 0 < len(drops_new):
								drops = copy.deepcopy(drops_new)
								if 1 == len(drops_new):
									break
					stage = drops[0].stage
					if drops[0].stage.id not in stages:
						stages.append(stage.id)
					for drop in stage.drops.all():
						if drop.item.id in needed_ids and drop.item.id not in covered:
							covered.append(drop.item.id)
				else:
					failed = True
		if 0 < len(stages):
			next_steps = {'hero' : winner['hero'], 'item' : winner['item'], 'stages' : []}
			covered = []
			for stage in stages:
				scraps = []
				stage = Stage.objects.filter(id=stage).prefetch_related('drops')
				for drop in stage.drops.all():
					if drop.item.id in needed_ids and drop.item.id not in covered:
						covered.append(drop.item.id)
						quantity = needed[drop.item.id]['total'] - ingredients[drop.item.id].quantity
						if 0 < quantity:
							scraps.append({'item' : drop.item, 'quantity' : quantity})
				next_steps.stages.append({'stage' : stage, 'scraps' : scraps})
		else:
			failed = True
	context = {
		'heroes' : heroes,
		'next' : next_steps,
		'chapters' : chapters,
		'failed' : failed
	}
	return render(request, 'drops/index.html', context)
