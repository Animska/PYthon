#EJERCICIO 1
def codificar(palabra:str,MAPA_EMOJIS:dict)->str:
    palabra_cod=""
    for letra in palabra:
        if letra.lower() in MAPA_EMOJIS.keys():
            palabra_cod+=MAPA_EMOJIS[letra.lower()]
        else:
            palabra_cod+=letra

    return palabra_cod

def decodificar(mensaje_emoji:str,MAPA_EMOJIS:dict)->str:
    palabra_descod=""
    #CORRECCION: dictionary comprehension es {} no dict()
    MAPA_DESCOD=dict((valor,clave) for (clave,valor) in MAPA_EMOJIS.items())
    for caracter in mensaje_emoji:
        if caracter in MAPA_DESCOD.keys():
            palabra_descod+=MAPA_DESCOD[caracter]
        else:
            palabra_descod+=caracter

    return palabra_descod

MAPA_EMOJIS = {
    'a': '🍎', 'b': '🎈', 'c': '🌎', 'd': '💎', 'e': '🐘', 'f': '🌸', 
    'g': '🦒', 'h': '🏡', 'i': '💡', 'j': '🪡', 'k': '🔑', 'l': '🦁', 
    'm': '🌙', 'n': '⛵', 'ñ': '🟤', 'o': '🟠', 'p': '🐧', 'q': '👑', 
    'r': '🌈', 's': '⭐', 't': '🌲', 'u': '🦄', 'v': '🌋', 'w': '🌊', 
    'x': '❌', 'y': '🟡', 'z': '🦓'
}

palabra_test = "España con ñandú 10"
codificado = codificar(palabra_test,MAPA_EMOJIS)
decodificado = decodificar(codificado,MAPA_EMOJIS)

print(f"Original: {palabra_test}")
print(f"Codificado: {codificado}")
print(f"Decodificado: {decodificado}")