respuesta=""

while respuesta not in ("S","N"):
    respuesta=input("introduzca S o N para continuar: ").upper()
    if respuesta in("S","N"):
        #1.-salida de true, 2.-Condicion, 3.-salida de else
        print("Continuamos") if respuesta=="S"  else print("Fin del programa")
    else:
        print("Respuesta incorrecta")