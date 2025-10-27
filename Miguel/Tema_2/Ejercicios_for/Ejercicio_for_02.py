# Calcular la media de una lista. Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]. Calcula la media de los números usando un bucle for

numeros = [10, 20, 30, 40, 50]
media=0
for i in numeros:
    media+=i
media/=len(numeros)
print(f"la media es: {media}")