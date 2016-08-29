from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist
import nested_admin

from .models import Recipe, Item, Ingredient


class IngredientInlineForm(forms.ModelForm):
	""" Def class"""
	
	class Meta:
		model = Ingredient
		fields = '__all__' 

	def __init__(self, *args, **kwargs):
		super(IngredientInlineForm, self).__init__(*args, **kwargs)
		try:
			self.fields['item'].queryset = Item.objects.exclude(item_name=self.instance.recipe.item.item_name)
			pass
		except ObjectDoesNotExist:
			pass


class IngredientInline(nested_admin.NestedTabularInline):
	""" Def class"""
	model = Ingredient
	form = IngredientInlineForm
	extra = 1


class RecipeInline(nested_admin.NestedTabularInline):
	""" Def class"""
	model = Recipe
	inlines = [IngredientInline]


class ItemAdmin(nested_admin.NestedModelAdmin):
	""" Def class"""
	fieldsets = [
	(None, {'fields':['item_name']}),
	(None, {'fields':['item_color']}),
	]
	inlines = [RecipeInline]
	list_display = ('item_name', 'item_color')
	list_filter = ['item_color']
	search_fields = ['item_name', 'item_color']

admin.site.register(Item, ItemAdmin)