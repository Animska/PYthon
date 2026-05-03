import logging
from api.repository import get_available_slots
from api.database import get_db_connection
import json

logging.basicConfig(level=logging.INFO)

def debug_slots():
    fecha = "2026-04-30" # O la fecha de hoy que esté probando el usuario
    # Intentar obtener la fecha actual si no
    from datetime import datetime
    # fecha = datetime.now().strftime("%Y-%m-%d")
    
    print(f"--- Debugging Slots for {fecha} ---")
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas WHERE DATE(fecha_hora) = %s", (fecha,))
    citas = cursor.fetchall()
    print(f"Citas en DB para ese día: {json.dumps(citas, indent=2, default=str)}")
    
    cursor.execute("SELECT * FROM medicos WHERE estado = 'Activo'")
    medicos = cursor.fetchall()
    print(f"Médicos activos: {json.dumps(medicos, indent=2, default=str)}")
    
    slots = get_available_slots(fecha, "Examen General")
    print(f"Slots disponibles (Examen General): {len(slots)}")
    # print(slots)

if __name__ == "__main__":
    debug_slots()
