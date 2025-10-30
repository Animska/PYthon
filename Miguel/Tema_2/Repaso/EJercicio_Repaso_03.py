import random

repetir=""
while repetir!="n":
    try:
        dificultad=int(input("Ingrese la dificultad en la que desea jugar(un numero entre 10 y 50): "))
        acierto=False
        if 10<=dificultad<=50 and type(dificultad==int):
            numero=random.randint(1,dificultad)
            print(numero)
            for i in range(1,5):
                try:
                    intento=int(input(f"{i}º intento:"))
                    if intento==numero:
                        print(f"¡Has acertado! Te ha costado {i} intentos!")
                        acierto=True
                        break
                    else:
                        print("apunta mas abajo") if intento>numero else print("apunta mas arriba")
                except ValueError:
                    print("¡ERROR!:debe introducir un numero")
            if acierto is not True:
                print("Lo siento no lo has adivinado ¡Mas suerte la proxima!")

            while True:
                repetir=input("Quieres repetir(s/n): ").lower()
                match repetir:
                    case "s"|"n":
                        break
                    case _:
                        print("Debes introducir s o n")
        else:
            print("¡ERROR!:La dificultad debe estar entre 10 y 50")
    except ValueError:
        print("¡ERROR!:La dificultad debe ser un numero")