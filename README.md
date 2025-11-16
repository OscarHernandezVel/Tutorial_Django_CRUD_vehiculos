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

---

**¡Feliz desarrollo! 🎉**

Para más información sobre Django, visita: [Django Documentation](https://docs.djangoproject.com/)

