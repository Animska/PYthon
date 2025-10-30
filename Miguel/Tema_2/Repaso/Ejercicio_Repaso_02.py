# Ejercicio 2
# Realizar un algoritmo para determinar, de N cantidades introducidas por teclado:
# - La media aritmética.
# - El número más alto.
# - El número más bajo.

n = int(input("¿Cuántos números vas a introducir?: "))
numeros = []

for i in range(n):
    num = float(input(f"Introduce el número {i+1}: "))
    numeros.append(num)

media = sum(numeros)/n
maximo = max(numeros)
minimo = min(numeros)
print("Media aritmética:", media)
print("Número más alto:", maximo)
print("Número más bajo:", minimo)
