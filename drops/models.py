from django.db import models
from gear.models import Item, Recipe, Ingredient


class Chapter(models.Model):
    """A group of stages = chapter, in the campaign """
    number = models.IntegerField(null = True, blank = False)
    name = models.CharField(max_length = 200, unique = True, null = True)
    minlevel = models.IntegerField(null = True)
    cost = models.IntegerField(null = True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return str(self.number) + ': ' + str(self.name)


class Stage(models.Model):
    #A stage in the campaign
    chapter = models.ForeignKey(Chapter, null = True, on_delete = models.CASCADE, related_name='chapter')
    number = models.IntegerField(null = True, blank = False)
    name = models.CharField(max_length = 200, unique = True, null = True)

    def __str__(self):
        return str(self.chapter.number) + '-' + str(self.number) + ': ' + self.name


class Drop(models.Model):
    #Gear dropped in a stage
    stage = models.ForeignKey(Stage, on_delete = models.CASCADE, related_name='drops')
    item = models.ForeignKey(Item, limit_choices_to={'recipe': None}, on_delete = models.CASCADE, null = True, related_name='drops')

    def __str__(self):
        return self.stage.name + ' drops ' + self.item.name
