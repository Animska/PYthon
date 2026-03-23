from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# Asegúrate de importar PlantaCreate y crear_planta
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

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)