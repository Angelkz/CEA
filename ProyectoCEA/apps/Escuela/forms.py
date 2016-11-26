from django import forms
from django.forms import ModelForm,TextInput,Textarea,Select
from .models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from table import Table
from table.columns import Column


class UsuarioForm(forms.Form):
	Username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'width: 15em;',"placeholder":'Username','id':'idUsername'}))
	Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'width: 15em;',"placeholder":'Password','id':'idPassword'}))

class TituloForm(forms.ModelForm):
	class Meta:
			model = Titulo
			fields = '__all__'
			error_messages ={
				'Nombre':{
				'required':_("Ingrese Nombre"),
				},
			}
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Titulo, Ejemplo: "Ingeniero Industrial"','title':'Nombre','required':'true','size': 10,'style' : ' width:  400px'}),
			}
			labels ={
			'Nombre':_('Nombre'),
			}

class TituloDelForm(forms.Form):
	#Nombre= forms.ModelChoiceField(queryset=Titulo.objects.all())
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Titulo.objects.all())



	class Meta:
	    model = Titulo
	    fields = '__all__'

class TituloReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Nombre = Column(field='Nombre', header=u'Nombre')
	class Meta:
		model = Titulo

class GradoMaximoForm(forms.ModelForm):
	class Meta:
			model = GradoMaximo
			fields = ('Nombre',)
			error_messages={
				'Nombre':{
				'required':_("Ingrese Nombre"),
				},
			}
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Grado Maximo, Ejemplo: "Maestria"','title':'Nombre','required':'true','size': 10,' style' : ' width:  400px'}),
			}
			labels={
			'Nombre':_('Nombre'),
			}

class GradoMaximoDelForm(forms.Form):
	#Nombre= forms.ModelChoiceField(queryset=GradoMaximo.objects.all())
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=GradoMaximo.objects.all())
 

	class Meta:
	    model = GradoMaximo
	    fields = '__all__'

class GradoMaximoReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Nombre = Column(field='Nombre', header=u'Nombre')
	class Meta:
		model = GradoMaximo

class NumeroHorasForm(forms.ModelForm):
	class Meta:
			model = NumeroHoras
			fields = ('Nombre',)
			error_messages = {
				'Nombre':{
				'required':_("Ingrese Nombre"),
				},
			}
			labels = {
			'Nombre':_('Nombre'),
			}			

class CarreraForm(forms.ModelForm):
	class Meta:
			model = Carrera
			fields = ('Nombre',)
			error_messages = {
				'Nombre': {
				'required':_("Ingrese Nombre"),
				},
			}
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Nombre, Ejemplo: "Contabilidad"','title':'Nombre','required':'true','size': 10,' style' : ' width:  400px'}),
			}
			labels = {
			'Nombre':_('Nombre'),
			}

class CarreraDelForm(forms.Form):

	#Nombre= forms.ModelChoiceField(queryset=Carrera.objects.all())
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Carrera.objects.all())
 

	class Meta:
	    model = Carrera
	    fields = '__all__'

class CarreraReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Nombre = Column(field='Nombre', header=u'Nombre')
	class Meta:
		model = Carrera

class CarreraDelForm(forms.Form):
	#Nombre= forms.ModelChoiceField(queryset=Carrera.objects.all())
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Carrera.objects.all())


	class Meta:
	    model = Carrera
	    fields = '__all__'

class DiaForm(forms.ModelForm):
	class Meta:
			model = Dia
			fields = '__all__'

class HoraForm(forms.ModelForm):
	class Meta:
			model = Hora
			fields = '__all__'

#Formulario Profesor ***Falta cambio  a registro de usuario******			

