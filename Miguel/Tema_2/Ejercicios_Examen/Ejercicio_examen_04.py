# Crea la función "generar_listas()". Esta función lee de teclado una serie de números
# enteros hasta que se introduzca el 0. La función guarda los números introducidos
# (enteros) en 2 listas, lista pares y lista impares.
# La función retorna ambas listas(tupla).
# Requisitos:
# + Utilizar una expresión IF
# + Hacer control de excepciones sobre el elemento introducido en teclado. Solamente
# pueden ser números enteros.

def generar_listas():
    lista_pares=[]
    lista_impares=[]
    
    while  True:
        try:
            num = int(input('Introduce un número entero (0 para terminar): '))
            if num ==0:
                break
            else:
                if num%2==0:
                    lista_pares.append(num)
                else:
                    lista_impares.append(num)
        except ValueError:
            print("ERROR! El valor ingresado no es un número entero")
    
    return (lista_pares,lista_impares)


    


pares,impares =generar_listas()

print(pares)
print(impares)