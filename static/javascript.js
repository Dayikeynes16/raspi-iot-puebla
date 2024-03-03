document.getElementById('imprimirBtn').addEventListener('click', function() {
  imprimirTicket();
});

function imprimirTicket() {
  var contenidoTicket = "<h1>¡Mi Ticket!</h1><p>Fecha: " + new Date() + "</p><p>Artículo: Producto XYZ</p><p>Precio: $10.00</p>";

  var ventana = window.open('', '', 'width=500,height=500');
  ventana.document.open();
  ventana.document.write('<html><head><title>Ticket</title></head><body>');
  ventana.document.write(contenidoTicket);
  ventana.document.write('</body></html>');
  ventana.document.close();

  ventana.print();
  ventana.close();
}

function toggleProductos(idPro){
     
    var listaProductos = document.getElementById(idPro).value;
    listaProductos = listaProductos.replace( /[<>'"]/g, '');
    listaProductos = listaProductos.replace(/(ProductoVenta:)/g, '')
    listaProductos = listaProductos.replace(/\[|\]/g, '');
    listaProductos = listaProductos.replace( /[']/g, '"');

    var elementos = listaProductos.split(', ');
    // Crea un array asociativo (objeto) para almacenar la información de cada producto
    var productos = [];

  // Itera sobre cada elemento y construye el objeto asociativo
    elementos.forEach(function(elemento) {
        // Utiliza expresiones regulares para extraer la información
        var matches = elemento.match(/^(.*?) \((.*?)\) \((.*?)\) \((.*?)\)$/);

        // Crea un objeto asociativo para almacenar la información
        var producto = {
            nombre: matches[1],
            cantidad: parseFloat(matches[2]),
            nVenta: parseInt(matches[3]),
            precio: parseFloat(matches[4])
        };


          

          // Agrega el producto al array de productos
          productos.push(producto);
      });
  
 
  var total = 0

  for (var i = 0; i < productos.length; i++) {
    total += productos[i].precio;
  }
  //console.log(productos)
    /* productos */
    var contenedor = document.getElementById('productosLista')
    contenedor.innerHTML = '';
    for (var i = 0; i < productos.length; i++) {
      
      var itemP = document.createElement('div');
      itemP.className ='itemP';

      var nombre = document.createElement('div');
      nombre.className ='nombre';
      nombre.innerHTML = productos[i].nombre;

      var cantidad = document.createElement('div');
      cantidad.className ='cantidad';
      cantidad.innerHTML = productos[i].cantidad;

      var preciodiv = document.createElement('div');
      preciodiv.className= 'precio';
      preciodiv.innerHTML = productos[i].precio;

      itemP.appendChild(nombre);
      itemP.appendChild(cantidad);
      itemP.appendChild(preciodiv);
      contenedor.appendChild(itemP);
    }
  
    /*pagar */
    var totalPrice = document.getElementById('totalPrice');
    totalPrice.innerHTML = total.toFixed(2);

    /*Formulario */

    document.getElementById('inputCobro').value = productos[0].nVenta;
    document.getElementById('inputCancelar').value = productos[0].nVenta;
    document.getElementById('inputdescuento').value = productos[0].nVenta;


}
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('toggleButton').addEventListener('click', function() {
      var form = document.getElementById('discountForm');
      if (form.style.display === 'none' || form.style.display === '') {
          form.style.display = 'block';
      } else {
          form.style.display = 'none';
      }
  });
});

