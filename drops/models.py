from django.db import models
from gear.models import Item, Recipe, Ingredient


class Stage(models.Model):
	"""A stage within a chapter of the campaign"""
	chapter = models.IntegerField(default = 1, choices = [
		(1, 'Chapter 1: hsfs'),
		(2, 'Chapter 2: kiusfs'),
		(3, 'Chapter 3: musfs'),
		(4, 'Chapter 4: thrht'),
		(5, 'Chapter 5: rgrddg')
	])
	level = models.IntegerField(null = True, blank = True)
	name = models.CharField(max_length = 200, unique = True, null = True)
	cost = models.IntegerField(null = True)
		
	def __str__(self):
		fullname = str(self.level) + ':' + self.name
		return fullname + ' ins ' + self.get_chapter_display()
		
		
class Drop(models.Model):
	"""Gear dropped in a stage """
	stage = models.ForeignKey(Stage, on_delete = models.CASCADE, related_name='drops')
	
	drops = models.ForeignKey(
		Item,
		limit_choices_to={'recipe': None},
		on_delete = models.CASCADE,
		null =True,
	)
	
	def __str__(self):
		return self.stage.name + ' drops ' + self.drops.name