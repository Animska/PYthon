from pathlib import Path

from procesador import ProcesadorTemperaturas
from api_client import ClienteClimaAPI
from generador_informes import GeneradorInformes

def main():
    print("="*70)
    print(" SISTEMA DE ANÁLISIS METEOROLÓGICO - MeteoData Solutions")
    print("="*70)
    print()
        
    # ===============================================================
    # PASO 1: PROCESAMIENTO DE DATOS HISTÓRICOS
    # ===============================================================
    print("PASO 1: Procesando datos históricos del CSV...")
    print("-" * 70)
    
    ruta_csv = Path("datos") / "temperaturas.csv"
    
    # Instanciar el procesador
    procesador = ProcesadorTemperaturas(ruta_csv)
    
    # Cargar datos del CSV
    procesador.cargar_desde_csv()
    
    # Calcular estadísticas
    estadisticas = procesador.calcular_estadisticas()
    
    # Mostrar estadísticas de forma legible
    print("\nEstadísticas de datos históricos:")
    print(f"   • Periodo: {estadisticas['periodo']['desde']} hasta {estadisticas['periodo']['hasta']}")
    print(f"   • Total de registros: {estadisticas['total_registros']}")
    print(f"   • Temperatura máxima absoluta: {estadisticas['temperatura_maxima_absoluta']}°C")
    print(f"   • Temperatura mínima absoluta: {estadisticas['temperatura_minima_absoluta']}°C")
    print(f"   • Temperatura media del periodo: {estadisticas['temperatura_media']}°C")
    print()
    
    print("PASO 2: Obteniendo datos actuales de la API...")
    print("-" * 70)
    
    cliente_api = ClienteClimaAPI()
    datos_api = cliente_api.obtener_clima_actual()
    
    if datos_api:
        # Datos obtenidos correctamente
        print("\n Clima actual:")
        print(f"   • Ciudad: {datos_api['ciudad']}")
        print(f"   • Temperatura: {datos_api['temperatura']}°C")
        print(f"   • Sensación térmica: {datos_api['sensacion_termica']}°C")
        print(f"   • Descripción: {datos_api['descripcion']}")
        print(f"   • Humedad: {datos_api['humedad']}%")
        print(f"   • Timestamp: {datos_api['timestamp']}")
    else:
        print(" No se pudieron obtener datos actuales, pero continuamos...")
    
    print()
    
    print("PASO 3: Generando informe JSON...")
    print("-" * 70)
    
    generador = GeneradorInformes()
    
    # Generar informe combinando datos históricos y actuales
    ruta_informe = generador.generar_informe_completo(
        procesador=procesador,
        datos_api=datos_api
    )
    
    print(f"\n Informe guardado en: {ruta_informe.absolute()}")
    print()
    
    print("PASO 4: Métricas del sistema")
    print("-" * 70)
    
    # Mostrar contador de clase (métricas globales)
    ProcesadorTemperaturas.mostrar_total_procesados()
    
    print()
    print("="*70)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("="*70)

if __name__ == "__main__":
    main()