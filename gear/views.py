from django.shortcuts import render
from heroes.models import Hero
from .models import Item, Recipe

def processItems(item, items, multiplier):
	try:
		for ingredient in item.recipe.ingredients.all():
			processItems(ingredient.item, items, multiplier * ingredient.quantity)
	except Recipe.DoesNotExist:
		if item.name not in items:
			items[item.name] = { 'total' : 0, 'color' : item.color }
		items[item.name]['total'] += 1 * multiplier
		pass

def index(request):
	heroes = Hero.objects.all().prefetch_related(
		'rarities__gear1__recipe__ingredients',
		'rarities__gear2__recipe__ingredients',
		'rarities__gear3__recipe__ingredients',
		'rarities__gear4__recipe__ingredients',
		'rarities__gear5__recipe__ingredients',
		'rarities__gear6__recipe__ingredients',
	)
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
				processItems(getattr(rarity, 'gear' + str(i)), items[label + '_' + str(i)], 1)
	context = {
		'heroes' : heroes,
		'items' : items,
	}
	return render(request, 'gear/index.html', context)
