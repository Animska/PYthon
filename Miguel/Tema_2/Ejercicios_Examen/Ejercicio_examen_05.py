# Crea una función que reciba dos listas, lista pares y lista impares.
# La función multiplica ambas listas elemento a elemento, guardando el resultado
# en una nueva lista. Al final retorna la lista “resultado”.
# Es decir, resultado[i]=pares[i] * impares[i].
# Hay que tener en cuenta que ambas listas pueden ser de diferente tamaño
def multiplicar_listas(pares, impares):
    max_len = max(len(pares), len(impares))
    resultado = []

    for i in range(max_len):
        valor_pares = pares[i] if i < len(pares) else None
        valor_impares = impares[i] if i < len(impares) else None

        if valor_pares is not None and valor_impares is not None:
            # Se podria usar tambien:
            # if (isinstance(valor_pares, int) and isinstance(valor_impares, int)) or (isinstance(valor_pares, str) and isinstance(valor_impares, int)):
            #     producto = valor_pares * valor_impares
            # pero en mi opinion asi queda mas claro aunque se repita codigo
            if (isinstance(valor_pares, int) and isinstance(valor_impares, int)):
                producto = valor_pares * valor_impares
            else:
                #si uno es un string, se multiplica poniendo primero el string para que funcione bien
                if isinstance(valor_pares, str) and isinstance(valor_impares, int):
                    producto = valor_pares * valor_impares
                elif isinstance(valor_impares, str) and isinstance(valor_pares, int):
                    producto = valor_impares * valor_pares
                else:
                    producto = 0 
            resultado.append(producto)
        else:
            #Si solo existe uno, digamos la posicion 4 y el otro array solo tiene 3 se añade directamente a resultado
            resultado.append(valor_pares if valor_pares is not None else valor_impares)

    return resultado

lista1 = [1, "B4C", 3, 4]
lista2 = [7, 8, 9]

print(multiplicar_listas(lista1, lista2))