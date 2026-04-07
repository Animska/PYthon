import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import httpx
# Asegúrate de importar PlantaCreate y crear_planta
from plantas import PlantaCreate, cargar_plantas, crear_planta, actualizar_planta, eliminar_planta

app = FastAPI(title="Agrosense API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

#--------------------------------------------Plantas------------------------------------------
@app.get("/plantas")
def get_plantas():
    plantas = cargar_plantas()
    return list(p.model_dump() for p in plantas.values())

@app.post("/plantas") # Asegúrate de que no haya un slash extra al final si en el JS tampoco lo hay
def post_plantas(planta: PlantaCreate): # <--- DEBES recibir el objeto aquí
    try:
        nueva_planta = crear_planta(planta) # <--- Ahora 'planta' existe
        return nueva_planta
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.put("/plantas/{planta_id}")
def put_planta(planta_id: str, planta_actualizada: PlantaCreate):
    # 1. Intentamos cargar las plantas actuales para verificar si el ID existe
    plantas = cargar_plantas()
    
    if planta_id not in plantas:
        # 2. Si no existe, lanzamos el error 404 como solicitaste
        raise HTTPException(status_code=404, detail="Planta no encontrada")
    
    try:
        # 3. Llamamos a la función de lógica que ya tienes en plantas.py
        actualizar_planta(planta_id, planta_actualizada)
        return {"message": f"Planta {planta_id} actualizada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.delete("/plantas/{planta_id}")
def delete_planta(planta_id: str):
    plantas = cargar_plantas()
    
    if planta_id not in plantas:
        raise HTTPException(status_code=404, detail="Planta no encontrada")
    
    try:
        eliminar_planta(planta_id)
        return {"message": f"Planta con ID {planta_id} eliminada exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#--------------------------------------------Sensores------------------------------------------
load_dotenv()
HOME_ASSISTANT_URL = os.getenv("HOME_ASSISTANT_URL")
HOME_ASSISTANT_TOKEN = os.getenv("HOME_ASSISTANT_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {HOME_ASSISTANT_TOKEN}",
    "Content-Type": "application/json",
}

@app.get("/sensores")
async def obtener_sensores():
    """
    Endpoint que consulta los sensores y devuelve los que contienen 'agsex_' 
    en su friendly_name (dentro de attributes)
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{HOME_ASSISTANT_URL}/api/states",
                headers=HEADERS
            )
            response.raise_for_status()
            
            todos_los_sensores = response.json()
            
            sensores_agsex = []
            for sensor in todos_los_sensores:
                # 1. Accedemos al diccionario de atributos
                attrs = sensor.get("attributes", {})
                
                # 2. Obtenemos el friendly_name (si no existe, usamos string vacío)
                friendly_name = attrs.get("friendly_name", "").lower()
                
                # 3. Filtramos por el prefijo solicitado
                if "agsex_" in friendly_name:
                    sensores_agsex.append(sensor)

            return sensores_agsex

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error en Home Assistant")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)