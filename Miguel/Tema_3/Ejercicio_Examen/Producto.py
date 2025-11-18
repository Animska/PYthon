class Producto:
    STOCK_TOTAL=dict()
    def __init__(self,nombre,codigo_lote):
        self.__nombre=nombre
        self.codigo_lote=codigo_lote

    @property
    def nombre(self):
    #Getter: devuelve el valor de _nombre.
        return self.__nombre

    @property
    def codigo_lote(self):
    #Getter: devuelve el valor de _lote.
        return self.__codigo_lote
        
    @codigo_lote.setter
    def codigo_lote(self, valor):
    #Setter: valida antes de asignar el valor.
        if len(valor)==8 and valor[0]=='L':
            self.__codigo_lote = valor
            self.STOCK_TOTAL[self.nombre] = self.STOCK_TOTAL.get(self.nombre, 0) + 1
            print(f"Producto {self.__nombre} (Lote:{self.codigo_lote}) creado y añadido al stock")
        else:
            raise ValueError
        
    def vender(self):
        if self.STOCK_TOTAL[self.nombre]>0:
            self.STOCK_TOTAL[self.nombre]-=1
            print(f"Venta de {self.nombre} realizada. Stock restante: {self.STOCK_TOTAL[self.nombre]}")
        
# producto1 = Producto('Rubicrono','LOTE-P45')
# producto2 = Producto('Rubicrono','LOTE-P46')
# producto3 = Producto('Concerta','LOTE-P46')

# print(producto1.STOCK_TOTAL)
# producto1.vender()