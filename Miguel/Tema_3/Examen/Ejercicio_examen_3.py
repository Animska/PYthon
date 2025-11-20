class Votante:
    VOTOS_TOTALES=dict()
    VOTANTES_REGISTRADOS=list()

    def __init__(self,nombre, apellidos, dni,edad):
        if Votante.validar_dni(dni) and Votante.validad_edad(edad):
            self.__nombre=nombre
            self.__apellidos=apellidos
            self.__dni=dni
            self.__edad=edad

    @property
    def nombre(self):
    #Getter: devuelve el valor de _nombre.
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__nombre = valor

    @property
    def apellidos(self):
    #Getter: devuelve el valor de _apellidos.
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__apellidos = valor

    @property
    def dni(self):
    #Getter: devuelve el valor de _dni.
        return self.__dni
    
    @dni.setter
    def dni(self, valor):
    #Setter: valida antes de asignar el valor.
        if Votante.validar_dni(valor):
            self.__dni = valor

    @property
    def edad(self):
    #Getter: devuelve el valor de _edad.
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
    #Setter: valida antes de asignar el valor.
        self.__edad = valor

    @staticmethod
    def validad_edad(edad:int)->bool:
        if edad<18:
            raise ValueError("ERROR! LA EDAD DEBE SER MAYOR DE 18")
        return True
    
    @staticmethod
    def calcular_letra_dni(numero_dni:str)->bool:
        LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"
        numero=int(numero_dni[0:-1])

        letra = LETRAS_DNI[numero%23]
        return letra
    
    @staticmethod
    def validar_dni(dni)->bool:
        letra=dni[-1]
        numero=dni[0:-1]

        if len(dni) != 9:
            raise  ValueError("ERROR!: El tamaño del DNI no puede superar los 9 caracteres")
            
        if len(numero) != 8:
            raise  ValueError("ERROR!: La parte numerica siempre debe tener 8 caracteres")
        
        if not numero.isdigit():
            raise  ValueError("ERROR!: Los ocho primeros caracteres deben ser un número")
        
        if not isinstance(letra,str):
            raise  ValueError("ERROR!: El ultimo caracter debe ser una letra")
        
        if letra != Votante.calcular_letra_dni(dni):
            raise  ValueError("ERROR!: La letra del DNI no es correcta")
        
        return True
    
    def votar(self,partido:str):
        if self.dni in Votante.VOTANTES_REGISTRADOS:
            raise ValueError("ERROR! Esta persona ya ha votado")
        
        Votante.VOTOS_TOTALES[partido.lower()] = self.VOTOS_TOTALES.get(partido.lower(), 0) + 1
        Votante.VOTANTES_REGISTRADOS.append(self.dni)
        print("Voto Registrado Correctamente.")

class Escrutinio:
    @staticmethod
    def mostrar_resultados(partidos_votos: dict):
        votos_emitidos = sum(votos for partido,votos in partidos_votos.items())
        print("-"*5+"ESCRUTINIO"+"-"*5)
        print(f"Total de votos:{votos_emitidos}")
        for partido,votos in partidos_votos.items():
            print(f"{partido.title()} ha recibido {votos} votos: {votos/votos_emitidos*100:.2f}%")

print("### PRUEBA EJERCICIO 3 ###")

# # Caso 1: Votante Válido
# try:
#     votante_ok = Votante("Elena", "Gómez", "46889241S", 35) # DNI VÁLIDO
#     print(f"Creado OK: {votante_ok.dni}")
# except ValueError as e:
#     print(f"Error inesperado: {e}")

# # Caso 2: Error de Letra (DNI con letra incorrecta)
# try:
#     votante_malo_letra = Votante("Félix", "López", "46889241X", 40) 
# except ValueError as e:
#     print(f"\nExcepción esperada (Letra incorrecta): {e}")

# # Caso 3: Error de Longitud (DNI de 10 caracteres)
# try:
#     votante_malo_long = Votante("Sara", "Mata", "123456789A", 25)
# except ValueError as e:
#     print(f"\nExcepción esperada (Longitud incorrecta): {e}")


try:
    votante1 = Votante("Elena", "Gómez", "46889241S", 35) # DNI VÁLIDO
    votante2 = Votante("Félix", "López", "46889241S", 40)
    votante3 = Votante("Félix", "López", "07256246E", 40)  

    votante1.votar("a")
    votante2.votar("a")
    votante3.votar("b")
    try:
        Escrutinio.mostrar_resultados(Votante.VOTOS_TOTALES)

    except ValueError as e:
        print(f"Error inesperado: {e}")

except ValueError as e:
    print(f"Error inesperado: {e}")