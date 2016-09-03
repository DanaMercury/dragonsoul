from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist
import nested_admin

from .models import Recipe, Item, Ingredient, GearStat


class IngredientInlineForm(forms.ModelForm):
	""" Def class"""

	class Meta:
		model = Ingredient
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(IngredientInlineForm, self).__init__(*args, **kwargs)
		try:
			self.fields['item'].queryset = Item.objects.exclude(name=self.instance.recipe.item.name)
		except ObjectDoesNotExist:
			pass


class IngredientInline(nested_admin.NestedTabularInline):
	""" Def class"""
	model = Ingredient
	form = IngredientInlineForm
	extra = 0


class RecipeInline(nested_admin.NestedTabularInline):
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
	list_display = ('name', 'color', 'equippable', 'level', 'description')
	list_filter = ['color', 'level', 'equippable']
	search_fields = ['name', 'description']

admin.site.register(Item, ItemAdmin)
