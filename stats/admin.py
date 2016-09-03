from django.contrib import admin

from .models import Stat

class StatAdmin(admin.ModelAdmin):
	""" Def class"""
	fieldsets = [
		(None, {'fields': ['name']}),
	]
	search_fields = ['name']
	ordering = ['name']

admin.site.register(Stat, StatAdmin)
