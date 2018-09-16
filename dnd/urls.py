from django.urls import re_path

from . import views

app_name = "dnd"

urlpatterns = [
	re_path(r'^$', views.index, name="index"),
	re_path(r'^spells/$', views.spells, name="spells"),
]
