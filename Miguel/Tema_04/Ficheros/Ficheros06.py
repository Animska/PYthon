import os
from pathlib import Path

def crear_estructura_informes():
    # 1. Ruta base: data/informes/2026/ventas
    ruta_base = Path("data") / "informes" / "2026" / "ventas"
    
    # 2. Crear toda la estructura con os.makedirs y exist_ok=True
    os.makedirs(ruta_base, exist_ok=True)
    
    # 3. Crear ruta completa del fichero usando operador /
    archivo_informe = ruta_base / "informe_final.txt"
    
    # 4. Escribir texto en el fichero
    archivo_informe.write_text("Informe Creado")
    
    print(f"Estructura creada: {ruta_base}")
    print(f"Archivo escrito: {archivo_informe}")

# Ejecutar
crear_estructura_informes()
