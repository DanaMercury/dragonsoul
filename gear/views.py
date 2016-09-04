from django.shortcuts import render
from heroes.models import Hero
from .models import Item, Recipe

def processItems(item, items, multiplier):
	try:
		ingredients = item.recipe.ingredient_set.all()
		for ingredient in ingredients:
			processItems(ingredient.item, items, multiplier * ingredient.quantity)
	except Recipe.DoesNotExist:
		if item.name not in items:
			items[item.name] = 0
		items[item.name] += 1 * multiplier
		pass

def index(request):
	heroes = Hero.objects.all()
	items = {}
	for hero in heroes:
		hero.rarities = hero.rarity_set.all()
		for rarity in hero.rarities:
			label = rarity.get_color_display() + str(rarity.level)
			for i in range(1,7):
				items[label + '_' + str(i)] = {}
				processItems(getattr(rarity, 'gear' + str(i)), items[label + '_' + str(i)], 1)
	context = {
		'heroes' : heroes,
		'items' : items,
	}
	return render(request, 'gear/index.html', context)
