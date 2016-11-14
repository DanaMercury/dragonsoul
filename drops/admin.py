from django.contrib import admin
from django import forms

from gear.models import Item
from .models import Chapter, Stage, Drop


class ChapterAdmin(admin.ModelAdmin):
	""" Form for adding a new chapter in the campaign """
	fieldsets = [
		(None, {'fields':['number', 'name','minlevel','cost',]}),
	]
	extra = 0
	list_display = ('number','name','minlevel','cost',)

admin.site.register(Chapter, ChapterAdmin)


class DropInline(admin.TabularInline):
	#Form for adding the items dropped
	model = Drop
	default = 1
	extra = 0


class StageAdmin(admin.ModelAdmin):
	#Enter data from a stage
	fieldsets = [
		(None, {'fields':['chapter','number','name', ]}),
	]
	inlines = [DropInline]
	list_display = ('chapter', 'number', 'name',)
	list_filter = ['chapter',]
	ordering = ('chapter', 'number',)

admin.site.register(Stage, StageAdmin)
