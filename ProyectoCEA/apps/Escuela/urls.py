from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import *


urlpatterns = [

 		url(r'^titulo/$', formTitulo, name = 'formTitulo'),
 		url(r'^titulodel/$', formTituloDel, name = 'formTituloDel'),
 		url(r'^gradomaximo/$', formGradoMaximo, name = 'formGradoMaximo'),
 		url(r'^gradomaximodel/$', formGradoMaximoDel, name = 'formGradoMaximoDel'),
 		url(r'^carrera/$', formCarrera, name = 'formCarrera'),
 		url(r'^carreradel/$', formCarreraDel, name = 'formCarreraDel'),
 		url(r'^profesor/$', formProfesor, name = 'formProfesor'),
 		url(r'^profesoraut/$', formProfesorAut, name = 'formProfesorAut'),
 		url(r'^profesordel/$', formProfesorDel, name = 'formProfesorDel'),
 		url(r'^materia/$', formMateria, name = 'formMateria'),
 		url(r'^materiadel/$', formMateriaDel, name = 'formMateriaDel'),
 		url(r'^profesormateria/$', formProfesorMateria, name = 'formProfesorMateria'),
 		url(r'^profesorhora/$', formProfesorHora, name = 'formProfesorHora'),
 		url(r'^registroUsu/$', registroUsu, name = 'registroUsu'),
]