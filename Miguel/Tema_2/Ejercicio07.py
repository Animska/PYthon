# Crea un programa que pida números al usuario y calcule su suma. 
# El programa termina cuando el usuario introduce un número vacío.
#  Usa el operador morsa

suma=0
while (numero := input("introduce un numero para su suma: ")):
    suma+=int(numero)
print(suma)