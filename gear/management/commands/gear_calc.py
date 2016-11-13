from django.conf import settings
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand, CommandError
from heroes.models import Hero, Rarity
from gear.models import Item, Recipe
from gear.views import processItems
import simplejson as json

class Command(BaseCommand):
	help = 'Recalculates the gear json'

	def handle(self, *args, **options):
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

		file = default_storage.open('items.json', 'w')
		file.write('items = ' + json.dumps(items) + ';')
		file.close()

