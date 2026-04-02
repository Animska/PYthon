import json
import os
from typing import Dict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(BASE_DIR / "data")
RECINTOS_FILE = Path(DATA_DIR / "plantas.json")


class Recinto(BaseModel):
    nombre: str
    descripcion: str = ""
    sensor_temperatura:str = ""

def cargar_recintos() -> Dict[str, Recinto]:
    if not os.path.exists(RECINTOS_FILE):
        return {}
    try:
        with open(RECINTOS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {r_id: Recinto(**r_data) for r_id, r_data in data.items()}
    except Exception:
        return {}

def guardar_recintos(recintos: Dict[str, Recinto]):
    with open(RECINTOS_FILE, 'w', encoding='utf-8') as f:
        data = {r_id: r.model_dump() for r_id, r in recintos.items()}
        json.dump(data, f, indent=4, ensure_ascii=False)