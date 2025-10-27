# Ejercicio 5
# Extrayendo el centro. Dada una lista con un número impar de elementos, extrae el
# elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]
indice_centro = int(len(lista)/2)
centro= lista[indice_centro]

print(centro)