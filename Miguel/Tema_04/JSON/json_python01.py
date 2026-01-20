import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
archivo = Path(BASE_DIR / "tareas.json")
# Definir la lista de tareas
tareas = [
    {'titulo': 'Revisar tema JSON', 'estado': True, 'prioridad': 1},
    {'titulo': 'Preparar informe de ventas', 'estado': False, 'prioridad': 2},
    {'titulo': 'Enviar correo al cliente', 'estado': False, 'prioridad': 3},
]

# Serializar y guardar en tareas.json con indent=2
with open(archivo, "w", encoding="utf-8") as f:
    json.dump(tareas, f, indent=2, ensure_ascii=False)
