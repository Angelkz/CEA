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
 		url(r'^profesortotalrep/$', formProfesorTotalRep, name = 'formProfesorTotalRep'),
 		url(r'^profesoraut/$', formProfesorAut, name = 'formProfesorAut'),
 		url(r'^profesordel/$', formProfesorDel, name = 'formProfesorDel'),
 		url(r'^profesorrepcont/$', formProfesorRepCont, name = 'formProfesorRepCont'),
 		url(r'^profesorrepprof/$', formProfesorRepProf, name = 'formProfesorRepProf'),
 		url(r'^profesorrepdisp/$', formProfesorRepDisp, name = 'formProfesorRepDisp'),
 		url(r'^materia/$', formMateria, name = 'formMateria'),
 		url(r'^materiadel/$', formMateriaDel, name = 'formMateriaDel'),
 		url(r'^profesormateria/$', formProfesorMateria, name = 'formProfesorMateria'),
 		url(r'^profesormateriarep/$', formProfesorMateriaRep, name = 'formProfesorMateriaRep'),
 		url(r'^profesorhora/$', formProfesorHora, name = 'formProfesorHora'),
 		url(r'^profesorhorarep/$', formProfesorHoraRep, name = 'formProfesorHoraRep'),
 		url(r'^registroUsu/$', registroUsu, name = 'registroUsu'),
 		url(r'^pdfProCont',imprimirProCont, name = 'imprimirProCont'),
 		url(r'^pdfProProf',imprimirProProf, name = 'imprimirProProf'),
 		url(r'^pdfProDisp',imprimirProDisp, name = 'imprimirProDisp'),
 		url(r'^pdfProMat',imprimirProMat, name = 'imprimirProMat'),
 		url(r'^pdfProHor',imprimirProHor, name = 'imprimirProHor'),
 		#url(r'^pdfTotalRep',imprimirTotalRep, name = 'imprimirTotalRep'),
]