from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Producto(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre +self.precio + " "


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    operador = models.IntegerField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    abierta = models.BooleanField(default=True)
    METODOS_DE_PAGO = (('efectivo', 'Efectivo'),('tarjeta', 'Tarjeta'),
    ('transferencia', 'Transferencia')) 
    metodo_de_pago = models.CharField(max_length=15, choices=METODOS_DE_PAGO, default='efectivo', null=True )
    def __str__(self):
        return f"{self.id_venta}"
 
class ProductoVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f" {self.producto.nombre} ({self.cantidad}) ({self.venta}) ({self.subtotal})"


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length = 100,null = True, blank = True)

    def __str__(self):
        return self.nickname - self.name
    
class PrecioEspecial(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_especial = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cliente.nickname}: {self.precio_especial}"
