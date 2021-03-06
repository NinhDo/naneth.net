"""space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from swn import views as swn_views
from space.views import index, projects
from api import views as api_views

urlpatterns = [
	re_path(r'^$', index, name="index"),
	re_path(r'^projects/$', projects, name="projects"),
	re_path(r'^space/', include("swn.urls")),
    re_path(r'^api/', include("api.urls")),
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^login/$', auth_views.LoginView, name="login"),
	re_path(r'^logout/$', auth_views.LogoutView, name="logout"),
	re_path(r'^signup/$', swn_views.signup, name="signup"),
]
