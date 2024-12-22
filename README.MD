# Proyecto: Vásquez Sergio FINAL 🎓

Este es un proyecto de sistema de inscripción desarrollado como evaluación final para la asignatura **Back-End**. El sistema incluye funcionalidades completas para la gestión de participantes e instituciones, y expone una API pública para futuras integraciones.

---

## 🖥️ Funcionalidades principales

- **Página principal**: Navegación clara con botones que llevan a las secciones principales del sistema.
- **Gestión de participantes**:
  - Listado completo de participantes inscritos.
  - Formulario para agregar inscripciones con validaciones.
  - Actualización y eliminación de inscripciones.
- **Gestión de instituciones**:
  - Listado de instituciones.
  - Formulario para agregar nuevas instituciones.
- **API REST**:
  - Endpoint para obtener los datos del autor del proyecto.
  - Endpoint para listar y buscar instituciones por ID.
- **Validaciones**:
  - Campos obligatorios con validaciones estrictas desde `forms.py`.
  - Correo electrónico, longitud de campos, y valores dentro de rangos permitidos.
- **Base de datos**:
  - Conexión a una base de datos MySQL configurada.

---

## 🚀 Tecnologías utilizadas

- **Lenguaje:** Python 3.12.6 🐍
- **Framework:** Django 5.1.4 🌐
- **Frontend:** Bootstrap 5 🎨
- **Base de datos:** MySQL 🗃️
- **API:** Django REST Framework 📡

---

## 🔧 Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

# Clona el repositorio
git clone https://github.com/Srg-vasquez/Sergio-Vasquez-FINAL.git

# Dirígete al directorio del proyecto
cd Sergio-Vasquez-FINAL

# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

# Configura la base de datos:
# 1. Asegúrate de tener MySQL en ejecución.
# 2. Crea una base de datos llamada 'django_seminario'.
# 3. Asegúrate de configurar las credenciales correctas en settings.py.

# Realiza las migraciones
python manage.py makemigrations
python manage.py migrate

# Inicia el servidor
python manage.py runserver
