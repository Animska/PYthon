# Contar palabras que empiezan con una letra. Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra. Cuenta cuántas palabras en la lista empiezan
# con esa letra (sin diferenciar mayúsculas/minúsculas).

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra=input("introduce una letra: ").lower()
palabras_inicio=[palabra for palabra in palabras if palabra[0]==letra]
print(f"palabras:{palabras_inicio}  numero de palabras: {len(palabras_inicio)}")