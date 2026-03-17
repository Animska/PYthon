from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from plantas import PlantaCreate, cargar_plantas, crear_planta, actualizar_planta, eliminar_planta

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


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)