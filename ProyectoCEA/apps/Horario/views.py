from django.shortcuts import render, RequestContext, render_to_response, redirect
from django.http import HttpResponse

from .forms import *
from .models import *
from apps.Escuela.forms import *
from apps.Escuela.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#para el pdf
from django.db import connection
from io import BytesIO
#report lab
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import *
from reportlab.platypus import Table
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
#pdf salon
def salones(request):
	print "Genero pdf"
	response = HttpResponse(content_type = 'application/pdf')
	pdf_name = "salones.pdf"
	buffe = BytesIO()
	doc = SimpleDocTemplate(buffe,
							pagesizes= landscape(A4),
							rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
	salones = []
	styles = getSampleStyleSheet()
	header = Paragraph("Departamento de Ciencias Economico Adminsitrativas: Salones", styles['Heading1'])
	salones.append(header)
	headings = ('Numero de salon','Capacidad')
	allsalones = [(a.Nombre,a.Capacidad) for a in Salon.objects.all()]
	print allsalones
	t = Table([headings]+ allsalones)
	t.setStyle(TableStyle(
		[
			('GRID', (0, 0), (14, -1), 1, colors.green),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.azure)
		]
	))
	salones.append(t)
	doc.build(salones)
	doc.pagesize = landscape(A4)
	response.write(buffe.getvalue())
	buffe.close()
	return response


