from django.db import models
from gear.models import Item, Recipe, Ingredient


class Chapter(models.Model):
	"""A group of stages = chapter, in the campaign """
	name = models.CharField(max_length = 200, unique = True, null = True)
	minlevel = models.IntegerField(null = True)
	cost = models.IntegerField(null = True)
	
	def __str__(self):
		return self.name


class Stage(models.Model):
	#A stage in the campaign
	chapter = models.ForeignKey(Chapter, null = True, on_delete = models.CASCADE, related_name='chapter')
	level = models.IntegerField(null = True, blank = True)
	name = models.CharField(max_length = 200, unique = True, null = True)
		
	def __str__(self):
		#fullname = str(self.level) + ':' + self.name
		return self.name #fullname + ' ins ' + self.get_chapter_display()


class Drop(models.Model):
	#Gear dropped in a stage
	stage = models.ForeignKey(Stage, on_delete = models.CASCADE, related_name='drops')
	drops = models.ForeignKey(
		Item,
		limit_choices_to={'recipe': None},
		on_delete = models.CASCADE,
		null =True,
	)
	
	def __str__(self):
		return self.stage.name + ' drops ' + self.drops.name
