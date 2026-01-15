from pathlib import Path

def crear_y_filtrar_log():
    # 1. Crear log_acceso.txt con write_text
    log_original = """[2024-11-20 10:05:01] ERROR: Fichero no encontrado en /data/a/fichero.txt
                    [2024-11-20 10:05:30] INFO: Usuario 'user_001' ha iniciado sesion.
                    [2024-11-20 10:06:15] WARN: Disco al 80%.
                    [2024-11-20 10:06:40] INFO: Usuario 'user_002' ha iniciado sesion.
                    [2024-11-20 10:07:05] ERROR: Conexión perdida con base de datos."""
    
    archivo_log = Path("log_acceso.txt")
    archivo_log.write_text(log_original)
    
    # 2. Leer línea por línea de forma eficiente
    errores_warn = []
    log_entrada = Path("log_acceso.txt")
    
    with log_entrada.open('r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if linea.startswith('[2024-11-20') and ('ERROR' in linea or 'WARN' in linea):
                errores_warn.append(linea)
    
    # 3. Escribir líneas filtradas en log_errores.txt
    log_errores = Path("log_errores.txt")
    log_errores.write_text('\n'.join(errores_warn) + '\n')
    
    print(f"Archivo log_acceso.txt creado con 5 líneas.")
    print(f"Filtradas {len(errores_warn)} líneas (ERROR/WARN) a log_errores.txt")

# Ejecutar programa
crear_y_filtrar_log()
