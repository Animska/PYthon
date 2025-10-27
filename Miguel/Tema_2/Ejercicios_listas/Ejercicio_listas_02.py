# Ejercicio 2
# Intercambio de posiciones. Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]
ultima_pos=numeros[-1]
numeros[-1]=numeros[0]
numeros[0]=ultima_pos

print(numeros)