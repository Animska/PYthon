# Crea una función que muestre y sume los elementos de una lista que se encuentran en
# un índice determinado según la serie 1,4,7...(o sea, sumando 3 al anterior índice,
# comenzando en 1)

def sumar_indices(lista):
    suma=0
    for i in range(1,len(lista),3):
        print(f"Lista[{i}]: {lista[i]}")
        suma += lista[i]
    print(f"Suma total: {suma}")

lista = [3, 13, 9, 49, 14, 10, 38, 11, 0, 34, 26, 34, 20, 9, 24, 42, 33, 35, 32, 14, 20, 24, 5]

sumar_indices(lista)