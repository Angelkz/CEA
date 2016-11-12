from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *
from .models import *


urlpatterns = [
 	url(r'^periodo/$', formPeriodo, name = 'formPeriodo'),
 	url(r'^periododel/$', formPeriodoDel, name = 'formPeriodoDel'),
 	url(r'^salon/$', formSalon, name = 'formSalon'),
 	url(r'^salondel/$', formSalonDel, name = 'formSalonDel'),
 	url(r'^clasehora/$', formClaseHora, name = 'formSalonClaseHora'),
 	url(r'^horariocarrera/$', formHorarioCarrera, name = 'formHorarioCarrera'),
 	url(r'^horariocarreradel/$', formHorarioCarreraDel, name = 'formHorarioCarreraDel'),
]

