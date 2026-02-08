from clases import Producto,Inventario,MovimientoInventario

def main():
    """Función principal de prueba del sistema."""
    
    print(f"\n{'='*90}")
    print("SISTEMA DE GESTIÓN DE INVENTARIO")
    print(f"{'='*90}\n")
    
    # Crear inventario
    inventario = Inventario()
    
    # Intentar cargar datos existentes
    print("Cargando datos existentes...")
    inventario.cargar_datos()
    
    print("\n--- AGREGANDO PRODUCTOS ---")
    
    # Crear productos
    try:
        prod1 = Producto("PROD001", "Laptop Dell", "Electrónica", 899.99, 0)
        inventario.agregar_producto(prod1)
        
        prod2 = Producto("PROD002", "Mouse Logitech", "Electrónica", 29.99, 0)
        inventario.agregar_producto(prod2)
        
        prod3 = Producto("PROD003", "Arroz Integral", "Alimentación", 3.50, 200)
        inventario.agregar_producto(prod3)
        
        prod4 = Producto("PROD004", "Aceite de Oliva", "Alimentación", 12.99, 50)
        inventario.agregar_producto(prod4)
        
        # Intentar agregar producto duplicado
        prod_duplicado = Producto("PROD001", "Otro Producto", "Otra", 100.0, 10)
        inventario.agregar_producto(prod_duplicado)
        
    except ValueError as e:
        print(f"✗ Error al crear producto: {e}")
    
    print("\n--- REGISTRANDO ENTRADAS ---")
    
    # Registrar entradas
    inventario.registrar_entrada("PROD001", 50, "Compra proveedor")
    inventario.registrar_entrada("PROD002", 100, "Reposición")
    inventario.registrar_entrada("PROD003", 150, "Compra mayorista")
    
    # Intentar entrada con cantidad negativa
    inventario.registrar_entrada("PROD001", -10, "Intento inválido")
    
    print("\n--- REGISTRANDO SALIDAS ---")
    
    # Registrar salidas
    inventario.registrar_salida("PROD001", 5, "Venta cliente")
    inventario.registrar_salida("PROD002", 10, "Venta online")
    inventario.registrar_salida("PROD003", 50, "Distribución tienda")
    
    # Intentar salida que supera el stock
    inventario.registrar_salida("PROD002", 200, "Pedido grande")
    
    # Intentar salida de producto inexistente
    inventario.registrar_salida("PROD999", 10, "Producto fantasma")
    
    print("\n--- LISTADO COMPLETO DE PRODUCTOS ---")
    inventario.listar_productos()
    
    print("--- PRODUCTOS POR CATEGORÍA: ELECTRÓNICA ---")
    inventario.listar_productos("Electrónica")
    
    print("--- PRODUCTOS POR CATEGORÍA: ALIMENTACIÓN ---")
    inventario.listar_productos("Alimentación")
    
    # Listar movimientos
    inventario.listar_movimientos()
    
    print("--- MOVIMIENTOS DEL PRODUCTO PROD001 ---")
    inventario.listar_movimientos("PROD001", limite=5)
    
    print("\n--- INFORME POR CATEGORÍAS ---")
    informe = inventario.generar_informe_categoria()
    
    for categoria, datos in informe.items():
        print(f"\nCategoría: {categoria}")
        print(f"  Productos: {datos['productos']}")
        print(f"  Stock total: {datos['stock_total']} unidades")
        print(f"  Valor total: {datos['valor_total']:,.2f}€")
    
    print("\n--- GUARDANDO DATOS ---")
    inventario.guardar_datos()
    
    print("\n--- DEMOSTRACIÓN DE CARGA DE DATOS ---")
    print("Creando nuevo inventario y cargando datos guardados...")
    
    nuevo_inventario = Inventario()
    nuevo_inventario.cargar_datos()
    
    print("\nProductos en el nuevo inventario:")
    nuevo_inventario.listar_productos()
    
    print(f"\n{'='*90}\n")


if __name__ == "__main__":
    main()