from django.urls import re_path

from . import views

app_name="api"
urlpatterns = [
	re_path(r'^hello/$', views.hello, name="hello"),
]
