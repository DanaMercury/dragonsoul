from django.db import models
from stats.models import Stat


class Item(models.Model):
	"""The smallest denominator. Could be scraps, scrolls, or equippable items"""
	name = models.CharField(max_length = 200, unique = True, null = True)
	color = models.IntegerField(default = 1, choices = [
		(1, 'white'),
		(2, 'green'),
		(3, 'blue'),
		(4, 'purple'),
		(5, 'orange')
	])
	level = models.IntegerField(null = True, blank = True)
	description = models.CharField(max_length = 200, unique = True, null = True)
	equippable = models.BooleanField(default = False)

	def __str__(self):
		return self.name


class Recipe(models.Model):
	"""Add Recipe def"""
	item = models.OneToOneField(Item, on_delete = models.CASCADE)
	cost = models.IntegerField(null = True)

	def __str__(self):
		return self.item.name + " recipe"


class Ingredient(models.Model):
	"""Add Ingredient def"""
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	quantity = models.IntegerField(null = True)

	def __str__(self):
		return str(self.quantity) + " " + self.item.name + " on " + self.recipe.item.name


class GearStat(models.Model):
	"""Add Stat def"""
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	stat = models.ForeignKey(Stat, on_delete = models.CASCADE)
	quantity = models.IntegerField(null = True)

	def __str__(self):
		return str(self.quantity) + " " + self.stat.name + " on " + self.item.name
