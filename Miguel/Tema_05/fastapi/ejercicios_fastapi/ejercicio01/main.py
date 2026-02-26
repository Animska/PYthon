import os
from pathlib import Path
import logging
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from dotenv import load_dotenv
import uvicorn


BASE_DIR = Path(__file__).parent.resolve()
env_path = Path(BASE_DIR / ".env")
load_dotenv(dotenv_path=env_path)

#configuracion logger
logger= logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title = "Weather API",
    description="API para consultar el clima de ciudades",
    version="1.0.0"
)

#configuracion permisiva (desarrollo) de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_BASE_URL = os.getenv("WEATHER_BASE_URL", "")


@app.get("/api/weather")
async def obtener_tiempo(ciudad:str):
    try:
        if not ciudad or ciudad.strip() == "":
            raise HTTPException(status_code=400, detail="Debes proporcionar el nombre de una ciudad")
    
        async with httpx.AsyncClient() as client:
            response = await client.get(
                WEATHER_BASE_URL,
                params={
                    "q": ciudad,
                    "appid": WEATHER_API_KEY,
                    "units":"metric",
                    "lang": "es"
                },timeout=10
            )
            if response.status_code==404:
                raise HTTPException(status_code=404, detail=f"No se encontro la ciudad {ciudad}")
            if response.status_code!=200:
                raise HTTPException(status_code=response.status_code, detail="Error al consultar al servicio del clima")
            data = response.json()
            logger.info("Se ha cargado la ciudad: %s", ciudad)
            resultado ={
                "ciudad": data["name"],
                "temperatura": data["main"]["temp"],
                "sensacion": data["main"]["feels_like"],
                "humedad": data["main"]["humidity"],
                "descripcion": data["weather"][0]["description"],
                "icono": data["weather"][0]["icon"],
                "viento": data["wind"]["speed"]
            }
            return resultado
    except httpx.TimeoutException:
        logger.warning("Timeout al consultar %s", ciudad)
        raise HTTPException(status_code=504, detail="Tiempo de espera agotado")
    except httpx.RequestError as e:
        logger.warning("error de conexion para la ciudad %s %s", ciudad,e)
        raise HTTPException(status_code=503, detail=f"Error de conexion: {str(e)}")
    except Exception as e:
        logger.warning("error inesperado al consultar la ciudad: %s [%e]", ciudad,e)
        raise HTTPException(status_code=500, detail=f"Error de conexion: {str(e)}")
    
#Endpoint STATUS
@app.get("/")
async def root()-> dict[str, str | dict[str, str]]:
    return {
        "mensaje": "Weather API funcionando correctamente",
        "version": "1.0.0",
        "endpoints": {
            "clima": "/api/weather?city=Madrid"
        },
    }

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)