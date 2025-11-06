# Crea una clase Rectangulo con atributos base y altura.
# Usa @property para:
# • Validar que ambos sean positivos.
# • Calcular el área como propiedad de solo lectura (area)
class Rectangulo:
    def __init__(self,base,altura):
        self.base = base # usa el setter
        self.altura = altura # usa el setter
        
    @property
    def base(self):
        #Getter: devuelve el valor de _base.
        return self.__base
        
    @base.setter
    def base(self, valor):
        #Setter: valida antes de asignar el valor.
        if valor<=0:
            raise ValueError("El valor no puede ser negativo.")
        self.__base = valor

    @property
    def altura(self):
        #Getter: devuelve el valor de _altura.
        return self.__altura
        
    @altura.setter
    def altura(self, valor):
        #Setter: valida antes de asignar el valor.
        if valor<=0:
            raise ValueError("El valor no puede ser negativo.")
        self.__altura = valor
            

    @property
    def area(self):
        return self.altura*self.base
        
    

rectangulo=Rectangulo(15,10)
print(rectangulo.area)
