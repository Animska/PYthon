import json
import locale
import sys
from pathlib import Path
from datetime import datetime, date
from typing import Dict, Optional

# Asumiendo que procesador.py está en el mismo directorio
from procesador import ProcesadorTemperaturas

class GeneradorInformes:
    @staticmethod
    def formatear_fecha_espanol(fecha: datetime) -> str:
        """Configura el locale y formatea la fecha."""
        try:
            # En Windows suele ser 'es-es', en Linux/Mac 'es_ES.UTF-8'
            sistema = sys.platform
            nombre_locale = 'es_ES.UTF-8' if sistema != 'win32' else 'es-es'
            locale.setlocale(locale.LC_TIME, nombre_locale)
        except locale.Error:
            # Fallback por si el sistema no tiene instalado el locale español
            print("Advertencia: Locale español no disponible. Usando predeterminado.")
        
        return fecha.strftime("%A, %d de %B de %Y")
    
    def generar_informe_completo(self, procesador: ProcesadorTemperaturas, datos_api: Optional[dict]) -> Path:
        BASE_DIR = Path(__file__).resolve().parent
        FILE_DIR = BASE_DIR / "reportes"
        FILE_DIR.mkdir(exist_ok=True)

        estadisticas_historias = procesador.calcular_estadisticas()
        
        informe = {
            "fecha_generacion": datetime.now().isoformat(),
            "fecha_generacion_legible": self.formatear_fecha_espanol(datetime.now()),
            "estadisticas_historicas": estadisticas_historias,
            "clima_actual": datos_api  # Corregido el espacio por guion bajo para consistencia
        }

        fecha_formateada = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = FILE_DIR / f"informe_{fecha_formateada}.json"

        try:
            # CORRECCION APLICADA: Uso de filename.open para mayor limpieza
            with filename.open("w", encoding="utf-8") as f:
                json.dump(informe, f, indent=4, ensure_ascii=False)
            
            # CORRECCION APLICADA: Retorno directo del objeto Path
            return filename
        except Exception as e:
            print(f"Error guardando el archivo {filename}: {e}")
            return filename

# --- SECCIÓN DE PRUEBAS ---
if __name__ == "__main__":
    # 1. Configuración de rutas
    BASE_DIR = Path(__file__).resolve().parent
    ruta_csv = BASE_DIR / "datos" / "temperaturas.csv"

    # 2. Inicialización (Asegúrate de que el CSV exista para no dar error)
    if not ruta_csv.exists():
        print(f"Error: No se encuentra el archivo en {ruta_csv}")
    else:
        procesador = ProcesadorTemperaturas(str(ruta_csv))
        procesador.cargar_desde_csv()

        # 3. Datos simulados
        datos_api_simulados = {
            "ciudad": "Madrid",
            "temperatura_actual": 18.5,
            "humedad": 62,
            "descripcion": "Parcialmente nublado",
            "timestamp": datetime.now().isoformat()
        }

        generador = GeneradorInformes()

        # 4. Ejecución
        print("Generando informe con datos de API...")
        ruta = generador.generar_informe_completo(procesador, datos_api_simulados)

        # 5. Lectura y verificación
        if ruta.exists():
            with ruta.open('r', encoding='utf-8') as f:
                contenido = json.load(f)
            print(f"\nInforme guardado en: {ruta}")
            print(json.dumps(contenido, indent=4, ensure_ascii=False))