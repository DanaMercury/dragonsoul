from django.db import models

class Collection(models.Model):
	"""Collection type, rec by DS"""
	name = models.CharField(max_length = 50, unique = True, null = True)

	def __str__(self):
		return self.name
		
		
class Equipper(models.Model):
	"""Heroes who use this type of collection"""
	from heroes.models import Hero
	collection = models.ForeignKey(Collection, on_delete = models.CASCADE, related_name='equippers')
	hero = models.ForeignKey(Hero, on_delete = models.CASCADE, null =True, related_name='equippers')

	def __str__(self):
		return self.collection.name + ' is used by ' + self.hero.name