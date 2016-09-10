from django.contrib import admin
from django import forms

from gear.models import Item
from .models import Drop, Stage


class DropInline(admin.TabularInline):
	""" Form for adding the items dropped """
	model = Drop
	default = 1
	extra = 0


class StageAdmin(admin.ModelAdmin):
	""" Enter data from a stage """
	fieldsets = [
		(None, {'fields':['chapter', 'level','name', 'cost',]}),
	]
	inlines = [DropInline]
	list_display = ('chapter', 'level', 'name', 'cost',)
	list_filter = ['chapter', 'cost']

admin.site.register(Stage, StageAdmin)