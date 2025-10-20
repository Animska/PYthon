"""
Ejercicio 3. Haz un programa que pida el nombre y la edad del usuario, y muestre
cuántos años tendrá dentro de 10 años. Usa input() y f-strings.
"""

nombre,edad=input("Introduce tu nombre y edad separados por un spacio:\n).split()")

print(f"Hola {nombre}, dentro de 10 años tendrás {int(edad)+10} años.")