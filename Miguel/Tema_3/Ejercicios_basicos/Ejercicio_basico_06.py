# Visualizar en pantalla aquellos productos cuyo precio esté entre 1.5 y 2.5 (incluidos).
from clases import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75)]

lista_productos = [producto for producto in productos if 1.5<=producto.precio<=2.5]

for producto in lista_productos:
    print(str(producto))