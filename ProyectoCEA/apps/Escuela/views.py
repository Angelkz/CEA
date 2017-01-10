from django.shortcuts import render, RequestContext, render_to_response, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



# Create your views here.

def registroUsu(request):
	mensaje =""
	if request.method == "POST":
		formulario = UsuarioForm(request.POST, request.FILES)
		if formulario.is_valid():

			#Captura de los campos del formulario
			username	=   formulario.cleaned_data['Username']
			password	=	formulario.cleaned_data['Password']
			#Validacion
			user = User.objects.filter(username=username)
			if user:
        			mensaje = 'Usuario ya registrado, ingresa otro'
			
			else:
					#Registro en el Modelo
					p 		= 	User()
					p.username = username
					p.set_password(password)
					p.save()
					# u = PerfilUsuario()
					# u.Usuario = p
					# u.save()
					mensaje = 'Usuario registrado completamente'
			
	else:
		formulario = UsuarioForm()

	formulario = UsuarioForm()
	ctx = 	{'form':formulario, 'mensaje':mensaje}
	return render_to_response('Escuela/registroUsu.html',ctx,context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def formTitulo(request):
	if request.method == 'POST':

		form = TituloForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['Nombre']
			objV = Titulo.objects.filter(Nombre=varV)
			if objV:
				form = TituloForm(request.POST)
				reporte = TituloReporte(Titulo.objects.all())
				ctx = {
				"mensaje": "Titulo ya registrado, ingresar otro", "form": form, "reporte": reporte
				}
			else:
				form.save()
				form = TituloForm()
				reporte = TituloReporte(Titulo.objects.all())
				ctx = {
					"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = TituloForm()
			reporte = TituloReporte(Titulo.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}

	else:
		form = TituloForm()
		reporte = TituloReporte(Titulo.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formTitulo_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formTituloDel(request):
	if request.method == 'POST':

		form = TituloDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = Titulo.objects.get(Nombre=dato)
			formDel.delete()

			form = TituloDelForm()
			reporte = TituloReporte(Titulo.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = TituloDelForm()
			reporte = TituloReporte(Titulo.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = TituloDelForm()
		reporte = TituloReporte(Titulo.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formTituloDel_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formGradoMaximo(request):
	if request.method == 'POST':

		form = GradoMaximoForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['Nombre']
			objV = GradoMaximo.objects.filter(Nombre=varV)
			if objV:
				form = GradoMaximoForm(request.POST)
				reporte = GradoMaximoReporte(GradoMaximo.objects.all())
				ctx = {
				"mensaje": "Grado Maximo ya registrado, ingresar otro", "form": form, "reporte": reporte
				}
			else:
				form.save()
				form = GradoMaximoForm()
				reporte = GradoMaximoReporte(GradoMaximo.objects.all())
				ctx = {
					"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = GradoMaximoForm()
			reporte = GradoMaximoReporte(GradoMaximo.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}

	else:
		form = GradoMaximoForm()
		reporte = GradoMaximoReporte(GradoMaximo.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formGradoMaximo_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formGradoMaximoDel(request):
	if request.method == 'POST':

		form = GradoMaximoDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = GradoMaximo.objects.get(Nombre=dato)
			formDel.delete()

			form = GradoMaximoDelForm()
			reporte = GradoMaximoReporte(GradoMaximo.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = GradoMaximoDelForm()
			reporte = GradoMaximoReporte(GradoMaximo.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = GradoMaximoDelForm()
		reporte = GradoMaximoReporte(GradoMaximo.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formGradoMaximoDel_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formCarrera(request):
	if request.method == 'POST':

		form = CarreraForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['Nombre']
			objV = Carrera.objects.filter(Nombre=varV)
			if objV:
				form = CarreraForm(request.POST)
				reporte = CarreraReporte(Carrera.objects.all())
				ctx = {
				"mensaje": "Carrera ya registrado, ingresar otro", "form": form, "reporte": reporte
				}
			else:
				form.save()
				form = CarreraForm()
				reporte = CarreraReporte(Carrera.objects.all())
				ctx = {
					"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = CarreraForm()
			reporte = CarreraReporte(Carrera.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}

	else:
		form = CarreraForm()
		reporte = CarreraReporte(Carrera.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formCarrera_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formCarreraDel(request):
	if request.method == 'POST':

		form = CarreraDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = Carrera.objects.get(Nombre=dato)
			formDel.delete()

			form = CarreraDelForm()
			reporte = CarreraReporte(Carrera.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = CarreraDelForm()
			reporte = CarreraReporte(Carrera.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = CarreraDelForm()
		reporte = CarreraReporte(Carrera.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formCarreraDel_view.html", ctx)

@login_required
def formProfesor(request):
	if request.method == 'POST':
		form = ProfesorForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['NumeroDocente']
			objV = Profesor.objects.filter(NumeroDocente=varV)
			if objV:
				ctx = {
				"mensaje": "Numero de docente ya registrado.", "form": form
				}
			else:
				form.save()
				form = ProfesorForm()
				ctx = {
					"mensaje": "Guardado", "form": form
				}
		else:
			ctx = {
				"mensaje": "Formulario incompleto", "form": form
			}

	else:
		form = ProfesorForm()
		ctx = { "form": form}

	return render(request, "Escuela/formProfesor_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formProfesorAut(request):
	if request.method == 'POST':

		form = ProfesorAutForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = str(form.cleaned_data['Nombre'])
			datoP = dato.partition(" ")
			formAut = Profesor.objects.get(NumeroDocente=datoP[0])
			formAut.Autorizado = "Si"
			formAut.save()

			form = ProfesorAutForm()
			reporte1 = ProfesorReporteContacto(Profesor.objects.all())
			reporte2 = ProfesorReporteProfesionales(Profesor.objects.all())
			reporte3 = ProfesorReporteDisponibilidad(Profesor.objects.all())
			ctx = {
				"mensaje": "Autorizado", "form": form, "reporte1": reporte1, "reporte2": reporte2, "reporte3": reporte3
			}
		else:
			form = ProfesorAutForm()
			reporte1 = ProfesorReporteContacto(Profesor.objects.all())
			reporte2 = ProfesorReporteProfesionales(Profesor.objects.all())
			reporte3 = ProfesorReporteDisponibilidad(Profesor.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte1": reporte1, "reporte2": reporte2, "reporte3": reporte3
			}

	else:
		form = ProfesorAutForm()
		reporte1 = ProfesorReporteContacto(Profesor.objects.all())
		reporte2 = ProfesorReporteProfesionales(Profesor.objects.all())
		reporte3 = ProfesorReporteDisponibilidad(Profesor.objects.all())
		ctx = { "form": form, "reporte1": reporte1, "reporte2": reporte2, "reporte3": reporte3 }

	return render(request, "Escuela/formProfesorAut_view.html", ctx)

#Reporte todos los profesores
@user_passes_test(lambda u: u.is_superuser)
def imprimir(request):
	#c=canvas.Canvas("test.pdf", pagesize = A4)
	#c.drawImage("static/images/1.png", 0, A4[1]/2, width=400, height=400)
	#c.showPage()
	#c.save()

	print "Genero pdf"
	response = HttpResponse(content_type = 'application/pdf')
	pdf_name = "profesores.pdf"
	buff = BytesIO()
	doc = SimpleDocTemplate(buff,
							pagesizes= landscape(A4),
							rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
	profes = []
	styles = getSampleStyleSheet()
	header = Paragraph("Departamento de Ciencias Economico Administravivas", styles['Heading1'])
	profes.append(header)
	headings = ('# Empleado',' Nombre','A Paterno','A Materno','titulo','Grado','Celular','T Casa','Email','Tutorias','Horario','Lab','Paqueteria')
	allprofes = [(p.NumeroDocente, p.Nombre , p.ApellidoPaterno, p.ApellidoMaterno, p.FK_Titulo, p.FK_GradoMaximo, p.TelefonoCelular, p.TelefonoCasa, p.Email, p.Tutorias, p.FK_NumeroHoras, p.Laboratorio, p.Paquete) for p in Profesor.objects.all()]
	print allprofes
	t = Table([headings]+ allprofes)
	t.setStyle(TableStyle(
		[
			('GRID', (0, 0), (14, -1), 1, colors.green),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.azure)
		]
	))
	profes.append(t)
	doc.pagesize = landscape(A4)
	doc.build(profes)
	response.write(buff.getvalue())
	buff.close()
	return response

@user_passes_test(lambda u: u.is_superuser)
def formProfesorDel(request):
	if request.method == 'POST':

		form = ProfesorDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = str(form.cleaned_data['Nombre'])
			datoP = dato.partition(" ")
			formDel = Profesor.objects.get(NumeroDocente=datoP[0])
			formDel.delete()

			form = ProfesorDelForm()
			reporte1 = ProfesorReporteContacto(Profesor.objects.all())
			reporte2 = ProfesorReporteProfesionales(Profesor.objects.all())
			reporte3 = ProfesorReporteDisponibilidad(Profesor.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte1": reporte1, "reporte2": reporte2, "reporte3": reporte3
			}
		else:
			form = ProfesorDelForm()
			reporte1 = ProfesorReporteContacto(Profesor.objects.all())
			reporte2 = ProfesorReporteProfesionales(Profesor.objects.all())
			reporte3 = ProfesorReporteDisponibilidad(Profesor.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte1": reporte1, "reporte2": reporte2, "reporte3": reporte3
			}

	else:
		form = ProfesorDelForm()
		reporte1 = ProfesorReporteContacto(Profesor.objects.all())
		reporte2 = ProfesorReporteProfesionales(Profesor.objects.all())
		reporte3 = ProfesorReporteDisponibilidad(Profesor.objects.all())
		ctx = { "form": form, "reporte1": reporte1, "reporte2": reporte2, "reporte3": reporte3 }

	return render(request, "Escuela/formProfesorDel_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formMateria(request):
	if request.method == 'POST':

		form = MateriaForm(request.POST)
		
		if (form.is_valid()):
			varV= form.cleaned_data['Clave']
			objV = Materia.objects.filter(Clave=varV)
			if objV:
				form = MateriaForm(request.POST)
				reporte = MateriaReporte(Materia.objects.all())
				ctx = {
				"mensaje": "Materia ya registrada, ingresar otra", "form": form, "reporte": reporte
				}
			else:
				form.save()
				form = MateriaForm()
				reporte = MateriaReporte(Materia.objects.all())
				ctx = {
					"mensaje": "Guardado", "form": form, "reporte": reporte
				}
		else:
			form = MateriaForm()
			reporte = MateriaReporte(Materia.objects.all())
			ctx = {
				"mensaje": "Formulario incompleto", "form": form, "reporte": reporte
			}

	else:
		form = MateriaForm()
		reporte = MateriaReporte(Materia.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formMateria_view.html", ctx)

@user_passes_test(lambda u: u.is_superuser)
def formMateriaDel(request):
	if request.method == 'POST':

		form = MateriaDelForm(request.POST, request.FILES)
		
		if (form.is_valid()):
			dato = form.cleaned_data['Nombre']
			formDel = Materia.objects.get(Nombre=dato)
			formDel.delete()

			form = MateriaDelForm()
			reporte = MateriaReporte(Materia.objects.all())
			ctx = {
				"mensaje": "Eliminado", "form": form, "reporte": reporte
			}
		else:
			form = MateriaDelForm()
			reporte = MateriaReporte(Materia.objects.all())
			ctx = {
				"mensaje": "Sin seleccion", "form": form, "reporte": reporte
			}

	else:
		form = MateriaDelForm()
		reporte = MateriaReporte(Materia.objects.all())
		ctx = { "form": form, "reporte": reporte }

	return render(request, "Escuela/formMateriaDel_view.html", ctx)

#pdf materia 
#Reporte todos las materias
@user_passes_test(lambda u: u.is_superuser)
def imprimirmateria(request):
	#c=canvas.Canvas("test.pdf", pagesize = A4)
	#c.drawImage("static/images/1.png", 0, A4[1]/2, width=400, height=400)
	#c.showPage()
	#c.save()

	print "Genero pdf"
	response = HttpResponse(content_type = 'application/pdf')
	pdf_name = "materias.pdf"
	buf = BytesIO()
	doc = SimpleDocTemplate(buf,
							pagesizes= landscape(A4),
							rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
	materias = []
	styles = getSampleStyleSheet()
	header = Paragraph(" Departamento de Ciencias Economico Administravivas: Materias", styles['Heading2'])
	materias.append(header)
	headings = ('Nombre','Clave','HorasTeoricas','HorasPracticas','Creditos','Carrera')
	allmaterias = [(m.Nombre,m.Clave,m.HorasTeoricas,m.HorasPracticas,m.Creditos,m.FK_Carrera) for m in Materia.objects.all()]
	print allmaterias
	t = Table([headings]+ allmaterias)
	t.setStyle(TableStyle(
		[
			('GRID', (0, 0), (14, -1), 1, colors.green),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.azure)
		]
	))
	materias.append(t)
	doc.pagesize = landscape(A4)
	doc.build(materias)
	response.write(buf.getvalue())
	buf.close()
	return response

@login_required
def formProfesorMateria(request):
	if request.method == 'POST':

		formP = ProfesorMateriaConForm(request.POST)
		formM = ProfesorMateriaForm(request.POST)
		Pro = request.POST.get('Pro')
		Mat =request.POST.get('Mat')
		
		if (formP.is_valid()):
			
			reporte = ProfesorMateria.objects.all().filter(FK_Profesor=formP.cleaned_data['FK_Profesor'])
			ctx = {
				"formM": formM, "reporte": reporte, "fase": False, "profesor": formP.cleaned_data['FK_Profesor']
			}

		elif(formM.is_valid()):
				datoP = Pro.partition(" ")
				varValPro = Profesor.objects.get(NumeroDocente=datoP[0])
				varValMat= formM.cleaned_data['FK_Materia']
				objV = ProfesorMateria.objects.filter(FK_Profesor=varValPro).filter(FK_Materia=varValMat)
				if objV:
					formM = ProfesorMateriaForm()
					reporte = ProfesorMateria.objects.all().filter(FK_Profesor=varValPro)
					ctx = {
					"mensaje": "Materia en el profesor ya registrada, ingresar otra", "formM": formM, "reporte": reporte, "fase": False, "profesor": Pro
					}
				else:
					obj = ProfesorMateria()
					obj.FK_Profesor = varValPro
					obj.FK_Materia = varValMat
					obj.save()
					formM = ProfesorMateriaForm()
					reporte = ProfesorMateria.objects.all().filter(FK_Profesor=varValPro)
					ctx = {
						"mensaje": "Guardado", "formM": formM, "reporte": reporte, "fase": False, "profesor": Pro
					}

		elif(Pro and Mat):
			datoP = Pro.partition(" ")
			objPro = Profesor.objects.get(NumeroDocente=datoP[0])
			datoM = Mat.partition(" ")
			obj = ProfesorMateria.objects.filter(FK_Profesor = objPro).filter(FK_Materia__Clave = datoM[0])
			obj.delete()
			reporte = ProfesorMateria.objects.all().filter(FK_Profesor=objPro)
			ctx = {
				"mensaje": "Eliminado", "reporte": reporte, "formM": formM, "fase": False, "profesor": Pro
			}

		else:
			formP = ProfesorMateriaConForm()
			formM = ProfesorMateriaForm()
			ctx = {
				"mensaje": "Sin seleccion", "formP": formP, "fase": True
			}

	else:
		formP = ProfesorMateriaConForm()
		ctx = { "formP": formP, "fase": True }

	return render(request, "Escuela/formProfesorMateria_view.html", ctx)

@login_required
def formProfesorHora(request):
	
	if request.method == 'POST':

		formP = ProfesorHoraConForm(request.POST)
		GHora = request.POST.get('GHora')
		GDia = request.POST.get('GDia')
		EHora = request.POST.get('EHora')
		EDia = request.POST.get('EDia')
		Pro = request.POST.get('Profesor')

		if (formP.is_valid()):

			profesor = formP.cleaned_data['FK_Profesor']
			query = ProfesorHora.objects.all().filter(FK_Profesor= profesor)

			lunes = query.filter(FK_Dia__Nombre = "Lunes")
			martes = query.filter(FK_Dia__Nombre = "Martes")
			miercoles = query.filter(FK_Dia__Nombre = "Miercoles")
			jueves = query.filter(FK_Dia__Nombre = "Jueves")
			viernes = query.filter(FK_Dia__Nombre = "Viernes")
			sabado = query.filter(FK_Dia__Nombre = "Sabado")
			domingo = query.filter(FK_Dia__Nombre = "Domingo")

			#Lunes
			if (lunes.filter(FK_Hora__Nombre = "7-8")):
				a78 = "D"
			else:
				a78 = "-"
			if (lunes.filter(FK_Hora__Nombre = "8-9")):
				a89 = "D"
			else:
				a89 = "-"
			if (lunes.filter(FK_Hora__Nombre = "9-10")):
				a910 = "D"
			else:
				a910 = "-"
			if (lunes.filter(FK_Hora__Nombre = "10-11")):
				a1011 = "D"
			else:
				a1011 = "-"
			if (lunes.filter(FK_Hora__Nombre = "11-12")):
				a1112 = "D"
			else:
				a1112 = "-"
			if (lunes.filter(FK_Hora__Nombre = "12-13")):
				a1213 = "D"
			else:
				a1213 = "-"
			if (lunes.filter(FK_Hora__Nombre = "13-14")):
				a1314 = "D"
			else:
				a1314 = "-"
			if (lunes.filter(FK_Hora__Nombre = "14-15")):
				a1415 = "D"
			else:
				a1415 = "-"
			if (lunes.filter(FK_Hora__Nombre = "15-16")):
				a1516 = "D"
			else:
				a1516 = "-"
			if (lunes.filter(FK_Hora__Nombre = "16-17")):
				a1617 = "D"
			else:
				a1617 = "-"
			if (lunes.filter(FK_Hora__Nombre = "17-18")):
				a1718 = "D"
			else:
				a1718 = "-"
			if (lunes.filter(FK_Hora__Nombre = "18-19")):
				a1819 = "D"
			else:
				a1819 = "-"
			if (lunes.filter(FK_Hora__Nombre = "19-20")):
				a1920 = "D"
			else:
				a1920 = "-"
			if (lunes.filter(FK_Hora__Nombre = "20-21")):
				a2021 = "D"
			else:
				a2021 = "-"
			if (lunes.filter(FK_Hora__Nombre = "21-22")):
				a2122 = "D"
			else:
				a2122 = "-"

			#Martes
			if (martes.filter(FK_Hora__Nombre = "7-8")):
				b78 = "D"
			else:
				b78 = "-"
			if (martes.filter(FK_Hora__Nombre = "8-9")):
				b89 = "D"
			else:
				b89 = "-"
			if (martes.filter(FK_Hora__Nombre = "9-10")):
				b910 = "D"
			else:
				b910 = "-"
			if (martes.filter(FK_Hora__Nombre = "10-11")):
				b1011 = "D"
			else:
				b1011 = "-"
			if (martes.filter(FK_Hora__Nombre = "11-12")):
				b1112 = "D"
			else:
				b1112 = "-"
			if (martes.filter(FK_Hora__Nombre = "12-13")):
				b1213 = "D"
			else:
				b1213 = "-"
			if (martes.filter(FK_Hora__Nombre = "13-14")):
				b1314 = "D"
			else:
				b1314 = "-"
			if (martes.filter(FK_Hora__Nombre = "14-15")):
				b1415 = "D"
			else:
				b1415 = "-"
			if (martes.filter(FK_Hora__Nombre = "15-16")):
				b1516 = "D"
			else:
				b1516 = "-"
			if (martes.filter(FK_Hora__Nombre = "16-17")):
				b1617 = "D"
			else:
				b1617 = "-"
			if (martes.filter(FK_Hora__Nombre = "17-18")):
				b1718 = "D"
			else:
				b1718 = "-"
			if (martes.filter(FK_Hora__Nombre = "18-19")):
				b1819 = "D"
			else:
				b1819 = "-"
			if (martes.filter(FK_Hora__Nombre = "19-20")):
				b1920 = "D"
			else:
				b1920 = "-"
			if (martes.filter(FK_Hora__Nombre = "20-21")):
				b2021 = "D"
			else:
				b2021 = "-"
			if (martes.filter(FK_Hora__Nombre = "21-22")):
				b2122 = "D"
			else:
				b2122 = "-"

			#Miercoles
			if (miercoles.filter(FK_Hora__Nombre = "7-8")):
				c78 = "D"
			else:
				c78 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "8-9")):
				c89 = "D"
			else:
				c89 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "9-10")):
				c910 = "D"
			else:
				c910 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "10-11")):
				c1011 = "D"
			else:
				c1011 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "11-12")):
				c1112 = "D"
			else:
				c1112 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "12-13")):
				c1213 = "D"
			else:
				c1213 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "13-14")):
				c1314 = "D"
			else:
				c1314 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "14-15")):
				c1415 = "D"
			else:
				c1415 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "15-16")):
				c1516 = "D"
			else:
				c1516 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "16-17")):
				c1617 = "D"
			else:
				c1617 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "17-18")):
				c1718 = "D"
			else:
				c1718 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "18-19")):
				c1819 = "D"
			else:
				c1819 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "19-20")):
				c1920 = "D"
			else:
				c1920 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "20-21")):
				c2021 = "D"
			else:
				c2021 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "21-22")):
				c2122 = "D"
			else:
				c2122 = "-"

			#Jueves
			if (jueves.filter(FK_Hora__Nombre = "7-8")):
				d78 = "D"
			else:
				d78 = "-"
			if (jueves.filter(FK_Hora__Nombre = "8-9")):
				d89 = "D"
			else:
				d89 = "-"
			if (jueves.filter(FK_Hora__Nombre = "9-10")):
				d910 = "D"
			else:
				d910 = "-"
			if (jueves.filter(FK_Hora__Nombre = "10-11")):
				d1011 = "D"
			else:
				d1011 = "-"
			if (jueves.filter(FK_Hora__Nombre = "11-12")):
				d1112 = "D"
			else:
				d1112 = "-"
			if (jueves.filter(FK_Hora__Nombre = "12-13")):
				d1213 = "D"
			else:
				d1213 = "-"
			if (jueves.filter(FK_Hora__Nombre = "13-14")):
				d1314 = "D"
			else:
				d1314 = "-"
			if (jueves.filter(FK_Hora__Nombre = "14-15")):
				d1415 = "D"
			else:
				d1415 = "-"
			if (jueves.filter(FK_Hora__Nombre = "15-16")):
				d1516 = "D"
			else:
				d1516 = "-"
			if (jueves.filter(FK_Hora__Nombre = "16-17")):
				d1617 = "D"
			else:
				d1617 = "-"
			if (jueves.filter(FK_Hora__Nombre = "17-18")):
				d1718 = "D"
			else:
				d1718 = "-"
			if (jueves.filter(FK_Hora__Nombre = "18-19")):
				d1819 = "D"
			else:
				d1819 = "-"
			if (jueves.filter(FK_Hora__Nombre = "19-20")):
				d1920 = "D"
			else:
				d1920 = "-"
			if (jueves.filter(FK_Hora__Nombre = "20-21")):
				d2021 = "D"
			else:
				d2021 = "-"
			if (jueves.filter(FK_Hora__Nombre = "21-22")):
				d2122 = "D"
			else:
				d2122 = "-"

			#Viernes
			if (viernes.filter(FK_Hora__Nombre = "7-8")):
				e78 = "D"
			else:
				e78 = "-"
			if (viernes.filter(FK_Hora__Nombre = "8-9")):
				e89 = "D"
			else:
				e89 = "-"
			if (viernes.filter(FK_Hora__Nombre = "9-10")):
				e910 = "D"
			else:
				e910 = "-"
			if (viernes.filter(FK_Hora__Nombre = "10-11")):
				e1011 = "D"
			else:
				e1011 = "-"
			if (viernes.filter(FK_Hora__Nombre = "11-12")):
				e1112 = "D"
			else:
				e1112 = "-"
			if (viernes.filter(FK_Hora__Nombre = "12-13")):
				e1213 = "D"
			else:
				e1213 = "-"
			if (viernes.filter(FK_Hora__Nombre = "13-14")):
				e1314 = "D"
			else:
				e1314 = "-"
			if (viernes.filter(FK_Hora__Nombre = "14-15")):
				e1415 = "D"
			else:
				e1415 = "-"
			if (viernes.filter(FK_Hora__Nombre = "15-16")):
				e1516 = "D"
			else:
				e1516 = "-"
			if (viernes.filter(FK_Hora__Nombre = "16-17")):
				e1617 = "D"
			else:
				e1617 = "-"
			if (viernes.filter(FK_Hora__Nombre = "17-18")):
				e1718 = "D"
			else:
				e1718 = "-"
			if (viernes.filter(FK_Hora__Nombre = "18-19")):
				e1819 = "D"
			else:
				e1819 = "-"
			if (viernes.filter(FK_Hora__Nombre = "19-20")):
				e1920 = "D"
			else:
				e1920 = "-"
			if (viernes.filter(FK_Hora__Nombre = "20-21")):
				e2021 = "D"
			else:
				e2021 = "-"
			if (viernes.filter(FK_Hora__Nombre = "21-22")):
				e2122 = "D"
			else:
				e2122 = "-"

			#Sabado
			if (sabado.filter(FK_Hora__Nombre = "7-8")):
				f78 = "D"
			else:
				f78 = "-"
			if (sabado.filter(FK_Hora__Nombre = "8-9")):
				f89 = "D"
			else:
				f89 = "-"
			if (sabado.filter(FK_Hora__Nombre = "9-10")):
				f910 = "D"
			else:
				f910 = "-"
			if (sabado.filter(FK_Hora__Nombre = "10-11")):
				f1011 = "D"
			else:
				f1011 = "-"
			if (sabado.filter(FK_Hora__Nombre = "11-12")):
				f1112 = "D"
			else:
				f1112 = "-"
			if (sabado.filter(FK_Hora__Nombre = "12-13")):
				f1213 = "D"
			else:
				f1213 = "-"
			if (sabado.filter(FK_Hora__Nombre = "13-14")):
				f1314 = "D"
			else:
				f1314 = "-"
			if (sabado.filter(FK_Hora__Nombre = "14-15")):
				f1415 = "D"
			else:
				f1415 = "-"
			if (sabado.filter(FK_Hora__Nombre = "15-16")):
				f1516 = "D"
			else:
				f1516 = "-"
			if (sabado.filter(FK_Hora__Nombre = "16-17")):
				f1617 = "D"
			else:
				f1617 = "-"
			if (sabado.filter(FK_Hora__Nombre = "17-18")):
				f1718 = "D"
			else:
				f1718 = "-"
			if (sabado.filter(FK_Hora__Nombre = "18-19")):
				f1819 = "D"
			else:
				f1819 = "-"
			if (sabado.filter(FK_Hora__Nombre = "19-20")):
				f1920 = "D"
			else:
				f1920 = "-"
			if (sabado.filter(FK_Hora__Nombre = "20-21")):
				f2021 = "D"
			else:
				f2021 = "-"
			if (sabado.filter(FK_Hora__Nombre = "21-22")):
				f2122 = "D"
			else:
				f2122 = "-"

			#Domingo
			if (domingo.filter(FK_Hora__Nombre = "7-8")):
				g78 = "D"
			else:
				g78 = "-"
			if (domingo.filter(FK_Hora__Nombre = "8-9")):
				g89 = "D"
			else:
				g89 = "-"
			if (domingo.filter(FK_Hora__Nombre = "9-10")):
				g910 = "D"
			else:
				g910 = "-"
			if (domingo.filter(FK_Hora__Nombre = "10-11")):
				g1011 = "D"
			else:
				g1011 = "-"
			if (domingo.filter(FK_Hora__Nombre = "11-12")):
				g1112 = "D"
			else:
				g1112 = "-"
			if (domingo.filter(FK_Hora__Nombre = "12-13")):
				g1213 = "D"
			else:
				g1213 = "-"
			if (domingo.filter(FK_Hora__Nombre = "13-14")):
				g1314 = "D"
			else:
				g1314 = "-"
			if (domingo.filter(FK_Hora__Nombre = "14-15")):
				g1415 = "D"
			else:
				g1415 = "-"
			if (domingo.filter(FK_Hora__Nombre = "15-16")):
				g1516 = "D"
			else:
				g1516 = "-"
			if (domingo.filter(FK_Hora__Nombre = "16-17")):
				g1617 = "D"
			else:
				g1617 = "-"
			if (domingo.filter(FK_Hora__Nombre = "17-18")):
				g1718 = "D"
			else:
				g1718 = "-"
			if (domingo.filter(FK_Hora__Nombre = "18-19")):
				g1819 = "D"
			else:
				g1819 = "-"
			if (domingo.filter(FK_Hora__Nombre = "19-20")):
				g1920 = "D"
			else:
				g1920 = "-"
			if (domingo.filter(FK_Hora__Nombre = "20-21")):
				g2021 = "D"
			else:
				g2021 = "-"
			if (domingo.filter(FK_Hora__Nombre = "21-22")):
				g2122 = "D"
			else:
				g2122 = "-"

			form = ProfesorHoraConForm()
			ctx = {
				 "form": form, "fase": False, "profesor": profesor, "a78": a78,  "a89": a89,  "a910": a910,  "a1011": a1011,  "a1112": a1112, 
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
		
		elif (GDia and GHora and Pro):
			datoP = Pro.partition(" ")
			objPro = Profesor.objects.get(NumeroDocente=datoP[0])
			objGDia = Dia.objects.get(Nombre=GDia)
			objGHora = Hora.objects.get(Nombre=GHora)
			obj = ProfesorHora()
			obj.FK_Profesor = objPro
			obj.FK_Dia = objGDia
			obj.FK_Hora = objGHora
			obj.save()

			query = ProfesorHora.objects.all().filter(FK_Profesor= objPro)
			lunes = query.filter(FK_Dia__Nombre = "Lunes")
			martes = query.filter(FK_Dia__Nombre = "Martes")
			miercoles = query.filter(FK_Dia__Nombre = "Miercoles")
			jueves = query.filter(FK_Dia__Nombre = "Jueves")
			viernes = query.filter(FK_Dia__Nombre = "Viernes")
			sabado = query.filter(FK_Dia__Nombre = "Sabado")
			domingo = query.filter(FK_Dia__Nombre = "Domingo")

			#Lunes
			if (lunes.filter(FK_Hora__Nombre = "7-8")):
				a78 = "D"
			else:
				a78 = "-"
			if (lunes.filter(FK_Hora__Nombre = "8-9")):
				a89 = "D"
			else:
				a89 = "-"
			if (lunes.filter(FK_Hora__Nombre = "9-10")):
				a910 = "D"
			else:
				a910 = "-"
			if (lunes.filter(FK_Hora__Nombre = "10-11")):
				a1011 = "D"
			else:
				a1011 = "-"
			if (lunes.filter(FK_Hora__Nombre = "11-12")):
				a1112 = "D"
			else:
				a1112 = "-"
			if (lunes.filter(FK_Hora__Nombre = "12-13")):
				a1213 = "D"
			else:
				a1213 = "-"
			if (lunes.filter(FK_Hora__Nombre = "13-14")):
				a1314 = "D"
			else:
				a1314 = "-"
			if (lunes.filter(FK_Hora__Nombre = "14-15")):
				a1415 = "D"
			else:
				a1415 = "-"
			if (lunes.filter(FK_Hora__Nombre = "15-16")):
				a1516 = "D"
			else:
				a1516 = "-"
			if (lunes.filter(FK_Hora__Nombre = "16-17")):
				a1617 = "D"
			else:
				a1617 = "-"
			if (lunes.filter(FK_Hora__Nombre = "17-18")):
				a1718 = "D"
			else:
				a1718 = "-"
			if (lunes.filter(FK_Hora__Nombre = "18-19")):
				a1819 = "D"
			else:
				a1819 = "-"
			if (lunes.filter(FK_Hora__Nombre = "19-20")):
				a1920 = "D"
			else:
				a1920 = "-"
			if (lunes.filter(FK_Hora__Nombre = "20-21")):
				a2021 = "D"
			else:
				a2021 = "-"
			if (lunes.filter(FK_Hora__Nombre = "21-22")):
				a2122 = "D"
			else:
				a2122 = "-"

			#Martes
			if (martes.filter(FK_Hora__Nombre = "7-8")):
				b78 = "D"
			else:
				b78 = "-"
			if (martes.filter(FK_Hora__Nombre = "8-9")):
				b89 = "D"
			else:
				b89 = "-"
			if (martes.filter(FK_Hora__Nombre = "9-10")):
				b910 = "D"
			else:
				b910 = "-"
			if (martes.filter(FK_Hora__Nombre = "10-11")):
				b1011 = "D"
			else:
				b1011 = "-"
			if (martes.filter(FK_Hora__Nombre = "11-12")):
				b1112 = "D"
			else:
				b1112 = "-"
			if (martes.filter(FK_Hora__Nombre = "12-13")):
				b1213 = "D"
			else:
				b1213 = "-"
			if (martes.filter(FK_Hora__Nombre = "13-14")):
				b1314 = "D"
			else:
				b1314 = "-"
			if (martes.filter(FK_Hora__Nombre = "14-15")):
				b1415 = "D"
			else:
				b1415 = "-"
			if (martes.filter(FK_Hora__Nombre = "15-16")):
				b1516 = "D"
			else:
				b1516 = "-"
			if (martes.filter(FK_Hora__Nombre = "16-17")):
				b1617 = "D"
			else:
				b1617 = "-"
			if (martes.filter(FK_Hora__Nombre = "17-18")):
				b1718 = "D"
			else:
				b1718 = "-"
			if (martes.filter(FK_Hora__Nombre = "18-19")):
				b1819 = "D"
			else:
				b1819 = "-"
			if (martes.filter(FK_Hora__Nombre = "19-20")):
				b1920 = "D"
			else:
				b1920 = "-"
			if (martes.filter(FK_Hora__Nombre = "20-21")):
				b2021 = "D"
			else:
				b2021 = "-"
			if (martes.filter(FK_Hora__Nombre = "21-22")):
				b2122 = "D"
			else:
				b2122 = "-"

			#Miercoles
			if (miercoles.filter(FK_Hora__Nombre = "7-8")):
				c78 = "D"
			else:
				c78 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "8-9")):
				c89 = "D"
			else:
				c89 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "9-10")):
				c910 = "D"
			else:
				c910 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "10-11")):
				c1011 = "D"
			else:
				c1011 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "11-12")):
				c1112 = "D"
			else:
				c1112 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "12-13")):
				c1213 = "D"
			else:
				c1213 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "13-14")):
				c1314 = "D"
			else:
				c1314 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "14-15")):
				c1415 = "D"
			else:
				c1415 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "15-16")):
				c1516 = "D"
			else:
				c1516 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "16-17")):
				c1617 = "D"
			else:
				c1617 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "17-18")):
				c1718 = "D"
			else:
				c1718 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "18-19")):
				c1819 = "D"
			else:
				c1819 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "19-20")):
				c1920 = "D"
			else:
				c1920 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "20-21")):
				c2021 = "D"
			else:
				c2021 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "21-22")):
				c2122 = "D"
			else:
				c2122 = "-"

			#Jueves
			if (jueves.filter(FK_Hora__Nombre = "7-8")):
				d78 = "D"
			else:
				d78 = "-"
			if (jueves.filter(FK_Hora__Nombre = "8-9")):
				d89 = "D"
			else:
				d89 = "-"
			if (jueves.filter(FK_Hora__Nombre = "9-10")):
				d910 = "D"
			else:
				d910 = "-"
			if (jueves.filter(FK_Hora__Nombre = "10-11")):
				d1011 = "D"
			else:
				d1011 = "-"
			if (jueves.filter(FK_Hora__Nombre = "11-12")):
				d1112 = "D"
			else:
				d1112 = "-"
			if (jueves.filter(FK_Hora__Nombre = "12-13")):
				d1213 = "D"
			else:
				d1213 = "-"
			if (jueves.filter(FK_Hora__Nombre = "13-14")):
				d1314 = "D"
			else:
				d1314 = "-"
			if (jueves.filter(FK_Hora__Nombre = "14-15")):
				d1415 = "D"
			else:
				d1415 = "-"
			if (jueves.filter(FK_Hora__Nombre = "15-16")):
				d1516 = "D"
			else:
				d1516 = "-"
			if (jueves.filter(FK_Hora__Nombre = "16-17")):
				d1617 = "D"
			else:
				d1617 = "-"
			if (jueves.filter(FK_Hora__Nombre = "17-18")):
				d1718 = "D"
			else:
				d1718 = "-"
			if (jueves.filter(FK_Hora__Nombre = "18-19")):
				d1819 = "D"
			else:
				d1819 = "-"
			if (jueves.filter(FK_Hora__Nombre = "19-20")):
				d1920 = "D"
			else:
				d1920 = "-"
			if (jueves.filter(FK_Hora__Nombre = "20-21")):
				d2021 = "D"
			else:
				d2021 = "-"
			if (jueves.filter(FK_Hora__Nombre = "21-22")):
				d2122 = "D"
			else:
				d2122 = "-"

			#Viernes
			if (viernes.filter(FK_Hora__Nombre = "7-8")):
				e78 = "D"
			else:
				e78 = "-"
			if (viernes.filter(FK_Hora__Nombre = "8-9")):
				e89 = "D"
			else:
				e89 = "-"
			if (viernes.filter(FK_Hora__Nombre = "9-10")):
				e910 = "D"
			else:
				e910 = "-"
			if (viernes.filter(FK_Hora__Nombre = "10-11")):
				e1011 = "D"
			else:
				e1011 = "-"
			if (viernes.filter(FK_Hora__Nombre = "11-12")):
				e1112 = "D"
			else:
				e1112 = "-"
			if (viernes.filter(FK_Hora__Nombre = "12-13")):
				e1213 = "D"
			else:
				e1213 = "-"
			if (viernes.filter(FK_Hora__Nombre = "13-14")):
				e1314 = "D"
			else:
				e1314 = "-"
			if (viernes.filter(FK_Hora__Nombre = "14-15")):
				e1415 = "D"
			else:
				e1415 = "-"
			if (viernes.filter(FK_Hora__Nombre = "15-16")):
				e1516 = "D"
			else:
				e1516 = "-"
			if (viernes.filter(FK_Hora__Nombre = "16-17")):
				e1617 = "D"
			else:
				e1617 = "-"
			if (viernes.filter(FK_Hora__Nombre = "17-18")):
				e1718 = "D"
			else:
				e1718 = "-"
			if (viernes.filter(FK_Hora__Nombre = "18-19")):
				e1819 = "D"
			else:
				e1819 = "-"
			if (viernes.filter(FK_Hora__Nombre = "19-20")):
				e1920 = "D"
			else:
				e1920 = "-"
			if (viernes.filter(FK_Hora__Nombre = "20-21")):
				e2021 = "D"
			else:
				e2021 = "-"
			if (viernes.filter(FK_Hora__Nombre = "21-22")):
				e2122 = "D"
			else:
				e2122 = "-"

			#Sabado
			if (sabado.filter(FK_Hora__Nombre = "7-8")):
				f78 = "D"
			else:
				f78 = "-"
			if (sabado.filter(FK_Hora__Nombre = "8-9")):
				f89 = "D"
			else:
				f89 = "-"
			if (sabado.filter(FK_Hora__Nombre = "9-10")):
				f910 = "D"
			else:
				f910 = "-"
			if (sabado.filter(FK_Hora__Nombre = "10-11")):
				f1011 = "D"
			else:
				f1011 = "-"
			if (sabado.filter(FK_Hora__Nombre = "11-12")):
				f1112 = "D"
			else:
				f1112 = "-"
			if (sabado.filter(FK_Hora__Nombre = "12-13")):
				f1213 = "D"
			else:
				f1213 = "-"
			if (sabado.filter(FK_Hora__Nombre = "13-14")):
				f1314 = "D"
			else:
				f1314 = "-"
			if (sabado.filter(FK_Hora__Nombre = "14-15")):
				f1415 = "D"
			else:
				f1415 = "-"
			if (sabado.filter(FK_Hora__Nombre = "15-16")):
				f1516 = "D"
			else:
				f1516 = "-"
			if (sabado.filter(FK_Hora__Nombre = "16-17")):
				f1617 = "D"
			else:
				f1617 = "-"
			if (sabado.filter(FK_Hora__Nombre = "17-18")):
				f1718 = "D"
			else:
				f1718 = "-"
			if (sabado.filter(FK_Hora__Nombre = "18-19")):
				f1819 = "D"
			else:
				f1819 = "-"
			if (sabado.filter(FK_Hora__Nombre = "19-20")):
				f1920 = "D"
			else:
				f1920 = "-"
			if (sabado.filter(FK_Hora__Nombre = "20-21")):
				f2021 = "D"
			else:
				f2021 = "-"
			if (sabado.filter(FK_Hora__Nombre = "21-22")):
				f2122 = "D"
			else:
				f2122 = "-"

			#Domingo
			if (domingo.filter(FK_Hora__Nombre = "7-8")):
				g78 = "D"
			else:
				g78 = "-"
			if (domingo.filter(FK_Hora__Nombre = "8-9")):
				g89 = "D"
			else:
				g89 = "-"
			if (domingo.filter(FK_Hora__Nombre = "9-10")):
				g910 = "D"
			else:
				g910 = "-"
			if (domingo.filter(FK_Hora__Nombre = "10-11")):
				g1011 = "D"
			else:
				g1011 = "-"
			if (domingo.filter(FK_Hora__Nombre = "11-12")):
				g1112 = "D"
			else:
				g1112 = "-"
			if (domingo.filter(FK_Hora__Nombre = "12-13")):
				g1213 = "D"
			else:
				g1213 = "-"
			if (domingo.filter(FK_Hora__Nombre = "13-14")):
				g1314 = "D"
			else:
				g1314 = "-"
			if (domingo.filter(FK_Hora__Nombre = "14-15")):
				g1415 = "D"
			else:
				g1415 = "-"
			if (domingo.filter(FK_Hora__Nombre = "15-16")):
				g1516 = "D"
			else:
				g1516 = "-"
			if (domingo.filter(FK_Hora__Nombre = "16-17")):
				g1617 = "D"
			else:
				g1617 = "-"
			if (domingo.filter(FK_Hora__Nombre = "17-18")):
				g1718 = "D"
			else:
				g1718 = "-"
			if (domingo.filter(FK_Hora__Nombre = "18-19")):
				g1819 = "D"
			else:
				g1819 = "-"
			if (domingo.filter(FK_Hora__Nombre = "19-20")):
				g1920 = "D"
			else:
				g1920 = "-"
			if (domingo.filter(FK_Hora__Nombre = "20-21")):
				g2021 = "D"
			else:
				g2021 = "-"
			if (domingo.filter(FK_Hora__Nombre = "21-22")):
				g2122 = "D"
			else:
				g2122 = "-"

			ctx = {
				 "fase": False, "profesor": Pro, "a78": a78,  "a89": a89,  "a910": a910,  "a1011": a1011,  "a1112": a1112, 
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

		elif (EDia and EHora and Pro):
			datoP = Pro.partition(" ")
			objPro = Profesor.objects.get(NumeroDocente=datoP[0])
			obj = ProfesorHora.objects.filter(FK_Profesor = objPro).filter(FK_Hora__Nombre = EHora).filter(FK_Dia__Nombre = EDia)
			obj.delete()

			query = ProfesorHora.objects.all().filter(FK_Profesor= objPro)
			lunes = query.filter(FK_Dia__Nombre = "Lunes")
			martes = query.filter(FK_Dia__Nombre = "Martes")
			miercoles = query.filter(FK_Dia__Nombre = "Miercoles")
			jueves = query.filter(FK_Dia__Nombre = "Jueves")
			viernes = query.filter(FK_Dia__Nombre = "Viernes")
			sabado = query.filter(FK_Dia__Nombre = "Sabado")
			domingo = query.filter(FK_Dia__Nombre = "Domingo")

			#Lunes
			if (lunes.filter(FK_Hora__Nombre = "7-8")):
				a78 = "D"
			else:
				a78 = "-"
			if (lunes.filter(FK_Hora__Nombre = "8-9")):
				a89 = "D"
			else:
				a89 = "-"
			if (lunes.filter(FK_Hora__Nombre = "9-10")):
				a910 = "D"
			else:
				a910 = "-"
			if (lunes.filter(FK_Hora__Nombre = "10-11")):
				a1011 = "D"
			else:
				a1011 = "-"
			if (lunes.filter(FK_Hora__Nombre = "11-12")):
				a1112 = "D"
			else:
				a1112 = "-"
			if (lunes.filter(FK_Hora__Nombre = "12-13")):
				a1213 = "D"
			else:
				a1213 = "-"
			if (lunes.filter(FK_Hora__Nombre = "13-14")):
				a1314 = "D"
			else:
				a1314 = "-"
			if (lunes.filter(FK_Hora__Nombre = "14-15")):
				a1415 = "D"
			else:
				a1415 = "-"
			if (lunes.filter(FK_Hora__Nombre = "15-16")):
				a1516 = "D"
			else:
				a1516 = "-"
			if (lunes.filter(FK_Hora__Nombre = "16-17")):
				a1617 = "D"
			else:
				a1617 = "-"
			if (lunes.filter(FK_Hora__Nombre = "17-18")):
				a1718 = "D"
			else:
				a1718 = "-"
			if (lunes.filter(FK_Hora__Nombre = "18-19")):
				a1819 = "D"
			else:
				a1819 = "-"
			if (lunes.filter(FK_Hora__Nombre = "19-20")):
				a1920 = "D"
			else:
				a1920 = "-"
			if (lunes.filter(FK_Hora__Nombre = "20-21")):
				a2021 = "D"
			else:
				a2021 = "-"
			if (lunes.filter(FK_Hora__Nombre = "21-22")):
				a2122 = "D"
			else:
				a2122 = "-"

			#Martes
			if (martes.filter(FK_Hora__Nombre = "7-8")):
				b78 = "D"
			else:
				b78 = "-"
			if (martes.filter(FK_Hora__Nombre = "8-9")):
				b89 = "D"
			else:
				b89 = "-"
			if (martes.filter(FK_Hora__Nombre = "9-10")):
				b910 = "D"
			else:
				b910 = "-"
			if (martes.filter(FK_Hora__Nombre = "10-11")):
				b1011 = "D"
			else:
				b1011 = "-"
			if (martes.filter(FK_Hora__Nombre = "11-12")):
				b1112 = "D"
			else:
				b1112 = "-"
			if (martes.filter(FK_Hora__Nombre = "12-13")):
				b1213 = "D"
			else:
				b1213 = "-"
			if (martes.filter(FK_Hora__Nombre = "13-14")):
				b1314 = "D"
			else:
				b1314 = "-"
			if (martes.filter(FK_Hora__Nombre = "14-15")):
				b1415 = "D"
			else:
				b1415 = "-"
			if (martes.filter(FK_Hora__Nombre = "15-16")):
				b1516 = "D"
			else:
				b1516 = "-"
			if (martes.filter(FK_Hora__Nombre = "16-17")):
				b1617 = "D"
			else:
				b1617 = "-"
			if (martes.filter(FK_Hora__Nombre = "17-18")):
				b1718 = "D"
			else:
				b1718 = "-"
			if (martes.filter(FK_Hora__Nombre = "18-19")):
				b1819 = "D"
			else:
				b1819 = "-"
			if (martes.filter(FK_Hora__Nombre = "19-20")):
				b1920 = "D"
			else:
				b1920 = "-"
			if (martes.filter(FK_Hora__Nombre = "20-21")):
				b2021 = "D"
			else:
				b2021 = "-"
			if (martes.filter(FK_Hora__Nombre = "21-22")):
				b2122 = "D"
			else:
				b2122 = "-"

			#Miercoles
			if (miercoles.filter(FK_Hora__Nombre = "7-8")):
				c78 = "D"
			else:
				c78 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "8-9")):
				c89 = "D"
			else:
				c89 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "9-10")):
				c910 = "D"
			else:
				c910 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "10-11")):
				c1011 = "D"
			else:
				c1011 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "11-12")):
				c1112 = "D"
			else:
				c1112 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "12-13")):
				c1213 = "D"
			else:
				c1213 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "13-14")):
				c1314 = "D"
			else:
				c1314 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "14-15")):
				c1415 = "D"
			else:
				c1415 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "15-16")):
				c1516 = "D"
			else:
				c1516 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "16-17")):
				c1617 = "D"
			else:
				c1617 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "17-18")):
				c1718 = "D"
			else:
				c1718 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "18-19")):
				c1819 = "D"
			else:
				c1819 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "19-20")):
				c1920 = "D"
			else:
				c1920 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "20-21")):
				c2021 = "D"
			else:
				c2021 = "-"
			if (miercoles.filter(FK_Hora__Nombre = "21-22")):
				c2122 = "D"
			else:
				c2122 = "-"

			#Jueves
			if (jueves.filter(FK_Hora__Nombre = "7-8")):
				d78 = "D"
			else:
				d78 = "-"
			if (jueves.filter(FK_Hora__Nombre = "8-9")):
				d89 = "D"
			else:
				d89 = "-"
			if (jueves.filter(FK_Hora__Nombre = "9-10")):
				d910 = "D"
			else:
				d910 = "-"
			if (jueves.filter(FK_Hora__Nombre = "10-11")):
				d1011 = "D"
			else:
				d1011 = "-"
			if (jueves.filter(FK_Hora__Nombre = "11-12")):
				d1112 = "D"
			else:
				d1112 = "-"
			if (jueves.filter(FK_Hora__Nombre = "12-13")):
				d1213 = "D"
			else:
				d1213 = "-"
			if (jueves.filter(FK_Hora__Nombre = "13-14")):
				d1314 = "D"
			else:
				d1314 = "-"
			if (jueves.filter(FK_Hora__Nombre = "14-15")):
				d1415 = "D"
			else:
				d1415 = "-"
			if (jueves.filter(FK_Hora__Nombre = "15-16")):
				d1516 = "D"
			else:
				d1516 = "-"
			if (jueves.filter(FK_Hora__Nombre = "16-17")):
				d1617 = "D"
			else:
				d1617 = "-"
			if (jueves.filter(FK_Hora__Nombre = "17-18")):
				d1718 = "D"
			else:
				d1718 = "-"
			if (jueves.filter(FK_Hora__Nombre = "18-19")):
				d1819 = "D"
			else:
				d1819 = "-"
			if (jueves.filter(FK_Hora__Nombre = "19-20")):
				d1920 = "D"
			else:
				d1920 = "-"
			if (jueves.filter(FK_Hora__Nombre = "20-21")):
				d2021 = "D"
			else:
				d2021 = "-"
			if (jueves.filter(FK_Hora__Nombre = "21-22")):
				d2122 = "D"
			else:
				d2122 = "-"

			#Viernes
			if (viernes.filter(FK_Hora__Nombre = "7-8")):
				e78 = "D"
			else:
				e78 = "-"
			if (viernes.filter(FK_Hora__Nombre = "8-9")):
				e89 = "D"
			else:
				e89 = "-"
			if (viernes.filter(FK_Hora__Nombre = "9-10")):
				e910 = "D"
			else:
				e910 = "-"
			if (viernes.filter(FK_Hora__Nombre = "10-11")):
				e1011 = "D"
			else:
				e1011 = "-"
			if (viernes.filter(FK_Hora__Nombre = "11-12")):
				e1112 = "D"
			else:
				e1112 = "-"
			if (viernes.filter(FK_Hora__Nombre = "12-13")):
				e1213 = "D"
			else:
				e1213 = "-"
			if (viernes.filter(FK_Hora__Nombre = "13-14")):
				e1314 = "D"
			else:
				e1314 = "-"
			if (viernes.filter(FK_Hora__Nombre = "14-15")):
				e1415 = "D"
			else:
				e1415 = "-"
			if (viernes.filter(FK_Hora__Nombre = "15-16")):
				e1516 = "D"
			else:
				e1516 = "-"
			if (viernes.filter(FK_Hora__Nombre = "16-17")):
				e1617 = "D"
			else:
				e1617 = "-"
			if (viernes.filter(FK_Hora__Nombre = "17-18")):
				e1718 = "D"
			else:
				e1718 = "-"
			if (viernes.filter(FK_Hora__Nombre = "18-19")):
				e1819 = "D"
			else:
				e1819 = "-"
			if (viernes.filter(FK_Hora__Nombre = "19-20")):
				e1920 = "D"
			else:
				e1920 = "-"
			if (viernes.filter(FK_Hora__Nombre = "20-21")):
				e2021 = "D"
			else:
				e2021 = "-"
			if (viernes.filter(FK_Hora__Nombre = "21-22")):
				e2122 = "D"
			else:
				e2122 = "-"

			#Sabado
			if (sabado.filter(FK_Hora__Nombre = "7-8")):
				f78 = "D"
			else:
				f78 = "-"
			if (sabado.filter(FK_Hora__Nombre = "8-9")):
				f89 = "D"
			else:
				f89 = "-"
			if (sabado.filter(FK_Hora__Nombre = "9-10")):
				f910 = "D"
			else:
				f910 = "-"
			if (sabado.filter(FK_Hora__Nombre = "10-11")):
				f1011 = "D"
			else:
				f1011 = "-"
			if (sabado.filter(FK_Hora__Nombre = "11-12")):
				f1112 = "D"
			else:
				f1112 = "-"
			if (sabado.filter(FK_Hora__Nombre = "12-13")):
				f1213 = "D"
			else:
				f1213 = "-"
			if (sabado.filter(FK_Hora__Nombre = "13-14")):
				f1314 = "D"
			else:
				f1314 = "-"
			if (sabado.filter(FK_Hora__Nombre = "14-15")):
				f1415 = "D"
			else:
				f1415 = "-"
			if (sabado.filter(FK_Hora__Nombre = "15-16")):
				f1516 = "D"
			else:
				f1516 = "-"
			if (sabado.filter(FK_Hora__Nombre = "16-17")):
				f1617 = "D"
			else:
				f1617 = "-"
			if (sabado.filter(FK_Hora__Nombre = "17-18")):
				f1718 = "D"
			else:
				f1718 = "-"
			if (sabado.filter(FK_Hora__Nombre = "18-19")):
				f1819 = "D"
			else:
				f1819 = "-"
			if (sabado.filter(FK_Hora__Nombre = "19-20")):
				f1920 = "D"
			else:
				f1920 = "-"
			if (sabado.filter(FK_Hora__Nombre = "20-21")):
				f2021 = "D"
			else:
				f2021 = "-"
			if (sabado.filter(FK_Hora__Nombre = "21-22")):
				f2122 = "D"
			else:
				f2122 = "-"

			#Domingo
			if (domingo.filter(FK_Hora__Nombre = "7-8")):
				g78 = "D"
			else:
				g78 = "-"
			if (domingo.filter(FK_Hora__Nombre = "8-9")):
				g89 = "D"
			else:
				g89 = "-"
			if (domingo.filter(FK_Hora__Nombre = "9-10")):
				g910 = "D"
			else:
				g910 = "-"
			if (domingo.filter(FK_Hora__Nombre = "10-11")):
				g1011 = "D"
			else:
				g1011 = "-"
			if (domingo.filter(FK_Hora__Nombre = "11-12")):
				g1112 = "D"
			else:
				g1112 = "-"
			if (domingo.filter(FK_Hora__Nombre = "12-13")):
				g1213 = "D"
			else:
				g1213 = "-"
			if (domingo.filter(FK_Hora__Nombre = "13-14")):
				g1314 = "D"
			else:
				g1314 = "-"
			if (domingo.filter(FK_Hora__Nombre = "14-15")):
				g1415 = "D"
			else:
				g1415 = "-"
			if (domingo.filter(FK_Hora__Nombre = "15-16")):
				g1516 = "D"
			else:
				g1516 = "-"
			if (domingo.filter(FK_Hora__Nombre = "16-17")):
				g1617 = "D"
			else:
				g1617 = "-"
			if (domingo.filter(FK_Hora__Nombre = "17-18")):
				g1718 = "D"
			else:
				g1718 = "-"
			if (domingo.filter(FK_Hora__Nombre = "18-19")):
				g1819 = "D"
			else:
				g1819 = "-"
			if (domingo.filter(FK_Hora__Nombre = "19-20")):
				g1920 = "D"
			else:
				g1920 = "-"
			if (domingo.filter(FK_Hora__Nombre = "20-21")):
				g2021 = "D"
			else:
				g2021 = "-"
			if (domingo.filter(FK_Hora__Nombre = "21-22")):
				g2122 = "D"
			else:
				g2122 = "-"

			ctx = {
				 "fase": False, "profesor": Pro, "a78": a78,  "a89": a89,  "a910": a910,  "a1011": a1011,  "a1112": a1112, 
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

		else:
			formP = ProfesorHoraConForm()
			ctx = {
				"mensaje": "Formulario incompleto", "form": formP, "fase": True
			}
	else:
		formP = ProfesorHoraConForm()
		ctx = { "formP": formP, "fase": True }

	return render(request, "Escuela/formProfesorHora_view.html", ctx)