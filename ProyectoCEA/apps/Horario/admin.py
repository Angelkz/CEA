from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Periodo)
admin.site.register(Semestre)
admin.site.register(Salon)
admin.site.register(HorarioCarrera)
admin.site.register(ClaseHora)