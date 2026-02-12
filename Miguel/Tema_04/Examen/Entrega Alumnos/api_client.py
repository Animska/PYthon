from pathlib import Path
import os
from datetime import datetime
from typing import Optional, Dict
import requests
from dotenv import load_dotenv


class ClienteClimaAPI:
    load_dotenv()
    def __init__(self) -> None:
        self.API_KEY = os.getenv('API_KEY')
        if not self.API_KEY:
            raise ValueError("Variable de entorno API_KEY no encontrada. Configúrala en el archivo .env")

        self.URL_BASE = os.getenv('URL_OPENWEATHER',"")
        self.CIUDAD_DEFECTO = os.getenv('CIUDAD_DEFECTO')
        self.UNIDADES = os.getenv('UNIDADES') if os.getenv('UNIDADES') else "metric"

        print(f"""
            “Cliente API inicializado
                - Ciudad por defecto: {self.CIUDAD_DEFECTO} 
                - Unidades: {self.UNIDADES}”
            """)
        
    def obtener_clima_actual(self, ciudad: Optional[str] = None) -> Optional[Dict]:
        params = {
            'q': ciudad if ciudad else self.CIUDAD_DEFECTO,
            'appid': self.API_KEY,
            'units': self.UNIDADES,
            'lang': 'es' # Para descripciones en español
            }
        
        response = requests.get(self.URL_BASE, params=params, timeout=10)
        response.raise_for_status()
        datos = response.json()

        return {
            "ciudad": datos["name"],
            "temperatura": datos['main']['temp'],
            "sensacion_termica": datos['main']['feels_like'],
            "descripcion": datos['weather'][0]['description'],
            "humedad": datos['main']['humidity'],
            "timestamp": datetime.now().isoformat()

        }



#PRUEBAS
if __name__ == "__main__":
    cliente_api = ClienteClimaAPI()
    clima_actual = cliente_api.obtener_clima_actual()
    print(clima_actual)

    cliente_api = ClienteClimaAPI()
    clima_actual = cliente_api.obtener_clima_actual("Zafra")
    print(clima_actual)
        