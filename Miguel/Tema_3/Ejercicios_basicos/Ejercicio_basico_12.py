from clases import Partido

class GestionPartidos:
    partidos = []

    @classmethod
    def agregar_partido(cls, partido):
        cls.partidos.append(partido)

    @classmethod
    def filtrar_por_local(cls, equipo_local):
        filtrados = [p for p in cls.partidos if p.equipo_local == equipo_local]
        for p in filtrados:
            print(p)

    @classmethod
    def ganados_del_equipo(cls, equipo):
        return sum(p.gano_equipo(equipo) for p in cls.partidos)

    @classmethod
    def mostrar_partidos_por_anio(cls, anio):
        #formato "dd:mm:aaaa"
        filtrados = []
        for p in cls.partidos:
            try:
                anio_p = int(p.fecha.split(":")[2])
                if anio_p == anio:
                    filtrados.append(p)
            except ValueError:
                print(f"Formato de fecha inválido en: {p.fecha}")
        for p in filtrados:
            print(p)

    @classmethod
    def mostrar_por_fecha(cls, fecha):
        filtrados = [p for p in cls.partidos if p.fecha == fecha]
        for p in filtrados:
            print(p)

    @classmethod
    def contar_partidos(cls):
        return len(cls.partidos)


p1 = Partido("Raimon", "Royal Academy", 2, 1, "Futbol Frontier", "17:7:2013")
p2 = Partido("Raimon", "Genesis", 1, 3, "LaLiga", "12:5:2013")
p3 = Partido("Inazuma Japon", "Little Giants", 4, 0, "Futbol Frontier Internacional", "21:7:2018")

GestionPartidos.agregar_partido(p1)
GestionPartidos.agregar_partido(p2)
GestionPartidos.agregar_partido(p3)

print("Partidos con Raimon como local:")
GestionPartidos.filtrar_por_local("Barcelona")

print("\nPartidos ganados por el Raimon:", GestionPartidos.ganados_del_equipo("Raimon"))

print("\nPartidos del año 2013:")
GestionPartidos.mostrar_partidos_por_anio(2013)

print("\nPartidos del 17-07-2013:")
GestionPartidos.mostrar_por_fecha("17:7:2013")

print("\nNúmero total de partidos:", GestionPartidos.contar_partidos())
