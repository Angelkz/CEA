from django import forms
from django.forms import ModelForm,TextInput,Textarea,Select
from .models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from table import Table
from table.columns import Column

class PeriodoForm(forms.ModelForm): 
	class Meta:
			model = Periodo
			fields =('Nombre',)
			error_messages ={
				'Nombre':{
				'required':_("Ingrese Nombre"),
				},
			}
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Periodo, Ejemplo: "Enero-Junio"','title':'Nombre','required':'true','size': 10,' style' : ' width:  400px'}),
			}
			labels ={
			'Nombre':_('Nombre'),
			}

class PeriodoDelForm(forms.Form):
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Periodo.objects.all())


	class Meta:
	    model = Periodo
	    fields = '__all__'

class PeriodoReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Nombre = Column(field='Nombre', header=u'Nombre')
	class Meta:
		model = Periodo

class SemestreForm(forms.ModelForm):
	class Meta:
			model = Semestre
			fields =('Nombre',)
			error_messages ={
				'Nombre':{
				'required':_("Ingrese Nombre"),
				},
			}
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Semestre, Ejemplo: "1"','title':'Nombre','required':'true','size': 10,' style' : ' width:  400px'}),
			}
			labels ={
			'Nombre':_('Nombre'),
			}

class SemestreDelForm(forms.Form):
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Semestre.objects.all())
 

	class Meta:
	    model = Semestre
	    fields = '__all__'

class SemestreReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Nombre = Column(field='Nombre', header=u'Nombre')
	class Meta:
		model = Semestre

class SalonForm(forms.ModelForm):
	class Meta:
			model = Salon
			fields = ('Nombre',)
			error_messages = {
				'Nombre':{
				'required':_("Ingrese Nombre"),
				},
			}
			widgets = {'Nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ejemplo: "1200"','title':'Nombre','required':'true','size': 10,' style' : ' width:  400px'}),
			}
			labels ={
			'Nombre':_('Nombre'),
			}

class SalonDelForm(forms.Form):
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=Salon.objects.all())


	class Meta:
	    model = Salon
	    fields = '__all__'

class SalonReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Nombre = Column(field='Nombre', header=u'Nombre')
	class Meta:
		model = Salon

class HorarioCarreraForm(forms.ModelForm):
	class Meta:
			model = HorarioCarrera
			fields = ('Clave','FK_Periodo','FK_Semestre','FK_Carrera',)
			widgets = {'Clave': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Clave,Ejemplo: "SC3B"','title':'Clave','required':'true','size': 10,' style' : ' width:  220px'}),
			'FK_Periodo': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Periodo','required':'true'}),
			'FK_Semestre': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Semestre','required':'true'}),
			'FK_Carrera': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Carrera','required':'true'}),

			} 
			labels ={
			'Clave':_('Clave'),
			'FK_Periodo':_('Periodo'),
			'FK_Semestre':_('Semestre'),
			'FK_Carrera':_('Carrera'),
			}

class HorarioCarreraDelForm(forms.Form):
	Nombre= forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','style':'width: 21em;','required':'true',}),queryset=HorarioCarrera.objects.all())


	class Meta:
	    model = HorarioCarrera
	    fields = '__all__'
	    widgets = {'Clave': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Periodo','required':'true'}),}
	    labels ={ 'Clave':_('Clave'),}
		

class HorarioCarreraReporte(Table):
	Fecha = Column(field='FecAct', header=u'Fecha de act')
	Clave = Column(field='Clave', header=u'Clave')
	FK_Periodo = Column(field='FK_Periodo', header=u'Periodo')
	FK_Semestre = Column(field='FK_Semestre', header=u'Semestre')
	FK_Carrera = Column(field='FK_Carrera', header=u'Carrera')
	class Meta:
		model = HorarioCarrera

class ClaseHoraForm(forms.ModelForm):
	class Meta:
			model = ClaseHora
			fields = ('FK_Salon','FK_Profesor','FK_Materia',)
			widgets = {
			'FK_Salon': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Salon','required':'true'}),
			'FK_Profesor': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Profesor','required':'true'}),
			'FK_Materia': Select(attrs={'class':'form-control','style':'width: 15em;','title':'Materia','required':'true'}),
			}

class ClaseHoraSelForm(forms.ModelForm):
	class Meta:
			model = ClaseHora
			fields = ('FK_HorarioCarrera',)
			widgets = {'FK_HorarioCarrera':Select(attrs={'class':'form-control','style':'width: 15em;','title':'HorarioCarrera','required':'true'}),
			}

class HorarioFiltroForm(forms.Form):
	Horario= forms.ModelChoiceField(queryset=HorarioCarrera.objects.all()) 

	class Meta:
	    model = HorarioCarrera
	    fields = '__all__'