# Buscar el máximo de una lista. Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros = [15, 5, 25, 10, 20]
num_maximo=numeros[0]
for i in numeros:
    if i>num_maximo:
        num_maximo=i
print(f"el numero maximo es: {num_maximo}")