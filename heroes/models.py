from django.db import models
from gear.models import Item


class Hero(models.Model):
	"""Name of the Hero"""
	name = models.CharField(max_length = 200, unique = True, null = True)

	def __str__(self):
		return self.name


class Rarity(models.Model):
	"""The color and level of the hero."""
	hero = models.ForeignKey(Hero, on_delete = models.CASCADE)
	color = models.IntegerField(default = 1, choices = [
		(1,'white'),
		(2,'green'),
		(3,'blue'),
		(4,'purple'),
		(5,'orange'),
	])
	level = models.IntegerField(null = True, blank = True)
	gear1 = models.ForeignKey(Item, on_delete = models.CASCADE, null =True, related_name="gear1")
	gear2 = models.ForeignKey(Item, on_delete = models.CASCADE, null =True, related_name="gear2")
	gear3 = models.ForeignKey(Item, on_delete = models.CASCADE, null =True, related_name="gear3")
	gear4 = models.ForeignKey(Item, on_delete = models.CASCADE, null =True, related_name="gear4")
	gear5 = models.ForeignKey(Item, on_delete = models.CASCADE, null =True, related_name="gear5")
	gear6 = models.ForeignKey(Item, on_delete = models.CASCADE, null =True, related_name="gear6")
	
	def __str__(self):
		return str(self.get_color_display()) + " " + str(self.level)