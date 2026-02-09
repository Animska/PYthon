"""
inventario con funciones de gestion, los productos
se guardan en una variable global dict()
"""

# Variable global del inventario
inventario = {}

def agregar_producto(nombre:str, precio:float, cantidad:int)->bool:
    """
    Agrega un nuevo producto si no existe.

    Args:
        -Nombre: nombre del producto
        -Precio: precio por unidad del producto
        -cantidad: cantidad de stock del producto
    """
    if nombre in inventario:
        return False
    inventario[nombre] = (precio, cantidad)
    return True

def get_producto(nombre:str)->tuple:
    """
    Retorna la tupla (precio, cantidad) o (0,0) si no existe.
    
    Args:
        -nombre: nombre del prodcuto
    """
    return inventario.get(nombre, (0, 0))

def actualizar_stock(nombre:str, cantidad:int)->bool:
    """
    Modifica la cantidad de un producto manteniendo su precio original.
    
    Args:
        -nombre: nombre del producto
        -cantidad: nueva cantidad del stock del producto
    """
    if nombre not in inventario:
        return False
    precio_actual = inventario[nombre][0]
    inventario[nombre] = (precio_actual, cantidad)
    return True

def eliminar_producto(nombre:str)->bool:
    """
    Elimina el producto del diccionario.

    Args:
        -nombre: nombre del producto
    """
    if nombre in inventario:
        del inventario[nombre]
        return True
    return False

def calcular_valor()->float:
    """
    Calcula el valor total: suma de (precio * cantidad) de todos los productos.

    Return:
        -valor total de todo el inventario
    """
    total = sum(precio * cantidad for precio, cantidad in inventario.values())
    return total

def return_dict()->dict:
    """
    Retorna el diccionario
    """
    return inventario
