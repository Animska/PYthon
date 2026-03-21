from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# Asegúrate de importar PlantaCreate y crear_planta
from plantas import PlantaCreate, cargar_plantas, crear_planta

app = FastAPI(title="Agrosense API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

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

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)