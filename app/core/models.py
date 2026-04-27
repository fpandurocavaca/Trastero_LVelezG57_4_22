"""
models.py

Aquí definimos las tablas del sistema.

Modelo actual (simple):
- Estantería -> tiene varias Baldas
- Balda -> tiene varias Cajas
- Caja -> tiene varios Objetos
- Objeto -> pertenece opcionalmente a una Caja

Más adelante podremos ampliar:
- objetos directamente en balda
- cajas dentro de cajas
- fotos
- movimientos/historial
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


# ------------------------
# ESTANTERÍAS
# ------------------------
class Estanteria(Base):
    """
    Tabla de estanterías.
    Ejemplo: "Estantería 1", "Estantería metálica", etc.
    """
    __tablename__ = "estanterias"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    # relationship permite acceder a las baldas de esta estantería.
    # Ejemplo: estanteria.baldas
    baldas = relationship("Balda", back_populates="estanteria")


# ------------------------
# BALDAS
# ------------------------
class Balda(Base):
    """
    Tabla de baldas.
    Cada balda pertenece a una estantería.
    """
    __tablename__ = "baldas"

    id = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False)

    # Clave foránea: cada balda está asociada a una estantería.
    estanteria_id = Column(Integer, ForeignKey("estanterias.id"), nullable=False)

    # relationship inversa: balda.estanteria devuelve el objeto Estanteria
    estanteria = relationship("Estanteria", back_populates="baldas")

    # Cada balda puede contener varias cajas
    cajas = relationship("Caja", back_populates="balda")


# ------------------------
# CAJAS
# ------------------------
class Caja(Base):
    """
    Tabla de cajas.
    Una caja está situada en una balda.
    """
    __tablename__ = "cajas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    balda_id = Column(Integer, ForeignKey("baldas.id"), nullable=False)
    balda = relationship("Balda", back_populates="cajas")

    objetos = relationship("Objeto", back_populates="caja")


# ------------------------
# OBJETOS
# ------------------------
class Objeto(Base):
    """
    Tabla de objetos almacenados en el trastero.

    Nota:
    Actualmente solo se permite que un objeto esté dentro de una caja.
    Más adelante se puede permitir que esté directamente en balda o suelo.
    """
    __tablename__ = "objetos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    cantidad = Column(Integer, default=1)

    # Si caja_id es NULL significa que el objeto no está en ninguna caja.
    caja_id = Column(Integer, ForeignKey("cajas.id"), nullable=True)

    caja = relationship("Caja", back_populates="objetos")