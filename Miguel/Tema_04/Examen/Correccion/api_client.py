from pathlib import Path
import os
from datetime import datetime
from typing import Optional, Dict
import requests
from dotenv import load_dotenv

class ClienteClimaAPI:
    def __init__(self) -> None:
        # CORRECCIÓN: Definimos la ruta absoluta al .env basándonos en la ubicación de este script
        env_path = Path(__file__).parent / '.env'
        load_dotenv(dotenv_path=env_path)

        self.API_KEY = os.getenv('API_KEY')
        if not self.API_KEY:
            raise ValueError("Variable de entorno API_KEY no encontrada. Revisa tu archivo .env")

        # CORRECCIÓN: Uso de valores por defecto directamente en getenv
        self.URL_BASE = os.getenv('URL_OPENWEATHER', "https://api.openweathermap.org/data/2.5/weather")
        self.CIUDAD_DEFECTO = os.getenv('CIUDAD_DEFECTO', "Madrid")
        self.UNIDADES = os.getenv('UNIDADES', "metric")

        print(f"""
        --- Cliente API Inicializado ---
        Ciudad por defecto: {self.CIUDAD_DEFECTO}
        Unidades:           {self.UNIDADES}
        --------------------------------
        """)
        
    def obtener_clima_actual(self, ciudad: Optional[str] = None) -> Optional[Dict]:
        # Si no se pasa ciudad, usamos la de defecto
        ciudad_consulta = ciudad if ciudad else self.CIUDAD_DEFECTO
        
        params = {
            'q': ciudad_consulta,
            'appid': self.API_KEY,
            'units': self.UNIDADES,
            'lang': 'es'
        }
        
        try:
            response = requests.get(self.URL_BASE, params=params, timeout=10)
            # Levanta una excepción si hay error (404, 500, etc.)
            response.raise_for_status()
            datos = response.json()

            return {
                "ciudad": datos["name"],
                "temperatura": f"{datos['main']['temp']}°",
                "sensacion_termica": f"{datos['main']['feels_like']}°",
                "descripcion": datos['weather'][0]['description'].capitalize(),
                "humedad": f"{datos['main']['humidity']}%",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return None

# --- PRUEBAS ---
if __name__ == "__main__":
    try:
        cliente = ClienteClimaAPI()
        
        # Prueba 1: Ciudad por defecto
        print(f"Consultando ciudad por defecto...")
        print(cliente.obtener_clima_actual())

        # Prueba 2: Ciudad específica
        print(f"\nConsultando Zafra...")
        print(cliente.obtener_clima_actual("Zafra"))
        
    except ValueError as e:
        print(f"Error de configuración: {e}")