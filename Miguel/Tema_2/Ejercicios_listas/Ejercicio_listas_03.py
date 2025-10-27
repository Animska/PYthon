# Ejercicio 3
# El sándwich de listas. Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan
# de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich=[]
sandwich.extend(pan)
sandwich.extend(ingredientes)
sandwich.extend(pan_abajo)
print(sandwich)