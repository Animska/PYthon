from api.repository import authenticate_user, create_appointment
from api.database import get_db_connection

def test_flow():
    # 1. Simular login de paciente (asumiendo que existe uno)
    print("Probando autenticación...")
    user = authenticate_user("paciente@test.com", "1234", "patient")
    if not user:
        # Intentar con otro email si el de arriba no existe
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT u.email FROM usuarios u JOIN pacientes p ON u.id = p.usuario_id LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        if row:
            user = authenticate_user(row['email'], "1234", "patient")
    
    if user and 'paciente_id' in user:
        print(f"Usuario autenticado correctamente: {user['nombre']} (ID Paciente: {user['paciente_id']})")
        
        # 2. Crear cita
        print("Creando cita de prueba...")
        appointment_data = {
            'paciente_id': user['paciente_id'],
            'medico_id': 1,
            'fecha_hora': '2026-05-01 10:00:00',
            'motivo': 'Examen General',
            'sintomas': 'Dolor de cabeza persistente',
            'prioridad_alta': True
        }
        
        success = create_appointment(appointment_data)
        if success:
            print("¡Cita creada con éxito!")
            
            # 3. Verificar en BD
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM citas WHERE paciente_id = %s ORDER BY id DESC LIMIT 1", (user['paciente_id'],))
            cita = cursor.fetchone()
            conn.close()
            
            if cita:
                print(f"Cita encontrada en BD: ID={cita['id']}, Motivo={cita['motivo']}, Sintomas={cita['sintomas']}, Prioridad={cita['prioridad_alta']}")
            else:
                print("Error: No se encontró la cita en la base de datos.")
        else:
            print("Error al crear la cita.")
    else:
        print("No se pudo autenticar al paciente para la prueba.")

if __name__ == "__main__":
    test_flow()
