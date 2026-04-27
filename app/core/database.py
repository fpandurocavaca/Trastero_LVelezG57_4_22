"""
database.py

Este fichero crea:
- el motor de conexión a SQLite (engine)
- la clase SessionLocal para abrir sesiones de BD
- la clase Base para que los modelos SQLAlchemy hereden de ella
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# engine = conexión principal a la base de datos.
# echo=True imprime todas las consultas SQL en consola (útil para debug).
# Cuando el proyecto esté estable, se recomienda poner echo=False.
engine = create_engine(DATABASE_URL, echo=False)

# SessionLocal permite abrir una sesión de trabajo con la BD.
# autoflush=False evita que SQLAlchemy guarde automáticamente cambios sin pedirlo.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base es la clase base para todos los modelos.
# Ejemplo: class Estanteria(Base): ...
Base = declarative_base()