"""
Crea un programa que:
1. Pida al usuario su nombre y apellido.
2. Muestre su nombre completo con la primera letra en mayúscula.
3. Indique cuántos caracteres tiene su nombre completo.
"""

nombre, apellido1, apellido2 = input("Introduzca su nombre completo\n").split()

print(f"Hola {(nombre+" "+apellido1+" "+apellido2).title()} su nombre contiene {len(nombre+apellido1+apellido2)} caracteres")