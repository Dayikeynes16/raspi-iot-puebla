from django.urls import path
from . import views

urlpatterns = [
  path('',  views.hello, name= "hello"),
  path('obtener_productos_venta/', views.obtener_productos_venta, name='obtener_productos_venta'),
  path('check/', views.check, name='check')
 ]