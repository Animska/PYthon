from pathlib import Path
from typing import List, Optional
import csv
import locale
from pydantic import ValidationError

# Asumiendo que RegistroTemperatura está en modelos.py
from modelos import RegistroTemperatura

class ProcesadorTemperaturas(): 
    total_procesados = 0

    def __init__(self, ruta_csv: Path) -> None:
        self.ruta_csv = ruta_csv
        self.registros: List[RegistroTemperatura] = []

    def cargar_desde_csv(self) -> None:
        """Lee el CSV usando DictReader y maneja errores de validación."""
        # CORRECCION: Comprobar que el archivo existe antes de abrirlo
        if not self.ruta_csv.exists():
            print(f"Error: El archivo {self.ruta_csv} no existe.")
            return

        # CORRECCION: Uso de with...open y DictReader para mayor profesionalismo
        try:
            with self.ruta_csv.open(mode='r', encoding='utf-8') as f:
                lector = csv.DictReader(f)
                
                for fila_num, fila_dict in enumerate(lector, start=1):
                    try:
                        # Usamos el constructor de tu modelo (asumiendo desde_dict o similar)
                        registro = RegistroTemperatura.desde_dict(fila_dict)
                        self.registros.append(registro)
                        ProcesadorTemperaturas.total_procesados += 1
                    except (ValidationError, ValueError, KeyError):
                        print(f"Error en fila {fila_num} del CSV, esta fila será omitida")

            print(f"Cargados {len(self.registros)} registros desde {self.ruta_csv.name}")
            
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")

    def calcular_estadisticas(self) -> dict:
        """Calcula métricas sobre los registros cargados."""
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        except locale.Error:
            # Fallback si el locale no está instalado en el sistema
            locale.setlocale(locale.LC_TIME, '')

        # CORRECCION: Si no hay registros, retornar diccionario con valores por defecto/None
        if not self.registros:
            return {
                "temperatura_maxima_absoluta": None,
                "temperatura_minima_absoluta": None,
                "temperatura_media": 0,
                "total_registros": 0,
                "periodo": {"desde": None, "hasta": None}
            }

        # Cálculos base
        temp_max_obj = max(self.registros, key=lambda r: r.temperatura_max)
        temp_min_obj = min(self.registros, key=lambda r: r.temperatura_min)
        
        # CORRECCION: Redondear temperaturas a 2 decimales
        t_max = round(temp_max_obj.temperatura_max, 2)
        t_min = round(temp_min_obj.temperatura_min, 2)
        t_media = round((t_max + t_min) / 2, 2)
        
        fecha_menor = min(self.registros, key=lambda r: r.fecha).fecha
        fecha_mayor = max(self.registros, key=lambda r: r.fecha).fecha
        
        return {
            "temperatura_maxima_absoluta": t_max,
            "temperatura_minima_absoluta": t_min,
            "temperatura_media": t_media,
            "total_registros": len(self.registros),
            "periodo": {
                # CORRECCION: Formato: %d de %B de %Y (ej: 24 de febrero de 2026)
                "desde": fecha_menor.strftime("%d de %B de %Y"),
                "hasta": fecha_mayor.strftime("%d de %B de %Y")
            }
        }
        
    @classmethod
    def mostrar_total_procesados(cls) -> None:
        print(f"Total de registros procesados por todas las instancias: {cls.total_procesados}")
        
# --- PRUEBAS ---
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    # Asegúrate de que esta ruta sea correcta en tu entorno
    ruta_csv = BASE_DIR / "datos" / "temperaturas.csv"
    
    procesador = ProcesadorTemperaturas(ruta_csv)
    
    procesador.cargar_desde_csv()
    estadisticas = procesador.calcular_estadisticas()
    
    print("\n--- Estadísticas calculadas ---")
    for clave, valor in estadisticas.items():
        if isinstance(valor, dict):
            print(f"{clave}:")
            for k, v in valor.items():
                print(f"  {k}: {v}")
        else:
            print(f"{clave}: {valor}")
    
    print("")
    ProcesadorTemperaturas.mostrar_total_procesados()