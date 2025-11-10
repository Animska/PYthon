from clases import Ciudad

class GestionCiudades:
    def __init__(self):
        # Lista de objetos Ciudad
        self.__ciudades = []

    def añadir_ciudad(self, ciudad):
        # Añade una nueva ciudad si no existe (usa __eq__)
        if ciudad not in self.__ciudades:
            self.__ciudades.append(ciudad)
            return True
        return False

    def mostrar_por_continente(self, continente):
        # Retorna las ciudades que pertenecen al continente dado
        return [c for c in self.__ciudades if c.continente == continente]

    def mostrar_mayor_poblacion(self, minimo):
        # Retorna las ciudades con población mayor que el número dado
        return [c for c in self.__ciudades if c.poblacion > minimo]

    def numero_ciudades_pais(self, pais):
        # Retorna el número de ciudades de un país dado
        return sum(1 for c in self.__ciudades if c.pais == pais)

    def ciudades_con_cadena(self, cadena):
        # Retorna el número de ciudades que contienen una cadena en su nombre
        return sum(1 for c in self.__ciudades if cadena.lower() in c.nombre.lower())

    def media_poblacion_pais(self, pais):
        # Retorna la media de la población de las ciudades de un país
        poblaciones = [c.poblacion for c in self.__ciudades if c.pais == pais]
        if not poblaciones:
            return 0
        return sum(poblaciones) / len(poblaciones)

    def lista_por_pais(self, pais):
        # Retorna una lista con las ciudades de un país
        return [c for c in self.__ciudades if c.pais == pais]

    def lista_por_continente(self, continente):
        # Retorna una lista con las ciudades de un continente
        return [c for c in self.__ciudades if c.continente == continente]

    def suma_total_habitantes(self):
        # Retorna la suma de los habitantes de todas las ciudades
        return sum(c.poblacion for c in self.__ciudades)

list_cities = [
Ciudad("Bogotá", 8000000, "Colombia", "América"),
Ciudad("Lima", 10000000, "Peru", "America"),
Ciudad("Paris", 5000000, "Francia", "Europa"),
Ciudad("Berlin", 4000000, "Alemania", "Europa"),
Ciudad("Tokio", 9000000, "Japón", "Asia"),
Ciudad("Sydney", 3000000, "Australia", "Oceanía"),
Ciudad("Johannesburgo", 5000000, "Sudáfrica", "África"),
Ciudad("Moscú", 10000000, "Rusia", "Europa"),
Ciudad("Nueva York", 8000000, "Estados Unidos", "América"),
Ciudad("Sao Paulo", 12000000, "Brasil", "América"),
Ciudad("Buenos Aires", 15000000, "Argentina", "América"),
Ciudad("Londres", 9000000, "Reino Unido", "Europa"),
Ciudad("Roma", 4000000, "Italia", "Europa"),
Ciudad("Pekín", 20000000, "China", "Asia"),
Ciudad("Delhi", 15000000, "India", "Asia"),
Ciudad("El Cairo", 7000000, "Egipto", "África"),
Ciudad("Ciudad del Cabo", 4000000, "Sudáfrica", "África"),
Ciudad("Melbourne", 5000000, "Australia", "Oceanía"),
Ciudad("Auckland", 2000000, "Nueva Zelanda", "Oceanía"),
Ciudad("Brisbane", 3000000, "Australia", "Oceanía"),
Ciudad("Madrid", 6000000, "España", "Europa"),
Ciudad("Lisboa", 3000000, "Portugal", "Europa"),
]

# Creamos la gestión
gestion = GestionCiudades()

# Añadimos todas las ciudades
for ciudad in list_cities:
    gestion.añadir_ciudad(ciudad)

# Mostrar ciudades de Europa
print("Ciudades en Europa:")
for c in gestion.mostrar_por_continente("Europa"):
    print(c)

# Mostrar ciudades con población mayor que 10 millones
print("\nCiudades con población mayor a 10,000,000:")
for c in gestion.mostrar_mayor_poblacion(10000000):
    print(c)

# Número de ciudades en Australia
print("\nNúmero de ciudades en Australia:")
print(gestion.numero_ciudades_pais("Australia"))

# Ciudades cuyo nombre contiene 'York'
print("\nNúmero de ciudades que contienen 'York' en su nombre:")
print(gestion.ciudades_con_cadena("York"))

# Media de población de ciudades en Sudáfrica
print("\nMedia de población en Sudáfrica:")
print(gestion.media_poblacion_pais("Sudáfrica"))

# Lista de ciudades en Perú
print("\nCiudades en Peru:")
for c in gestion.lista_por_pais("Peru"):
    print(c)

# Lista de ciudades en América
print("\nCiudades en América:")
for c in gestion.lista_por_continente("América"):
    print(c)

# Suma total de habitantes
print("\nSuma total de habitantes en todas las ciudades:")
print(gestion.suma_total_habitantes())

