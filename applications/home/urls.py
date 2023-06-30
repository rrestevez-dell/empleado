from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('about/', views.AboutView.as_view(), name='about'),
    path('lista/', views.PrurbaListView.as_view()),
    path('lista_prueba/', views.ModeloPruebaListView.as_view()),
    path('add_prue/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path(
        'resumen-foundation/', 
        views.ResumenFoundationView.as_view(), 
        name='Resumen_foundation'
    ),
]