from django.db import models
from gear.models import Item
from stats.models import Stat


class Hero(models.Model):
	"""Name of the Hero"""
	name = models.CharField(max_length = 200, unique = True, null = True)
	image = models.ImageField(upload_to = 'heroes', height_field = 'height', width_field = 'width', null = True)
	height = models.IntegerField(default = 0)
	width = models.IntegerField(default = 0)
	primary = models.ForeignKey(Stat, on_delete = models.CASCADE, limit_choices_to={'primary': True}, null = True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']


class Rarity(models.Model):
	"""The color and level of the hero."""
	hero = models.ForeignKey(Hero, on_delete = models.CASCADE, related_name="rarities")
	color = models.IntegerField(default = 1, choices = [
		(1,'White'),
		(2,'Green'),
		(3,'Blue'),
		(4,'Purple'),
		(5,'Orange'),
	])
	level = models.IntegerField(default = 0)
	gear1 = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,
		related_name="gear1"
	)
	gear2 = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,
		related_name="gear2"
	)
	gear3 = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,
		related_name="gear3"
	)
	gear4 = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,
		related_name="gear4"
	)
	gear5 = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,
		related_name="gear5"
	)
	gear6 = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,
		related_name="gear6"
	)

	def __str__(self):
		if 0 == self.level:
			level = ''
		else:
			level = '+' + str(self.level)
		return self.get_color_display() + ' ' + level

	class Meta:
		ordering = ['color', 'level']

class Quest(models.Model):
	"""Optional field for legendary quest."""
	hero = models.ForeignKey(Hero, on_delete = models.CASCADE, related_name="quests")
	#name = models.CharField(max_length = 200, unique = True, null = True)
	#description = models.CharField(max_length = 200, unique = True, null = True)
	color = models.IntegerField(default = 5, choices = [
		(5,'Orange'),
	])
	sacrifice = models.ForeignKey(
		Item,
		limit_choices_to={'equippable': True},
		on_delete = models.CASCADE,
		null =True,

	)
	quantity = models.IntegerField(null = True)

	def __str__(self):
		return str(self.quantity) + ' ' + self.sacrifice.name

	class Meta:
		ordering = ['id']

