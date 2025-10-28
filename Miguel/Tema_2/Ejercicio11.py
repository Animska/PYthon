# Ejercicio 11
# Dado un texto, cuenta cuántas veces aparece cada letra (ignorando espacios y sin
# distinguir mayúsculas y minúsculas).

letras={}
texto="Toyota          audi".replace(" ","").lower()

for i in texto:
    if i not in letras:
        letras[i]=texto.count(i)

print(letras)