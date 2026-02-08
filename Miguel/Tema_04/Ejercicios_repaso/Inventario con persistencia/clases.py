from datetime import datetime
from typing import Optional
from pathlib import Path
import json
import os

class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int, fecha_creacion: Optional[datetime] = None) -> None:
        # Validaciones iniciales
        if precio <= 0:
            raise ValueError("ERROR! El precio debe ser mayor que 0")
        if stock < 0:
            raise ValueError("ERROR! El stock no puede ser negativo")
        
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()

    def agregar_stock(self, cantidad: int) -> None:
        """
        Agrega la cantidad al stock del producto

        Args:
            -cantidad: cantidad que se le añadira al stock del producto
        """
        if cantidad <= 0:
            raise ValueError("ERROR! La cantidad debe ser mayor que 0")
        self.stock += cantidad
        print(f"Se han añadido {cantidad} unidades al stock de {self.nombre}")

    def reducir_stock(self, cantidad: int) -> bool:
        """
        Reduce la cantidad al stock del producto

        Args:
            -cantidad: cantidad que se le reducira al stock del producto

        Return:
            -booleano si la funcion puede o no realizar la reduccion
        """
        if cantidad <= 0:
            raise ValueError("ERROR! La cantidad debe ser mayor que 0")
        if cantidad > self.stock:
            print(f"Error: La cantidad a reducir ({cantidad}) es mayor al stock disponible ({self.stock})")
            return False

        self.stock -= cantidad
        print(f"Stock actual de {self.nombre}: {self.stock}")
        return True

    def calcular_valor_inventario(self) -> float:
        """
        Calcula el valor total de todo el stock del producto

        Return:
            -float con el valor del stock
        """
        return self.stock * self.precio

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
            "fecha_creacion": self.fecha_creacion.isoformat()
        }

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} - {self.categoria} | Precio: {self.precio}€ | Stock: {self.stock} unidades"

    @staticmethod
    def from_dict(data: dict) -> 'Producto':
        return Producto(
            codigo=data.get("codigo"),
            nombre=data.get("nombre"),
            categoria=data.get("categoria"),
            precio=data.get("precio"),
            stock=data.get("stock"), # Era "stockl"
            fecha_creacion=datetime.fromisoformat(data.get("fecha_creacion"))
        )

class MovimientoInventario:
    def __init__(self, producto_codigo: str, tipo: str, cantidad: int, observaciones: str = "",fecha: Optional[datetime] = None) -> None:
        if tipo.lower() not in ["entrada","salida"]:
            raise ValueError("ERROR!")

        if cantidad < 0 :
            raise ValueError("ERROR! La cantidad debe ser positiva")
        self.producto_codigo = producto_codigo
        self.tipo = tipo
        self.cantidad = cantidad
        self.observaciones = observaciones
        self.fecha = fecha if fecha else datetime.now()

    def to_dict(self)->dict:
        return {
            "producto_codigo": self.producto_codigo,
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "fecha": self.fecha.isoformat(),
            "observaciones": self.observaciones
        }

    def __str__(self) -> str:
        return f"[{self.fecha}] ENTRADA - {self.producto_codigo} - {self.cantidad} unidades - {self.observaciones}"

    @staticmethod
    def from_dict(data:dict)-> 'MovimientoInventario':
        return MovimientoInventario(
            producto_codigo = data.get("producto_codigo"),
            tipo = data.get("tipo"),
            cantidad = data.get("cantidad"),
            observaciones = data.get("observaciones"),
            fecha = datetime.fromisoformat(data.get("fecha"))
        )

