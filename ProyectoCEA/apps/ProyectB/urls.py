from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *


urlpatterns = [
	url(r'^$', 'apps.ProyectB.views.home', name='home'),
	url(r'^index/$', 'apps.ProyectB.views.home', name='home'),
    url(r'^about/$', 'apps.ProyectB.views.about', name='about'),
    url(r'^config/$', 'apps.ProyectB.views.config', name='config'),
    url(r'^contact/$', 'apps.ProyectB.views.contact', name='contact'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'ProyectB/login.html'} , name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
]