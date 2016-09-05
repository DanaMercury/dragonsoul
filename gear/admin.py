from django.contrib import admin
from django import forms
import nested_admin

from .models import Recipe, Item, Ingredient, GearStat


class IngredientInline(nested_admin.NestedTabularInline):
	""" Def class"""
	model = Ingredient
	extra = 0


class RecipeInline(nested_admin.NestedStackedInline):
	""" Def class"""
	model = Recipe
	inlines = [IngredientInline]
	max_num = 1
	extra = 0
	validate_max = True


class StatInline(nested_admin.NestedTabularInline):
	""" Def class"""
	model = GearStat
	extra = 0


class ItemAdmin(nested_admin.NestedModelAdmin):
	""" Def class"""
	fieldsets = [
		(None, {'fields':['name', 'color', 'level', 'description', 'equippable']}),
	]
	inlines = [StatInline, RecipeInline]
	list_display = ('name', 'color', 'level', 'description', 'equippable')
	list_filter = ['color', 'equippable', 'level']
	search_fields = ['name', 'description']
	ordering = ['name']

admin.site.register(Item, ItemAdmin)
