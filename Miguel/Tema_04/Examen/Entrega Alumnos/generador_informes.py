import json
import locale
from pathlib import Path
from datetime import datetime, date
from typing import Dict

from procesador import ProcesadorTemperaturas


class GeneradorInformes:
    @staticmethod
    def formatear_fecha_espanol(fecha:date)->str:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        fecha_formateada = fecha.strftime("%A,%d de %B de %Y")
        return fecha_formateada
    
    def generar_informe_completo(self, procesador: ProcesadorTemperaturas, datos_api:dict) -> Path:
        BASE_DIR = Path(__file__).resolve().parent
        FILE_DIR = BASE_DIR / "reportes"
        FILE_DIR.mkdir(exist_ok=True)

        estadisticas_historias = procesador.calcular_estadisticas()
        print(estadisticas_historias)
        informe ={
            "fecha_generacion":datetime.now().isoformat(),
            "fecha_generacion_legible":self.formatear_fecha_espanol(datetime.now()),
            "estadisticas_historicas":estadisticas_historias,
            "clima actual":datos_api
        }

        fecha_formateada = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = FILE_DIR /f"informe_{fecha_formateada}.json"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(informe, f, indent=4, ensure_ascii=False)
            
            return Path(filename)
        except Exception as e:
            print(f"Error guardando: {e}")
            return Path(filename)


#PRUEBAS
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    ruta_csv = BASE_DIR / "datos/temperaturas.csv"

    # Crear procesador y cargar datos del CSV
    procesador = ProcesadorTemperaturas(ruta_csv)
    procesador.cargar_desde_csv()

    # Probar generar informe con datos de API simulados
    datos_api_simulados = {
        "ciudad": "Madrid",
        "temperatura_actual": 18.5,
        "humedad": 62,
        "descripcion": "Parcialmente nublado",
        "timestamp": datetime.now().isoformat()
    }

    generador = GeneradorInformes()
    ruta = generador.generar_informe_completo(procesador, datos_api_simulados)

    # Leer y mostrar el contenido del informe generado
    with ruta.open('r', encoding='utf-8') as f:
        contenido = json.load(f)
    print("\nContenido del informe:")
    print(json.dumps(contenido, indent=4, ensure_ascii=False))

    # Probar también con datos_api = None
    print("\n--- Prueba con datos_api = None ---")
    ruta2 = generador.generar_informe_completo(procesador, None)
    with ruta2.open('r', encoding='utf-8') as f:
        contenido2 = json.load(f)
    print("\nContenido del informe (sin API):")
    print(json.dumps(contenido2, indent=4, ensure_ascii=False))