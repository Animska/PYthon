class Rectangulo:
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
        

    def area(self):
        """Calcula el area del Rectangulo"""
        return self.largo*self.ancho

    @classmethod
    def cuadrado(cls,lado):
        return(cls(lado,lado))
    
    @staticmethod
    def es_valido(base,altura):
        return True if base>0 and altura>0 else False

rect=Rectangulo(15,10)
cuadrao=Rectangulo.cuadrado(7)
print(rect.area())
print(cuadrao.area())
print(Rectangulo.es_valido(rect.largo,rect.ancho))