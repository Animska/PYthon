# Realiza una función que reciba un número entero positivo N y muestre en pantalla un
# patrón de asteriscos con N filas

def asteriscos(numero):
    for i in range(numero):
        print("*" * i)

asteriscos(17)