from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Dashboard principal
    path("", views.dashboard_home, name="home"),

    # Clientes
    path("clientes/", views.clientes_view, name="clientes"),
    path("clientes/<int:cliente_id>/", views.admin_detalle_cliente, name="admin_detalle_cliente"),
    path("clientes/editar/<int:cliente_id>/", views.admin_editar_cliente, name="admin_editar_cliente"),

    # Estadísticas
    path("estadisticas/", views.estadisticas_view, name="estadisticas"),

    # Pedidos
    path("pedidos/", views.pedidos_view, name="pedidos"),
    path("pedidos/<int:pedido_id>/detalle/", views.detalle_pedido, name="admin_detalle_pedido"),
    path("pedidos/<int:pedido_id>/confirmar/", views.confirmar_pedido, name="admin_confirmar_pedido"),
    path("pedidos/<int:pedido_id>/cancelar/", views.cancelar_pedido, name="admin_cancelar_pedido"),

    # Productos
    path("productos/", views.productos_view, name="productos"),
    path("producto/nuevo/", views.admin_agregar_producto, name="admin_agregar_producto"),
    path("producto/editar/<int:producto_id>/", views.admin_editar_producto, name="admin_editar_producto"),
    path("producto/eliminar/<int:producto_id>/", views.admin_eliminar_producto, name="admin_eliminar_producto"),
    path("producto/<int:producto_id>/destacar/", views.toggle_destacado, name="toggle_destacado"),  # NUEVO
]
