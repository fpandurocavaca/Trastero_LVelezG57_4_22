"""
config.py

Este fichero contiene configuración general del proyecto:
- Rutas a carpetas importantes
- Ruta de la base de datos
- URL de conexión SQLAlchemy

Así evitamos escribir rutas "a mano" en muchos ficheros.
"""

import os

# BASE_DIR es la carpeta raíz del proyecto.
# Si este fichero está en app/config.py, entonces BASE_DIR será el padre de "app".
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta donde guardaremos la base de datos SQLite
DATA_DIR = os.path.join(BASE_DIR, "data")

# Carpeta donde guardaremos fotos asociadas a objetos
PHOTOS_DIR = os.path.join(BASE_DIR, "photos")

# Ruta completa del fichero SQLite
DB_PATH = os.path.join(DATA_DIR, "trastero.db")

# URL que usa SQLAlchemy para conectarse a SQLite
DATABASE_URL = f"sqlite:///{DB_PATH}"