class ProfesorForm(forms.ModelForm): 
	class Meta:
			model = Profesor
			fields = ('Nombre','ApellidoPaterno','ApellidoMaterno','FK_Titulo','FK_GradoMaximo','TelefonoCelular','TelefonoCasa','Email','Tutorias','NumeroEmpleado','FK_NumeroHoras','Laboratorio','Paquete',)
			widgets = {'Nombre':TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "Laura"','id':'Nombre','required':'true','size': 10,' style' : ' width:  300px'}),
			'ApellidoPaterno': TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "Flores"','title':'ApellidoPaterno','required':'true','size': 10,' style' : ' width:  300px'}),
			'ApellidoMaterno': TextInput(attrs={'class': 'form-control','placeholder': 'Ejemplo: "Valencia"','title':'Nombre','required':'true','size': 10,' style' : ' width:  300px'}),
			'FK_Titulo': Select(attrs={'class':'form-control','style':'width: 21em;','title':'Titulo','required':'true'}),
			'FK_GradoMaximo': Select(attrs={'class':'form-control','style':'width: 21em;','title':'GradoMaximo','required':'true'}),
			'TelefonoCelular':TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "6643365026"','title':'TelefonoCelular','required':'true','size': 10,' style' : ' width:  300px'}),
			'TelefonoCasa':TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "6842332"','title':'TelefonoCasa','required':'true','size': 10,' style' : ' width:  300px'}),
			'Email':TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "pos@gmail.com"','title':'Email','required':'true','size': 10,' style' : ' width:  300px'}),
			'NumeroEmpleado':TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "256"','title':'NumeroEmpleado','required':'true','size': 10,' style' : ' width:  300px'}),
			'FK_NumeroHoras': Select(attrs={'class':'form-control','style':'width: 21em;','title':'FK_NumeroHoras','required':'true'}),
			}

class ProfesorDelForm(forms.Form):
	#Nombre= forms.ModelChoiceField(queryset=Profesor.objects.all()) 
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Profesor.objects.all())


	class Meta:
	    model = Profesor
	    fields = '__all__'

class ProfesorAutForm(forms.Form):
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Profesor.objects.all().filter(Autorizado=False)) 

	class Meta:
	    model = Profesor
	    fields = '__all__'
	    widgets = {'Nombre':Select(attrs={'class':'form-control','style':'width: 21em;','title':'Titulo','required':'true'}),
	    }

class ProfesorReporteContacto(Table):
	Autorizado = Column(field='Autorizado', header=u'Autorizado')
	NumeroEmpleado = Column(field='NumeroEmpleado', header=u'N# Empleado')
	Nombre = Column(field='Nombre', header=u'Nombre')
	ApellidoPaterno = Column(field='ApellidoPaterno', header=u'Apellido paterno')
	ApellidoMaterno = Column(field='ApellidoMaterno', header=u'Apellido materno')
	TelefonoCelular = Column(field='TelefonoCelular', header=u'Telefono celular')
	TelefonoCasa = Column(field='TelefonoCasa', header=u'Telefono de casa')
	Email = Column(field='Email', header=u'Correo')
	
	class Meta:
		model = Profesor

class ProfesorReporteProfesionales(Table):
	Autorizado = Column(field='Autorizado', header=u'Autorizado')
	NumeroEmpleado = Column(field='NumeroEmpleado', header=u'N# Empleado')
	Nombre = Column(field='Nombre', header=u'Nombre')
	ApellidoPaterno = Column(field='ApellidoPaterno', header=u'Apellido paterno')
	ApellidoMaterno = Column(field='ApellidoMaterno', header=u'Apellido materno')
	FK_Titulo = Column(field='FK_Titulo', header=u'Titulo')
	FK_GradoMaximo = Column(field='FK_GradoMaximo', header=u'Grado Maximo')
	FK_NumeroHoras = Column(field='FK_NumeroHoras', header=u'Numero de horas')
	
	class Meta:
		model = Profesor

class ProfesorReporteDisponibilidad(Table):
	NumeroEmpleado = Column(field='NumeroEmpleado', header=u'N# Empleado')
	Nombre = Column(field='Nombre', header=u'Nombre')
	ApellidoPaterno = Column(field='ApellidoPaterno', header=u'Apellido paterno')
	ApellidoMaterno = Column(field='ApellidoMaterno', header=u'Apellido materno')
	Tutorias = Column(field='Tutorias', header=u'Tutorias')
	Laboratorio = Column(field='Laboratorio', header=u'Laboratorio')
	Paquete = Column(field='Paquete', header=u'Paquete')
	
	class Meta:
		model = Profesor

