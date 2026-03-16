# Manual de Programador — Milufer Matias

**Versión:** 1.0  
**Fecha:** Marzo 2026  
**Framework:** Django 5.2.8  
**Python:** 3.13.12  
**Dirigido a:** Desarrolladores que mantienen o extienden el proyecto

---

## Tabla de contenidos

1. [Descripción general del proyecto](#1-descripción-general-del-proyecto)
2. [Requisitos del entorno](#2-requisitos-del-entorno)
3. [Instalación y puesta en marcha](#3-instalación-y-puesta-en-marcha)
4. [Estructura del proyecto](#4-estructura-del-proyecto)
5. [Apps y sus responsabilidades](#5-apps-y-sus-responsabilidades)
6. [Modelos de datos](#6-modelos-de-datos)
7. [Vistas y URLs](#7-vistas-y-urls)
8. [Templates](#8-templates)
9. [Archivos estáticos (CSS)](#9-archivos-estáticos-css)
10. [Configuración (settings.py)](#10-configuración-settingspy)
11. [Carrito de compras (sesiones)](#11-carrito-de-compras-sesiones)
12. [Sistema de permisos y control de acceso](#12-sistema-de-permisos-y-control-de-acceso)
13. [Patrones de diseño responsive aplicados](#13-patrones-de-diseño-responsive-aplicados)
14. [Bugs conocidos y advertencias activas](#14-bugs-conocidos-y-advertencias-activas)
15. [Guía de extensión del proyecto](#15-guía-de-extensión-del-proyecto)
16. [Despliegue en producción](#16-despliegue-en-producción)

---

## 1. Descripción general del proyecto

**Milufer Matias** es una aplicación web de comercio electrónico construida con el framework Django. Permite a los usuarios explorar productos, agregarlos a un carrito de compras, realizar pedidos y gestionar sus perfiles. Los administradores disponen de un panel de control personalizado para gestionar el inventario, los clientes y los pedidos, así como consultar estadísticas de ventas.

### Tecnologías utilizadas

| Tecnología | Versión | Rol |
|---|---|---|
| Python | 3.13.12 | Lenguaje base |
| Django | 5.2.8 | Framework web |
| Pillow | Última | Manejo de imágenes de productos |
| SQLite | Incorporado | Base de datos (desarrollo) |
| HTML5 | — | Plantillas / estructura |
| CSS3 | — | Estilos y diseño responsive |

> **Restricción de proyecto:** Solo se usan HTML, CSS y Python. No se han incorporado frameworks de JavaScript ni librerías de CSS externas (Bootstrap, Tailwind, etc.). Todo el diseño es CSS puro.

---

## 2. Requisitos del entorno

- Python 3.10 o superior
- pip
- Entorno virtual (recomendado)
- Sistema operativo: Linux, macOS o Windows

### Dependencias Python

```
Django>=5.0
Pillow
```

---

## 3. Instalación y puesta en marcha

### 3.1 Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Milufer_Matias
```

### 3.2 Crear y activar entorno virtual

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3.3 Instalar dependencias

```bash
pip install django pillow
```

### 3.4 Aplicar migraciones

```bash
python manage.py migrate
```

### 3.5 Crear superusuario

```bash
python manage.py createsuperuser
```

O directamente mediante el shell de Django (útil en scripts):

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
u = User.objects.create_superuser("MatiasT", "danitru07@gmail.com", "Matias..--")
u.save()
```

### 3.6 Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

---

## 4. Estructura del proyecto

```
Milufer_Matias/
│
├── manage.py                  # Punto de entrada de gestión Django
├── db.sqlite3                 # Base de datos SQLite (desarrollo)
│
├── milufer/                   # Configuración del proyecto Django
│   ├── settings.py            # Configuración global
│   ├── urls.py                # URLs raíz del proyecto
│   └── wsgi.py / asgi.py      # Entry points de servidor
│
├── productos/                 # App: catálogo de productos
│   ├── models.py              # Categoria, Producto
│   ├── views.py               # inicio, catalogo, producto_detalle
│   └── urls.py
│
├── usuarios/                  # App: autenticación y perfiles
│   ├── models.py              # Direccion, UsuarioEliminado
│   ├── views.py               # login, registro, perfil, logout, direcciones
│   └── urls.py
│
├── ventas/                    # App: carrito y pedidos
│   ├── models.py              # Pedido, PedidoProducto
│   ├── views.py               # agregar_carrito, ver_carrito, finalizar_compra...
│   └── urls.py
│
├── dashboard/                 # App: panel de administración personalizado
│   ├── models.py              # (vacío — usa modelos de otras apps)
│   ├── views.py               # productos, clientes, pedidos, estadísticas
│   ├── forms.py               # ProductoForm, ClienteForm
│   └── urls.py
│
├── templates/                 # Plantillas HTML globales
│   ├── base.html              # Layout base (navbar, footer)
│   ├── inicio.html
│   ├── catalogo.html
│   ├── producto.html
│   ├── login.html
│   ├── registro.html
│   ├── perfil.html
│   ├── carrito.html
│   ├── finalizar_compra.html
│   ├── direccion_form.html
│   └── dashboard/             # Plantillas del panel admin
│       ├── dashboard.html
│       ├── productos.html
│       ├── producto_form.html
│       ├── clientes.html
│       ├── detalle_cliente.html
│       ├── editar_cliente.html
│       ├── pedidos.html
│       ├── detalle_pedido.html
│       └── estadisticas.html
│
├── static/                    # Archivos estáticos
│   └── css/
│       ├── base.css
│       ├── home.css
│       ├── catalogo.css
│       ├── login.css
│       ├── registro.css
│       ├── carrito.css
│       ├── perfil.css
│       └── dashboard/
│           ├── dashboard.css
│           ├── productos.css
│           ├── clientes.css
│           ├── pedidos.css
│           └── estadisticas.css
│
└── media/                     # Archivos subidos por usuarios (imágenes)
    └── productos/
```

---

## 5. Apps y sus responsabilidades

### `productos`
Gestiona el catálogo público de la tienda.
- **Modelos:** `Categoria`, `Producto`
- **Vistas:** Página de inicio con productos destacados, catálogo con filtros por categoría, página de detalle de producto
- **Namespace de URLs:** `productos`

### `usuarios`
Gestiona la autenticación, registro y perfiles de usuario.
- **Modelos:** `Direccion` (relación 1:N con `User`), `UsuarioEliminado` (registro histórico)
- **Vistas:** Login, logout, registro, perfil, CRUD de direcciones
- **Namespace de URLs:** `usuarios`
- Usa el modelo `User` incorporado de Django (`django.contrib.auth.models.User`)

### `ventas`
Gestiona el carrito de compras basado en sesiones y los pedidos en base de datos.
- **Modelos:** `Pedido`, `PedidoProducto`
- **Vistas:** Ver carrito, agregar/eliminar productos del carrito, finalizar compra
- **Namespace de URLs:** `ventas`
- El carrito se almacena en `request.session["carrito"]` como diccionario `{str(producto_id): {"cantidad": int}}`

### `dashboard`
Panel de control exclusivo para superusuarios.
- **Modelos:** Ninguno propio (opera sobre los de otras apps)
- **Vistas:** CRUD de productos, listado/edición de clientes, gestión de pedidos, estadísticas agregadas
- **Formas:** `ProductoForm` (ModelForm de Producto), `ClienteForm` (ModelForm de User)
- **Namespace de URLs:** `dashboard`
- Todo acceso está protegido con el decorador `@superuser_required`

---

## 6. Modelos de datos

### `Categoria` (app: productos)

| Campo | Tipo | Restricciones |
|---|---|---|
| nombre | CharField(100) | unique=True |
| descripcion | TextField | blank, null |
| activo | BooleanField | default=True |

### `Producto` (app: productos)

| Campo | Tipo | Restricciones |
|---|---|---|
| categoria | ForeignKey(Categoria) | PROTECT |
| nombre | CharField(200) | — |
| descripcion | TextField | blank, null |
| precio | DecimalField(10,2) | — |
| stock | PositiveIntegerField | default=0 |
| imagen | ImageField | upload_to="productos/", blank, null |
| activo | BooleanField | default=True |
| creado | DateTimeField | auto_now_add=True |
| actualizado | DateTimeField | auto_now=True |

> La relación `Categoria → Producto` usa `on_delete=PROTECT`: no se puede eliminar una categoría que tenga productos activos.

### `Pedido` (app: ventas)

| Campo | Tipo | Restricciones |
|---|---|---|
| usuario | ForeignKey(User) | SET_NULL, null=True |
| total | DecimalField(10,2) | default=0 |
| estado | CharField(20) | choices: pendiente/confirmado/cancelado/expirado |
| fecha_creacion | DateTimeField | auto_now_add |
| fecha_actualizacion | DateTimeField | auto_now |
| expiracion | DateTimeField | — |

### `PedidoProducto` (app: ventas)

| Campo | Tipo | Restricciones |
|---|---|---|
| pedido | ForeignKey(Pedido) | CASCADE, related_name="items" |
| producto | ForeignKey(Producto) | CASCADE |
| cantidad | IntegerField | — |
| precio | DecimalField(10,2) | — |

### `Direccion` (app: usuarios)

| Campo | Tipo | Restricciones |
|---|---|---|
| usuario | ForeignKey(User) | CASCADE |
| direccion | CharField(255) | — |
| ciudad | CharField(100) | — |
| referencia | CharField(255) | blank |
| principal | BooleanField | default=False |

### `UsuarioEliminado` (app: usuarios)

Registro histórico de usuarios eliminados para auditoría.

| Campo | Tipo |
|---|---|
| nombre | CharField(150) |
| email | EmailField |
| telefono | CharField(20) |
| fecha_registro | DateTimeField |
| fecha_eliminacion | DateTimeField (auto) |

---

## 7. Vistas y URLs

### URLs raíz (`milufer/urls.py`)

```
/                   → productos.urls (inicio, catálogo, detalle)
/usuarios/          → usuarios.urls  (login, registro, perfil, direcciones)
/ventas/            → ventas.urls    (carrito, pedidos, finalizar compra)
/dashboard/         → dashboard.urls (panel admin)
/admin/             → Django admin incorporado
/media/             → (solo en DEBUG) archivos subidos
```

> **Advertencia conocida:** En `milufer/urls.py` el prefijo `/usuarios/` está incluido **dos veces** (una sin namespace y otra con `namespace='usuarios'`). Esto genera una advertencia de Django sobre namespace duplicado. La segunda entrada es la que funciona correctamente; la primera debe eliminarse en una refactorización futura.

### Namespaces de URL por app

| App | Namespace | Ejemplo de uso en template |
|---|---|---|
| productos | `productos` | `{% url 'productos:inicio' %}` |
| usuarios | `usuarios` | `{% url 'usuarios:login' %}` |
| ventas | `ventas` | `{% url 'ventas:carrito' %}` |
| dashboard | `dashboard` | `{% url 'dashboard:productos' %}` |

### Control de acceso por vista

| Decorador | Uso |
|---|---|
| `@login_required` | Vistas que requieren autenticación (carrito, perfil) |
| `@superuser_required` | Todas las vistas del dashboard |

`superuser_required` es un decorador local definido en `dashboard/views.py` que usa `user_passes_test(lambda u: u.is_superuser)`. No confundir con `@staff_member_required`.

---

## 8. Templates

Todas las plantillas están en `templates/` a nivel raíz, configurado en `settings.py`:

```python
'DIRS': [BASE_DIR / 'templates'],
```

### Herencia de plantillas

Todas las páginas extienden `base.html`:

```html
{% extends "base.html" %}
{% block content %}
    <!-- contenido de la página -->
{% endblock %}
```

`base.html` incluye:
- Barra de navegación con links dinámicos según autenticación
- Carga de archivos CSS por página mediante bloques
- Footer

### Variables de contexto importantes

| Vista | Variable de contexto | Tipo |
|---|---|---|
| `inicio` | `productos_destacados` | QuerySet de Producto |
| `catalogo` | `productos`, `categorias` | QuerySets |
| `producto_detalle` | `producto` | Instancia de Producto |
| `ver_carrito` | `items_carrito`, `total_carrito` | Lista de dicts, Decimal |
| `perfil_view` | `usuario`, `direcciones` | User, QuerySet |
| `estadisticas_view` | múltiples | varios (ver views.py) |

### Condicionales de superusuario en templates

El template `perfil.html` oculta la sección de direcciones para administradores:

```html
{% if not request.user.is_superuser %}
    <div class="seccion-direcciones">
        ...
    </div>
{% endif %}
```

---

## 9. Archivos estáticos (CSS)

Los archivos CSS están en `static/css/` y son cargados individualmente por cada template mediante el bloque `{% block estilos %}`.

### Convención de archivos CSS

Cada vista tiene su propio archivo CSS:

| Template | CSS correspondiente |
|---|---|
| `inicio.html` | `home.css` |
| `catalogo.html` | `catalogo.css` |
| `carrito.html` | `carrito.css` |
| `perfil.html` | `perfil.css` |
| `login.html` | `login.css` |
| `dashboard/*.html` | `dashboard/*.css` |

### Patrón responsive para tablas (card-style)

Para todas las tablas del proyecto se implementó un patrón de conversión a tarjetas en dispositivos móviles (`max-width: 768px`). Es el siguiente:

**En el HTML — añadir `data-label` a cada `<td>`:**

```html
<td data-label="Nombre">{{ producto.nombre }}</td>
<td data-label="Precio">{{ producto.precio }}</td>
```

**En el CSS — ocultar encabezados y convertir filas en bloques:**

```css
@media (max-width: 768px) {
    .tabla-productos thead {
        display: none;
    }
    .tabla-productos tr {
        display: block;
        margin-bottom: 1rem;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 0.8rem;
    }
    .tabla-productos td {
        display: block;
        text-align: right;
        padding: 6px 8px;
        position: relative;
        padding-left: 50%;
    }
    .tabla-productos td::before {
        content: attr(data-label);
        position: absolute;
        left: 8px;
        font-weight: 600;
    }
    .tabla-productos td:last-child {
        border-bottom: none;
    }
}
```

Este patrón se aplica en: `carrito.css`, `dashboard/productos.css`, `dashboard/clientes.css`, `dashboard/pedidos.css`.

---

## 10. Configuración (settings.py)

### Valores clave

```python
DEBUG = True                        # Cambiar a False en producción
ALLOWED_HOSTS = []                  # Añadir dominio en producción
SECRET_KEY = '...'                  # NUNCA exponer en producción

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"   # Para collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_URL = 'usuarios:login'             # Redirige decoradores de login
```

### Base de datos

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

SQLite es adecuado para desarrollo. Para producción se recomienda migrar a PostgreSQL o MySQL.

---

## 11. Carrito de compras (sesiones)

El carrito **no usa base de datos** — se almacena en la sesión del usuario como un diccionario en `request.session["carrito"]`.

### Estructura del carrito en sesión

```python
{
    "15": {"cantidad": 2},
    "7":  {"cantidad": 1},
}
```

Las claves son `str(producto.id)` para ser serializables por JSON.

### Lógica de negocio del carrito

- **Agregar:** Si el producto ya existe, suma la cantidad. Si supera el stock, la recorta.
- **Eliminar uno:** Reduce en 1. Si llega a 0, elimina la entrada.
- **Eliminar todo:** Borra la entrada del producto completo.
- **Vista del carrito:** Recorre el carrito, carga cada `Producto` de la BD, valida stock vigente. Si el stock cayó a 0, el item se elimina automáticamente de la sesión.

### Importante para depuración

Si un producto fue eliminado de la BD pero sigue en la sesión de un usuario, la vista del carrito lo detecta por el `except Producto.DoesNotExist` y limpia la sesión silenciosamente.

---

## 12. Sistema de permisos y control de acceso

### Niveles de usuario

| Nivel | Flag de Django | Acceso |
|---|---|---|
| Anónimo | — | Solo lectura: inicio, catálogo, detalle de producto |
| Cliente | `is_authenticated` | Carrito, perfil, direcciones, finalizar compra |
| Administrador | `is_superuser` | Todo lo anterior + dashboard completo |

### Decoradores usados

```python
# views.py de ventas y usuarios
@login_required
def agregar_carrito(request, producto_id):
    ...

# dashboard/views.py
def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def productos_view(request):
    ...
```

### En templates

```html
{% if user.is_authenticated %}
    <a href="{% url 'ventas:carrito' %}">Carrito</a>
{% else %}
    <a href="{% url 'usuarios:login' %}">Iniciar sesión</a>
{% endif %}

{% if user.is_superuser %}
    <a href="{% url 'dashboard:inicio' %}">Dashboard</a>
{% endif %}
```

---

## 13. Patrones de diseño responsive aplicados

### Breakpoints utilizados

| Breakpoint | Propósito |
|---|---|
| `max-width: 1024px` | Tabletas en horizontal |
| `max-width: 768px` | Tabletas en vertical / móviles grandes |
| `max-width: 480px` | Teléfonos |

### Adaptaciones por sección

| Sección | Adaptación mobile |
|---|---|
| Navegación (`home.css`) | Botones con `min-width` reducido, `row-gap` para separación |
| Catálogo | Grid de tarjetas pasa de múltiples columnas a 1 columna |
| Login | Contenedor centrado con `width: calc(100% - 32px); max-width: 320px; margin: 40px auto` |
| Carrito | Tabla → tarjetas apiladas con `data-label` |
| Dashboard tables | Tabla → tarjetas apiladas con `data-label` |
| Estadísticas | Canvas forzado a `width: 100% !important; height: auto !important` |
| Perfil | `.info-usuario` centrado con `text-align: center; justify-content: center` |

---

## 14. Bugs conocidos y advertencias activas

### Advertencias de `manage.py check` (7 items)

| Código | Descripción | Impacto |
|---|---|---|
| **W003** | Namespace duplicado `usuarios` en `milufer/urls.py` | Bajo — la segunda declaración (con namespace) es la que funciona |
| **W042** (×6) | Ausencia de `default_auto_field` en modelos de Categoria, Producto, Pedido, PedidoProducto, Direccion, UsuarioEliminado | Bajo — Django usa BigAutoField por defecto en versiones modernas |

**Corrección recomendada para el namespace duplicado** en `milufer/urls.py`:

```python
# Eliminar esta línea duplicada:
path("usuarios/", include("usuarios.urls")),

# Mantener solo esta:
path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
```

**Corrección recomendada para `default_auto_field`** en cada `apps.py`:

```python
class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'
```

### Bugs funcionales conocidos

| Bug | Ubicación | Descripción |
|---|---|---|
| URL inválida | `ventas/views.py` approx. línea con `redirect` | Usa `productos:detalle` pero el nombre correcto en `productos/urls.py` podría ser diferente — verificar que coincida el `name=` del path |
| Sin recuperación de contraseña | Proyecto completo | No existe vista ni template de `password_reset`. Las URLs de Django auth para reset no están configuradas |
| Variable de contexto incorrecta | `inicio.html` | La vista pasa `productos_destacados` pero el template podría iterar sobre `productos` — verificar la variable usada en el template |

---

## 15. Guía de extensión del proyecto

### Agregar una nueva app

```bash
python manage.py startapp nueva_app
```

1. Agrega `'nueva_app'` a `INSTALLED_APPS` en `settings.py`
2. Crea `nueva_app/urls.py` con su `urlpatterns`
3. Incluye las URLs en `milufer/urls.py`
4. Crea los templates en `templates/nueva_app/`
5. Crea los estilos en `static/css/nueva_app.css`

### Agregar un nuevo modelo

1. Define el modelo en `models.py` de la app correspondiente
2. Ejecuta:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Si deseas verlo en `/admin/`, regístralo en `admin.py`:
   ```python
   from django.contrib import admin
   from .models import MiModelo
   admin.site.register(MiModelo)
   ```

### Agregar una nueva categoría de producto

Desde `/admin/` → Productos → Categorías → Agregar.

O desde el shell:

```python
from productos.models import Categoria
Categoria.objects.create(nombre="Nueva Categoría", activo=True)
```

### Crear un superusuario adicional

```bash
python manage.py createsuperuser
```

O desde `/admin/` → Usuarios → seleccionar usuario → activar `is_staff` e `is_superuser`.

---

## 16. Despliegue en producción

> El entorno actual es de **desarrollo**. Antes de desplegar a producción es obligatorio realizar los siguientes cambios:

### Cambios en `settings.py`

```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']

# Generar una nueva SECRET_KEY (nunca usar la de desarrollo)
SECRET_KEY = 'clave-segura-generada-aleatoriamente'
```

Genera una nueva clave con:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Recolectar archivos estáticos

```bash
python manage.py collectstatic
```

Esto copia todos los archivos CSS e imágenes estáticas a `staticfiles/` para ser servidos por el servidor web.

### Migrar de SQLite a PostgreSQL (recomendado)

1. Instala el adaptador: `pip install psycopg2-binary`
2. Crea la base de datos en PostgreSQL
3. Actualiza `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nombre_bd',
           'USER': 'usuario',
           'PASSWORD': 'contraseña',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
4. Ejecuta las migraciones: `python manage.py migrate`

### Servidor web recomendado

- **Gunicorn** como servidor WSGI:
  ```bash
  pip install gunicorn
  gunicorn milufer.wsgi:application --bind 0.0.0.0:8000
  ```
- **Nginx** como proxy reverso y para servir archivos estáticos y de media.

### Consideraciones de seguridad para producción

- Usar variables de entorno para `SECRET_KEY`, credenciales de BD y cualquier configuración sensible (paquete `python-decouple` o `django-environ`).
- Activar HTTPS (certificado SSL/TLS).
- Configurar `SECURE_SSL_REDIRECT = True` y otras opciones de seguridad de Django.
- Configurar `CSRF_COOKIE_SECURE = True` y `SESSION_COOKIE_SECURE = True`.
- Configurar copias de seguridad automáticas de la base de datos.

---

*Manual generado en base al análisis completo del proyecto Milufer Matias — Marzo 2026*
