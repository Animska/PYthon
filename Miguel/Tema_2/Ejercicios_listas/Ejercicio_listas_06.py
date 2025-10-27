# Ejercicio 6
# Reversa parcial. Dada una lista, invierte solo la primera mitad de la lista (utilizando
# slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
lista_reversa=lista[2::-1]+lista[3:]

print(lista_reversa)