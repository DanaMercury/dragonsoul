from django.db import models


class Item(models.Model):
	"""The smallest denominator. Could be scraps, scrolls, or equippable items"""
	item_name = models.CharField(max_length = 200, unique = True, default= "item name")
	item_color = models.IntegerField(choices = [(1, 'white'), (2, 'green')], default = 1)
	
	def __str__(self):
		return self.item_name


class Recipe(models.Model):
	"""Add Recipe def"""
	item = models.OneToOneField(Item, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.item.item_name + " recipe"
		

class Ingredient(models.Model):
	"""Add Ingredient def"""
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return str(self.quantity) + " " + self.item.item_name