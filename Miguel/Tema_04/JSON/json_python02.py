import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
archivo = BASE_DIR / "tareas.json"

# - Cargue el fichero tareas.json del ejercicio anterior.
with open(archivo, "r", encoding="utf-8") as f:
    tareas = json.load(f)

# - Cuente cuántas tareas tienen el estado igual a False (tareas pendientes).
pendientes = [tarea for tarea in tareas if not tarea['estado']]
num_pendientes = len(pendientes)

# - Muestre los títulos de las tareas pendientes.
print(f"Hay {num_pendientes} tareas pendientes:")
for tarea in pendientes:
    print(f"- {tarea['titulo']}")

# - Añada una nueva tarea a la lista ('titulo': 'Planificar examen', 'estado': False, 'prioridad': 3).
nueva_tarea = {'titulo': 'Planificar examen', 'estado': False, 'prioridad': 3}
tareas.append(nueva_tarea)

# - Sobrescriba el fichero tareas.json con la lista actualizada.
with open(archivo, "w", encoding="utf-8") as f:
    json.dump(tareas, f, indent=2, ensure_ascii=False)

print("Nueva tarea añadida y archivo actualizado.")
