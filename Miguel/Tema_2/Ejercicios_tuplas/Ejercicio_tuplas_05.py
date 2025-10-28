# Crea una función "contar_pares_impares" que reciba por parámetro:
# - lista: una lista de números enteros
# La función debe devolver 2 enteros (una tupla). El primer entero indica
# la cantidad de números pares y el segundo entero indica la cantidad de números
# impares de la lista recibida por parámetro.

def contar_pares_impares(lista):
    pares = len([num for num in lista if num%2==0])
    impares = len(lista) - pares
    return (pares,impares)

lista = list(range(1,21))

pares,impares = contar_pares_impares(lista)
print(f"numeros pares: {pares}")
print(f"numeros impares: {impares}")