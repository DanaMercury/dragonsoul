from django.db import models

class Item(models.Model):
	"""The smallest denominator. Could be scraps, scrolls, or equippable items"""
	name = models.CharField(max_length = 200, unique = True, null = True)
	image = models.ImageField(upload_to = 'items', height_field = 'height', width_field = 'width', null = True)
	height = models.IntegerField(default = 0)
	width = models.IntegerField(default = 0)
	color = models.IntegerField(default = 1, choices = [
		(1, 'White'),
		(2, 'Green'),
		(3, 'Blue'),
		(4, 'Purple'),
		(5, 'Orange')
	])
	level = models.IntegerField(null = True, blank = True)
	description = models.CharField(max_length = 200, unique = True, null = True)
	equippable = models.BooleanField(default = False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Recipe(models.Model):
	"""Add Recipe def"""
	item = models.OneToOneField(Item, on_delete = models.CASCADE, related_name="recipe")
	cost = models.IntegerField(null = True)

	def __str__(self):
		return self.item.name + ' recipe'


class Ingredient(models.Model):
	"""Add Ingredient def"""
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, related_name='ingredients')
	item = models.ForeignKey(Item, on_delete = models.CASCADE, related_name='ingredients')
	quantity = models.IntegerField(null = True)

	def __str__(self):
		return str(self.quantity) + ' ' + self.item.name + ' on ' + self.recipe.item.name


class GearStat(models.Model):
	"""Add Stat def"""
	from stats.models import Stat
	item = models.ForeignKey(Item, on_delete = models.CASCADE, related_name="stats")
	stat = models.ForeignKey(Stat, on_delete = models.CASCADE)
	quantity = models.IntegerField(null = True)

	def __str__(self):
		return str(self.quantity) + ' ' + self.stat.name + ' on ' + self.item.name
