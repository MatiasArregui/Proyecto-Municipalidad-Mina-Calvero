# Proyecto Municipalidad Mina Calvero

Este proyecto es un sistema web desarrollado con Django para la gestión administrativa de la Municipalidad de Mina Calvero. Incluye módulos para diferentes áreas de gestión municipal como Defensa Civil, Seguridad Vial, entre otros.

## Tecnologías utilizadas

* Python 3.x
* Django
* HTML5, CSS3, Bootstrap
* JavaScript
* SQLite3 (base de datos por defecto)

## Estructura del proyecto

```
Proyecto-Municipalidad-Mina-Calvero/
│
├── municipalidad/          # Proyecto Django principal
├── seguridadVial/          # App para gestión de seguridad vial
├── db.sqlite3              # Base de datos
├── manage.py               # Script de gestión de Django
├── requirements.txt        # Dependencias del proyecto
├── Lib/, Include/, Scripts/ y pyvenv.cfg  # Entorno virtual
```

## Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/Proyecto-Municipalidad-Mina-Calvero.git
cd Proyecto-Municipalidad-Mina-Calvero
```

2. **Crear y activar entorno virtual (opcional)**

Si no está creado:

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones y correr el servidor**

```bash
python manage.py migrate
python manage.py runserver
```

## Características principales

* Gestión de instituciones, personas, elementos y catástrofes
* Sistema de login (por implementar/mejorar)
* Formularios con validaciones
* Filtros y tablas responsivas
* Uso de Bootstrap y JavaScript para mejorar la interfaz

## Autores

* Equipo de desarrollo de la Municipalidad de Mina Calvero

## Licencia

Este proyecto es de uso educativo y privado. Si desea reutilizarlo, contactar previamente al autor.
