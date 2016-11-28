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
	needed_ids = ''
	ingredient_ids = ''
	debug = ''
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
			ingredients[values[0]] = { 'item_id' : int(values[0]), 'needed' : int(values[1]), 'quantity' : int(values[2]) }
		sets = candidates_raw.split('__')
		candidates = []
		for pair in sets:
			values = pair.split(':');
			candidates.append({ 'hero' : Hero.objects.get(id=int(values[0])), 'item' : Item.objects.get(id=int(values[1])), 'unique_id' : values[2] })
		json_data = urllib.request.urlopen('http://dragonsoul.s3.amazonaws.com/items.json').read()
		items = json.loads(json_data.decode('utf-8').replace('items = ', '').replace(';', ''))
		winners = copy.deepcopy(candidates)
		if 1 != len(winners):
			new_winners = {}
			most = 0
			for candidate in winners:
				points = 0
				for stat in candidate['item'].stats.all():
					if stat.stat.id == candidate['hero'].primary.id:
						points = points + 4
					else:
						litmus = False
						for recc in candidate['hero'].stat_users.all():
							if stat.stat.id == recc.stat.id:
								litmus = True
								if True == recc.recommended:
									points = points + 3
								elif False == recc.stat.primary:
									points = points + 1
								break
						if False == litmus:
							if True == stat.stat.primary:
								points = points + 2
							elif True == stat.stat.all_benefit:
								points = points + 1
				if points not in new_winners:
					new_winners[points] = []
				new_winners[points].append(candidate)
				if points > most:
					most = points
			winners = copy.deepcopy(new_winners[most])
			if 1 != len(winners):
				new_winners = {}
				most = 0
				for candidate in winners:
					points = 0
					for stat in candidate['item'].stats.all():
						if stat.stat.id == candidate['hero'].primary.id:
							points = points + (4 * stat.quantity)
						else:
							litmus = False
							for recc in candidate['hero'].stat_users.all():
								if stat.stat.id == recc.stat.id:
									litmus = True
									if True == recc.recommended:
										points = points + (3 * stat.quantity)
									elif False == recc.stat.primary:
										points = points + (1 * stat.quantity)
									break
							if False == litmus:
								if True == stat.stat.primary:
									points = points + (2 * stat.quantity)
								elif True == stat.stat.all_benefit:
									points = points + (1 * stat.quantity)
					if points not in new_winners:
						new_winners[points] = []
					new_winners[points].append(candidate)
					if points > most:
						most = points
				winners = copy.deepcopy(new_winners[most])
				if 1 != len(winners):
					new_winners = {}
					least = 9999999999999999
					for candidate in winners:
						count = 0
						item = items[candidate['unique_id']]
						for scrap in item:
							count = count + item[scrap]['total']
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
		ingredient_ids = list(ingredients.keys())
		stages = []
		debug = []
		for item_id in needed_ids:
			debug.append({'covered' : covered, 'have' : ingredients[item_id]['quantity'], 'needed' : needed[item_id]['total'] })
			stage_options = {}
			most = 0
			if item_id not in covered and ingredients[item_id]['quantity'] < needed[item_id]['total']:
				points = 0
				drops = Drop.objects.filter(item = item_id).filter(stage__chapter__id__lte = max_chapter).order_by('-stage__id').prefetch_related('stage__drops')
				debug.append({'length' : len(drops), 'drops' : drops})
				if 0 < len(drops):
					points = 100
					debug.append({'looping' : True})
					if 1 != len(drops):
						for drop in drops:
							points = 100
							for dropped_item in drop.stage.drops.all():
								debug.append({'item' : dropped_item.item.id});
								if str(dropped_item.item.id) in needed_ids and 0 < ingredients[str(dropped_item.item.id)]['needed']:
									debug.append({'match' : 'needed'})
									points = points + 10
								elif str(dropped_item.item.id) in ingredient_ids and 0 < ingredients[str(dropped_item.item.id)]['needed']:
									debug.append({'match' : 'ingredients'})
									points = points + 1
							debug.append({'points' : points})
							if 1 < points:
								if points not in stage_options:
									stage_options[points] = []
								stage_options[points].append(drop.stage.id)
							if points > most:
								most = points
					debug.append({'stage_options' : stage_options})
					stage = stage_options[most][0]
					if stage not in stages:
						stages.append(stage)
						stage = Stage.objects.get(id=stage)
						for drop in stage.drops.all():
							if str(drop.item.id) in needed_ids and drop.item.id not in covered:
								covered.append(drop.item.id)
				else:
					failed = True
		next_steps = {'hero' : winner['hero'], 'item' : winner['item'], 'stages' : []}
		if 0 < len(stages):
			covered = []
			for stage in stages:
				scraps = []
				stage = Stage.objects.get(id=stage)
				for drop in stage.drops.all():
					if str(drop.item.id) in needed_ids and drop.item.id not in covered:
						covered.append(drop.item.id)
						quantity = needed[str(drop.item.id)]['total'] - ingredients[str(drop.item.id)]['quantity']
						if 0 < quantity:
							scraps.append({'item' : drop.item, 'quantity' : quantity})
				next_steps['stages'].append({'stage' : stage, 'scraps' : scraps})
		else:
			failed = True
	context = {
		'heroes' : heroes,
		'next' : next_steps,
		'chapters' : chapters,
		'failed' : failed,
		'needed_ids' : needed_ids,
		'ingredient_ids' : ingredient_ids,
		'debug' : debug,
	}
	return render(request, 'drops/index.html', context)
