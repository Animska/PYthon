# Ejercicio 2
# Combinar y limpiar listas. Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento
# eliminado.
# Limpia completamente lista_b usando clear().ç

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a.pop(3))
lista_b.clear()
print(lista_a)
print(lista_b)