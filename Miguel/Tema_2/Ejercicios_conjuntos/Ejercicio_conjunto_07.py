# Ejercicio 7 – Poker
# Vamos a representar una mano de poker utilizando una tupla de cinco elementos, donde
# cada elemento es una tupla (valor, palo).
# Por ejemplo: (('9', 'picas'), ('3', 'corazones'), ('8', 'diamantes'), ('9', 'tréboles'), ('5',
# 'tréboles'))
# La función proporcionada genera una mano aleatoria.
# Debes implementar varias funciones para evaluar si tiene poker, escalera de color,
# escalera o color. Estas funciones retornan true/false si cumple los criterios. Es decir, si
# la mano recibida como parámetro es poker, la función "es_poker" retorna True.
# Una vez tengas las funciones por separado, crea una nueva función que reciba la mano y
# devuelva la combinación de mejor puntuación en forma de string, es decir, retorna uno
# de estos valores:
import random

COLORES = set({"Corazones","Picas","Diamantes","Treboles"})
NUMEROS = set({'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'})
orden_valores = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def generar_mano():
    baraja = [(numero, color) for color in COLORES for numero in NUMEROS]
    mano = tuple(random.sample(baraja, 5))
    return mano

def es_pareja(mano):
    valores = [carta[0] for carta in mano]
    return any(valores.count(valor) == 2 for valor in set(valores))

def es_dobles_parejas(mano):
    valores = [carta[0] for carta in mano]
    pares = [valor for valor in set(valores) if valores.count(valor) == 2]
    return len(pares) == 2

def es_trio(mano):
    valores = [carta[0] for carta in mano]
    return any(valores.count(valor) == 3 for valor in set(valores))

def es_escalera(mano):
    
    valores = sorted([orden_valores[carta[0]] for carta in mano])
    return valores == list(range(valores[0], valores[0]+5)) or valores == [2, 3, 4, 5, 14]  # A puede ser bajo

def es_color(mano):
    palos = [carta[1] for carta in mano]
    return all(palo == palos[0] for palo in palos)

def es_full_house(mano):
    valores = [carta[0] for carta in mano]
    tiene_trio = any(valores.count(valor) == 3 for valor in set(valores))
    pares = [valor for valor in set(valores) if valores.count(valor) == 2]
    return tiene_trio and len(pares) == 1

def es_poker(mano):
    valores = [carta[0] for carta in mano]
    return any(valores.count(valor) == 4 for valor in set(valores))

def es_escalera_color(mano):
    return es_escalera(mano) and es_color(mano)

def es_escalera_real(mano):
    valores = sorted([orden_valores.get(carta[0], 0) for carta in mano])
    return valores == [10, 11, 12, 13, 14] and es_color(mano)

#si quieres que solo cuente el que da mas puntos conviertelo a lista o tupla y haz un break
#lo he hecho como set para usarlo en este ejercicio
JUGADAS = set([
    ("Escalera Real", es_escalera_real, 1000),
    ("Escalera de color", es_escalera_color, 800),
    ("Poker", es_poker, 500),
    ("Full House", es_full_house, 300),
    ("Color", es_color, 100),
    ("Escalera", es_escalera, 75),
    ("Trío", es_trio, 50),
    ("Dobles Parejas", es_dobles_parejas, 30),
    ("Pareja", es_pareja, 10),
])

def jugada(mano, puntuacion):
    tiene_puntaje = False
    for nombre, funcion, puntaje in JUGADAS:
        if funcion(mano):
            print(f"{nombre},+{puntaje}")
            puntuacion += puntaje
            tiene_puntaje = True
    if not tiene_puntaje:
        print("Nada, siga balatreando +1")
        puntuacion += 1
    return puntuacion

seguir=""
puntuacion_maxima=0
while not seguir:
    #la variable seguir estara vacia si pulsamos solo enter en la linea 105
    puntuacion=0
    try:
        for i in range(5):
            input("Pulsa enter para coger cartas")
            #sensacion falsa de control sobre el juego
            mano=generar_mano()
            print(mano)
            puntuacion=jugada(mano,puntuacion)
            if puntuacion>puntuacion_maxima:
                puntuacion_maxima=puntuacion
            print(f"puntuacion= {puntuacion}")
        print("----------------------------------------------------------")
        print(f"Puntuacion total: {puntuacion}")
        print(f"Puntuacion maxima: {puntuacion_maxima}")
        seguir=input("¿Quieres seguir jugando?")
        #para parar de jugar tienes que escribir lo que sea
        print("----------------------------------------------------------")
    except ValueError as e:
        print("ERROR! Las rondas debe ser un numero")
        print(e)