class Empleado:
    def __init__(self,nombre,identificador,departamento,salario):
        self.nombre = nombre # usa el setter
        self.identificador = identificador # usa el setter
        self.departamento = departamento # usa el setter
        self.salario = salario # usa el setter
        
    @property
    def nombre(self):
    #Getter: devuelve el valor de _nombre.
        return self.__nombre
        
    @nombre.setter
    def nombre(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__nombre = valor
        
    @property
    def identificador(self):
    #Getter: devuelve el valor de _identificador.
        return self.__identificador
        
    @identificador.setter
    def identificador(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__identificador = valor
        
    @property
    def departamento(self):
    #Getter: devuelve el valor de _departamento.
        return self.__departamento
        
    @departamento.setter
    def departamento(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__departamento = valor
        
    @property
    def salario(self):
    #Getter: devuelve el valor de _salario.
        return self.__salario
        
    @salario.setter
    def salario(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__salario = valor