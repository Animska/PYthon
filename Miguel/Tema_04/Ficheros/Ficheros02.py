from pathlib import Path

def crear_reporte_ventas():
    # 1. Crear ruta al fichero usando pathlib
    archivo = Path("reporte_ventas.csv")
    
    # 2. Escribir contenido completo usando write_text
    contenido = """Region,Ventas_2024,Ventas_2025
                Norte,10500.50,12300.00
                Sur,8900.25,9500.75"""
    
    archivo.write_text(contenido)
    print("Archivo reporte_ventas.csv creado exitosamente")

# Ejecutar la función
crear_reporte_ventas()
