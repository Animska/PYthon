class Producto:
    inventario = 0

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.__stock = 0  # Inicializa el atributo a 0 para que en el setter se pueda añadir a inventario
        self.stock = stock  

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0.0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor <= 0 :
            raise ValueError("El stock debe ser mayor que 0.")
        Producto.inventario -= self.__stock
        self.__stock = valor
        Producto.inventario += valor

    @classmethod
    def mostrar_total_inventario(cls):
        return cls.inventario

    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock para realizar esa venta")
        self.stock -= cantidad
        print("¡Venta completada!")

    def __str__(self):
        return f"""
        Nombre del producto: {self.nombre}.
        Precio por unidad: {self.precio:.2f}€.
        Unidades en Stock: {self.stock} unidades.
        """


# Pruebas
psp = Producto("PSP", 184.99, 200)
ds = Producto("Nintendo 3DS", 199.99, 500)
ps2 = Producto("PlayStation 2", 130.99, 1500)

# print(psp.precio)
# print(ds.nombre)
# print(ps2.stock)

# # psp.precio = 199.99
# # print(psp.precio)

# print(f"Inventario: {Producto.mostrar_total_inventario()}")
# # psp.vender(20)
# # print(psp.stock)

# # psp.stock = 2000
# # print(Producto.mostrar_total_inventario())

print(str(ps2))
