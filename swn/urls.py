from django.urls import re_path

from . import views

app_name="swn"
urlpatterns = [
	re_path(r'^$', views.index, name="index"),
	re_path(r'^system/$', views.system_list, name="system_list"),
	re_path(r'^faction/$', views.faction, name="faction"),
	re_path(r'^faction/(?P<faction_name>[A-z-]+)/$', views.faction_overview, name="faction_overview"),
	re_path(r'^system/(?P<system_name>[A-z-]+)/$', views.system, name="system"),
	re_path(r'^system/(?P<system_name>[A-z-]+)/(?P<planet_name>[A-z-]+)/$', views.planet, name="planet"),
	re_path(r'^planet/$', views.planet_directory, name="planet_directory"),
	re_path(r'^aliens/$', views.alien_races, name="alien_races"),
	re_path(r'^politicalgroups/$', views.political_groups, name="political_groups"),
	re_path(r'^corporations/$', views.corporations, name="corporations"),
	re_path(r'^religions/$', views.religions, name="religions"),
	re_path(r'^npcs/$', views.npcs, name="npcs"),
	re_path(r'^save_planet_notes/$', views.save_planet_notes, name="save_planet_notes"),
	re_path(r'^save_notes/$', views.save_notes, name="save_notes"),
]
