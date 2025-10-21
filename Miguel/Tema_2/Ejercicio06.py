# Crea un programa que pida al usuario un número entre 1 y 10 y que:
# 1. Compruebe que el número está en ese rango (si no, pide otro).
# 2. Muestre su tabla de multiplicar.
# 3. Pregunte si desea repetir con otro número (s/n)
while True:
    numero = int(input("Introduce un número: "))
    if 1 <= numero <= 10:
        print(f"Tabla de multiplicar de: {numero}")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")        
        while True:
            repetir = input("¿Quieres repetir? (S/N): ").upper()
            match repetir:
                case "S":
                    break 
                case "N":
                    print("Programa finalizado.")
                    exit()
                case _:
                    print("Valor incorrecto, usa S o N.")
    else:
        print("Ese número no está entre el 1 y el 10.")
