import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
archivo = BASE_DIR / "config.json"

def crear_configuracion():
    """Crea el archivo config.json inicial"""
    config = {
        "app_name": "Mi Aplicación Web",
        "version": "1.0.0",
        "database": {
            "host": "localhost",
            "port": 5432,
            "nombre": "mi_bd"
        },
        "debug": True
    }
    
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def cargar_configuracion():
    """1. Carga la configuración desde config.json"""
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Archivo config.json no encontrado")
        return None

def mostrar_configuracion(config):
    """2. Muestra información de la configuración"""
    print(f"Nombre: {config['app_name']}")
    print(f"Versión: {config['version']}")
    print("Configuración BD:")
    bd = config['database']
    print(f"  Host: {bd['host']}")
    print(f"  Puerto: {bd['port']}")
    print(f"  Nombre: {bd['nombre']}")
    
    # 3. Modo debug
    if config['debug']:
        print("Modo DEBUG activado")

def modificar_debug(config, nuevo_valor):
    """4. Modifica el valor de debug"""
    config['debug'] = nuevo_valor
    return config

def guardar_configuracion(config):
    """5. Guarda la configuración actualizada"""
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error guardando: {e}")
        return False

# Programa principal
if __name__ == "__main__":
    # Crear config inicial (ejecutar una vez)
    crear_configuracion()
    
    # Cargar, mostrar y modificar
    config = cargar_configuracion()
    if config:
        mostrar_configuracion(config)
        
        # Cambiar debug a False
        config = modificar_debug(config, False)
        
        # Guardar cambios
        if guardar_configuracion(config):
            print("Configuración actualizada correctamente")
