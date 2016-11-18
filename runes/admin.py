from django.contrib import admin

from .models import Collection, Equipper
from heroes.models import Hero

class EquipperInline(admin.TabularInline):
	""" Form for adding which heroes benefit from the collection type """
	model = Equipper
	default = 1
	extra = 0

class CollectionAdmin(admin.ModelAdmin):
	""" Form for adding collection types """
	fieldsets = [
		(None, {'fields': ['name']}),
	]
	inlines = [EquipperInline]
	search_fields = ['name']
	ordering = ['name']

admin.site.register(Collection, CollectionAdmin)