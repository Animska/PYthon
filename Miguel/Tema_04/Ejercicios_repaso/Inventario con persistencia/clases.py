from datetime import datetime
from typing import Optional
import json
import os
from pathlib import Path


class Producto:
    """Representa un producto en el inventario."""
    
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, 
                 stock: int, fecha_creacion: Optional[datetime] = None) -> None:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
    
    def agregar_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        self.stock += cantidad
    
    def reducir_stock(self, cantidad: int) -> bool:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        if cantidad > self.stock:
            return False
        
        self.stock -= cantidad
        return True
    
    def calcular_valor_inventario(self) -> float:
        return self.stock * self.precio
    
    def to_dict(self) -> dict:
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio': self.precio,
            'stock': self.stock,
            'fecha_creacion': self.fecha_creacion.isoformat()
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Producto':
        return Producto(
            codigo=data['codigo'],
            nombre=data['nombre'],
            categoria=data['categoria'],
            precio=data['precio'],
            stock=data['stock'],
            fecha_creacion=datetime.fromisoformat(data['fecha_creacion'])
        )
    
    def __str__(self) -> str:
        """Representación en string del producto."""
        return (f"[{self.codigo}] {self.nombre} - {self.categoria} | "
                f"Precio: {self.precio:.2f}€ | Stock: {self.stock} unidades")


