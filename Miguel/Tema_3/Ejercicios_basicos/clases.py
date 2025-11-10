class Producto:
    def __init__(self,nombre,categoria,precio,cantidad):
        self.nombre = nombre # usa el setter
        self.categoria = categoria # usa el setter
        self.precio = precio # usa el setter
        self.cantidad = cantidad # usa el setter
        
    @property
    def nombre(self):
        #Getter: devuelve el valor de _nombre.
        return self.__nombre
        
    @nombre.setter
    def nombre(self, valor):
        #Setter: valida antes de asignar el valor.
        self.__nombre = valor
        
    @property
    def categoria(self):
        #Getter: devuelve el valor de _categoria.
        return self.__categoria
        
    @categoria.setter
    def categoria(self, valor):
        #Setter: valida antes de asignar el valor.
        self.__categoria = valor
        
    @property
    def precio(self):
        #Getter: devuelve el valor de _precio.
        return self.__precio
        
    @precio.setter
    def precio(self, valor):
        #Setter: valida antes de asignar el valor.
        if valor < 0.0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor
        
    @property
    def cantidad(self):
        #Getter: devuelve el valor de _cantidad.
        return self.__cantidad
        
    @cantidad.setter
    def cantidad(self, valor):
        #Setter: valida antes de asignar el valor.
        if valor < 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.__cantidad = valor

    def __str__(self):
        return f"""
        Nombre del producto: {self.nombre}.
        Categoria del producto: {self.categoria}
        Precio por unidad: {self.precio:.2f}€.
        Unidades en Stock: {self.cantidad} unidades.
        """
    
    @staticmethod
    def mas_caro(producto1,producto2):
        if producto1.precio > producto2.precio:
            print(str(producto1))
        elif producto1.precio == producto2.precio:
            print("Ambos productos cuestan lo mismo")
        else:
            print(str(producto2))

    def anadir_cantidad(self,valor):
        if valor < 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.__cantidad += valor
        print("Cantidad añadida satisfactoriamente")

class Vehiculo:
    def __init__(self, matricula, marca, modelo, color, anio, kilometros, potencia):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.kilometros = kilometros
        self.potencia = potencia
        self.__fechas_reparacion = []

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        self.__color = valor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, valor):
        self.__anio = valor

    @property
    def kilometros(self):
        return self.__kilometros

    @kilometros.setter
    def kilometros(self, valor):
        self.__kilometros = valor

    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, valor):
        self.__potencia = valor

    def agregar_reparacion(self, fecha):
        self.__fechas_reparacion.append(fecha)

    def numero_reparaciones(self):
        return len(self.__fechas_reparacion)

    def __eq__(self, other):
        if isinstance(other, Vehiculo):
            return self.matricula == other.matricula
        return False

    def __str__(self):
        return (f"Vehículo {self.matricula}: {self.marca} {self.modelo} - {self.color} - "
                f"Año: {self.anio} - Km: {self.kilometros} - Potencia: {self.potencia}CV - "
                f"Reparaciones: {len(self.__fechas_reparacion)}")
    
class Partido:
    def __init__(self, equipo_local, equipo_visitante, goles_local, goles_visitante, campeonato, fecha):
        self.equipo_local = equipo_local  # usa el setter
        self.equipo_visitante = equipo_visitante  # usa el setter
        self.goles_local = goles_local  # usa el setter
        self.goles_visitante = goles_visitante  # usa el setter
        self.campeonato = campeonato  # usa el setter
        self.fecha = fecha  # usa el setter

    @property
    def equipo_local(self):
        # Getter: devuelve el valor de _equipo_local
        return self.__equipo_local

    @equipo_local.setter
    def equipo_local(self, valor):
        # Setter: valida antes de asignar el valor
        self.__equipo_local = valor

    @property
    def equipo_visitante(self):
        # Getter: devuelve el valor de _equipo_visitante
        return self.__equipo_visitante

    @equipo_visitante.setter
    def equipo_visitante(self, valor):
        # Setter: valida antes de asignar el valor
        self.__equipo_visitante = valor

    @property
    def goles_local(self):
        # Getter: devuelve el valor de _goles_local
        return self.__goles_local

    @goles_local.setter
    def goles_local(self, valor):
        # Setter: valida antes de asignar el valor
        self.__goles_local = valor

    @property
    def goles_visitante(self):
        # Getter: devuelve el valor de _goles_visitante
        return self.__goles_visitante

    @goles_visitante.setter
    def goles_visitante(self, valor):
        # Setter: valida antes de asignar el valor
        self.__goles_visitante = valor

    @property
    def campeonato(self):
        # Getter: devuelve el valor de _campeonato
        return self.__campeonato

    @campeonato.setter
    def campeonato(self, valor):
        # Setter: valida antes de asignar el valor
        self.__campeonato = valor

    @property
    def fecha(self):
        # Getter: devuelve el valor de _fecha
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        # Setter: valida antes de asignar el valor
        self.__fecha = valor

    def __str__(self):
        return (f"{self.fecha} - {self.campeonato}: "
                f"{self.equipo_local} {self.goles_local} - {self.goles_visitante} {self.equipo_visitante}")
    
    def gano_equipo(self, equipo):
        if self.goles_local > self.goles_visitante and equipo == self.equipo_local:
            return True
        elif self.goles_visitante > self.goles_local and equipo == self.equipo_visitante:
            return True
        return False

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre  # usa el setter
        self.telefono = telefono  # usa el setter
        self.correo = correo  # usa el setter

    @property
    def nombre(self):
        # Getter: devuelve el valor de _nombre
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Setter: valida antes de asignar el valor
        self.__nombre = valor

    @property
    def telefono(self):
        # Getter: devuelve el valor de _telefono
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        # Setter: valida antes de asignar el valor
        self.__telefono = valor

    @property
    def correo(self):
        # Getter: devuelve el valor de _correo
        return self.__correo

    @correo.setter
    def correo(self, valor):
        # Setter: valida antes de asignar el valor
        self.__correo = valor

    def __str__(self):
        # Representación legible del contacto
        return f"{self.nombre} - {self.telefono} - {self.correo}"

    def __repr__(self):
        # Representación técnica del contacto
        return f"Contacto({self.nombre!r}, {self.telefono!r}, {self.correo!r})"

    def __eq__(self, other):
        # Compara si dos contactos son iguales
        if isinstance(other, Contacto):
            return (self.nombre == other.nombre and
                    self.telefono == other.telefono and
                    self.correo == other.correo)
        return False
    
