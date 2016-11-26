from django.shortcuts import render
from gear.models import Item
from heroes.models import Hero, Rarity
from .models import Drop, Chapter
import copy

def index(request, max_chapter = 0, ingredients_raw = '', candidates_raw = ''):
    chapters = Chapter.objects.all().order_by('-number')
    heroes = Hero.objects.all().prefetch_related(
        'rarities__gear1',
        'rarities__gear2',
        'rarities__gear3',
        'rarities__gear4',
        'rarities__gear5',
        'rarities__gear6',
        'quests'
    )
    next_steps = ''
    failed = False
    ingredients = ''
    candidates = ''
    drops = ''
    if('' != ingredients_raw and '' != candidates_raw):
        sets = ingredients_raw.split('_')
        ingredients = []
        for pair in sets:
            values = pair.split(':');
            ingredients.append({ 'item_id' : int(values[0]), 'quantity' : int(values[1]) })
        sets = candidates_raw.split('_')
        candidates = []
        for pair in sets:
            values = pair.split(':');
            candidates.append({ 'hero_id' : int(values[0]), 'item_id' : int(values[1]) })

        # YOUR CODE GOES HERE




        # END OF YOUR CODE	

        # MAKE SURE YOU HAVE CREATED A LIST OF DICTIONARIES CALLED 'next_steps'
        # EACH DICTIONARY SHOULD HAVE THIS FORMAT:
        # { 'stage' : STAGE_ID, 'scraps' : [{'item' : ITEM_OBJECT, 'quantity' : NUMBER_NEEDED}, ...] }

    context = {
        'heroes' : heroes,
        'next' : next_steps,
        'chapters' : chapters,
        'failed' : failed
    }
    return render(request, 'drops/index.html', context)
