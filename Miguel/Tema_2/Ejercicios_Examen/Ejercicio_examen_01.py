# Ejercicio 1
# Crea una función que pida al usuario:
# 1º: Divisor: Un entero que servirá para comprobar si un número es múltiplo de el o no.
# 2º: Una vez establecido el divisor, se le pedirá al usuario que introduzca números
# enteros.
# El programa debe calcular si el número introducido es múltiplo o no de "divisor". El
# programa acaba cuando se introduce el 0.
# 3º: Al finalizar, se muestran cuantos números son múltiplos de divisor y cuantos no lo
# son. El 0 no debe tenerse en cuenta como múltiplo ni como no múltiplo.
# No es necesario verificar y asegurar que se introducen realmente enteros.

def es_multiplo():
    divisor=int(input("Introduce un divisor (entero):"))
    lista_nums=[]
    while (num := int(input('Introduce un número entero (0 para terminar): '))) != 0:
        lista_nums.append(num)
    pares=len([num for num in lista_nums if num % divisor == 0])
    print(f"Números múltiplos de {divisor}: {pares}")
    print(f"Números no múltiplos de {divisor}: {len(lista_nums) - pares}")


es_multiplo()