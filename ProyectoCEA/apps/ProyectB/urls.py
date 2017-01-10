from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', 'apps.ProyectB.views.home', name='home'),
	url(r'^index/$', 'apps.ProyectB.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'ProyectB/login.html'} , name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^index/$', auth_views.login),
]