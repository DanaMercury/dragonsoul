from django.shortcuts import render
from gear.models import Item
from heroes.models import Hero, Rarity
from .models import Drop
import copy

def index(request, ingredients_raw = ''):
	heroes = Hero.objects.all().prefetch_related(
		'rarities__gear1',
		'rarities__gear2',
		'rarities__gear3',
		'rarities__gear4',
		'rarities__gear5',
		'rarities__gear6',
		'quests'
	)
	next_step = ''
	ingredients = ''
	drops = ''
	if('' != ingredients_raw):
		sets = ingredients_raw.split('_')
		ingredients = []
		for pair in sets:
			values = pair.split(':');
			ingredients.append({ 'item' : int(values[0]), 'quantity' : int(values[1]) });
		ingredients = sorted(ingredients, key=lambda k: k['quantity'], reverse=True)
		drops = Drop.objects.filter(item = ingredients[0]['item']).order_by('-id')
		if 1 != len(drops):
			for ingredient in ingredients[1:]:
				drops_new = []
				for drop in drops:
					for item in drop.stage.drops.all():
						if item.item.id == ingredient['item']:
							drops_new.append(drop)
							break
				if 0 < len(drops_new):
					drops = copy.deepcopy(drops_new)
					if 1 == len(drops_new):
						break
		stage = drops[0].stage
		scraps = []
		drop_items = {}
		for drop in stage.drops.all():
			drop_items[drop.item.id] = drop.item
		for ingredient in ingredients:
			if ingredient['item'] in drop_items:
				scraps.append({'item' : drop_items[ingredient['item']], 'quantity' : ingredient['quantity']})
		next_step = {
			'stage' : stage,
			'scraps' : scraps
		}
	context = {
		'heroes' : heroes,
		'next' : next_step,
	}
	return render(request, 'drops/index.html', context)
