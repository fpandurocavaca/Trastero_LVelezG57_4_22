"""
crud.py

CRUD significa:
Create, Read, Update, Delete

Este fichero contiene funciones para:
- crear estanterías, baldas, cajas, objetos
- listar estanterías, baldas, cajas, objetos

Ventaja:
La CLI o la GUI no tendrán SQL directamente, solo llamarán a estas funciones.
"""

from sqlalchemy.orm import Session
from app.core.models import Estanteria, Balda, Caja, Objeto


# -------------------------
# ESTANTERÍAS
# -------------------------
def crear_estanteria(db: Session, nombre: str) -> Estanteria:
    """
    Crea una estantería y la guarda en la base de datos.
    """
    est = Estanteria(nombre=nombre)
    db.add(est)
    db.commit()
    db.refresh(est)  # refresca el objeto para obtener ID asignado
    return est


def listar_estanterias(db: Session):
    """
    Devuelve todas las estanterías existentes.
    """
    return db.query(Estanteria).order_by(Estanteria.id).all()


# -------------------------
# BALDAS
# -------------------------
def crear_balda(db: Session, estanteria_id: int, numero: int) -> Balda:
    """
    Crea una balda asociada a una estantería.
    """
    balda = Balda(estanteria_id=estanteria_id, numero=numero)
    db.add(balda)
    db.commit()
    db.refresh(balda)
    return balda


def listar_baldas(db: Session):
    """
    Devuelve todas las baldas existentes.
    """
    return db.query(Balda).order_by(Balda.id).all()


# -------------------------
# CAJAS
# -------------------------
def crear_caja(db: Session, balda_id: int, nombre: str) -> Caja:
    """
    Crea una caja asociada a una balda.
    """
    caja = Caja(nombre=nombre, balda_id=balda_id)
    db.add(caja)
    db.commit()
    db.refresh(caja)
    return caja


def listar_cajas(db: Session):
    """
    Devuelve todas las cajas existentes.
    """
    return db.query(Caja).order_by(Caja.id).all()


# -------------------------
# OBJETOS
# -------------------------
def crear_objeto(db: Session, caja_id: int, nombre: str, descripcion: str, cantidad: int) -> Objeto:
    """
    Crea un objeto y lo guarda dentro de una caja.
    """
    obj = Objeto(
        nombre=nombre,
        descripcion=descripcion,
        cantidad=cantidad,
        caja_id=caja_id
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def listar_objetos(db: Session):
    """
    Devuelve todos los objetos existentes.
    """
    return db.query(Objeto).order_by(Objeto.id).all()