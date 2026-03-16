from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

# Página de inicio
def inicio(request):
    # Solo productos activos y destacados (máx. 5)
    productos_destacados = Producto.objects.filter(activo=True, destacado=True)[:5]
    return render(request, "inicio.html", {"productos_destacados": productos_destacados})

# Catálogo completo
def catalogo(request):
    categorias = Categoria.objects.all()
    destacados = Producto.objects.filter(activo=True, destacado=True)
    productos = Producto.objects.filter(activo=True, destacado=False)

    return render(request, "catalogo.html", {
        "categorias": categorias,
        "destacados": destacados,
        "productos": productos,
    })

# Detalle de un producto
def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)
    return render(request, "producto.html", {"producto": producto})
