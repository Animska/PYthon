class Trazabilidad:

    @staticmethod
    def consultar_stock_total(stock_total_dict):
        if not stock_total_dict:
            print("El stock esta vacio")
            return
        
        for producto in sorted(stock_total_dict.keys()):
            print(f"Producto: {producto}, Stock disponible: {stock_total_dict[producto]}")

    @staticmethod
    def generar_reporte_bajo_stock(stock_total_dict,umbral):
        productos_bajo_stock = {nombre:cantidad for nombre,cantidad in stock_total_dict.items() if cantidad <= umbral}
        print("REPORTE DE PRODUCTOS BAJO STOCK")
        if not productos_bajo_stock:
            print("El stock de todos los productos esta por encma del umbral")
            return
        for nombre,cantidad in productos_bajo_stock.items():
            print(f"{nombre} cantidad:{cantidad}")

    @staticmethod
    def  listar_nombres_disponibles(stock_total_dict):
        nombres_stock = [nombre for nombre,cantidad in stock_total_dict.items() if cantidad > 0]
        inventario = ", ".join(sorted(nombres_stock))
        return inventario

