# Manual de Administrador — Milufer Matias

**Versión:** 1.0  
**Fecha:** Marzo 2026  
**Dirigido a:** Administradores de la tienda (superusuarios)

---

## Tabla de contenidos

1. [Introducción](#1-introducción)
2. [Acceso al panel de administración](#2-acceso-al-panel-de-administración)
3. [Vista general del Dashboard](#3-vista-general-del-dashboard)
4. [Gestión de productos](#4-gestión-de-productos)
5. [Gestión de clientes](#5-gestión-de-clientes)
6. [Gestión de pedidos](#6-gestión-de-pedidos)
7. [Estadísticas](#7-estadísticas)
8. [Panel de administración de Django (/admin/)](#8-panel-de-administración-de-django-admin)
9. [Consideraciones de seguridad](#9-consideraciones-de-seguridad)
10. [Preguntas frecuentes del administrador](#10-preguntas-frecuentes-del-administrador)

---

## 1. Introducción

Este manual está destinado a los administradores de la tienda **Milufer Matias**. Como administrador (superusuario) tienes acceso exclusivo a un panel de control desde donde puedes gestionar productos, clientes, pedidos y visualizar estadísticas de ventas.

**Credenciales de acceso administrador:**
- **Usuario:** MatiasT
- **Correo:** danitru07@gmail.com
- **Contraseña:** Matias..--

> **Importante:** Guarda estas credenciales en un lugar seguro. No las compartas con usuarios que no deban tener acceso administrativo.

---

## 2. Acceso al panel de administración

El panel de administración personalizado está disponible en:

```
http://127.0.0.1:8000/dashboard/
```

Para acceder:

1. Inicia sesión con tu cuenta de administrador en la página de login (`/usuarios/login/`).
2. Una vez autenticado, navega a `/dashboard/` o usa el botón de administración si está disponible en la barra de navegación.

> **Solo los superusuarios tienen acceso al dashboard.** Si un usuario normal intenta acceder, será redirigido automáticamente.

---

## 3. Vista general del Dashboard

Al ingresar al dashboard verás el **resumen general** de la tienda con tarjetas informativas:

| Tarjeta | Información que muestra |
|---|---|
| Total de ventas | Suma total de todos los pedidos registrados |
| Pedidos del mes | Cantidad de pedidos en el mes actual |
| Clientes registrados | Total de cuentas de usuario |
| Productos activos | Total de productos marcados como activos |
| Pedidos pendientes | Pedidos que aún no han sido confirmados o cancelados |

En la barra lateral (sidebar) encontrarás los accesos directos a todas las secciones del panel:
- **Inicio** → Resumen general
- **Productos** → Gestión de catálogo
- **Clientes** → Listado de usuarios
- **Pedidos** → Gestión de órdenes
- **Estadísticas** → Métricas y reportes

---

## 4. Gestión de productos

### 4.1 Ver listado de productos

Navega a **Dashboard → Productos**.

Verás una tabla con todos los productos registrados, incluyendo:
- ID
- Nombre
- Precio
- Stock
- Botones de acción: Editar / Eliminar

> En dispositivos móviles, la tabla se convierte en tarjetas individuales por producto para facilitar la lectura.

### 4.2 Agregar un producto nuevo

1. En la vista de productos, haz clic en **"Agregar producto"**.
2. Completa el formulario con los siguientes campos:

| Campo | Descripción | Obligatorio |
|---|---|---|
| Nombre | Nombre del producto | Sí |
| Categoría | Categoría a la que pertenece | Sí |
| Descripción | Texto descriptivo del producto | No |
| Precio | Precio de venta (con decimales) | Sí |
| Stock | Unidades disponibles | Sí |
| Imagen | Foto del producto (formatos: JPG, PNG, WEBP) | No |
| Activo | Si está marcado, el producto aparece en la tienda | Sí |

3. Haz clic en **"Guardar"** para crear el producto.

### 4.3 Editar un producto

1. En la tabla de productos, haz clic en el botón **"Editar"** del producto que deseas modificar.
2. El formulario se cargará con los datos actuales del producto.
3. Realiza los cambios necesarios y haz clic en **"Guardar"**.

### 4.4 Eliminar un producto

1. En la tabla de productos, haz clic en el botón **"Eliminar"** del producto.
2. El producto será eliminado permanentemente de la base de datos.

> **Precaución:** Esta acción no se puede deshacer. Si un producto está vinculado a pedidos históricos, considera **desactivarlo** (desmarca "Activo") en lugar de eliminarlo, para conservar el historial de ventas.

### 4.5 Gestión de categorías

Las categorías se gestionan desde el panel de administración de Django (`/admin/`):

1. Ingresa a `/admin/`
2. Ve a **Productos → Categorías**
3. Agrega, edita o desactiva categorías según necesites.

---

## 5. Gestión de clientes

### 5.1 Ver listado de clientes

Navega a **Dashboard → Clientes**.

Verás la lista de todos los usuarios registrados con:
- ID
- Nombre de usuario
- Correo electrónico
- Fecha de registro
- Botones de acción: Ver detalle / Editar

### 5.2 Ver detalle de un cliente

1. Haz clic en **"Ver"** junto al cliente que deseas revisar.
2. Se abrirá una vista con toda su información personal y su historial de actividad.

### 5.3 Editar un cliente

1. Haz clic en **"Editar"** junto al cliente.
2. Puedes modificar los siguientes campos:
   - Nombre de usuario
   - Correo electrónico
   - Nombre y apellido
   - Estado activo/inactivo

3. Haz clic en **"Guardar"** para confirmar los cambios.

> **Desactivar un cliente** (is_active = False) impide que ese usuario pueda iniciar sesión, sin eliminar su cuenta ni su historial de pedidos.

---

## 6. Gestión de pedidos

### 6.1 Ver listado de pedidos

Navega a **Dashboard → Pedidos**.

Verás una tabla con todos los pedidos registrados:
- ID del pedido
- Cliente
- Fecha de creación
- Total
- Estado (Pendiente / Confirmado / Cancelado / Expirado)
- Botones de acción

### 6.2 Acciones sobre pedidos

Para cada pedido dispones de los siguientes botones:

| Botón | Acción |
|---|---|
| **Ver** | Muestra el detalle completo: productos, cantidades, cliente y dirección |
| **Confirmar** | Cambia el estado del pedido a "Confirmado" |
| **Cancelar** | Cambia el estado del pedido a "Cancelado" |

### 6.3 Estados de los pedidos

| Estado | Descripción |
|---|---|
| **Pendiente** | Recién creado por el cliente, esperando confirmación |
| **Confirmado** | Aprobado por el administrador, en proceso de entrega |
| **Cancelado** | Cancelado manualmente (por cliente o administrador) |
| **Expirado** | Tiempo de procesamiento agotado automáticamente |

> Controla los pedidos pendientes con regularidad para procesarlos antes de que expiren.

---

## 7. Estadísticas

Navega a **Dashboard → Estadísticas** para acceder a un reporte visual y numérico del rendimiento de la tienda.

### Métricas disponibles:

**Ventas:**
- Total de ventas acumulado
- Ventas del mes actual
- Ventas del año actual
- Ticket medio por pedido

**Productos:**
- Top 5 productos más vendidos (por unidades)

**Clientes:**
- Total de clientes registrados
- Clientes nuevos este mes

**Pedidos:**
- 5 pedidos más recientes

> En dispositivos móviles, los gráficos y listas se adaptan al tamaño de pantalla automáticamente.

---

## 8. Panel de administración de Django (/admin/)

Además del dashboard personalizado, Django incluye su propio panel de administración en:

```
http://127.0.0.1:8000/admin/
```

Ingresa con las mismas credenciales de superusuario.

Desde aquí puedes hacer operaciones avanzadas como:

| Sección | Qué puedes hacer |
|---|---|
| **Usuarios** | Crear, editar, eliminar y asignar permisos a usuarios |
| **Grupos** | Crear grupos de permisos personalizados |
| **Categorías** | Gestionar categorías de productos |
| **Productos** | CRUD completo de productos |
| **Pedidos** | Ver y editar pedidos directamente en la base de datos |
| **Direcciones** | Ver las direcciones de envío de los clientes |

> El panel `/admin/` es más técnico y potente. Úsalo con precaución para operaciones que el dashboard no cubra.

---

## 9. Consideraciones de seguridad

- **No compartas tu contraseña de administrador** con nadie que no deba tener acceso. 
- **Cambia la contraseña periódicamente.** Puedes hacerlo desde `/admin/` → Usuarios → tu usuario → cambiar contraseña.
- **Cierra siempre tu sesión** después de trabajar en el panel, especialmente desde dispositivos compartidos.
- **Haz copias de seguridad** de la base de datos (`db.sqlite3`) regularmente para proteger el historial de pedidos y clientes.
- **No elimines productos con pedidos asociados.** En su lugar, márcalos como inactivos para preservar el historial.
- **Las cuentas de cliente desactivadas** no pueden iniciar sesión, pero sus datos se conservan.

---

## 10. Preguntas frecuentes del administrador

**¿Cómo recupero el acceso si olvido la contraseña de administrador?**  
Ejecuta en la terminal del servidor:
```bash
python manage.py changepassword MatiasT
```

**¿Puedo haber más de un administrador?**  
Sí. Desde `/admin/` → Usuarios, marca a cualquier usuario como `is_staff` y `is_superuser` para darle acceso completo al dashboard y al panel de Django.

**¿Qué pasa si elimino una categoría que tiene productos?**  
No se puede eliminar una categoría que tenga productos asociados (el sistema está configurado con `PROTECT`). Primero debes reasignar o eliminar los productos de esa categoría.

**¿Dónde se guardan las imágenes de los productos?**  
Las imágenes se almacenan en la carpeta `media/productos/` dentro del proyecto.

**¿Cómo agrego un nuevo administrador sin acceso a la terminal?**  
Desde `/admin/` → Usuarios → selecciona el usuario → activa los campos `staff status` y `superuser status` → guarda.
