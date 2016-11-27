from django.contrib import admin

from .models import Stat, Stat_User
from heroes.models import Hero


class Stat_UserInline(admin.TabularInline):
	""" Form for adding stats used by each hero"""
	model = Stat_User
	default = 1
	extra = 0


class StatAdmin(admin.ModelAdmin):
	""" Form for Stat class """
	fieldsets = [
		(None, {'fields': ['name', 'all_benefit', 'primary']}),
	]
	inlines = [Stat_UserInline]
	list_display = ('name', 'all_benefit','primary',)
	search_fields = ['name']
	ordering = ['name']

admin.site.register(Stat, StatAdmin)
