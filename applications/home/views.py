from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
from .models import Prueba
# Create your views here.

from .forms import PruebaForm

class AboutView(TemplateView):
    template_name = "home/about.html"

class IndexView(TemplateView):
    template_name = "home/home.html"

 
class ResumenFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"

class PrurbaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['C', 'B', 'C']
    context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    success_url = '/'
