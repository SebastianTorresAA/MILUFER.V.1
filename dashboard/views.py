from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto, Categoria
from .forms import ProductoForm
from usuarios.models import User
from ventas.models import Pedido, PedidoProducto
from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from django.contrib.auth.decorators import user_passes_test
from django import forms

# Decorador que restringe a superusuarios
def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# -------------------------------
# Productos
# -------------------------------
@superuser_required
def productos_view(request):
    productos = Producto.objects.all()
    return render(request, "dashboard/productos.html", {"productos": productos})

@superuser_required
def admin_agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard:productos")
    else:
        form = ProductoForm()
    categorias = Categoria.objects.all()
    return render(request, "dashboard/producto_form.html", {"form": form, "categorias": categorias})

@superuser_required
def admin_editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("dashboard:productos")
    else:
        form = ProductoForm(instance=producto)
    categorias = Categoria.objects.all()
    return render(request, "dashboard/producto_form.html", {"form": form, "categorias": categorias, "producto": producto})

@superuser_required
def admin_eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect("dashboard:productos")

# -------------------------------
# Clientes
# -------------------------------
class ClienteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "is_active"]

@superuser_required
def clientes_view(request):
    clientes = User.objects.all().order_by("-date_joined")
    return render(request, "dashboard/clientes.html", {"clientes": clientes})

@superuser_required
def admin_detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(User, id=cliente_id)
    return render(request, "dashboard/detalle_cliente.html", {"cliente": cliente})

@superuser_required
def admin_editar_cliente(request, cliente_id):
    cliente = get_object_or_404(User, id=cliente_id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("dashboard:clientes")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "dashboard/editar_cliente.html", {"form": form, "cliente": cliente})

# -------------------------------
# Estadísticas
# -------------------------------
@superuser_required
def estadisticas_view(request):
    ventas_totales = Pedido.objects.aggregate(Sum("total"))["total__sum"] or 0
    total_pedidos = Pedido.objects.count()
    total_clientes = User.objects.count()
    ticket_medio = ventas_totales / total_pedidos if total_pedidos > 0 else 0

    # Calcular unidades vendidas y ingresos correctamente
    productos_top = (
        Producto.objects.annotate(
            unidades_vendidas=Sum("pedidoproducto__cantidad"),
            ingresos=Sum(
                ExpressionWrapper(
                    F("pedidoproducto__cantidad") * F("pedidoproducto__precio"),
                    output_field=DecimalField()
                )
            ),
        )
        .filter(unidades_vendidas__gt=0)
        .order_by("-unidades_vendidas")[:5]
    )

    pedidos_recientes = Pedido.objects.order_by("-fecha_creacion")[:5]

    return render(request, "dashboard/estadisticas.html", {
        "ventas_totales": ventas_totales,
        "total_pedidos": total_pedidos,
        "total_clientes": total_clientes,
        "ticket_medio": ticket_medio,
        "productos_top": productos_top,
        "pedidos_recientes": pedidos_recientes,
    })

# -------------------------------
# Pedidos
# -------------------------------
@superuser_required
def pedidos_view(request):
    pedidos = Pedido.objects.all().order_by("-fecha_creacion")
    return render(request, "dashboard/pedidos.html", {"pedidos": pedidos})

# -------------------------------
# Dashboard principal
# -------------------------------
@superuser_required
def dashboard_home(request):
    return render(request, "dashboard/dashboard.html")
