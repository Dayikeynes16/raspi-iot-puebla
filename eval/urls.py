from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
  path('hello/',  views.hello, name= "hello"),
  path('obtener_productos_venta/', views.obtener_productos_venta, name='obtener_productos_venta'),
  path('check/', views.check, name='check'),
  path('finalizar_venta/', views.finalizar_venta, name='finalizar_venta'),
  path('eliminar_venta/', views.eliminar_venta, name='eliminar_venta'),
  path('signup/', views.signup, name='signup'),
  path('logout/', views.signout, name='logout'),
  path('', views.signin, name='signin'),
  path('report/', views.report, name='report'),
  path('barcode/', views.barcode, name = 'barcode'),
  path('delete_product/', views.delete_product, name='delete_product'),
  path('finalizar_venta_barras/', views.finalizar_venta_barras, name='finalizar_barras'),
  path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
  path('clientes/', views.clientes , name = 'cliente'),
  path('discount/', views.discount, name = 'discount'),
  path('descuento/', views.descuento, name='descuento')
 ]