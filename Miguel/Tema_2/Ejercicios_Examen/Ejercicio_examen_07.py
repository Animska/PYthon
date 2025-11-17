# Ejercicio 7
# Disponemos de 2 parámetros de entrada en la función:
# - palabra_objetivo: La palabra que hay que adivinar.
# - letras_introducidas: Lista de letras ya introducidas.
# La función es "dar_pista(palabra_objetivo, letras_introducidas)"
# La función busca la letra que se repite menos veces en "palabra_objetivo" y
# que aún no está en "letras_introducidas" y la retorna. Si hay varias letras que
# se repiten el mismo número mínimo de veces, elegir la primera de ellas.
# Se puede usar la función lista.count('letra') que cuenta las apariciones de 'letra'
# en la lista

def dar_pista(palabra_objetivo, letras_introducidas):
    letras_unicas = {}
    for letra in palabra_objetivo:
        letras_unicas[letra] = letras_unicas.get(letra, 0) + 1

    letras_filtradas = {letra: freq for letra, freq in letras_unicas.items() if letra not in letras_introducidas}

    freq_min = min(letras_filtradas.values())

    for letra in palabra_objetivo:
        if letra in letras_filtradas and letras_filtradas[letra] == freq_min:
            return letra

# Ejemplo de uso
palabra = "programacion"
letras_introd = ['p', 'r', 'o','g']
print(dar_pista(palabra, letras_introd))
