# Crea una función "extraer_elemento(lista)" que recibe por parámetro una lista.
# La función realiza:
# - Si la lista está vacía, indica que "La lista está vacía"
# - Si la lista tiene un elemento: mostrar el elemento con el mensaje "Solo hay 1
# elemento: x"
# - Si la lista tiene más de 1 elemento pero el primero es par, mostrar: "Primer elemento
# es par -> x"
# - Si la lista tiene más de 1 elemento pero el primero es impar, mostrar: "Primer
# elemento es impar-> x"
# La función retorna el resto de la lista no mostrada, o, si se produce una excepción,
# retorna None.
# Requisitos:
# - Utilizar estructura match con patrones sobre la lista.
# El control de excepciones contempla:
# - Si ha ocurrido error al hacer operación aritmética a la hora de comprobar si era par o
# impar, mostrar "Error" + el tipo de excepción + el mensaje interno"

def extraer_elemento(lista):
    try:
        match len(lista):
            case 0:
                print("La lista esta vacia")
            case 1:
                print(f"Solo hay 1 elemento: {lista[0]}")
            case _:
                try:
                    if lista[0] % 2 == 0:
                        print(f"Primer elemento es par -> {lista[0]}")
                    else:
                        print(f"Primer elemento es impar -> {lista[0]}")
                except Exception as e:
                    print(f"Error!: {e}")
                    return None
                
                resto=lista[1:]
                return resto
    
    except Exception as e:
        print(f"Error!: {e}")
        return None
    

#con patron de match
# def extraer_elemento(lista):
#     try:
#         match lista:
#             case []:
#                 print("La lista está vacía")
#                 return []
#             case [x]:
#                 print(f"Solo hay 1 elemento: {x}")
#                 return []
#             case [primero, *resto]:
#                 try:
#                     if primero % 2 == 0:
#                         print(f"Primer elemento es par -> {primero}")
#                     else:
#                         print(f"Primer elemento es impar -> {primero}")
#                 except Exception as e:
#                     print(f"Error {type(e).__name__}: {e}")
#                     return None
#                 return resto
#     except Exception as e:
#         print(f"Error {type(e).__name__}: {e}")
#         return None


# Lista vacía
print(extraer_elemento([]))  

# Lista con un solo elemento
print(extraer_elemento([7]))  

# Lista con primero par y más elementos
print(extraer_elemento([4, 5, 6]))  

# Lista con primero impar y más elementos
print(extraer_elemento([3, 5, 6]))  

# Lista con primero que no permite % (genera excepción)
print(extraer_elemento(["a", 5, 6]))  