class Ciudad:
    def __init__(self, nombre, poblacion, pais, continente):
        self.nombre = nombre  # usa el setter
        self.poblacion = poblacion  # usa el setter
        self.pais = pais  # usa el setter
        self.continente = continente  # usa el setter

    @property
    def nombre(self):
        # Getter: devuelve el valor de _nombre
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Setter: valida antes de asignar el valor
        self.__nombre = valor

    @property
    def poblacion(self):
        # Getter: devuelve el valor de _poblacion
        return self.__poblacion

    @poblacion.setter
    def poblacion(self, valor):
        # Setter: valida antes de asignar el valor
        self.__poblacion = valor

    @property
    def pais(self):
        # Getter: devuelve el valor de _pais
        return self.__pais

    @pais.setter
    def pais(self, valor):
        # Setter: valida antes de asignar el valor
        self.__pais = valor

    @property
    def continente(self):
        # Getter: devuelve el valor de _continente
        return self.__continente

    @continente.setter
    def continente(self, valor):
        # Setter: valida antes de asignar el valor
        self.__continente = valor

    def __str__(self):
        # Representación legible de la ciudad
        return f"{self.nombre} - {self.poblacion} - {self.pais} - {self.continente}"

    def __repr__(self):
        # Representación técnica de la ciudad
        return f"Ciudad({self.nombre!r}, {self.poblacion!r}, {self.pais!r}, {self.continente!r})"

    def __eq__(self, other):
        # Dos ciudades son iguales si coinciden nombre y continente
        if isinstance(other, Ciudad):
            return self.nombre == other.nombre and self.continente == other.continente
        return False

class Movie:
    def __init__(self, titulo, año, director, reparto, genero, minutos, productora):
        self.titulo = titulo  # usa el setter
        self.año = año  # usa el setter
        self.director = director  # usa el setter
        self.reparto = reparto  # usa el setter
        self.genero = genero  # usa el setter
        self.minutos = minutos  # usa el setter
        self.productora = productora  # usa el setter

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, valor):
        self.__año = valor

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, valor):
        self.__director = valor

    @property
    def reparto(self):
        return self.__reparto

    @reparto.setter
    def reparto(self, valor):
        self.__reparto = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        self.__genero = valor

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, valor):
        self.__minutos = valor

    @property
    def productora(self):
        return self.__productora

    @productora.setter
    def productora(self, valor):
        self.__productora = valor

    def __str__(self):
        return (f"{self.titulo} ({self.año}) - Director: {self.director}, Género: {self.genero}, "
                f"Duración: {self.minutos} minutos, Productora: {self.productora}")

    def __repr__(self):
        return (f"Movie({self.titulo!r}, {self.año!r}, {self.director!r}, "
                f"{self.reparto!r}, {self.genero!r}, {self.minutos!r}, {self.productora!r})")

    def __eq__(self, other):
        if isinstance(other, Movie):
            return (self.titulo == other.titulo and self.año == other.año and 
                    self.director == other.director)
        return False
    
    def __lt__(self, otra):
        return self.minutos < otra.minutos
