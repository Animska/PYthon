from pathlib import Path
from typing import List
import csv
import locale
from pydantic import ValidationError

from modelos import RegistroTemperatura

class ProcesadorTemperaturas(): 
    total_procesados=0

    def __init__(self,ruta_csv) -> None:
        self.ruta_csv = ruta_csv
        self.registros = []

    def cargar_desde_csv(self) -> None:
        # 2. Leer el contenido con read_text()
        contenido = self.ruta_csv.read_text()
        lineas = contenido.strip().split('\n')
        
        # Ignorar cabecera (primera línea)
        datos_lineas = lineas[1:]  # Desde el índice 1 hasta el final
        cnt_lineas=0#contador lineas
        for linea in datos_lineas:
            cnt_lineas+=1
            campos = linea.split(',')
            try:
                registro = RegistroTemperatura.desde_dict({
                    "fecha":campos[0],
                    "temperatura_max":campos[1],
                    "temperatura_min":campos[2],
                    "ciudad":campos[3]
                })
                self.registros.append(registro)
                ProcesadorTemperaturas.total_procesados+=1
            except ValidationError:
                print(f"Error en fila {cnt_lineas} del CSV, esta fila será omitida")

        print(f"“Cargados {self.total_procesados} registros desde {self.ruta_csv.name}”")

    def calcular_estadisticas(self)->dict:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

        temperatura_max = max(self.registros, key=lambda registro:registro.temperatura_max).temperatura_max
        temperatura_min = min(self.registros, key=lambda registro:registro.temperatura_min).temperatura_min
        temperatura_media = (temperatura_max + temperatura_min)/2
        total_registros = len(self.registros)
        fecha_menor = min(self.registros, key=lambda registro:registro.fecha).fecha
        fecha_mayor = max(self.registros, key=lambda registro:registro.fecha).fecha
        
        return {
            "temperatura_maxima_absoluta":temperatura_max,
            "temperatura_minima_absoluta":temperatura_min,
            "temperatura_media": round(temperatura_media,2),
            "total_registros": total_registros,
            "periodo": {
                "desde": fecha_menor.strftime("%d-%m-%Y"),
                "hasta": fecha_mayor.strftime("%d-%m-%Y")
            }
        }
        
    @classmethod
    def mostrar_total_procesados(cls)->None:
        print (f"Total de registros procesados por todas las instancias: {cls.total_procesados}")
        
    
#PRUEBAS  
if __name__ == "__main__":
    # Ejemplo de uso
    BASE_DIR = Path(__file__).resolve().parent
    ruta_csv = Path(BASE_DIR / "datos/temperaturas.csv")
    procesador = ProcesadorTemperaturas(ruta_csv)
    
    try:
        procesador.cargar_desde_csv()
        procesador.calcular_estadisticas()
        estadisticas = procesador.calcular_estadisticas()
        print("\nEstadísticas calculadas:")
        for clave, valor in estadisticas.items():
            print(f"{clave}: {valor}")
        
        ProcesadorTemperaturas.mostrar_total_procesados()
    
    except FileNotFoundError as e:
        print(e)