# Diseñar una clase llamada “Vehículo” con los atributos marca, modelo, año y precio.
# Crear dos objetos pertenecientes a esa clase e imprimir en pantalla la marca, el
# modelo y el precio de cada vehículo (mediante __str__).
from clases import Vehiculo_basic

coche1=Vehiculo_basic("Toyota","Supra A90",2019,60000.00)
coche2=Vehiculo_basic("Toyota","GT86",2013,20000.00)

print(coche1)
print(coche2)