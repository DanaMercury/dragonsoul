from django.db import models

class Collection(models.Model):
	"""Collection type, rec by DS"""
	name = models.CharField(max_length = 50, unique = True, null = True)

	def __str__(self):
		return self.name