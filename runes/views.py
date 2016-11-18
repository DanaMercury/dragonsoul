from django.shortcuts import render
from heroes.models import Hero
from stats.models import Stat
from .models import Collection
import copy

def index(request):
    heroes = Hero.objects.all().order_by('id')
    stats = Stat.objects.all().order_by('name')
    collections = Collection.objects.all().order_by('id')
    context = {
        'heroes' : heroes,
        'stats' : stats,
        'collections' : collections,
    }
    return render(request, 'runes/index.html', context)
