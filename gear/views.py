from django.shortcuts import render
from heroes.models import Hero, Rarity
from drops.models import Stage
from .models import Item, Recipe

def processItems(item, items, multiplier, master_items):
	try:
		for ingredient in item.recipe.ingredients.all():
			processItems(master_items[ingredient.item.id], items, multiplier * ingredient.quantity, master_items)
	except Recipe.DoesNotExist:
		if item.name not in items:
			items[item.id] = { 'total' : 0, 'color' : item.color, 'name' : item.name, 'id' : item.id, 'image' : item.image.url }
		items[item.id]['total'] += multiplier
		pass

def index(request):
	heroes = Hero.objects.all().prefetch_related(
		'rarities__gear1',
		'rarities__gear2',
		'rarities__gear3',
		'rarities__gear4',
		'rarities__gear5',
		'rarities__gear6',
		'quests',
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
		for quest in hero.quests.all().order_by('id'):
			label = str(hero.id) + '_quest' + str(quest.id)
			items[label] = {}
			item_id = quest.sacrifice.id
			processItems(master_items[item_id], items[label], quest.quantity, master_items)
	context = {
		'heroes' : heroes,
		'items' : items,
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
