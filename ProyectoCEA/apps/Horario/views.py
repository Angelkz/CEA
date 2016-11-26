from django.shortcuts import render

from .forms import *
from .models import *
from apps.Escuela.forms import *
from apps.Escuela.models import *

def formPeriodo(request):	
	if request.method == 'POST':

		form = PeriodoForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['Nombre']
			objV = Periodo.objects.filter(Nombre=varV)
			if objV:
				reporte = PeriodoReporte(Periodo.objects.all())
				ctx = {
				"mensaje": "Periodo ya registrado, ingresar otro", "form": form, "reporte": reporte
				}
			else:
				form.save()
				form = PeriodoForm()
				reporte = PeriodoReporte(Periodo.objects.all())
				ctx = {
					"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = PeriodoForm()
			reporte = PeriodoReporte(Periodo.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}

	else:
		form = PeriodoForm()
		reporte = PeriodoReporte(Periodo.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Horario/formPeriodo_view.html", ctx)

def formPeriodoDel(request):
	if request.method == 'POST':

		form = PeriodoDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = Periodo.objects.get(Nombre=dato)
			formDel.delete()

			form = PeriodoDelForm()
			reporte = PeriodoReporte(Periodo.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = PeriodoDelForm()
			reporte = PeriodoReporte(Periodo.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = PeriodoDelForm()
		reporte = PeriodoReporte(Periodo.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Horario/formPeriodoDel_view.html", ctx)

def formSalon(request):
	if request.method == 'POST':

		form = SalonForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['Nombre']
			objV = Salon.objects.filter(Nombre=varV)
			if objV:
				reporte = SalonReporte(Salon.objects.all())
				ctx = {
				"mensaje": "Salon ya registrado, ingresar otro", "form": form, "reporte": reporte
				}
			else:
				form.save()
				form = SalonForm()
				reporte = SalonReporte(Salon.objects.all())
				ctx = {
					"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = SalonForm()
			reporte = SalonReporte(Salon.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}

	else:
		form = SalonForm()
		reporte = SalonReporte(Salon.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Horario/formSalon_view.html", ctx)

def formSalonDel(request):
	if request.method == 'POST':

		form = SalonDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = Salon.objects.get(Nombre=dato)
			formDel.delete()

			form = SalonDelForm()
			reporte = SalonReporte(Salon.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = SalonDelForm()
			reporte = SalonReporte(Salon.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = SalonDelForm()
		reporte = SalonReporte(Salon.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Horario/formSalonDel_view.html", ctx)


def formHorarioCarrera(request):
	if request.method == 'POST':
		form = HorarioCarreraForm(request.POST)
		if form.is_valid():
			obj = HorarioCarrera()
			obj.Clave  = form.cleaned_data['Clave']
			obj.FK_Semestre  = form.cleaned_data['FK_Semestre']
			obj.FK_Periodo  = form.cleaned_data['FK_Periodo']
			obj.FK_Carrera  = form.cleaned_data['FK_Carrera']

			filtro = HorarioCarrera.objects.all().filter(Clave=obj.Clave)
			if filtro:
				form = HorarioCarreraForm()
				reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
				ctx = {
				"mensaje": "Clave de horario existente, ingresar otro", "form": form, "reporte": reporte
				}
			else:
				obj.save()
        		form = HorarioCarreraForm()
        		reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
        		ctx = {
				"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = HorarioCarreraForm()
			reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}
	else:
		form = HorarioCarreraForm()
		reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Horario/formHorarioCarrera_view.html", ctx)

def formHorarioCarreraDel(request):
	if request.method == 'POST':

		form = HorarioCarreraDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = HorarioCarrera.objects.get(Clave=dato)
			formDel.delete()

			form = HorarioCarreraDelForm()
			reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = HorarioCarreraDelForm()
			reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = HorarioCarreraDelForm()
		reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Horario/formHorarioCarreraDel_view.html", ctx)

def formClaseHora(request):
	
	if request.method == 'POST':

		form = ClaseHoraSelForm(request.POST)

		GHora = request.POST.get('GHora')
		GDia = request.POST.get('GDia')
		Grupo = request.POST.get('Grupo')
		EHora = request.POST.get('EHora')
		EDia = request.POST.get('EDia')
		
		formG = ClaseHoraForm(request.POST)
		varGrupo = request.POST.get('varGrupo')
		varDia = request.POST.get('varDia')
		varHora = request.POST.get('varHora')

		if (form.is_valid()):
			
			Grupo = form.cleaned_data['FK_HorarioCarrera']
			#Obtencion de datos
			a78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Lunes")
			a89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Lunes")
			a910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Lunes")
			a1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Lunes")
			a1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Lunes")
			a1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Lunes")
			a1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Lunes")
			a1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Lunes")
			a1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Lunes")
			a1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Lunes")
			a1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Lunes")
			a1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Lunes")
			a1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Lunes")
			a2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Lunes")
			a2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Lunes")
			b78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Martes")
			b89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Martes")
			b910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Martes")
			b1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Martes")
			b1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Martes")
			b1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Martes")
			b1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Martes")
			b1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Martes")
			b1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Martes")
			b1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Martes")
			b1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Martes")
			b1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Martes")
			b1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Martes")
			b2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Martes")
			b2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Martes")
			c78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Miercoles")
			c89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Miercoles")
			c910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Miercoles")
			c1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Miercoles")
			c1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Miercoles")
			c1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Miercoles")
			c1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Miercoles")
			c1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Miercoles")
			c1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Miercoles")
			c1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Miercoles")
			c1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Miercoles")
			c1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Miercoles")
			c1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Miercoles")
			c2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Miercoles")
			c2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Miercoles")
			d78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Jueves")
			d89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Jueves")
			d910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Jueves")
			d1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Jueves")
			d1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Jueves")
			d1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Jueves")
			d1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Jueves")
			d1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Jueves")
			d1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Jueves")
			d1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Jueves")
			d1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Jueves")
			d1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Jueves")
			d1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Jueves")
			d2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Jueves")
			d2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Jueves")
			e78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Viernes")
			e89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Viernes")
			e910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Viernes")
			e1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Viernes")
			e1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Viernes")
			e1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Viernes")
			e1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Viernes")
			e1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Viernes")
			e1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Viernes")
			e1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Viernes")
			e1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Viernes")
			e1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Viernes")
			e1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Viernes")
			e2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Viernes")
			e2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Viernes")
			f78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Sabado")
			f89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Sabado")
			f910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Sabado")
			f1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Sabado")
			f1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Sabado")
			f1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Sabado")
			f1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Sabado")
			f1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Sabado")
			f1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Sabado")
			f1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Sabado")
			f1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Sabado")
			f1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Sabado")
			f1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Sabado")
			f2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Sabado")
			f2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Sabado")
			g78 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Domingo")
			g89 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Domingo")
			g910 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Domingo")
			g1011 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Domingo")
			g1112 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Domingo")
			g1213 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Domingo")
			g1314 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Domingo")
			g1415 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Domingo")
			g1516 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Domingo")
			g1617 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Domingo")
			g1718 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Domingo")
			g1819 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Domingo")
			g1920 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Domingo")
			g2021 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Domingo")
			g2122 = ClaseHora.objects.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Domingo")

			ctx = {
				 "grupo": Grupo, "fase": "fase2", "a78": a78,  "a89": a89,  "a910": a910,  "a1011": a1011,  "a1112": a1112, 
				 "a1213": a1213, "a1314": a1314, "a1415": a1415, "a1516": a1516, "a1617": a1617, "a1718": a1718, "a1819": a1819,
				 "a1920": a1920, "a2021": a2021, "a2122": a2122, "b78": b78,  "b89": b89,  "b910": b910,  "b1011": b1011,  "b1112": b1112, 
				 "b1213": b1213, "b1314": b1314, "b1415": b1415, "b1516": b1516, "b1617": b1617, "b1718": b1718, "b1819": b1819,
				 "b1920": b1920, "b2021": b2021, "b2122": b2122, "c78": c78,  "c89": c89,  "c910": c910,  "c1011": c1011,  "c1112": c1112, 
				 "c1213": c1213, "c1314": c1314, "c1415": c1415, "c1516": c1516, "c1617": c1617, "c1718": c1718, "c1819": c1819,
				 "c1920": c1920, "c2021": c2021, "c2122": c2122, "d78": d78,  "d89": d89,  "d910": d910,  "d1011": d1011,  "d1112": d1112, 
				 "d1213": d1213, "d1314": d1314, "d1415": d1415, "d1516": d1516, "d1617": d1617, "d1718": d1718, "d1819": d1819,
				 "d1920": d1920, "d2021": d2021, "d2122": d2122, "e78": e78,  "e89": e89,  "e910": e910,  "e1011": e1011,  "e1112": e1112, 
				 "e1213": e1213, "e1314": e1314, "e1415": e1415, "e1516": e1516, "e1617": e1617, "e1718": e1718, "e1819": e1819,
				 "e1920": e1920, "e2021": e2021, "e2122": e2122, "f78": f78,  "f89": f89,  "f910": f910,  "f1011": f1011,  "f1112": f1112, 
				 "f1213": f1213, "f1314": f1314, "f1415": f1415, "f1516": f1516, "f1617": f1617, "f1718": f1718, "f1819": f1819,
				 "f1920": f1920, "f2021": f2021, "f2122": f2122, "g78": g78,  "g89": g89,  "g910": g910,  "g1011": g1011,  "g1112": g1112, 
				 "g1213": g1213, "g1314": g1314, "g1415": g1415, "g1516": g1516, "g1617": g1617, "g1718": g1718, "g1819": g1819,
				 "g1920": g1920, "g2021": g2021, "g2122": g2122,
				}

		elif (EDia and EHora and Grupo):
			objGru = HorarioCarrera.objects.get(Clave=Grupo)
			obj = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = EHora).filter(FK_Dia__Nombre = EDia)
			obj.delete()

			#Obtencion de datos
			a78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Lunes")
			a89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Lunes")
			a910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Lunes")
			a1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Lunes")
			a1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Lunes")
			a1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Lunes")
			a1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Lunes")
			a1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Lunes")
			a1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Lunes")
			a1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Lunes")
			a1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Lunes")
			a1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Lunes")
			a1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Lunes")
			a2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Lunes")
			a2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Lunes")
			b78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Martes")
			b89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Martes")
			b910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Martes")
			b1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Martes")
			b1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Martes")
			b1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Martes")
			b1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Martes")
			b1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Martes")
			b1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Martes")
			b1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Martes")
			b1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Martes")
			b1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Martes")
			b1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Martes")
			b2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Martes")
			b2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Martes")
			c78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Miercoles")
			c89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Miercoles")
			c910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Miercoles")
			c1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Miercoles")
			c1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Miercoles")
			c1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Miercoles")
			c1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Miercoles")
			c1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Miercoles")
			c1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Miercoles")
			c1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Miercoles")
			c1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Miercoles")
			c1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Miercoles")
			c1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Miercoles")
			c2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Miercoles")
			c2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Miercoles")
			d78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Jueves")
			d89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Jueves")
			d910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Jueves")
			d1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Jueves")
			d1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Jueves")
			d1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Jueves")
			d1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Jueves")
			d1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Jueves")
			d1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Jueves")
			d1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Jueves")
			d1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Jueves")
			d1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Jueves")
			d1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Jueves")
			d2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Jueves")
			d2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Jueves")
			e78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Viernes")
			e89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Viernes")
			e910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Viernes")
			e1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Viernes")
			e1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Viernes")
			e1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Viernes")
			e1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Viernes")
			e1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Viernes")
			e1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Viernes")
			e1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Viernes")
			e1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Viernes")
			e1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Viernes")
			e1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Viernes")
			e2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Viernes")
			e2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Viernes")
			f78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Sabado")
			f89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Sabado")
			f910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Sabado")
			f1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Sabado")
			f1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Sabado")
			f1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Sabado")
			f1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Sabado")
			f1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Sabado")
			f1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Sabado")
			f1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Sabado")
			f1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Sabado")
			f1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Sabado")
			f1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Sabado")
			f2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Sabado")
			f2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Sabado")
			g78 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Domingo")
			g89 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Domingo")
			g910 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Domingo")
			g1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Domingo")
			g1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Domingo")
			g1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Domingo")
			g1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Domingo")
			g1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Domingo")
			g1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Domingo")
			g1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Domingo")
			g1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Domingo")
			g1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Domingo")
			g1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Domingo")
			g2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Domingo")
			g2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Domingo")

			ctx = {
				 "grupo": objGru, "fase": "fase2", "a78": a78,  "a89": a89,  "a910": a910,  "a1011": a1011,  "a1112": a1112, 
				 "a1213": a1213, "a1314": a1314, "a1415": a1415, "a1516": a1516, "a1617": a1617, "a1718": a1718, "a1819": a1819,
				 "a1920": a1920, "a2021": a2021, "a2122": a2122, "b78": b78,  "b89": b89,  "b910": b910,  "b1011": b1011,  "b1112": b1112, 
				 "b1213": b1213, "b1314": b1314, "b1415": b1415, "b1516": b1516, "b1617": b1617, "b1718": b1718, "b1819": b1819,
				 "b1920": b1920, "b2021": b2021, "b2122": b2122, "c78": c78,  "c89": c89,  "c910": c910,  "c1011": c1011,  "c1112": c1112, 
				 "c1213": c1213, "c1314": c1314, "c1415": c1415, "c1516": c1516, "c1617": c1617, "c1718": c1718, "c1819": c1819,
				 "c1920": c1920, "c2021": c2021, "c2122": c2122, "d78": d78,  "d89": d89,  "d910": d910,  "d1011": d1011,  "d1112": d1112, 
				 "d1213": d1213, "d1314": d1314, "d1415": d1415, "d1516": d1516, "d1617": d1617, "d1718": d1718, "d1819": d1819,
				 "d1920": d1920, "d2021": d2021, "d2122": d2122, "e78": e78,  "e89": e89,  "e910": e910,  "e1011": e1011,  "e1112": e1112, 
				 "e1213": e1213, "e1314": e1314, "e1415": e1415, "e1516": e1516, "e1617": e1617, "e1718": e1718, "e1819": e1819,
				 "e1920": e1920, "e2021": e2021, "e2122": e2122, "f78": f78,  "f89": f89,  "f910": f910,  "f1011": f1011,  "f1112": f1112, 
				 "f1213": f1213, "f1314": f1314, "f1415": f1415, "f1516": f1516, "f1617": f1617, "f1718": f1718, "f1819": f1819,
				 "f1920": f1920, "f2021": f2021, "f2122": f2122, "g78": g78,  "g89": g89,  "g910": g910,  "g1011": g1011,  "g1112": g1112, 
				 "g1213": g1213, "g1314": g1314, "g1415": g1415, "g1516": g1516, "g1617": g1617, "g1718": g1718, "g1819": g1819,
				 "g1920": g1920, "g2021": g2021, "g2122": g2122,
				}

		elif (GDia and GHora and Grupo):
			formG = ClaseHoraForm()
			ctx = { "formG": formG, "fase": "fase3", "varGrupo":Grupo, "varDia":GDia, "varHora":GHora, }

		elif (formG.is_valid() and varGrupo and varDia and varHora):

			obj = ClaseHora()
			objHorCar = HorarioCarrera.objects.get(Clave=varGrupo)
			objHora = Hora.objects.get(Nombre=varHora)
			objDia = Dia.objects.get(Nombre=varDia)

			obj.FK_HorarioCarrera  = objHorCar
			obj.FK_Hora  = objHora
			obj.FK_Dia = objDia
			obj.FK_Salon = formG.cleaned_data['FK_Salon']
			obj.FK_Profesor  = formG.cleaned_data['FK_Profesor']
			obj.FK_Materia  = formG.cleaned_data['FK_Materia']

			filtro1 = ClaseHora.objects.all().filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora = objHora).filter(FK_Dia = objDia)
			filtro2 = ClaseHora.objects.all().filter(FK_Profesor = obj.FK_Profesor).filter(FK_Hora = objHora).filter(FK_Dia = objDia)
			filtro3 = ClaseHora.objects.all().filter(FK_Salon = obj.FK_Salon).filter(FK_Hora = objHora).filter(FK_Dia = objDia)
			
			if filtro1:
				formG = ClaseHoraForm()
				fase = "fase3"
				mensaje = "Clase existente en el mismo horario."				

			elif filtro2:
				formG = ClaseHoraForm()
				fase = "fase3"
				mensaje = "Profesor no disponible en ese horario."

			elif filtro3:
				formG = ClaseHoraForm()
				fase = "fase3"
				mensaje = "Salon ocupado en ese horario."
			else:
				obj.save()
				formG = ClaseHoraForm()
				fase = "fase2"
				mensaje = "Guardado"

			#Obtencion de datos
			a78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Lunes")
			a89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Lunes")
			a910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Lunes")
			a1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Lunes")
			a1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Lunes")
			a1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Lunes")
			a1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Lunes")
			a1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Lunes")
			a1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Lunes")
			a1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Lunes")
			a1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Lunes")
			a1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Lunes")
			a1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Lunes")
			a2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Lunes")
			a2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Lunes")
			b78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Martes")
			b89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Martes")
			b910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Martes")
			b1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Martes")
			b1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Martes")
			b1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Martes")
			b1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Martes")
			b1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Martes")
			b1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Martes")
			b1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Martes")
			b1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Martes")
			b1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Martes")
			b1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Martes")
			b2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Martes")
			b2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Martes")
			c78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Miercoles")
			c89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Miercoles")
			c910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Miercoles")
			c1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Miercoles")
			c1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Miercoles")
			c1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Miercoles")
			c1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Miercoles")
			c1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Miercoles")
			c1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Miercoles")
			c1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Miercoles")
			c1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Miercoles")
			c1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Miercoles")
			c1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Miercoles")
			c2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Miercoles")
			c2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Miercoles")
			d78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Jueves")
			d89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Jueves")
			d910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Jueves")
			d1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Jueves")
			d1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Jueves")
			d1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Jueves")
			d1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Jueves")
			d1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Jueves")
			d1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Jueves")
			d1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Jueves")
			d1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Jueves")
			d1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Jueves")
			d1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Jueves")
			d2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Jueves")
			d2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Jueves")
			e78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Viernes")
			e89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Viernes")
			e910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Viernes")
			e1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Viernes")
			e1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Viernes")
			e1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Viernes")
			e1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Viernes")
			e1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Viernes")
			e1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Viernes")
			e1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Viernes")
			e1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Viernes")
			e1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Viernes")
			e1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Viernes")
			e2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Viernes")
			e2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Viernes")
			f78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Sabado")
			f89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Sabado")
			f910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Sabado")
			f1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Sabado")
			f1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Sabado")
			f1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Sabado")
			f1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Sabado")
			f1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Sabado")
			f1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Sabado")
			f1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Sabado")
			f1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Sabado")
			f1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Sabado")
			f1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Sabado")
			f2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Sabado")
			f2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Sabado")
			g78 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Domingo")
			g89 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Domingo")
			g910 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Domingo")
			g1011 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Domingo")
			g1112 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Domingo")
			g1213 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Domingo")
			g1314 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Domingo")
			g1415 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Domingo")
			g1516 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Domingo")
			g1617 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Domingo")
			g1718 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Domingo")
			g1819 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Domingo")
			g1920 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Domingo")
			g2021 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Domingo")
			g2122 = ClaseHora.objects.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Domingo")

			ctx = {
				 "mensaje": mensaje, "formG": formG, "fase": fase, "grupo": objHorCar, "a78": a78,  "a89": a89,  "a910": a910,  "a1011": a1011,  "a1112": a1112, 
				 "a1213": a1213, "a1314": a1314, "a1415": a1415, "a1516": a1516, "a1617": a1617, "a1718": a1718, "a1819": a1819,
				 "a1920": a1920, "a2021": a2021, "a2122": a2122, "b78": b78,  "b89": b89,  "b910": b910,  "b1011": b1011,  "b1112": b1112, 
				 "b1213": b1213, "b1314": b1314, "b1415": b1415, "b1516": b1516, "b1617": b1617, "b1718": b1718, "b1819": b1819,
				 "b1920": b1920, "b2021": b2021, "b2122": b2122, "c78": c78,  "c89": c89,  "c910": c910,  "c1011": c1011,  "c1112": c1112, 
				 "c1213": c1213, "c1314": c1314, "c1415": c1415, "c1516": c1516, "c1617": c1617, "c1718": c1718, "c1819": c1819,
				 "c1920": c1920, "c2021": c2021, "c2122": c2122, "d78": d78,  "d89": d89,  "d910": d910,  "d1011": d1011,  "d1112": d1112, 
				 "d1213": d1213, "d1314": d1314, "d1415": d1415, "d1516": d1516, "d1617": d1617, "d1718": d1718, "d1819": d1819,
				 "d1920": d1920, "d2021": d2021, "d2122": d2122, "e78": e78,  "e89": e89,  "e910": e910,  "e1011": e1011,  "e1112": e1112, 
				 "e1213": e1213, "e1314": e1314, "e1415": e1415, "e1516": e1516, "e1617": e1617, "e1718": e1718, "e1819": e1819,
				 "e1920": e1920, "e2021": e2021, "e2122": e2122, "f78": f78,  "f89": f89,  "f910": f910,  "f1011": f1011,  "f1112": f1112, 
				 "f1213": f1213, "f1314": f1314, "f1415": f1415, "f1516": f1516, "f1617": f1617, "f1718": f1718, "f1819": f1819,
				 "f1920": f1920, "f2021": f2021, "f2122": f2122, "g78": g78,  "g89": g89,  "g910": g910,  "g1011": g1011,  "g1112": g1112, 
				 "g1213": g1213, "g1314": g1314, "g1415": g1415, "g1516": g1516, "g1617": g1617, "g1718": g1718, "g1819": g1819,
				 "g1920": g1920, "g2021": g2021, "g2122": g2122, "varGrupo":varGrupo, "varDia":varDia, "varHora":varHora,
				}
		
		else:
			form = ClaseHoraSelForm()
			ctx = {
				"mensaje": "Etc", "form": form, "fase": "fase1"
			}
	else:
		form = ClaseHoraSelForm()
		ctx = { "form": form, "fase": "fase1" }

	return render(request, "Horario/formClaseHora_view.html", ctx)
