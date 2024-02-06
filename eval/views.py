from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from Metricas.settings import os
from decimal import Decimal
from .models import Producto, ProductoVenta, Venta
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

from datetime import datetime, timedelta



@login_required
def hello(request):
    ventas = Venta.objects.filter(finalizada=False, abierta = False)
    listaVentas = {}
    productos_venta = ProductoVenta.objects.filter(venta__in=ventas)
    for i in ventas:
        idP = str(i.id_venta)
        listaVentas[idP] = []
        for j in productos_venta:
            if i == j.venta:
                listaVentas[idP].append(j)
    print(productos_venta)
                  
    context = {'ventas': listaVentas}
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

def finalizar_venta(request):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_de_pago')
        id = request.POST.get('id_venta')
        id = int(id)
        venta = get_object_or_404(Venta, id_venta=id)
        venta.finalizada = True
        venta.metodo_de_pago = metodo_pago
        venta.fecha = timezone.now().date()
        venta.save()
        ProductoVenta.objects.filter(venta=venta).delete()
        

        return redirect('hello')
    
def finalizar_venta_barras(request):
    if request.method == 'POST':
        metodo_pago = request.POST.get('metodo_de_pago')
        id = request.POST.get('id_venta')
        id = int(id)
        venta = get_object_or_404(Venta, id_venta=id)
        venta.finalizada = True
        venta.metodo_de_pago = metodo_pago
        venta.fecha = timezone.now().date()
        venta.save()
        ProductoVenta.objects.filter(venta=venta).delete()
        

        return redirect('barcode')
    
def eliminar_venta(request):
    if request.method == 'POST':
        id = request.POST.get('id_venta')
        id = int(id)
        venta = get_object_or_404(Venta, id_venta=id)
        venta.delete()

        return redirect('hello')

@login_required
def report(request):
    fecha_actual = timezone.now().date()
    ventas = Venta.objects.filter(finalizada=True, fecha__range=[fecha_actual, fecha_actual + timedelta(days=1)])
    total = 0
    card = 0
    spei = 0
    efectivo = 0
    for i in ventas:
        total = total + i.total
        if i.metodo_de_pago == 'tarjeta':
            card = card + i.total
        if i.metodo_de_pago == 'transferencia':
            spei = spei + i.total
        if i.metodo_de_pago == 'efectivo':
            efectivo = efectivo + i.total
    context = {'total' : total, 'card' : card , 'spei':spei, 'efectivo':efectivo, 'ventas':ventas}
    return render (request, 'report.html', context)

def barcode(request):
    venta_activa = Venta.objects.filter(finalizada=False, abierta=True, operador=2).first()
    if not venta_activa:
        venta_activa = Venta.objects.create(operador=2, abierta=True)
    productos = Producto.objects.all()
    productos_venta = ProductoVenta.objects.filter(venta=venta_activa)
    total = 0
    for producto_venta in productos_venta:
        total += producto_venta.subtotal
    venta_activa.total = total
    venta_activa.save()

    if request.method == 'POST':
        peso = Decimal(request.POST.get('peso', 0))
        producto_id = int(request.POST.get('producto', 0))
        if peso > 0 and producto_id > 0:
            producto = Producto.objects.get(pk=producto_id)
            subtotal = peso * producto.precio
            producto_venta = ProductoVenta(cantidad=peso, subtotal=subtotal, producto=producto, venta=venta_activa)
            producto_venta.save()
            total += subtotal
            venta_activa.total = total
            venta_activa.save()
            return redirect ('barcode')

    context = {'productos': productos, 'productos_venta': productos_venta, 'venta_activa': venta_activa}
    return render(request, 'venta_barras.html', context)

def delete_product(request):
    if request.method == 'POST':
        
        product_id = request.POST.get('product_id')
       
        producto_venta = get_object_or_404(ProductoVenta, id=product_id)
        
        producto_venta.delete()
        return redirect('barcode')

def agregar_producto(request):
    if request.method == 'POST':
        codigo_barras = request.POST.get('codigo_barras')
        codigo_producto = int(codigo_barras[4:6])  
        peso_producto = int(codigo_barras[8:]) 
        peso = Decimal(peso_producto/1000)
        producto = get_object_or_404(Producto, codigo=codigo_producto)        
        venta_activa = Venta.objects.filter(finalizada=False, abierta=True, operador=2).first()
        subtotal = peso * producto.precio
        producto_venta = ProductoVenta( producto=producto,venta=venta_activa,cantidad=peso,subtotal=subtotal)
        producto_venta.save()
        return redirect('barcode')
    
    return redirect('barcode')
        
        
        
        

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('hello')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})





@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('hello')
