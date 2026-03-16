# Milufer Matias — Tienda en Línea

Aplicación web de comercio electrónico desarrollada con **Django 5.2.8** y **Python 3.13**. Permite a los clientes explorar un catálogo de productos, gestionar un carrito de compras y realizar pedidos. Los administradores disponen de un panel de control personalizado con estadísticas, gestión de inventario, clientes y pedidos.

---

## Stack tecnológico

| Tecnología | Versión | Uso |
|---|---|---|
| Python | 3.13.12 | Lenguaje base |
| Django | 5.2.8 | Framework web |
| Pillow | Última | Procesamiento de imágenes |
| SQLite | Incorporado | Base de datos (desarrollo) |
| HTML5 / CSS3 | — | Frontend sin frameworks externos |

---

## Requisitos previos

- Python 3.10 o superior
- pip

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd Milufer_Matias

# 2. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows

# 3. Instalar dependencias
pip install django pillow

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Iniciar servidor de desarrollo
python manage.py runserver
```

La aplicación queda disponible en: **http://127.0.0.1:8000/**

---

## Estructura del proyecto

```
Milufer_Matias/
├── milufer/            # Configuración del proyecto (settings, urls raíz, wsgi)
├── productos/          # App: catálogo de productos y categorías
├── usuarios/           # App: autenticación, registro y perfiles de usuario
├── ventas/             # App: carrito de compras (sesiones) y pedidos
├── dashboard/          # App: panel de administración personalizado
├── templates/          # Plantillas HTML globales
│   └── dashboard/      # Plantillas del panel admin
├── static/
│   └── css/            # Hojas de estilo por vista (CSS puro, sin frameworks)
│       └── dashboard/
└── media/              # Archivos subidos (imágenes de productos)
```

---

## URLs principales

| Ruta | Descripción |
|---|---|
| `/` | Página de inicio con productos destacados |
| `/catalogo/` | Catálogo completo con filtros por categoría |
| `/producto/<id>/` | Detalle de producto |
| `/usuarios/login/` | Inicio de sesión |
| `/usuarios/registro/` | Registro de nuevo usuario |
| `/usuarios/perfil/` | Perfil y direcciones del usuario |
| `/ventas/carrito/` | Carrito de compras |
| `/ventas/finalizar/` | Finalizar compra |
| `/dashboard/` | Panel de administración (solo superusuarios) |
| `/admin/` | Panel de administración de Django |

---

## Apps y responsabilidades

### `productos`
Gestiona el catálogo público. Modelos: `Categoria`, `Producto`.

### `usuarios`
Autenticación y perfiles. Modelos: `Direccion`, `UsuarioEliminado`. Usa `User` de Django.

### `ventas`
Carrito basado en sesiones y pedidos en base de datos. Modelos: `Pedido`, `PedidoProducto`.  
Al finalizar la compra genera un enlace de WhatsApp con el resumen del pedido.

### `dashboard`
Panel exclusivo para superusuarios. Sin modelos propios — opera sobre las otras apps.  
Protegido con el decorador local `@superuser_required`.

---

## Variables de configuración clave (`settings.py`)

```python
DEBUG = True                         # Cambiar a False en producción
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
LOGIN_URL = 'usuarios:login'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## Comandos útiles

```bash
# Verificar el proyecto (errores y advertencias)
python manage.py check

# Crear migraciones después de cambiar modelos
python manage.py makemigrations
python manage.py migrate

# Recolectar archivos estáticos para producción
python manage.py collectstatic

# Abrir el shell de Django
python manage.py shell

# Cambiar contraseña de un usuario
python manage.py changepassword <username>
```

---

## Documentación adicional

| Documento | Descripción |
|---|---|
| [MANUAL_USUARIO.md](MANUAL_USUARIO.md) | Guía para clientes de la tienda |
| [MANUAL_ADMINISTRADOR.md](MANUAL_ADMINISTRADOR.md) | Guía para administradores del panel |
| [MANUAL_PROGRAMADOR.md](MANUAL_PROGRAMADOR.md) | Documentación técnica completa del proyecto |

---

## Notas para producción

Antes de desplegar a producción:

1. Cambiar `DEBUG = False` y configurar `ALLOWED_HOSTS`
2. Generar una nueva `SECRET_KEY` segura
3. Migrar la base de datos a PostgreSQL
4. Ejecutar `python manage.py collectstatic`
5. Configurar un servidor web (Nginx + Gunicorn)
6. Activar HTTPS

Consulta el [Manual de Programador](MANUAL_PROGRAMADOR.md#16-despliegue-en-producción) para la guía completa de despliegue.
