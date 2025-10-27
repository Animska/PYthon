# Dada la siguiente tupla: datos = ("Juan", 25, "España")
# Desempaquétala en tres variables y muestra un mensaje como:
# Juan tiene 25 años y vive en España.

datos = ("Juan", 25, "España")

nombre=datos[0]
edad=datos[1]
pais=datos[2]

print(f"{nombre} tiene {edad} años y vive en {pais}")