STOCK_INICIAL = {
    "martillo": (15.50, 50),
    "clavo_caja": (5.00, 200),
    "sierra_manual": (35.99, 10),
    "cinta_metrica": (8.25, 75),
}

PEDIDOS = [
    {"producto": "martillo", "cantidad": 5},
    {"producto": "sierra_manual", "cantidad": 12},  # No hay stock
    {"producto": "clavo_caja", "cantidad": 150},
    {"producto": "cinta_metrica", "cantidad": 10},
    {"producto": "llave_inglesa", "cantidad": 3}   # Producto no listado
]


def procesar_pedidos(stock: dict, pedidos: list) -> tuple:
    productos_faltantes = []
    costo_total_pedidos = 0.0
    for pedido in pedidos:
        producto = pedido['producto']
        cantidad = pedido['cantidad']
        if producto not in stock:
            productos_faltantes.append(producto)
            continue

        precio_unitario, cantidad_en_stock = stock[producto]
        if cantidad_en_stock < cantidad:
            productos_faltantes.append(producto)
            continue

        stock[producto] = (precio_unitario, cantidad_en_stock - cantidad)
        costo_total_pedidos += precio_unitario * cantidad

    return (stock, costo_total_pedidos, productos_faltantes)


# Prueba
stock_final, costo_final, faltantes = procesar_pedidos(STOCK_INICIAL, PEDIDOS)

print("\n--- EJERCICIO: GESTIÓN DE STOCK ---")
print(f"Costo Total de Pedidos Procesados: {costo_final}€")
print(f"Productos Faltantes/No Existentes: {faltantes}")
print(f"Stock Final de Sierras: {stock_final['sierra_manual']}") # 10 (no se restó)