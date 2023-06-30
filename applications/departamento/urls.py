#from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'lista-depa/', 
        views.DepartamentoListView.as_view(), 
        name='dep_lista'
    ),
    path(
        'new-departamento/', 
        views.NewDepartamentoView.as_view(), 
        name='nuevo_depa'
    )
]

