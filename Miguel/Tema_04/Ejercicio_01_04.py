productos = [
{'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
{'nombre': 'Mouse', 'precio': 25, 'stock': 12},
{'nombre': 'Monitor', 'precio': 350, 'stock': 2},
{'nombre': 'Teclado', 'precio': 75, 'stock': 8}
]

productos_ordenados = sorted(productos,key=lambda p: p['precio'])
for producto in productos_ordenados:
    print(f"{producto['nombre']}: {producto['precio']}€")