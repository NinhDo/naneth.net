from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group

from swn.forms import UserForm, PlanetNotesForm, NotesForm
from .models import *
import math

# Create your views here.
def user_is_gm(user):
	group = Group.objects.get(name="GM")
	return group in user.groups.all()


def index(request):
	planet_list = get_list_or_404(Planet.objects.order_by("system", "name"))
	hex_list = get_list_or_404(System.objects.values_list("nav_designation", flat=True))
	points, rad, centers, data_list = generate_points()
	for i, data in enumerate(data_list):
		for planet in planet_list:
			if data[2] == planet.system.nav_designation:
				data_list[i] = (data[0], data[1], data[2], planet.system)
	h = rad * 2 * 10
	w = rad * 13
	context = {
		'planet_list': planet_list,
		'hex_list': hex_list,
		'points': points,
		'h': h,
		'w': w,
		'centers': centers,
		'len': len(points),
		'data_list': data_list,
	}
	return render(request, "swn/sector.html", context)


def system(request, system_name):
	system = get_object_or_404(System, alias=system_name)
	planet_list = get_list_or_404(Planet, system=system)
	if not system.notes:
		notes = Notes()
		notes.save()
		system.notes = notes
		system.save()
	context = {
		'system': system,
		'planet_list': planet_list,
	}
	return render(request, "swn/system.html", context)


def planet(request, system_name, planet_name):
	system = get_object_or_404(System, alias=system_name)
	planet = get_object_or_404(Planet, alias=planet_name)
	if not system.notes:
		notes = Notes()
		notes.save()
		system.notes = notes
		system.save()
	if not planet.notes:
		notes = Notes()
		notes.save()
		planet.notes = notes
		planet.save()
	context = {
		'system': system,
		'planet': planet,
	}
	return render(request, "swn/planet.html", context)


def system_list(request):
	system_list = get_list_or_404(System.objects.order_by("nav_designation"))
	context = {
		'system_list': system_list,
	}
	return render(request, "swn/system_list.html", context)


def faction(request):
	faction_list = get_list_or_404(Faction.objects.all().order_by("name"))
	context = {
		'faction_list': faction_list,
	}
	return render(request, "swn/faction.html", context)


def faction_overview(request, faction_name):
	faction = get_object_or_404(Faction, alias=faction_name)
	if not faction.notes:
		notes = Notes()
		notes.save()
		faction.notes = notes
		faction.save()
	context = {
		'faction': faction,
	}
	return render(request, "swn/faction_overview.html", context)


def planet_directory(request):
	planet_list = get_list_or_404(Planet.objects.order_by("system", "name"))
	context = {
		"planet_list": planet_list,
	}
	return render(request, "swn/planet_directory.html", context)


def alien_races(request):
	alien_races_list = get_list_or_404(Alien.objects.order_by("name"))
	context = {
		"alien_races_list": alien_races_list,
	}
	return render(request, "swn/alien_races.html", context)


def political_groups(request):
	political_groups_list = get_list_or_404(PoliticalGroup.objects.order_by("name"))
	context = {
		"political_groups_list": political_groups_list,
	}
	return render(request, "swn/political_groups.html", context)


def corporations(request):
	corporations_list = get_list_or_404(Corporation.objects.order_by("name"))
	context = {
		"corporations_list": corporations_list,
	}
	return render(request, "swn/planet_directory.html", context)


def religions(request):
	religions_list = get_list_or_404(Religion.objects.order_by("name"))
	context = {
		"religions_list": religions_list,
	}
	return render(request, "swn/planet_directory.html", context)


def npcs(request):
	npcs_list = get_list_or_404(NPC.objects.order_by("name"))
	context = {
		"npcs_list": npcs_list,
	}
	return render(request, "swn/planet_directory.html", context)


def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/space')
	else:
		form = UserForm()
	return render(request, 'registration/signup.html', {'form': form})


@login_required
@user_passes_test(user_is_gm)
def save_planet_notes(request):
	planet = Planet.objects.get(id=request.GET["planet"]);
	if request.method == "POST":
		form = PlanetNotesForm(request.POST or None, instance=planet)
		if form.is_valid:
			form.save()
		else:
			return JsonResponse({"error_message": "Invalid form"})
	return JsonResponse({})


@login_required
def save_notes(request):
	instance = Notes.objects.get(id=request.GET["id"])
	if request.method == "POST":
		form = NotesForm(request.POST or None, instance=instance)
		if form.is_valid:
			form.save()
		else:
			return JsonResponse({"error_message": "Invalid form"})
	return JsonResponse({})


def generate_points():
	angles = [0, math.pi / 3, math.pi * 2 / 3, math.pi, math.pi * 4 / 3, math.pi * 5 / 3]
	centers = []
	ret = []
	data_list = []
	p = ""
	rad = 40
	px = rad
	py = rad
	width = rad * 2
	horiz = width * 3/4
	height = math.sqrt(3)/2 * width
	vert = height
	for x in range(8):
		if x % 2:
			py = rad * 2 + vert / 2
		else:
			py = rad * 2
		for y in range(10):
			for n in angles:
				p += "{:.5f},{:.5f} ".format(px + rad * math.cos(n), py + rad * math.sin(n))
			ret.append(p)
			centers.append((px, py))
			data_list.append((p, (px, py), "{:02d}{:02d}".format(x, y), None))
			p = ""
			py += vert
		px += horiz
	return (ret, rad, centers, data_list)
