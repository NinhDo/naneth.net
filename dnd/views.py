from django.http import JsonResponse
from django.shortcuts import render, get_list_or_404
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from .models import *

def index(request):
	context = {
		'test': 'test',
	}
	return render(request, "dnd/index.html", context)

def spells(request):
	spells = Spell.objects.order_by("name").values()
	spell_list = list(spells)
	return JsonResponse(spell_list, safe=False)
