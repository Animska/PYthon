# Contar cuántos productos tienen un precio entre 2 y 3 (excluidos).
from clases import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75)]

lista_productos = [producto for producto in productos if 2<producto.precio<3]

print(f"Cantidad de productos entre 2 y 3€: {len(lista_productos)}")