from pathlib import Path

def actualizar_reporte_ventas():
    archivo = Path("reporte_ventas.csv")
    
    # 1. Verificar si el archivo existe
    if not archivo.exists():
        print("El archivo reporte_ventas.csv no existe")
        return
    
    try:
        # 2. Leer el contenido con read_text()
        contenido = archivo.read_text()
        lineas = contenido.strip().split('\n')
        
        # Ignorar cabecera (primera línea) usando slicing
        datos_lineas = lineas[1:]  # Desde el índice 1 hasta el final
        
        suma_2025 = 0.0
        
        # 3. Calcular suma de Ventas_2025
        for linea in datos_lineas:
            campos = linea.split(',')
            if len(campos) >= 3:
                try:
                    ventas_2025 = float(campos[2])
                    suma_2025 += ventas_2025
                except ValueError:
                    print(f"Error convirtiendo {campos[2]} a float")
                    continue
        
        # 4. Añadir línea total usando open('a') en modo append
        linea_total = f"Total,0,{suma_2025:.2f}\n"
        with archivo.open('a') as f:
            f.write(linea_total)
        
        print(f"Total Ventas_2025: {suma_2025:.2f} añadido al archivo")
        
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

# Ejecutar
actualizar_reporte_ventas()