#Fin formulario profesor/usuario *****

class MateriaForm(forms.ModelForm):
	class Meta:
			model = Materia
			fields = ('Nombre','Serie','HorasTeoricas','HorasPracticas','Creditos','FK_Carrera',)
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Nombre, Ejemplo: "Algebra"','title':'Nombre','required':'true','size': 10,' style' : ' width:  400px'}),
			'Serie': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Serie, Ejemplo: "1B"','title':'Serie','required':'true','size': 10,' style' : ' width:  400px'}),
			'HorasTeoricas': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Horas Teoricas, Ejemplo: "4"','title':'HorasTeoricas','required':'true','size': 10,' style' : ' width:  400px'}),
			'HorasPracticas': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Horas Practicas, Ejemplo: "2"','title':'HorasPracticas','required':'true','size': 10,' style' : ' width:  400px'}),
			'Creditos': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Creditos, Ejemplo: "6"','title':'Creditos','required':'true','size': 10,' style' : ' width:  400px'}),
			'FK_Carrera': Select(attrs={'class':'form-control','style':'width: 29em;','title':'Carrera','required':'true'}),
			}

class MateriaReporte(Table):
	Nombre = Column(field='Nombre', header=u'Nombre')
	Serie = Column(field='Serie', header=u'Serie')
	HorasTeoricas = Column(field='HorasTeoricas', header=u'Horas teoricas')
	HorasPracticas = Column(field='HorasPracticas', header=u'Horas practicas')
	Creditos = Column(field='Creditos', header=u'Creditos')
	FK_Carrera = Column(field='FK_Carrera', header=u'Carrera')
	
	class Meta:
		model = Materia

class MateriaDelForm(forms.Form):
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Materia.objects.all())
	#Nombre= forms.ModelChoiceField(queryset=Materia.objects.all()) 

	class Meta:
	    model = Materia
	    fields = '__all__'

class ProfesorMateriaForm(forms.ModelForm):
	class Meta:
			model = ProfesorMateria
			fields = ('FK_Materia',)
			widgets = {
			'FK_Materia': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Materia','required':'true'}),
			}

class ProfesorMateriaReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	FK_Profesor = Column(field='FK_Profesor', header=u'Profesor')
	FK_Materia = Column(field='FK_Materia', header=u'Materia')
	class Meta:
		model = ProfesorMateria

class ProfesorMateriaConForm(forms.ModelForm):
	class Meta:
	    model = ProfesorMateria
	    fields = ('FK_Profesor',)
	    widgets = {'FK_Profesor': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Profesor','required':'true'}),}

class ProfesorHoraForm(forms.ModelForm):
	class Meta:
			model = ProfesorHora
			fields = ('FK_Profesor','FK_Dia', 'FK_Hora',)
			widgets = {'FK_Profesor': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Profesor','required':'true'}),
			'FK_Dia':Select(attrs={'class':'form-control','style':'width: 15em;','title':'Dia','required':'true'}),
			'FK_Hora':Select(attrs={'class':'form-control','style':'width: 15em;','title':'Hora','required':'true'}), 
			}

class ProfesorHoraConForm(forms.ModelForm):
	class Meta:
	    model = ProfesorHora
	    fields = ('FK_Profesor',)
	    widgets = {'FK_Profesor': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Profesor','required':'true'}),}

# class UsuBuildNom(forms.Form):
# 	Build= forms.ModelChoiceField(queryset=UsuBuild.objects.all()) 
# 	Build_Oponente= forms.ModelChoiceField(queryset=UsuBuild.objects.all())
# 	Niveles 	= (
# 		(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12), (13,13), (14,14), (15,15), (16,16), (17,17), (18,18)
# 			  )
# 	Nivel	=	forms.ChoiceField(choices = Niveles)
# 	Nivel_Oponente	=	forms.ChoiceField(choices = Niveles)

# 	class Meta:
# 	    model = UsuBuild
# 	    fields = '__all__'