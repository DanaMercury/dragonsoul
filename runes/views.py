from django.shortcuts import render
from heroes.models import Hero
from stats.models import Stat
from .models import Collection
import copy

def index(request):
    heroes = Hero.objects.all()
    stats = Stat.objects.all()
    collections = Collection.objects.all()
    context = {
        'heroes' : heroes,
        'stats' : stats,
        'collections' : collections,
    }
    return render(request, 'runes/index.html', context)
