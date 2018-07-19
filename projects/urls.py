from django.urls import re_path

from . import views

app_name = "projects"

urlpatterns = [
	re_path(r'^$', views.index, name="index"),
]
