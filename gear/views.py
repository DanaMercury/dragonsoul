from django.shortcuts import render
from heroes.models import Hero
from .models import Item, Recipe

def processItems(item, items, multiplier, master_items):
	try:
		for ingredient in item.recipe.ingredients.all():
			processItems(master_items[ingredient.item.id], items, multiplier * ingredient.quantity, master_items)
	except Recipe.DoesNotExist:
		if item.name not in items:
			items[item.name] = { 'total' : 0, 'color' : item.color }
		items[item.name]['total'] += 1 * multiplier
		pass

def index(request):
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
			if None == rarity.level:
					level = ''
			else:
					level = '+' + str(rarity.level)
			label = hero.name + rarity.get_color_display() + ' ' + level
			for i in range(1,7):
				items[label + '_' + str(i)] = {}
				item_id = getattr(rarity, 'gear' + str(i)).id
				processItems(master_items[item_id], items[label + '_' + str(i)], 1, master_items)
	context = {
		'heroes' : heroes,
		'items' : items,
	}
	return render(request, 'gear/index.html', context)
