# Crea una función llamada "premios" para simular un sorteo de lotería de 2 cifras. Se
# harán 20 tiradas. Se debe utilizar el módulo random para generar las tiradas. Cada tirada
# es un número, todas las tiradas se almacenan en un conjunto y se retornan. No puede
# haber 2 números iguales, es decir, si ya ha salido el 54, no puede volver a salir...
# Crea otra función llamada "apuesta" con 5 tiradas aleatorias. Estas serán los números
# que juega el jugador.
# Crea otra función llamada "comprobación" que compara ambos conjuntos para saber
# cuántos números ha acertado. Debes hacer la comprobación mediante operaciones de
# conjuntos. Debes retornar una tupla con la cantidad de números acertados y la cantidad
# de números no acertados, es decir (acertados, no_acertados)

import random

def premios():
    tiradas =set()
    while len(tiradas)<20:
        tiradas.add(random.randint(1,50))    
    return tiradas

def apuesta():
    tiradas_jugador=set()
    while len(tiradas_jugador)<5:
        try:
            tiradas_jugador.add(int(input("introduce un numero entre 1 y 50: ")))
        except ValueError as e:
            print("ERROR!",e)
    return tiradas_jugador

def comprobacion(premios,apuesta):
    acertados=len(premios.intersection(apuesta))
    no_acertados=len(premios)-acertados
    return acertados,no_acertados

premios=premios()
apuesta=apuesta()
acertados,no_acertados=comprobacion(premios,apuesta)

print(f"aciertos:{acertados} fallos:{no_acertados}")