from django.contrib import admin

from .models import Hero, Rarity, Quest


class RarityInline(admin.StackedInline):
	""" Deets from Rarity model """
	model = Rarity
	extra = 0

class QuestInline(admin.TabularInline):
	""" Deets on Quest model """
	model = Quest
	extra = 0

class HeroAdmin(admin.ModelAdmin):
	""" Putting Rarity and Quest forms into the Hero form """
	fieldsets = [
		(None, {'fields':['name','image']}),
	]
	inlines = [RarityInline, QuestInline]
	search_fields = ['name']

admin.site.register(Hero, HeroAdmin)
