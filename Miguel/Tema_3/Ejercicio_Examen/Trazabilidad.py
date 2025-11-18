class Trazabilidad:

    @staticmethod
    def consultar_stock_total(stock_total_dict):
        for producto in sorted(stock_total_dict.keys()):
            print(f"Producto: {producto}, Stock disponible: {stock_total_dict[producto]}")

    @staticmethod
    def generar_reporte_bajo_stock(stock_total_dict,umbral):
        if all(stock > umbral for stock in stock_total_dict.values()):
            print("“Todos los productos están por encima del umbral”")
        else:
            for producto in sorted(stock_total_dict.keys()):
                print(f"Producto: {producto}, Stock disponible: {stock_total_dict[producto]}")

    @staticmethod
    def  listar_nombres_disponibles(stock_total_dict):
        inventario = ", ".join(producto for producto in stock_total_dict.keys())
        return inventario

