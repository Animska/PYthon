# Crear una función que reciba como parámetro una lista.
# La función recorre la lista en orden inverso y suma los 5 últimos números que sean
# múltiplos de 3.
# reversed(lista) invierte una lista o usa slicing.
# Si no existen 5 números múltiplos de 3, informar de este hecho.
# Por último, mostrar la suma por pantalla.
# El 0 se considera múltiplo de todos los números

def ejercicio3(lista):
    multiplos_3 = [num for num in reversed(lista) if num % 3 == 0 or num == 0][:5]
    suma = sum(multiplos_3)
    for num in multiplos_3:
        print(f"Número múltiplo de 3 encontrado: {num}")
    print(f"Suma de los últimos 5 múltiplos de 3: {suma}")

lista = [3, 13, 9, 49, 14, 10, 38, 11, 0, 34, 26, 34, 20, 9, 24, 42, 33, 35, 32, 14, 20, 24, 5, 0]
ejercicio3(lista)
