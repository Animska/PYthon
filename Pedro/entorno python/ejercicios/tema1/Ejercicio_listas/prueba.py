numeros = []

while (numero:=float(input("Ingresa un número: "))) != 0:
    numeros.append(numero)

print("Lista original:", numeros)

# Eliminar duplicados
numeros_sin_duplicados = set(numeros)

print("Lista sin duplicados:", numeros_sin_duplicados)