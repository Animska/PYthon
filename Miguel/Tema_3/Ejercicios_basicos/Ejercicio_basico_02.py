# En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y añadiremos
# un método llamado “nombre_completo” que retorne en una cadena los atributos marca
# y modelo concatenados y separados por un guión (Seat-Ibiza). Crear dos objetos y
# probar el método
from clases import Vehiculo_basic

    
coche1=Vehiculo_basic("Toyota","Supra A90",2019,60000.00)
coche2=Vehiculo_basic("Toyota","GT86",2013,20000.00)

print(coche1)
print(coche2)

print(coche1.nombre_completo())