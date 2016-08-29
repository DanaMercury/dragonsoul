from django.db import models

class Stat(models.Model):
	"""Each type of stat."""
	name = models.CharField(max_length = 50, unique = True, null = True)

	def __str__(self):
		return self.name
