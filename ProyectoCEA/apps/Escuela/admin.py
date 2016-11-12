from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(PerfilUsuario)
admin.site.register(Titulo)
admin.site.register(GradoMaximo)
admin.site.register(NumeroHoras)
admin.site.register(Carrera)
admin.site.register(Dia)
admin.site.register(Hora)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(ProfesorMateria)
admin.site.register(ProfesorHora)