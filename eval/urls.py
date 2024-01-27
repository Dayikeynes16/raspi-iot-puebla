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
  path('tasks/', views.tasks, name='tasks'),
  path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
  path('logout/', views.signout, name='logout'),
  path('', views.signin, name='signin'),
  path('create_task/', views.create_task, name='create_task'),
  path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
  path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
  path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
  path('report/', views.report, name='report'),
  path('barcode/', views.barcode, name = 'barcode'),
  path('delete_product/', views.delete_product, name='delete_product'),
  path('finalizar_venta_barras/', views.finalizar_venta_barras, name='finalizar_barras'),
  path('agregar_producto/', views.agregar_producto, name='agregar_producto'),


 ]