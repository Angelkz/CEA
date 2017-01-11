from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from apps.Escuela.views import *
from apps.Horario.views import *



urlpatterns = [
    url('', include('apps.Horario.urls')),
    url('', include('apps.ProyectB.urls')),
    url('', include('apps.Escuela.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pdf2',salones, name = 'imprimir2'),
    url(r'^pdf3',imprimirmateria, name = 'imprimir3'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