class Inventario:
    BASE_DIR = Path(__file__).resolve().parent
    CARPETA_DATA = BASE_DIR / "data"
    

    def __init__(self, archivo_productos: str = "productos.json", archivo_movimientos: str ="movimientos.json") -> None:
        self.CARPETA_DATA.mkdir(parents=True, exist_ok=True)
        self.archivo_productos = Path(self.CARPETA_DATA / archivo_productos)
        self.archivo_movimientos = Path(self.CARPETA_DATA / archivo_movimientos)
        self.productos = dict()
        self.movimientos = list()

    def agregar_producto(self,producto:Producto)-> bool:
        """
        Agrega un producto al diccionario de productos

        Args:
            -Producto que deseas agregar

        Return:
            -bool si se ha añadido correctamente
        """
        if producto.codigo in self.productos.keys():
            return False

        self.productos[producto.codigo] = producto
        return True

    def buscar_producto(self,codigo:str)->Optional[Producto]:
        """
        Busca y devuelve un producto en productos

        Args:
            -codigo: codigo del producto que buscamos

        Return:
            -Producto que buscamos
            -None si no lo encuentra
        """
        if codigo in self.productos.keys():
            return self.productos[codigo]

    def registrar_entrada(self,codigo:str, cantidad:int,observaciones:str="")-> bool:
        """
        Registra un MovimientoInventario de tipo entrada y suma al stock

        Args:
            -codigo: codigo del producto del que se registra la entrada
            -cantidad: cantidad del producto
            -observaciones: observaciones opcionales

        Return:
            -bool si se ha podido registrar la entrada o no
        """
        producto = self.buscar_producto(codigo)
        if producto is None:
            print("ERROR! El producto no existe.")
            return False
        try:
            movimiento = MovimientoInventario(codigo, "ENTRADA", cantidad, observaciones)
            producto.agregar_stock(cantidad)
            self.movimientos.append(movimiento)
            print("ENTRADA AÑADIDA SATISFACTORIAMENTE")
            return True
        except ValueError as e:
            print(e)
            return False

    def registrar_salida(self, codigo:str, cantidad:int, observaciones:str="")->bool:
        """
        Registra un MovimientoInventario de tipo salida y resta al stock

        Args:
            -codigo: codigo del producto del que se registra la salida
            -cantidad: cantidad del producto
            -observaciones: observaciones opcionales

        Return:
            -bool si se ha podido registrar la salida o no
        """
        producto = self.buscar_producto(codigo)
        if producto is None:
            print("ERROR! El producto no existe.")
            return False

        try:
            if not producto.reducir_stock(cantidad):
                print("Stock insuficiente")
                return False

            movimiento = MovimientoInventario(codigo, "SALIDA", cantidad, observaciones)
            self.movimientos.append(movimiento)
            print("ENTRADA AÑADIDA SATISFACTORIAMENTE")
            return True

        except ValueError as e:
            print(e)
            return False

    def listar_productos(self,categoria:Optional[str] = None)->None:
        """
        Lista los productos del diccionario productos en una tabla por terminal

        Args:
            -categoria: Categoria de los productos se muestran, si esta
            vacio enseñara todos los producto
        """
        #inventario vacío
        if not self.productos:
            print("\n" + "!" * 30)
            print("No hay productos en el inventario")
            print("!" * 30)
            return

        #por categoría
        productos_a_mostrar = self.productos.values()
        if categoria:
            productos_a_mostrar = [p for p in self.productos.values() if p.categoria.lower() == categoria.lower()]
        
            if not productos_a_mostrar:
                print(f"\nNo se encontraron productos en la categoría: '{categoria}'")
                return

        valor_inventario = 0.00
        #tabla
        print(f"\n{'INVENTARIO DE PRODUCTOS':^85}")
        print("-" * 85)
        print(f"{'Código':<10} {'Nombre':<20} {'Categoría':<15} {'Precio':<12} {'Stock':<10} {'Valor Total':<12}")
        print("-" * 85)
        for p in productos_a_mostrar:
            valor_inventario += p.calcular_valor_inventario()
            print(f"{p.codigo:<10} {p.nombre:<20} {p.categoria:<15} ${p.precio:<11.2f} {p.stock:<10} ${p.calcular_valor_inventario():<11.2f}")
        print("-" * 85)
        total_general = valor_inventario
        print(f"{'VALOR TOTAL DEL INVENTARIO:':>71} ${total_general:>11.2f}\n")

    def listar_movimientos(self, codigo_producto: Optional[str] = None, limite: int = 10) -> None:
        """
        Lista los movimientos de la lista movimientos

        Args:
            -codigo_producto: codigo del producto que queremos filtrar los moviminetos, si no
            se da ninguno enseñara todos los movimientos
            -limite: cantidad de productos que enseñara, por defecto 10
        """
        if codigo_producto:
            movimientos_filtrados = [
                m for m in self.movimientos if m.producto_codigo == codigo_producto
            ]
        else:
            movimientos_filtrados = self.movimientos

        if not movimientos_filtrados:
            print("No hay movimientos registrados.")
            return

        #Ordenar por fecha
        movimientos_ordenados = sorted(
            movimientos_filtrados, 
            key=lambda x: x.fecha, 
            reverse=True
        )

        for movimiento in movimientos_ordenados[:limite]:
            print(movimiento)

    def guardar_datos(self) -> bool:
        """
        Guarda la información de productos y movimientos en archivos JSON.
        """
        try:
            # Guardar inventario
            productos_data = [p.to_dict() for p in self.productos.values()]
            with open(self.archivo_productos, 'w', encoding='utf-8') as f:
                json.dump(productos_data, f, indent=4, ensure_ascii=False)

            # Guardar movimientos
            movimientos_data = [m.to_dict() for m in self.movimientos]
            with open(self.archivo_movimientos, 'w', encoding='utf-8') as f:
                json.dump(movimientos_data, f, indent=4, ensure_ascii=False)

            return True

        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            return False

    def cargar_datos(self)->bool:
        """
        Carga los datos de productos y movimientos desde archivos JSON.
        """
        try:
            if not os.path.exists(self.archivo_productos) or not os.path.exists(self.archivo_movimientos):
                print("Aviso: Uno o ambos archivos de datos no existen.")
                return False
            # Cargar inventario
            with open(archivo_productos, 'r', encoding='utf-8') as f:
                datos_prod = json.load(f)
                self.productos = {
                    item['codigo']: Producto.from_dict(item) 
                    for item in datos_prod
                }

            #Cargar movimientos
            with open(archivo_movimientos, 'r', encoding='utf-8') as f:
                datos_mov = json.load(f)
                self.movimientos = [MovimientoInventario.from_dict(item) for item in datos_mov]

            print("Datos cargados exitosamente.")
            return True

        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return False

    def generar_informe_categoria(self)->dict[str,dict]:
        informe = {}

        for producto in self.productos.values():
            cat = producto.categoria
        
            # Si la categoría no existe en el informe, la inicializamos
            if cat not in informe:
                informe[cat] = {
                    'productos': 0,
                    'stock_total': 0,
                    'valor_total': 0.0
                }
        
            # Acumulamos los datos del producto actual
            informe[cat]['productos'] += 1
            informe[cat]['stock_total'] += producto.stock
            informe[cat]['valor_total'] += producto.calcular_valor_inventario()

        return informe