from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from .models import Carrito, ProductoCarrito
from django.contrib import messages

def add_to_cart(request, producto_id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=producto_id)
        
        carrito, creado = Carrito.objects.get_or_create(session_key=request.session.session_key)

        producto_en_carrito, creado = ProductoCarrito.objects.get_or_create(
            carrito=carrito, 
            producto=producto
        )
        if not creado:
            producto_en_carrito.cantidad += 1
            producto_en_carrito.save()
        else:
            messages.success(request, f"{producto.nombre} fue añadido al carrito.")

    return redirect('cart:view_cart')

def view_cart(request):
    try:
        carrito = Carrito.objects.get(session_key=request.session.session_key)
        productos_carrito = ProductoCarrito.objects.filter(carrito=carrito)
    except Carrito.DoesNotExist:
        productos_carrito = []
    
    context = {'productos_carrito': productos_carrito}
    return render(request, 'cart/cart.html', context)