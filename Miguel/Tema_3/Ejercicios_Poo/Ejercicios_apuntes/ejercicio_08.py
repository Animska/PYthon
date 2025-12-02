"""
Ejercicio 08 - Clases abstractas
"""
from abc import ABC, abstractmethod

class  MetodoPago(ABC):
    """
    Clase abstracta para Metodos de Pago
    """
    @abstractmethod
    def procesar_pago(self,cantidad:float)->bool:
        """
        Procesa el pago, la cantidad es el dinero
        :return: devuelve si el pago se ha podido procesar
        :rtype: bool
        """

    @abstractmethod
    def obtener_nombre(self)->str:
        """
        Docstring para obtener_nombre
        
        :return: nombre del metodo usado
        :rtype: str
        """

class TarjetaDeCredito(MetodoPago):
    """
    Docstring para TarjetaDeCredito
    atributos titular(string) y numero(int)
    """
    def __init__(self,titular:str,numero:int):
        self.titular=titular
        self.numero=numero

    def procesar_pago(self, cantidad:float)->bool:
        print(f"Procesando pago de {cantidad:.2f}€ con tarjeta de {self.titular}")
        return True

    def obtener_nombre(self)->str:
        return "Tarjeta de Credito"

class Bizum(MetodoPago):
    """
    Docstring para Bizum
    atributos: telefono(int)
    """
    def __init__(self, telefono: int):
        self.telefono = telefono

    def procesar_pago(self, cantidad: float) -> bool:
        print(f"Procesando Bizum de {cantidad:.2f}€ al TLF {self.telefono}")
        return True

    def obtener_nombre(self) -> str:
        return "Bizum"


class TransferenciaBancaria(MetodoPago):
    """
    Docstring para TransferenciaBancaria
    Atributos: iban(string)
    """
    def __init__(self, iban: str):
        self.iban = iban

    def procesar_pago(self, cantidad: float) -> bool:
        print(f"Ordenando transferencia de {cantidad:.2f}€ al IBAN {self.iban}")
        return True

    def obtener_nombre(self) -> str:
        return "Transferencia bancaria"

def realizar_cobro(metodo: MetodoPago, cantidad:float):
    """
    Docstring para realizar_cobro
    
    :param metodo(objeto): tipo de metodo de pago 
    :type metodo: MetodoPago
    :param cantidad: cantidad de dinero para el cobro
    :type cantidad: float
    """
    print(f"Intentando cobrar con {metodo.obtener_nombre()}")
    if metodo.procesar_pago(cantidad):
        print("PAGO ACEPTADO")
    else:
        print("PAGO DENEGADO")

    print()

metodos: list[MetodoPago] = [
    TarjetaDeCredito("Ana Pérez", "1111 2222 3333 4444"),
    Bizum("600123123"),
    TransferenciaBancaria("ES76 2100 1234 5601 2345 6789"),
]

for m in metodos:
    realizar_cobro(m, 49.99)