@user_passes_test(lambda u: u.is_superuser)
def formHorarioCarrera(request):
	if request.method == 'POST':
		form = HorarioCarreraForm(request.POST)
		if form.is_valid():
			obj = HorarioCarrera()
			obj.Serie  = form.cleaned_data['Serie']
			obj.FK_Semestre  = form.cleaned_data['FK_Semestre']
			obj.FK_Periodo  = form.cleaned_data['FK_Periodo']
			obj.FK_Carrera  = form.cleaned_data['FK_Carrera']

			filtro = HorarioCarrera.objects.all().filter(Serie=obj.Serie)
			if filtro:
				form = HorarioCarreraForm()
				reporte = HorarioCarreraReporte(HorarioCarrera.objects.all())
				ctx = {
				"mensaje": "Serie de grupo existente.", "form": form, "reporte": reporte
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

@user_passes_test(lambda u: u.is_superuser)
def formHorarioCarreraDel(request):
	if request.method == 'POST':

		form = HorarioCarreraDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = HorarioCarrera.objects.get(Serie=dato)
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

@user_passes_test(lambda u: u.is_superuser)
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
			#QueryGeneral y objeto.
			queryGen = ClaseHora.objects.all()
			Grupo = form.cleaned_data['FK_HorarioCarrera']
			#Obtencion de datos
			a78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Lunes")
			a89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Lunes")
			a910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Lunes")
			a1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Lunes")
			a1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Lunes")
			a1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Lunes")
			a1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Lunes")
			a1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Lunes")
			a1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Lunes")
			a1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Lunes")
			a1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Lunes")
			a1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Lunes")
			a1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Lunes")
			a2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Lunes")
			a2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Lunes")
			b78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Martes")
			b89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Martes")
			b910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Martes")
			b1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Martes")
			b1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Martes")
			b1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Martes")
			b1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Martes")
			b1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Martes")
			b1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Martes")
			b1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Martes")
			b1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Martes")
			b1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Martes")
			b1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Martes")
			b2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Martes")
			b2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Martes")
			c78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Miercoles")
			c89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Miercoles")
			c910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Miercoles")
			c1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Miercoles")
			c1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Miercoles")
			c1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Miercoles")
			c1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Miercoles")
			c1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Miercoles")
			c1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Miercoles")
			c1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Miercoles")
			c1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Miercoles")
			c1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Miercoles")
			c1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Miercoles")
			c2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Miercoles")
			c2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Miercoles")
			d78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Jueves")
			d89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Jueves")
			d910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Jueves")
			d1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Jueves")
			d1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Jueves")
			d1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Jueves")
			d1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Jueves")
			d1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Jueves")
			d1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Jueves")
			d1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Jueves")
			d1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Jueves")
			d1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Jueves")
			d1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Jueves")
			d2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Jueves")
			d2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Jueves")
			e78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Viernes")
			e89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Viernes")
			e910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Viernes")
			e1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Viernes")
			e1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Viernes")
			e1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Viernes")
			e1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Viernes")
			e1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Viernes")
			e1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Viernes")
			e1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Viernes")
			e1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Viernes")
			e1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Viernes")
			e1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Viernes")
			e2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Viernes")
			e2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Viernes")
			f78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Sabado")
			f89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Sabado")
			f910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Sabado")
			f1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Sabado")
			f1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Sabado")
			f1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Sabado")
			f1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Sabado")
			f1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Sabado")
			f1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Sabado")
			f1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Sabado")
			f1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Sabado")
			f1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Sabado")
			f1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Sabado")
			f2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Sabado")
			f2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Sabado")
			g78 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Domingo")
			g89 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Domingo")
			g910 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Domingo")
			g1011 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Domingo")
			g1112 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Domingo")
			g1213 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Domingo")
			g1314 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Domingo")
			g1415 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Domingo")
			g1516 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Domingo")
			g1617 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Domingo")
			g1718 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Domingo")
			g1819 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Domingo")
			g1920 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Domingo")
			g2021 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Domingo")
			g2122 = queryGen.filter(FK_HorarioCarrera = Grupo).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Domingo")

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
			objGru = HorarioCarrera.objects.get(Serie=Grupo)
			obj = ClaseHora.objects.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = EHora).filter(FK_Dia__Nombre = EDia)
			obj.delete()

			#QueryGen
			queryGen = ClaseHora.objects.all()

			#Obtencion de datos
			a78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Lunes")
			a89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Lunes")
			a910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Lunes")
			a1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Lunes")
			a1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Lunes")
			a1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Lunes")
			a1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Lunes")
			a1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Lunes")
			a1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Lunes")
			a1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Lunes")
			a1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Lunes")
			a1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Lunes")
			a1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Lunes")
			a2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Lunes")
			a2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Lunes")
			b78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Martes")
			b89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Martes")
			b910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Martes")
			b1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Martes")
			b1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Martes")
			b1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Martes")
			b1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Martes")
			b1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Martes")
			b1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Martes")
			b1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Martes")
			b1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Martes")
			b1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Martes")
			b1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Martes")
			b2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Martes")
			b2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Martes")
			c78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Miercoles")
			c89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Miercoles")
			c910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Miercoles")
			c1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Miercoles")
			c1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Miercoles")
			c1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Miercoles")
			c1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Miercoles")
			c1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Miercoles")
			c1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Miercoles")
			c1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Miercoles")
			c1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Miercoles")
			c1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Miercoles")
			c1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Miercoles")
			c2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Miercoles")
			c2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Miercoles")
			d78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Jueves")
			d89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Jueves")
			d910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Jueves")
			d1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Jueves")
			d1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Jueves")
			d1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Jueves")
			d1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Jueves")
			d1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Jueves")
			d1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Jueves")
			d1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Jueves")
			d1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Jueves")
			d1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Jueves")
			d1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Jueves")
			d2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Jueves")
			d2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Jueves")
			e78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Viernes")
			e89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Viernes")
			e910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Viernes")
			e1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Viernes")
			e1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Viernes")
			e1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Viernes")
			e1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Viernes")
			e1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Viernes")
			e1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Viernes")
			e1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Viernes")
			e1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Viernes")
			e1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Viernes")
			e1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Viernes")
			e2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Viernes")
			e2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Viernes")
			f78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Sabado")
			f89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Sabado")
			f910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Sabado")
			f1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Sabado")
			f1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Sabado")
			f1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Sabado")
			f1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Sabado")
			f1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Sabado")
			f1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Sabado")
			f1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Sabado")
			f1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Sabado")
			f1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Sabado")
			f1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Sabado")
			f2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Sabado")
			f2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Sabado")
			g78 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Domingo")
			g89 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Domingo")
			g910 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Domingo")
			g1011 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Domingo")
			g1112 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Domingo")
			g1213 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Domingo")
			g1314 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Domingo")
			g1415 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Domingo")
			g1516 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Domingo")
			g1617 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Domingo")
			g1718 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Domingo")
			g1819 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Domingo")
			g1920 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Domingo")
			g2021 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Domingo")
			g2122 = queryGen.filter(FK_HorarioCarrera = objGru).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Domingo")

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
			
			
			filtroProHora = ProfesorHora.objects.filter(FK_Dia__Nombre=GDia).filter(FK_Hora__Nombre=GHora).values('FK_Profesor__NumeroDocente')
			formG.fields["FK_Profesor"].queryset = Profesor.objects.filter(Autorizado="Si").filter(NumeroDocente__in=filtroProHora)
			
			filtroHorCar = HorarioCarrera.objects.get(Serie=Grupo)
			filtroProMat = ProfesorMateria.objects.filter(FK_Profesor__NumeroDocente__in = filtroProHora).values('FK_Materia__Clave')
			formG.fields["FK_Materia"].queryset = Materia.objects.filter(Clave__in=filtroProMat).filter(FK_Carrera=filtroHorCar.FK_Carrera)

			ctx = { "formG": formG, "fase": "fase3", "varGrupo":Grupo, "varDia":GDia, "varHora":GHora, }

		elif (formG.is_valid() and varGrupo and varDia and varHora):

			obj = ClaseHora()
			objHorCar = HorarioCarrera.objects.get(Serie=varGrupo)
			objHora = Hora.objects.get(Nombre=varHora)
			objDia = Dia.objects.get(Nombre=varDia)

			obj.FK_HorarioCarrera  = objHorCar
			obj.FK_Hora  = objHora
			obj.FK_Dia = objDia
			obj.FK_Salon = formG.cleaned_data['FK_Salon']
			obj.FK_Profesor  = formG.cleaned_data['FK_Profesor']
			obj.FK_Materia  = formG.cleaned_data['FK_Materia']

			filtro1 = ClaseHora.objects.all().filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora = objHora).filter(FK_Dia = objDia).filter(FK_HorarioCarrera__FK_Periodo = objHorCar.FK_Periodo)
			filtro2 = ClaseHora.objects.all().filter(FK_Profesor = obj.FK_Profesor).filter(FK_Hora = objHora).filter(FK_Dia = objDia).filter(FK_HorarioCarrera__FK_Periodo = objHorCar.FK_Periodo)
			filtro3 = ClaseHora.objects.all().filter(FK_Salon = obj.FK_Salon).filter(FK_Hora = objHora).filter(FK_Dia = objDia).filter(FK_HorarioCarrera__FK_Periodo = objHorCar.FK_Periodo)
			filtro4 = ProfesorMateria.objects.all().filter(FK_Profesor =obj.FK_Profesor).filter(FK_Materia=obj.FK_Materia)
			
			if filtro1:
				fase = "fase3"
				mensaje = "Espacio ocupado en el mismo horario del grupo."				

			elif filtro2:
				fase = "fase3"
				mensaje = "Profesor no disponible en ese horario. Datos: " + str(filtro2)

			elif filtro3:
				fase = "fase3"
				mensaje = "Salon ocupado en ese horario. Datos: " + str(filtro3)

			elif filtro4 == None:
				fase = "fase3"
				mensaje = "Maestro sin disponibilidad de materia, asignar primero" + str(filtro4)

			else:
				obj.save()
				formG = ClaseHoraForm()
				fase = "fase2"
				mensaje = "Guardado"

			#QueryGen
			queryGen = ClaseHora.objects.all()

			#Obtencion de datos
			a78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Lunes")
			a89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Lunes")
			a910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Lunes")
			a1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Lunes")
			a1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Lunes")
			a1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Lunes")
			a1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Lunes")
			a1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Lunes")
			a1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Lunes")
			a1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Lunes")
			a1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Lunes")
			a1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Lunes")
			a1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Lunes")
			a2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Lunes")
			a2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Lunes")
			b78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Martes")
			b89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Martes")
			b910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Martes")
			b1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Martes")
			b1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Martes")
			b1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Martes")
			b1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Martes")
			b1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Martes")
			b1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Martes")
			b1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Martes")
			b1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Martes")
			b1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Martes")
			b1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Martes")
			b2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Martes")
			b2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Martes")
			c78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Miercoles")
			c89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Miercoles")
			c910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Miercoles")
			c1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Miercoles")
			c1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Miercoles")
			c1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Miercoles")
			c1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Miercoles")
			c1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Miercoles")
			c1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Miercoles")
			c1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Miercoles")
			c1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Miercoles")
			c1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Miercoles")
			c1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Miercoles")
			c2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Miercoles")
			c2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Miercoles")
			d78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Jueves")
			d89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Jueves")
			d910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Jueves")
			d1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Jueves")
			d1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Jueves")
			d1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Jueves")
			d1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Jueves")
			d1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Jueves")
			d1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Jueves")
			d1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Jueves")
			d1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Jueves")
			d1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Jueves")
			d1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Jueves")
			d2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Jueves")
			d2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Jueves")
			e78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Viernes")
			e89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Viernes")
			e910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Viernes")
			e1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Viernes")
			e1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Viernes")
			e1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Viernes")
			e1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Viernes")
			e1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Viernes")
			e1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Viernes")
			e1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Viernes")
			e1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Viernes")
			e1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Viernes")
			e1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Viernes")
			e2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Viernes")
			e2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Viernes")
			f78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Sabado")
			f89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Sabado")
			f910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Sabado")
			f1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Sabado")
			f1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Sabado")
			f1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Sabado")
			f1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Sabado")
			f1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Sabado")
			f1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Sabado")
			f1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Sabado")
			f1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Sabado")
			f1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Sabado")
			f1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Sabado")
			f2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Sabado")
			f2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Sabado")
			g78 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "7-8").filter(FK_Dia__Nombre = "Domingo")
			g89 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "8-9").filter(FK_Dia__Nombre = "Domingo")
			g910 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "9-10").filter(FK_Dia__Nombre = "Domingo")
			g1011 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "10-11").filter(FK_Dia__Nombre = "Domingo")
			g1112 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "11-12").filter(FK_Dia__Nombre = "Domingo")
			g1213 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "12-13").filter(FK_Dia__Nombre = "Domingo")
			g1314 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "13-14").filter(FK_Dia__Nombre = "Domingo")
			g1415 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "14-15").filter(FK_Dia__Nombre = "Domingo")
			g1516 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "15-16").filter(FK_Dia__Nombre = "Domingo")
			g1617 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "16-17").filter(FK_Dia__Nombre = "Domingo")
			g1718 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "17-18").filter(FK_Dia__Nombre = "Domingo")
			g1819 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "18-19").filter(FK_Dia__Nombre = "Domingo")
			g1920 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "19-20").filter(FK_Dia__Nombre = "Domingo")
			g2021 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "20-21").filter(FK_Dia__Nombre = "Domingo")
			g2122 = queryGen.filter(FK_HorarioCarrera = objHorCar).filter(FK_Hora__Nombre = "21-22").filter(FK_Dia__Nombre = "Domingo")

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
