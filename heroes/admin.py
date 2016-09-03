from django.contrib import admin

from .models import Hero, Rarity


class RarityInline(admin.StackedInline):
	""" Def class"""
	model = Rarity
	extra = 0
	
	
class HeroAdmin(admin.ModelAdmin):
	""" Def class"""
	fieldsets = [
		(None, {'fields':['name']}),
	]
	inlines = [RarityInline]
	search_fields = ['name']

admin.site.register(Hero, HeroAdmin)