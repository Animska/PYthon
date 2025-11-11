from clases import Empleado

empleado1 = Empleado(1, "Ana", "Contabilidad", 2500)
empleado2 = Empleado(2, "Luis", "Ventas", 2500)
empleado3 = Empleado(3, "Marta", "IT", 3000)


print(empleado1)
print(empleado2)
print(empleado3)


print("empleado1 == empleado2:", empleado1 == empleado2)  # True
print("empleado2 == empleado3:", empleado2 == empleado3)  # False
