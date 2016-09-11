from django.contrib import admin
from django import forms

from gear.models import Item
from .models import Chapter, Stage, Drop


class ChapterAdmin(admin.ModelAdmin):
	""" Form for adding a new chapter in the campaign """
	fieldsets = [
		(None, {'fields':['name','minlevel','cost',]}),
	]
	extra = 0
	list_display = ('name','minlevel','cost',)

admin.site.register(Chapter, ChapterAdmin)


class ChapterInline(admin.TabularInline):
	#Form for adding the items dropped
	model = Chapter
	default = 1
	extra = 0


class DropInline(admin.TabularInline):
	#Form for adding the items dropped
	model = Drop
	default = 1
	extra = 0


class StageAdmin(admin.ModelAdmin):
	#Enter data from a stage
	fieldsets = [
		(None, {'fields':['chapter','level','name', ]}),
	]
	inlines = [DropInline]
	list_display = ('chapter', 'level', 'name',)
	list_filter = ['chapter',]

admin.site.register(Stage, StageAdmin)
