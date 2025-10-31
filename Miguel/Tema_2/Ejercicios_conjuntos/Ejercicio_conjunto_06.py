# Ejercicio 6 – Agenda telefónica
# Implementa una agenda telefónica simple utilizando un diccionario. Las claves serán los
# nombres y los valores serán tuplas con el número de teléfono y la dirección.
# Debes crear las siguientes funciones:
# - Introducir un nuevo contacto
# - Buscar un contacto por nombre y mostrar su teléfono y dirección.
# - Eliminar contacto por nombre
# - Mostrar toda la agenda
# - Eliminar toda la agenda

agenda={}

def introducir_contacto(nombre, telefono, direccion):
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        agenda[nombre] = (telefono, direccion)
        print(f"Contacto {nombre} agregado.")

def buscar_contacto(nombre):
    if nombre in agenda:
        telefono, direccion = agenda[nombre]
        print(f"Nombre: {nombre}, Teléfono: {telefono}, Dirección: {direccion}")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado para eliminar.")

def mostrar_agenda():
    if agenda:
        for nombre, (telefono, direccion) in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}, Dirección: {direccion}")
    else:
        print("La agenda está vacia.")

def eliminar_toda_agenda():
    agenda.clear()
    print("Se ha eliminado toda la agenda.")

opcion=None
while opcion!=6:
    print("¡Bienvenido a tu agenda! ¿Que deseas hacer?")
    try:
        opcion=int(input("""
        Introduzca la operacion:
            0.-Introducir Contacto
            1.-Buscar Contacto
            2.-Eliminar Contacto
            3.-Eliminar Toda La Agenda
            4.-Mostrar Agenda
            5.-Salir
        """))
        match opcion:
            case 0:
                nombre,telefono,direccion=input("Introduce el nombre,telefono y direccion separados por coma de quien quieras añadir: ").split(",").lower()
                introducir_contacto(nombre, telefono, direccion)
            case 1:
                nombre=input("Introduce el nombre del contacto que deseas buscar: ").lower()
                buscar_contacto(nombre)
            case 2:
                nombre=input("Introduce el nombre del contacto que deseas eliminar: ").lower
                eliminar_contacto(nombre)
            case 3:
                eliminar_toda_agenda()
            case 4:
                mostrar_agenda()
            case 5:
                print("Saliendo...")
                break
            case _:
                print("¡Error! La opcion debe estar entre 0 y 5")
    except ValueError as e:
        print("¡Error! la opcion debe ser un numero")
        print(e)
    print("--------------------------------------------------------------")