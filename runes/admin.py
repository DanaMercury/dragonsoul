from django.contrib import admin

from .models import Collection

class CollectionAdmin(admin.ModelAdmin):
	""" Def class"""
	fieldsets = [
		(None, {'fields': ['name']}),
	]
	search_fields = ['name']
	ordering = ['name']

admin.site.register(Collection, CollectionAdmin)
