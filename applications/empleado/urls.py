from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name='empleado_all'
    ),
    path(
        'listar_by_area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name = 'empleados_elarea'
    ),
    path(
        'listar_empadmin/', 
        views.ListaEmpleadosAdnmin.as_view(),
        name = 'empleados_admin'
    ),
    path(
        'buscar-empleado/', 
        views.ListEmpleadosByKword.as_view()
    ),
    path(
        'Lista_habilidades/', 
         views.ListHabilidadesEmpleado.as_view()
    ),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name = 'empleado_add'
    ),
    path(
        'succes/', 
        views.SuccesView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),
    path(
        'succes2/', 
        views.Succes2View.as_view(), 
        name='eliminar_empleado'
    ),

]