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

    def __eq__(self, otro):
        if isinstance(otro, Empleado):
            return self.__salario == otro.__salario
        return False
    def __str__(self):
        return (f"ID: {self.identificador}, Nombre: {self.nombre}, "
                f"Departamento: {self.departamento}, Salario: {self.__salario}")


empleado1 = Empleado(1, "Ana", "Contabilidad", 2500)
empleado2 = Empleado(2, "Luis", "Ventas", 2500)
empleado3 = Empleado(3, "Marta", "IT", 3000)


print(empleado1)
print(empleado2)
print(empleado3)


print("empleado1 == empleado2:", empleado1 == empleado2)  # True
print("empleado2 == empleado3:", empleado2 == empleado3)  # False
