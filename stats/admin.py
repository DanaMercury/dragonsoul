from django.contrib import admin

from .models import Stat

class StatAdmin(admin.ModelAdmin):
	""" Def class"""
	fieldsets = [
		(None, {'fields': ['name']}),
	]
	list_display = ('name', 'name') #replace second name with description ASAP
	search_fields = ['name']

admin.site.register(Stat, StatAdmin)
