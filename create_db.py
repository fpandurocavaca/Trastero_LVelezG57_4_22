"""
create_db.py

Script para crear la base de datos SQLite.

Este script crea el fichero:
data/trastero.db

Ejecutar:
python3 create_db.py
"""

import os
from app.core.database import engine, Base
from app.core import models  # IMPORTANTE: se importa para que SQLAlchemy conozca las tablas
from app.config import DATA_DIR


def main():
    # Creamos la carpeta data/ si no existe
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    print("Creando base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada correctamente.")


if __name__ == "__main__":
    main()
    