from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.iniciar_sesion, name='login'),
    path('perfil/', views.perfil, name='perfil')
]