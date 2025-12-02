"""
Ejercicio 06 - Polimorfismo
"""
class Lavadora:
    """
    Docstring para Lavadora
    """
    def diagnostico(self)->str:
        """
        Docstring para diagnostico
        
        :rtype: str
        """
        return "Tambor OK – Bomba OK – Filtros O"

class Horno:
    """
    Docstring para Horno
    """
    def diagnostico(self)->str:
        """
        Docstring para diagnostico
        
        :rtype: str
        """
        return "Resistencias OK – Sensor temperatura OK"

class AireAcondicionado:
    """
    Docstring para AireAcondicionado
    """
    def diagnostico(self)->str:
        """
        Docstring para diagnostico
        
        :rtype: str
        """
        return "Compresor OK – Nivel de gas correcto"

def probar(electrodomestico):
    """
    Docstring para probar
    
    :param Electrodomestico:
    :return: retorna el la funcion de cada clase diferente
    """
    print(electrodomestico.diagnostico())

aparatos = [
Lavadora(),
Horno(),
AireAcondicionado(),
]
for a in aparatos:
    probar(a)
