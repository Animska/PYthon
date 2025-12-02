"""
Ejercicio 05 - Herencia
"""
class VehiculoElectrico:
    """
    Docstring para VehiculoElectrico
        Atributos:
            -identificador(string)->identificador del vehiculo
            -nivel_bateria(int)->nivel de bateria del vehiculo
    """
    #Type hints
    identificador:str
    nivel_bateria:int

    def __init__(self,identificador:str,nivel_bateria:int):
        self.identificador=identificador
        self.nivel_bateria=nivel_bateria

    @property
    def identificador(self)->str:
        """
        Docstring para getter identificador
        
        :return: identificador
        :rtype: str
        """
        return self.__identificador

    @identificador.setter
    def identificador(self, valor)->None:
    #Setter: valida antes de asignar el valor.
        self.__identificador = valor

    @property
    def nivel_bateria(self)->int:
        """
        Getter para nivel_bateria
        
        :return: nivel_bateria
        :rtype: int
        """
    #Getter: devuelve el valor de _nivel_bateria.
        return self.__nivel_bateria

    @nivel_bateria.setter
    def nivel_bateria(self, valor)->None:
    #Setter: valida antes de asignar el valor.
        if valor < 0 :
            valor=0
        self.__nivel_bateria = valor

    def estado(self)->str:
        """
        Docstring para estado
        
        :return: estado del vehiculo
        :rtype: str
        """
        return f"[{self.identificador}] Bateria: {self.nivel_bateria}%"

class BiciElectrica(VehiculoElectrico):
    """
    Docstring para BiciElectrica
        -Hereda de VehiculoElectrico
        -añade el atributo num_marchas:int
        -sobrescribe el metodo estado()
    """

    def __init__(self,identificador:str,nivel_bateria:int,num_marchas:int):
        super().__init__(identificador,nivel_bateria)
        self.num_marchas=num_marchas

    @property
    def num_marchas(self)->int:
        """
        Docstring para num_marchas
        
        :param self: Descripción
        :return: Descripción
        :rtype: int
        """
    #Getter: devuelve el valor de _num_marchas.
        return self.__num_marchas

    @num_marchas.setter
    def num_marchas(self, valor)->None:
    #Setter: valida antes de asignar el valor.
        if valor <=0:
            raise ValueError("ERROR! La marcha minima debe ser 1")
        self.__num_marchas = valor

    def estado(self)->str:
        return f"{super().estado()} | Tipo: Bicicleta eléctrica | Marchas: {self.num_marchas}"

class PatineteElectrico(VehiculoElectrico):
    """
    Docstring para PatineteElectrico
    -Hereda de VehiculoElectrico
    -Añade el atributo vel_max
    """
    def __init__(self,identificador:str,nivel_bateria:int,vel_max:int):
        super().__init__(identificador,nivel_bateria)
        self.vel_max=vel_max

    @property
    def vel_max(self)->int:
        """
        getter de vel_max
        
        :return: vel_max
        :rtype: int
        """
    #Getter: devuelve el valor de _num_marchas.
        return self.__vel_max

    @vel_max.setter
    def vel_max(self, valor)->None:
    #Setter: valida antes de asignar el valor.
        if valor <=0:
            raise ValueError("ERROR! La velocidad maxima minima debe ser 1")
        self.__vel_max = valor

    def estado(self)->str:
        return f"{super().estado()} | Tipo: Patinete eléctrico | Vel. max:: {self.vel_max}Km/h"


v1 = BiciElectrica("B-101", 85, 6)
v2 = PatineteElectrico("P-202", 60, 25)
flota = [v1, v2]
for v in flota:
    try:
        print(v.estado())
    except ValueError as e:
        print(e)
