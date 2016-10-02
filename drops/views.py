from django.shortcuts import render
from gear.models import Item
from heroes.models import Hero, Rarity
from gear.views import processItems
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
	)
	raw_items = Item.objects.all().prefetch_related('recipe__ingredients')
	master_items = {}
	for item in raw_items:
		master_items[item.id] = item
	items = {}
	for hero in heroes:
		for rarity in hero.rarities.all():
			label = str(hero.id) + '_' + str(rarity.id)
			for i in range(1,7):
				items[label + '_' + str(i)] = {}
				item_id = getattr(rarity, 'gear' + str(i)).id
				processItems(master_items[item_id], items[label + '_' + str(i)], 1, master_items)
	next_step = ''
	ingredients = ''
	drops = ''
	if('' != ingredients_raw):
		sets = ingredients_raw.split('_')
		ingredients = []
		for pair in sets:
			values = pair.split(':');
			ingredients.append({ 'item' : int(values[0]), 'quantity' : int(values[1]) });

		# THIS IS WHERE YOUR CODE GOES -- INSIDE THIS IF STATEMENT
		# THIS IS CURRENTLY TEMPORARY CODE

		ingredients = sorted(ingredients, key=lambda k: k['quantity'], reverse=True)
		drops_raw = Drop.objects.filter(item = ingredients[0]['item']);
		drops_processed = []
		for drop in drops_raw.all():
			drops_processed.append(drop)
		if 1 != len(drops_processed):
			for ingredient in ingredients[1:]:
				drops_new = []
				for drop in drops_processed:
					for item in drop.stage.drops.all():
						if item.item.id == ingredient['item']:
							drops_new.append(drop)
							break
				if 0 < len(drops_new):
					drops_processed = copy.deepcopy(drops_new)
					if 1 == len(drops_new):
						break
		stage = drops_processed[0].stage
		scraps = []
		drop_items = {}
		for drop in stage.drops.all():
			drop_items[drop.item.id] = drop.item
		for ingredient in ingredients:
			if ingredient['item'] in drop_items:
				scraps.append({'item' : drop_items[ingredient['item']], 'quantity' : ingredient['quantity']})

		# THIS IS THE END OF THE TEMPORARY CODE

		next_step = {
			'stage' : stage,
			'scraps' : scraps
		}
	context = {
		'heroes' : heroes,
		'items' : items,
		'next' : next_step,
	}
	return render(request, 'drops/index.html', context)
