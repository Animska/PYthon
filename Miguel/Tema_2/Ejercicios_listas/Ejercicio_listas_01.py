# Ejercicio 1
# El mensaje secreto. Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje
# "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
lista_mensaje=mensaje[7:]
mensaje_descifrado="".join(lista_mensaje)
print(mensaje_descifrado)