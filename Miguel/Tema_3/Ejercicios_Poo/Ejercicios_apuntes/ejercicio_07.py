"""
Ejercicio 07 - Composicion
"""
import random


class SensorDeHumedad:
    """
    Docstring para SensorDeHumedad

    Atributos:
        -humedad(int)->humedad del ambiente
    """
    @staticmethod
    def obtener_humedad()->int:
        """
        Docstring para obtener_humedad
        
        :return: devuelve numero aleatorio entre 0 y 100
        :rtype: int
        """
        return random.randint(0,100)

class Bomba:
    """
    Docstring para Bomba
    Atributos:
        -bomba(bool)la bomba esta encendida o apagada
    """
    def __init__(self):
        self.bomba=False

    def encender(self)->None:
        """
        Docstring para encender
        
        Enciende la bomba
        """
        self.bomba=True
        print("Bomba ENCENDIDA")

    def apagar(self)->None:
        """
        Docstring para apagar
        
        Apaga la bomba
        """
        self.bomba=False
        print("Bomba APAGADA")

    def estado(self)->str:
        """
        Docstring para estado
        
        :return: retorna una cadena segun el estado de la bomba
        :rtype: str
        """
        return "ENCENDIDA" if self.bomba else ("APAGADA")

class ControladorRiego:
    """
    Docstring para ControladorRiego
    Atributos:
        sensor_de_humedad(Objeto SensorDeHumedad)
        bomba(Objeto Bomba)
    """
    def __init__(self):
        self.sensor_de_humedad=SensorDeHumedad()
        self.bomba=Bomba()

    def ciclo_control(self)->None:
        """
        Docstring para ciclo_control
        
        Si la humedad es menor al 40% enciende la bomba
        si es mayor del 40% la apaga e imprime su estado
        """
        humedad=self.sensor_de_humedad.obtener_humedad()
        print(f"Humedad actual del suelo {humedad}%")
        if humedad < 40 :
            self.bomba.encender()
        else:
            self.bomba.apagar()

        print(f"Estado de bomba: {self.bomba.estado()}")
        print()

controlador = ControladorRiego()
# Simulamos dos ciclos de control
controlador.ciclo_control()
controlador.ciclo_control()
