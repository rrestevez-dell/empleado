# from typing import Any, Dict, Optional
# from django.db.models.query import QuerySet
# from django.forms.models import BaseModelForm
# from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

#Si vamos a trabajar con un listView este nos pide un queriset o modelo por tanto
#Modelo
from .models import Empleado
#Form
from .forms import EmpleadoForm

class InicioView(TemplateView):
    #vista que carga la pagina de inicio
    template_name = "inicio.html" 



# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un area de la empresa
# 3.- Listar empleados por trabajo 
# 4.- Listar los empleados por palabra clave
# 5.- Listar abilidades de un empleado

# 1. 
class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    #Paginacion
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        print('========', palabra_clave)
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista

class ListaEmpleadosAdnmin(ListView):
    template_name = 'empleado/list_admin.html'
    #Paginacion
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    

    #Que pasa si no le pongo esta forma de acceder
    #context_object_name = 'lista'

    #veamos otra forma


#2. queryset

class ListByAreaEmpleado(ListView):
    """Lista empleado de un area"""
    template_name = 'empleado/lista_by_area.html'
    context_object_name = 'empleados'

    #usando un filto entrandolo del codigo
    """queryset = Empleado.objects.filter(
        departamento__shor_name = 'contabilidad' 
    )"""

    def get_queryset(self):
        #El codigo que quiera
        #Usando un filtro a travez de una url
        elarea = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = elarea 
        )
        return lista
    
    #veamos un filtro a travez de una caja de texto

    #4.

class ListEmpleadosByKword(ListView):
    """Lista empleado por palabra clave a traves de caja de texto"""
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('************')
        palabra_clave = self.request.GET.get("kword", '')
        #print('========', palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave 
        )
        return lista
    
#5.Listar  habilidades de un empleado

class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=5)
        #print(empleado.habilidades.all())
        return empleado.habilidades.all()
    
#detailView


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"

    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #Todo un proceso
        context['titulo'] = 'Empleado del mes'
        return context
    

class SuccesView(TemplateView):
    template_name = "empleado/succes.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #Logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**********MetodoPOST*********')
        print('*******************')
        print('++++++++++++++++')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        #Logica del proceso
        print('**********MetodoFROM_VALID*********')
        print('*******************')
        return super(EmpleadoUpdateView, self).form_valid(form)
    
class Succes2View(TemplateView):
    template_name = "empleado/succes2.html"

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

