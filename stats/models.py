from django.db import models

class Stat(models.Model):
	"""Each type of stat."""
	name = models.CharField(max_length = 50, unique = True, null = True)
	all_benefit = models.BooleanField(default = False)

	def __str__(self):
		return self.name
		

class Stat_User(models.Model):
	"""Heroes who use a particular stat"""
	from heroes.models import Hero
	
	stat = models.ForeignKey(Stat, on_delete = models.CASCADE, related_name='stat_users')
	hero = models.ForeignKey(Hero, on_delete = models.CASCADE, null = True, related_name='stat_users')
	
	def __str__(self):
		return self.hero.name + ' benefits from equipping runes with ' + self.stat.name