from django.shortcuts import render, HttpResponse, redirect
from Metricas.settings import os
from decimal import Decimal
from .models import Producto, ProductoVenta, Venta
from django.http import JsonResponse



def hello(request):
    ventas = Venta.objects.filter(finalizada=False)
    productos_venta = ProductoVenta.objects.filter(venta__in=ventas)
    context = {'ventas': ventas, 'productos_venta' : productos_venta}
    return render(request, 'cuestionariopart1.html', context)


def check (request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        producto = Producto(nombre = nombre, precio = precio)
        producto.save()
        
        return redirect ('hello')



def obtener_productos_venta(request):
    id_venta = request.GET.get('id_venta')
    productos = ProductoVenta.objects.filter(venta__id_venta=id_venta).values('producto__nombre', 'cantidad')
    return JsonResponse(list(productos), safe=False)
