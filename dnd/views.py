from django.shortcuts import render
from .models import *

def index(request):
	context = {
		'test': 'test',
	}
	return render(request, "dnd/index.html", context)
