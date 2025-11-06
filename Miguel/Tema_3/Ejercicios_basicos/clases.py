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
    def __init__(self,marca,modelo,anio,precio):
        self.marca = marca # usa el setter
        self.modelo = modelo # usa el setter
        self.anio = anio # usa el setter
        self.precio = precio # usa el setter
    
    @property
    def marca(self):
        #Getter: devuelve el valor de _marca.
        return self.__marca
        
    @marca.setter
    def marca(self, valor):
        #Setter: valida antes de asignar el valor.
        self.__marca = valor
        
    @property
    def modelo(self):
        #Getter: devuelve el valor de _modelo.
        return self.__modelo
        
    @modelo.setter
    def modelo(self, valor):
        #Setter: valida antes de asignar el valor.
        self.__modelo = valor
        
    @property
    def anio(self):
        #Getter: devuelve el valor de _año.
        return self.__año
        
    @anio.setter
    def anio(self, valor):
        #Setter: valida antes de asignar el valor.
        self.__año = valor


    @property
    def precio(self):
        #Getter: devuelve el valor de _precio.
        return self.__precio
        
    @precio.setter
    def precio(self, valor):
        #Setter: valida antes de asignar el valor.
        if valor <= 0.0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor

    def __str__(self):
        return f"""
        Marca y Modelo del vehiculo: {self.marca} {self.modelo}.
        Año del vehiculo: {self.anio}.
        Precio de salida: {self.precio} €.
        """
    
    def nombre_completo(self):
        cadena=self.marca+"-"+self.modelo
        return cadena