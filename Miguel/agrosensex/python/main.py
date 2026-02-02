import os
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(BASE_DIR / "data")
PLANTAS_FILE = Path(DATA_DIR / "plantas.json")

class PlantaCreate(BaseModel):
    nombre: str
    nombre_cientifico: Optional[str] = ""
    descripcion: Optional[str] = ""
    recinto_id: Optional[str] = None
    cantidad: int = 1
    imagen_url: Optional[str] = ""
    fecha_adquisicion: Optional[str] = None
    ultimo_riego: Optional[str] = None
    necesita_trasplante: bool = False
    notas: Optional[str] = ""
class Planta(PlantaCreate):
    id: str
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()

def cargar_plantas() -> Dict[str, Planta]:
    """Carga las plantas desde el archivo JSON. Devuelve {} si no existe."""
    if not os.path.exists(PLANTAS_FILE):
        return {}
    
    try:
        with open(PLANTAS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Convertir dicts a objetos Planta
            plantas = {}
            for planta_id, planta_data in data.items():
                planta_data['id'] = planta_id
                plantas[planta_id] = Planta(**planta_data)
            return plantas
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error cargando plantas: {e}")
        return {}

def guardar_plantas(plantas: Dict[str, Planta]):
    """Guarda las plantas en el archivo JSON."""
    data = {}
    for planta_id, planta in plantas.items():
        data[planta_id] = planta.model_dump(exclude={'id'})
        data[planta_id]['id'] = planta_id
    
    try:
        with open(PLANTAS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    except Exception as e:
        print(f"Error guardando plantas: {e}")

def generar_planta_id(nombre: str) -> str:
    """Genera un ID único para la planta: nombre_sin_espacios_timestamp."""
    nombre_sin_espacios = nombre.lower().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{nombre_sin_espacios}_{timestamp}"

def crear_planta(planta: PlantaCreate):
    """Crea una nueva planta si no existe."""
    plantas = cargar_plantas()
    planta_id = generar_planta_id(planta.nombre)
    
    if planta_id in plantas:
        print(f"La planta con ID '{planta_id}' ya existe.")
        return
    
    # Crear objeto Planta completo
    nueva_planta = Planta(
        id=planta_id,
        **planta.model_dump()
    )
    
    plantas[planta_id] = nueva_planta
    guardar_plantas(plantas)
    print(f"Planta creada exitosamente con ID: {planta_id}")

def actualizar_planta(planta_id: str, planta_data: PlantaCreate):
    """Actualiza una planta existente."""
    plantas = cargar_plantas()
    
    if planta_id not in plantas:
        print(f"No se encontró la planta con ID: {planta_id}")
        return
    
    # Actualizar campos de PlantaCreate y updated_at
    planta_actual = plantas[planta_id]
    update_data = planta_data.model_dump(exclude_unset=True)
    update_data['updated_at'] = datetime.now().isoformat()
    
    updated_planta = Planta(
        id=planta_id,
        **{**planta_actual.model_dump(), **update_data}
    )
    
    plantas[planta_id] = updated_planta
    guardar_plantas(plantas)
    print(f"Planta con ID '{planta_id}' actualizada exitosamente.")

def eliminar_planta(planta_id: str):
    """Elimina una planta por su ID."""
    plantas = cargar_plantas()
    
    if planta_id not in plantas:
        print(f"No se encontró la planta con ID: {planta_id}")
        return
    
    del plantas[planta_id]
    guardar_plantas(plantas)
    print(f"Planta con ID '{planta_id}' eliminada exitosamente.")

# Ejemplo de uso para pruebas
if __name__ == "__main__":
    # Crear planta de prueba
    nueva_planta_test = PlantaCreate(
        nombre="Monstera Deliciosa",
        nombre_cientifico="Monstera deliciosa",
        descripcion="Planta tropical con hojas grandes y agujereadas.",
        recinto_id="salon_principal",
        cantidad=1,
        imagen_url="https://ejemplo.com/monstera.jpg",
        fecha_adquisicion="2024-05-15",
        ultimo_riego="2024-05-20",
        necesita_trasplante=False,
        notas="Le gusta la luz indirecta y mucha humedad."
    )
    
    # Descomenta para probar cada función:
    crear_planta(nueva_planta_test)
    
    # Para actualizar (cambia el ID por el que generó crear_planta):
    # id_planta = "monstera_deliciosa_20260202192125"  # Tu ID real
    # planta_modificada = PlantaCreate(
    #     nombre="Cactus Deliciosa",
    #     nombre_cientifico="Cactus deliciosa",
    #     descripcion="Planta tropical con hojas grandes y agujereadas.",
    #     recinto_id="salon_principal",
    #     cantidad=1,
    #     imagen_url="https://ejemplo.com/cactus.jpg",
    #     fecha_adquisicion="2024-05-17",
    #     ultimo_riego="2024-05-20",
    #     necesita_trasplante=False,
    #     notas="Le gusta la luz indirecta y mucha humedad."
    # )
    # actualizar_planta(id_planta, planta_modificada)
    
    # Para eliminar:
    # eliminar_planta(id_planta)