from django.shortcuts import render
from gear.models import Item
from heroes.models import Hero, Rarity
from gear.views import processItems
from .models import Stage

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
	if('' != ingredients_raw):
		sets = ingredients_raw.split('_')
		ingredients = []
		for pair in sets:
			values = pair.split(':');
			ingredients.append({ 'item' : values[0], 'quantity' : values[1] });

		# THIS IS WHERE YOU CODE GOES -- INSIDE THIS IF STATEMENT




		# FAKE DATA
		next_step = {
			'stage' : Stage.objects.get(id = 1),
			'scraps' : [{
				'item' : Item.objects.get(id = 1),
				'quantity' : 1
			}]}

	context = {
		'heroes' : heroes,
		'items' : items,
		'next' : next_step,
	}
	return render(request, 'drops/index.html', context)
