# Ejercicio 1
# Añadir y modificar elementos. Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista=list(range(1,6))
lista.append(6)
lista.insert(2,10)
lista[0]=0
print(lista)