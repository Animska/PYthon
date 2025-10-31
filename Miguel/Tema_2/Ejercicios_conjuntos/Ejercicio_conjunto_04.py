# Crea una función llamada contar_palabras que reciba un texto y cuente la frecuencia de
# cada palabra en el texto. Debes eliminar primero los signos de puntuación.
# La función Retorna un diccionario que almacena las palabras como claves y su
# frecuencia como valores.
# Una vez obtienes el resultado, muestra la frecuencia de cada palabra recorriendo el
# diccionario con un for.

def contar_palabras(texto):
        signos=set(".,;:?¡!()[]{}«»\"'-—…")
        string_limpio ="".join(char for char in texto if char not in signos).lower()
        array_string=string_limpio.split(" ")
        recuento={}

        for palabra in array_string:
                recuento[palabra] = recuento.get(palabra, 0) + 1

        for palabra, cuenta in recuento.items():
                print(f"{palabra.title()}: {cuenta}")


contar_palabras("¡El Mitsubishi EVO VI tiene un turbo muy gordo, el Mitsubishi EVO VI es muy buen coche, el Mitsubishi EVO VI es muy rapido!")