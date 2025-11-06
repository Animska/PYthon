from clases import Producto

productos = [Producto("tomate", "fruta", 2.3, 100),
    Producto("patata", "verdura", 1.5, 200),
    Producto("cebolla", "verdura", 1.8, 150),
    Producto("manzana", "fruta", 3.2, 50),
    Producto("pera", "fruta", 2.7, 75)]

verduras = [producto for producto in productos if producto.categoria=="verdura"]

for verdura in verduras:
    print(str(verdura))