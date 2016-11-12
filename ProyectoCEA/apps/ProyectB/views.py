from django.shortcuts import render, render_to_response, RequestContext
from django.template import RequestContext
from django.views.generic import TemplateView

# Create your views here.
class login(TemplateView):
	template_name = 'ProyectB/login.html'

def home(request):
	return render(request, "ProyectB/index_view.html", {})

def about(request):
	return render(request, "ProyectB/about.html", {})

def config(request):
	return render(request, "ProyectB/config.html", {})

def contact(request):
	return render(request, "ProyectB/contact.html", {})

def login(request):
	return render_to_response('ProyectB/login.html',context_instance=RequestContext(request))

def logout(request):
    logout(request)


		