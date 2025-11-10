from clases import Vehiculo

class GestionVehiculos:
    def __init__(self):
        self.lista_vehiculos = []

    def añadir_vehiculo(self, vehiculo):
        if any(v.matricula == vehiculo.matricula for v in self.lista_vehiculos):
            return False
        self.lista_vehiculos.append(vehiculo)
        return True

    def numero_reparaciones(self, matricula):
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo:
            return vehiculo.numero_reparaciones()
        return 0

    def eliminar_vehiculo(self, matricula):
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo:
            self.lista_vehiculos.remove(vehiculo)
            return True
        return False

    def ordenar_por_anio(self):
        self.lista_vehiculos.sort(key=lambda v: v.anio)

    def agregar_reparacion(self, matricula, fecha):
        vehiculo = self.buscar_vehiculo(matricula)
        if vehiculo:
            vehiculo.agregar_reparacion(fecha)
            return True
        return False

    def mostrar_todos(self):
        for vehiculo in self.lista_vehiculos:
            print(vehiculo)

    def buscar_vehiculo(self, matricula):
        for vehiculo in self.lista_vehiculos:
            if vehiculo.matricula == matricula:
                return vehiculo
        return None
    
lista_vehiculos = [
Vehiculo("ABC123", "Toyota", "Corolla", "Rojo", 2019, 20000, 150),
Vehiculo("DEF456", "Nissan", "Sentra", "Azul", 2018, 18000, 140),
Vehiculo("GHI789", "Chevrolet", "Spark", "Blanco", 2017, 160400, 130),
Vehiculo("JKL012", "Mazda", "3", "Negro", 2016, 15000, 120),
Vehiculo("KKL122", "Volkswagen", "Golf", "Blanco", 2020, 230400, 120),
Vehiculo("MMG122", "Nissan", "Micra", "Azul", 2020, 123000, 86),
Vehiculo("ZZE123", "Seat", "Ibiza", "Blanco", 2010, 67000, 120),
]

# Crear instancia de la gestión
gestion = GestionVehiculos()

# Añadir los vehículos a la gestión
for v in lista_vehiculos:
    resultado = gestion.añadir_vehiculo(v)
    print(f"Añadido vehículo matricula {v.matricula}: {resultado}")

# Mostrar todos los vehículos
print("\nLista inicial de vehículos:")
gestion.mostrar_todos()

# Añadir reparaciones a algunos vehículos
gestion.agregar_reparacion("ABC123", "2023-01-15")
gestion.agregar_reparacion("ABC123", "2024-06-03")
gestion.agregar_reparacion("DEF456", "2024-02-28")

# Mostrar número de reparaciones para un vehículo
matricula_buscar = "ABC123"
num_rep = gestion.numero_reparaciones(matricula_buscar)
print(f"\nNúmero de reparaciones de vehículo {matricula_buscar}: {num_rep}")

# Eliminar un vehículo
matricula_eliminar = "GHI789"
resultado = gestion.eliminar_vehiculo(matricula_eliminar)
print(f"\nEliminación vehículo con matrícula {matricula_eliminar}: {resultado}")

# Ordenar vehículos por año
gestion.ordenar_por_anio()
print("\nLista ordenada por año:")
gestion.mostrar_todos()
