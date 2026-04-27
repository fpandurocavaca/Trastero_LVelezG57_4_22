"""
main_cli.py

Aplicación por consola para gestionar el trastero.

IMPORTANTE:
Este CLI se usa para probar que la base de datos funciona.
Más adelante la aplicación principal será la GUI con Tkinter.

Ejecutar con:
python3 -m app.cli.main_cli
"""

from app.core.database import SessionLocal
from app.core import crud


# -------------------------
# FUNCIONES DE MENÚ
# -------------------------
def menu():
    """
    Muestra el menú principal.
    """
    print("\n--- MENÚ TRASTERO ---")
    print("1. Crear estantería")
    print("2. Crear balda")
    print("3. Crear caja")
    print("4. Crear objeto")
    print("5. Listar estanterías")
    print("6. Listar baldas")
    print("7. Listar cajas")
    print("8. Listar objetos")
    print("0. Salir")


def opcion_crear_estanteria(db):
    nombre = input("Nombre estantería: ").strip()
    est = crud.crear_estanteria(db, nombre)
    print(f"OK -> Estantería creada con ID {est.id}")


def opcion_crear_balda(db):
    estanterias = crud.listar_estanterias(db)

    if not estanterias:
        print("No hay estanterías. Primero crea una estantería.")
        return

    print("\nEstanterías existentes:")
    for e in estanterias:
        print(f"{e.id} - {e.nombre}")

    estanteria_id = int(input("ID estantería: "))
    numero = int(input("Número de balda: "))

    balda = crud.crear_balda(db, estanteria_id, numero)
    print(f"OK -> Balda creada con ID {balda.id}")


def opcion_crear_caja(db):
    baldas = crud.listar_baldas(db)

    if not baldas:
        print("No hay baldas. Primero crea una balda.")
        return

    print("\nBaldas existentes:")
    for b in baldas:
        print(f"{b.id} - Estantería {b.estanteria_id} - Balda {b.numero}")

    balda_id = int(input("ID balda: "))
    nombre = input("Nombre caja: ").strip()

    caja = crud.crear_caja(db, balda_id, nombre)
    print(f"OK -> Caja creada con ID {caja.id}")


def opcion_crear_objeto(db):
    cajas = crud.listar_cajas(db)

    if not cajas:
        print("No hay cajas. Primero crea una caja.")
        return

    print("\nCajas existentes:")
    for c in cajas:
        print(f"{c.id} - {c.nombre} (Balda ID: {c.balda_id})")

    caja_id = int(input("ID caja: "))
    nombre = input("Nombre objeto: ").strip()
    descripcion = input("Descripción: ").strip()
    cantidad = int(input("Cantidad: "))

    obj = crud.crear_objeto(db, caja_id, nombre, descripcion, cantidad)
    print(f"OK -> Objeto creado con ID {obj.id}")


def opcion_listar_estanterias(db):
    estanterias = crud.listar_estanterias(db)

    if not estanterias:
        print("No hay estanterías.")
        return

    print("\n--- ESTANTERÍAS ---")
    for e in estanterias:
        print(f"{e.id} - {e.nombre}")


def opcion_listar_baldas(db):
    baldas = crud.listar_baldas(db)

    if not baldas:
        print("No hay baldas.")
        return

    print("\n--- BALDAS ---")
    for b in baldas:
        print(f"{b.id} - Estantería ID {b.estanteria_id} - Balda número {b.numero}")


def opcion_listar_cajas(db):
    cajas = crud.listar_cajas(db)

    if not cajas:
        print("No hay cajas.")
        return

    print("\n--- CAJAS ---")
    for c in cajas:
        print(f"{c.id} - {c.nombre} - Balda ID {c.balda_id}")


def opcion_listar_objetos(db):
    objetos = crud.listar_objetos(db)

    if not objetos:
        print("No hay objetos.")
        return

    print("\n--- OBJETOS ---")
    for o in objetos:
        caja = o.caja.nombre if o.caja else "SIN CAJA"
        print(f"{o.id} - {o.nombre} ({o.cantidad}) - Caja: {caja}")


# -------------------------
# MAIN
# -------------------------
def main():
    """
    Función principal del CLI.
    Abre sesión a la base de datos y ejecuta el menú.
    """
    db = SessionLocal()

    while True:
        menu()
        opcion = input("Selecciona opción: ").strip()

        if opcion == "1":
            opcion_crear_estanteria(db)
        elif opcion == "2":
            opcion_crear_balda(db)
        elif opcion == "3":
            opcion_crear_caja(db)
        elif opcion == "4":
            opcion_crear_objeto(db)
        elif opcion == "5":
            opcion_listar_estanterias(db)
        elif opcion == "6":
            opcion_listar_baldas(db)
        elif opcion == "7":
            opcion_listar_cajas(db)
        elif opcion == "8":
            opcion_listar_objetos(db)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

    db.close()


if __name__ == "__main__":
    main()