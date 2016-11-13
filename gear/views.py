from django.shortcuts import render
from heroes.models import Hero, Rarity
from drops.models import Stage
from .models import Item, Recipe

def processItems(item, items, multiplier, master_items):
	try:
		for ingredient in item.recipe.ingredients.all():
			processItems(master_items[ingredient.item.id], items, multiplier * ingredient.quantity, master_items)
	except Recipe.DoesNotExist:
		if item.id not in items:
			items[item.id] = { 'total' : 0, 'color' : item.color, 'name' : item.name, 'id' : item.id, 'image' : item.image.url }
		items[item.id]['total'] += multiplier
		pass

def index(request):
	heroes = Hero.objects.all()
	context = {
		'heroes' : heroes,
	}
	return render(request, 'gear/index.html', context)

def catalog(request):
	equippables = []
	scrolls = []
	scroll_scraps = []
	scraps = []
	items = Item.objects.all().order_by('-color', 'name')
	for item in items:
		if item.equippable:
			equippables.append(item)
		elif -1 != item.name.lower().find('scrap') and -1 != item.name.lower().find('scroll'):
			scroll_scraps.append(item)
		elif -1 != item.name.lower().find('scroll'):
			scrolls.append(item)
		elif -1 != item.name.lower().find('scrap'):
			scraps.append(item)
	context = {
		'equippables' : equippables,
		'scrolls' : scrolls,
		'scroll_scraps' : scroll_scraps,
		'scraps' : scraps,
	}
	return render(request, 'gear/catalog.html', context)

def detail(request, item_id):
	item = Item.objects.get(id=item_id)
	rarities = Rarity.objects.all().prefetch_related('hero','gear1','gear2','gear3','gear4','gear5','gear6')
	stages = Stage.objects.all().prefetch_related('chapter', 'drops')
	classification = ''
	if item.equippable:
		classification = 'Equippable'
	elif -1 != item.name.lower().find('scrap') and -1 != item.name.lower().find('scroll'):
		classification = 'Scroll Scrap'
	elif -1 != item.name.lower().find('scroll'):
		classification = 'Scroll'
	elif -1 != item.name.lower().find('scrap'):
		classification = 'Scrap'
	context = {
		'item' : item,
		'classification' : classification,
		'rarities' : rarities,
		'stages' : stages,
	}
	return render(request, 'gear/detail.html', context)
