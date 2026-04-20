from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.iniciar_sesion, name='login'),
    path('perfil/', views.perfil, name='perfil'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('producto/nuevo/', views.crear_producto, name='crear_producto'),
]