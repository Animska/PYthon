# Ejercicio 6
# Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

cadenas=["Manzana", "pera", "BANANA", "naranja"]
cadenas.sort(key=str.lower)
print(cadenas)