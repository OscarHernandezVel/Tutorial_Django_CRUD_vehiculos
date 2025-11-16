# 🚗 Tutorial Django CRUD Vehículos

Una aplicación web completa de **gestión de vehículos** desarrollada con **Django 5.2**, demostrando operaciones CRUD (Crear, Leer, Actualizar, Eliminar) con una interfaz moderna usando **Bootstrap 4**.

## 📋 Características

✅ **CRUD Completo**
- Crear nuevos vehículos
- Listar vehículos registrados
- Editar información de vehículos
- Eliminar vehículos con confirmación

✅ **Interfaz de Usuario**
- Diseño responsivo con Bootstrap 4
- Navbar de navegación
- Tablas interactivas
- Modales de confirmación
- Formularios validados

✅ **Funcionalidades**
- Base de datos SQLite
- Panel de administración Django
- Validación de formularios
- Mensajes de éxito/error
- Gestión de colores (ROJO, AZUL, VERDE)

## 🛠️ Requisitos

- Python 3.11+
- Django 5.2.8
- pip (gestor de paquetes Python)

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio-url>
cd Tutorial_Django_CRUD_vehiculos
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
cd crud_example
python manage.py migrate
```

### 5. Crear superusuario (opcional, para el admin)

```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: **http://127.0.0.1:8000/**

## 🗂️ Estructura del Proyecto

```
Tutorial_Django_CRUD_vehiculos/
├── crud_example/                    # Proyecto Django
│   ├── crud_example/               # Configuración del proyecto
│   │   ├── __init__.py
│   │   ├── settings.py             # Configuraciones globales
│   │   ├── urls.py                 # Rutas principales
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── vehiclesapp/                # Aplicación de vehículos
│   │   ├── migrations/             # Migraciones de BD
│   │   ├── templates/              # Plantillas HTML
│   │   │   ├── base.html           # Plantilla base
│   │   │   ├── hello_world.html    # Página de inicio
│   │   │   ├── list_viewi.html     # Lista de vehículos
│   │   │   ├── vehiculo_form.html  # Formulario CRUD
│   │   │   └── vehiculo_confirm_delete.html  # Confirmación eliminación
│   │   ├── static/                 # Archivos estáticos (CSS, JS)
│   │   ├── models.py               # Modelo de datos
│   │   ├── views.py                # Vistas (lógica)
│   │   ├── urls.py                 # Rutas de la app
│   │   ├── admin.py                # Panel de administración
│   │   ├── apps.py
│   │   └── tests.py
│   ├── manage.py                   # Herramienta de gestión Django
│   ├── db.sqlite3                  # Base de datos
│   └── requirements.txt            # Dependencias
└── README.md
```

## 🚀 Rutas Disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Página de inicio |
| `/list/` | Listar todos los vehículos |
| `/create/` | Crear nuevo vehículo |
| `/update/<id>/` | Editar vehículo |
| `/delete/<id>/` | Eliminar vehículo |
| `/admin/` | Panel de administración Django |

## 📊 Modelo de Datos

### Vehículo (vehiculo)

```python
class vehiculo(models.Model):
    placa = CharField(max_length=6)           # Placa del vehículo
    marca = CharField(max_length=10)          # Marca (ej: Toyota, Ford)
    color = CharField(                        # Color disponible
        choices=[
            ('1', 'ROJO'),
            ('2', 'AZUL'),
            ('3', 'VERDE'),
        ]
    )
    modelo = IntegerField()                   # Año/modelo del vehículo
```

## 💻 Uso de la Aplicación

### Crear un Vehículo

1. Haz clic en **"Agregar Vehículo"** en la navbar o la página de inicio
2. Completa el formulario con:
   - **Placa**: Máximo 6 caracteres (ej: ABC123)
   - **Marca**: Máximo 10 caracteres (ej: Toyota)
   - **Color**: Selecciona entre ROJO, AZUL o VERDE
   - **Modelo**: Año del vehículo (ej: 2023)
3. Haz clic en **"Crear"**

### Ver Vehículos

1. Ve a **"Lista"** en la navbar
2. Verás todos los vehículos registrados en una tabla

### Editar un Vehículo

1. En la lista, haz clic en **"Editar"** (ícono de lápiz)
2. Modifica los datos que desees
3. Haz clic en **"Actualizar"**

### Eliminar un Vehículo

1. En la lista, haz clic en **"Eliminar"** (ícono de papelera)
2. Confirma la eliminación en el modal
3. El vehículo será eliminado permanentemente

## 🔧 Comandos Útiles

```bash
# Crear migraciones después de cambios en models.py
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Crear superusuario para el admin
python manage.py createsuperuser

# Iniciar servidor de desarrollo
python manage.py runserver

# Iniciar servidor en puerto específico
python manage.py runserver 0.0.0.0:8000

# Acceder a la consola de Django
python manage.py shell
```

## 📚 Vistas (Views)

- **home()**: Página de inicio con enlaces de navegación
- **list_view()**: Muestra todos los vehículos
- **create_view()**: Formulario para crear vehículos
- **update_view()**: Formulario para editar vehículos
- **delete_view()**: Confirmación y eliminación de vehículos

## 🎨 Dependencias Externas

- **Bootstrap 4.5.2**: Framework CSS responsivo
- **Font Awesome 4.7**: Iconografía
- **jQuery 3.5.1**: Interactividad
- **Popper.js 1.16**: Para tooltips y popovers

## 🐛 Solución de Problemas

### Error: "No such table: vehiclesapp_vehiculo"
```bash
python manage.py migrate
```

### Error: "No installed app with label 'vehiclesapp'"
Verifica que `'vehiclesapp.apps.VehiclesappConfig'` esté en `INSTALLED_APPS` en `settings.py`.

### Puerto 8000 en uso
```bash
python manage.py runserver 8001
```

## 📝 Notas de Desarrollo

- Las plantillas heredan de `base.html` para mantener consistencia
- El modelo `vehiculo` tiene validaciones en el formulario
- Se usan modales Bootstrap para confirmaciones
- Todos los formularios incluyen protección CSRF

## 🚀 Mejoras Futuras

- [ ] Agregar autenticación de usuarios
- [ ] Implementar búsqueda y filtrado
- [ ] Añadir paginación a la lista
- [ ] Exportar datos a PDF/Excel
- [ ] API REST con Django REST Framework
- [ ] Tests unitarios y de integración
- [ ] Desplegar en producción (Heroku, AWS, etc.)

## 👨‍💻 Autor

Tutorial de Django CRUD - Ingeniería de Requerimientos

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**¡Feliz desarrollo! 🎉**

Para más información sobre Django, visita: [Django Documentation](https://docs.djangoproject.com/)