class MovimientoInventario:
    """Representa un movimiento de entrada o salida de stock."""
    
    def __init__(self, producto_codigo: str, tipo: str, cantidad: int, 
        observaciones: str = "", fecha: Optional[datetime] = None) -> None:
        
        if tipo not in ["ENTRADA", "SALIDA"]:
            raise ValueError("El tipo debe ser 'ENTRADA' o 'SALIDA'")
        
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        
        self.producto_codigo = producto_codigo
        self.tipo = tipo
        self.cantidad = cantidad
        self.observaciones = observaciones
        self.fecha = fecha if fecha else datetime.now()
    
    def to_dict(self) -> dict:
        return {
            'producto_codigo': self.producto_codigo,
            'tipo': self.tipo,
            'cantidad': self.cantidad,
            'fecha': self.fecha.isoformat(),
            'observaciones': self.observaciones
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'MovimientoInventario':
        return MovimientoInventario(
            producto_codigo=data['producto_codigo'],
            tipo=data['tipo'],
            cantidad=data['cantidad'],
            observaciones=data['observaciones'],
            fecha=datetime.fromisoformat(data['fecha'])
        )
    
    def __str__(self) -> str:
        """Representación en string del movimiento."""
        fecha_str = self.fecha.strftime('%d/%m/%Y %H:%M')
        return (f"[{fecha_str}] {self.tipo} - {self.producto_codigo} - "
                f"{self.cantidad} unidades - {self.observaciones}")


class Inventario:
    """Gestiona el inventario completo de productos y movimientos."""
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = Path(BASE_DIR/"data")
    os.makedirs(DATA_DIR, exist_ok=True)
    
    def __init__(self, archivo_productos: str = "productos.json", 
                 archivo_movimientos: str = "movimientos.json") -> None:
        self.productos: dict[str, Producto] = {}
        self.movimientos: list[MovimientoInventario] = []
        self.archivo_productos = archivo_productos
        self.archivo_movimientos = archivo_movimientos
    
    def agregar_producto(self, producto: Producto) -> bool:
        if producto.codigo in self.productos:
            print(f"Error: Ya existe un producto con el código {producto.codigo}")
            return False
        
        self.productos[producto.codigo] = producto
        print(f"Producto agregado: {producto}")
        return True
    
    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return self.productos.get(codigo)
    
    def registrar_entrada(self, codigo: str, cantidad: int, 
                         observaciones: str = "") -> bool:
        producto = self.buscar_producto(codigo)
        
        if not producto:
            print(f"✗ Error: No existe el producto con código {codigo}")
            return False
        
        try:
            # Crear el movimiento
            movimiento = MovimientoInventario(codigo, "ENTRADA", cantidad, observaciones)
            
            # Agregar stock al producto
            producto.agregar_stock(cantidad)
            
            # Registrar el movimiento
            self.movimientos.append(movimiento)
            
            print(f"✓ Entrada registrada: {cantidad} unidades de {codigo}")
            return True
            
        except ValueError as e:
            print(f"✗ Error: {e}")
            return False
    
    def registrar_salida(self, codigo: str, cantidad: int, 
                        observaciones: str = "") -> bool:
        producto = self.buscar_producto(codigo)
        
        if not producto:
            print(f"Error: No existe el producto con código {codigo}")
            return False
        
        try:
            # Intentar reducir el stock
            if not producto.reducir_stock(cantidad):
                print(f"Stock insuficiente para realizar la salida de {cantidad} "
                      f"unidades de {codigo} (disponible: {producto.stock})")
                return False
            
            # Crear y registrar el movimiento
            movimiento = MovimientoInventario(codigo, "SALIDA", cantidad, observaciones)
            self.movimientos.append(movimiento)
            
            print(f"Salida registrada: {cantidad} unidades de {codigo}")
            return True
            
        except ValueError as e:
            print(f"✗ Error: {e}")
            return False
    
    def listar_productos(self, categoria: Optional[str] = None) -> None:
        if not self.productos:
            print("No hay productos en el inventario")
            return
        
        # Filtrar productos
        productos_filtrados = list(self.productos.values())
        
        if categoria:
            productos_filtrados = [p for p in productos_filtrados 
                                  if p.categoria.lower() == categoria.lower()]
            titulo = f"PRODUCTOS - CATEGORÍA: {categoria.upper()}"
        else:
            titulo = "LISTADO COMPLETO DE PRODUCTOS"
        
        if not productos_filtrados:
            print(f"No hay productos en la categoría {categoria}")
            return
        
        # Mostrar tabla
        print(f"\n{'='*90}")
        print(titulo)
        print(f"{'='*90}")
        print(f"{'CÓDIGO':<10} {'NOMBRE':<20} {'CATEGORÍA':<15} {'PRECIO':>10} {'STOCK':>8} {'VALOR TOTAL':>12}")
        print(f"{'='*90}")
        
        valor_total_inventario = 0.0
        
        for producto in productos_filtrados:
            valor_producto = producto.calcular_valor_inventario()
            valor_total_inventario += valor_producto
            
            print(f"{producto.codigo:<10} {producto.nombre:<20} {producto.categoria:<15} "
                  f"{producto.precio:>9.2f}€ {producto.stock:>8} {valor_producto:>11.2f}€")
        
        print(f"{'='*90}")
        print(f"VALOR TOTAL DEL INVENTARIO: {valor_total_inventario:,.2f}€")
        print(f"{'='*90}\n")
    
    def listar_movimientos(self, codigo_producto: Optional[str] = None, 
                          limite: int = 10) -> None:
        if not self.movimientos:
            print("No hay movimientos registrados")
            return
        
        # Filtrar movimientos
        movimientos_filtrados = self.movimientos
        
        if codigo_producto:
            movimientos_filtrados = [m for m in movimientos_filtrados 
                                    if m.producto_codigo == codigo_producto]
            titulo = f"MOVIMIENTOS DEL PRODUCTO {codigo_producto}"
        else:
            titulo = f"ÚLTIMOS {limite} MOVIMIENTOS"
        
        if not movimientos_filtrados:
            print(f"No hay movimientos para el producto {codigo_producto}")
            return
        
        # Ordenar por fecha (más recientes primero)
        movimientos_ordenados = sorted(movimientos_filtrados, 
                                      key=lambda m: m.fecha, 
                                      reverse=True)
        
        # Limitar cantidad
        movimientos_mostrar = movimientos_ordenados[:limite]
        
        print(f"\n{'='*90}")
        print(titulo)
        print(f"{'='*90}")
        
        for movimiento in movimientos_mostrar:
            print(movimiento)
        
        print(f"{'='*90}\n")
    
    def guardar_datos(self) -> bool:
        try:
            # Guardar productos
            productos_dict = [producto.to_dict() for producto in self.productos.values()]
            
            with open(self.archivo_productos, 'w', encoding='utf-8') as f:
                json.dump(productos_dict, f, indent=4, ensure_ascii=False)
            
            # Guardar movimientos
            movimientos_dict = [movimiento.to_dict() for movimiento in self.movimientos]
            
            with open(self.archivo_movimientos, 'w', encoding='utf-8') as f:
                json.dump(movimientos_dict, f, indent=4, ensure_ascii=False)
            
            print(f"Datos guardados correctamente en archivos JSON")
            return True
            
        except Exception as e:
            print(f"✗ Error al guardar datos: {e}")
            return False
    
    def cargar_datos(self) -> bool:
        # Verificar si existen los archivos
        if not os.path.exists(self.archivo_productos):
            print(f"ℹ  No se encontró el archivo {self.archivo_productos}")
            return False
        
        if not os.path.exists(self.archivo_movimientos):
            print(f"ℹ  No se encontró el archivo {self.archivo_movimientos}")
            return False
        
        try:
            # Cargar productos
            with open(self.archivo_productos, 'r', encoding='utf-8') as f:
                productos_dict = json.load(f)
            
            for prod_dict in productos_dict:
                producto = Producto.from_dict(prod_dict)
                self.productos[producto.codigo] = producto
            
            # Cargar movimientos
            with open(self.archivo_movimientos, 'r', encoding='utf-8') as f:
                movimientos_dict = json.load(f)
            
            for mov_dict in movimientos_dict:
                movimiento = MovimientoInventario.from_dict(mov_dict)
                self.movimientos.append(movimiento)
            
            print(f" Datos cargados correctamente desde archivos JSON")
            print(f"  Productos cargados: {len(self.productos)}")
            print(f"  Movimientos cargados: {len(self.movimientos)}")
            return True
            
        except Exception as e:
            print(f" Error al cargar datos: {e}")
            return False
    
    def generar_informe_categoria(self) -> dict[str, dict]:
        informe: dict[str, dict] = {}
        
        for producto in self.productos.values():
            if producto.categoria not in informe:
                informe[producto.categoria] = {
                    'productos': 0,
                    'stock_total': 0,
                    'valor_total': 0.0
                }
            
            informe[producto.categoria]['productos'] += 1
            informe[producto.categoria]['stock_total'] += producto.stock
            informe[producto.categoria]['valor_total'] += producto.calcular_valor_inventario()
        
        return informe
