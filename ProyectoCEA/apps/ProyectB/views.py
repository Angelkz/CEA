from django.shortcuts import render, render_to_response, RequestContext
from django.template import RequestContext
from django.views.generic import TemplateView

# Create your views here.
class login(TemplateView):
	template_name = 'ProyectB/login.html'

def home(request):
	return render(request, "ProyectB/index_view.html", {})

def login(request):
	return render_to_response('ProyectB/login.html',context_instance=RequestContext(request))

def logout(request):
    logout(request)