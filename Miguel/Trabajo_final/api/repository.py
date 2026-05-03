from typing import Optional, Dict, Any, List
import logging
from datetime import datetime, timedelta
from .database import get_db_connection

DURATIONS = {
    "Examen General": 30,
    "Tratamiento": 60,
    "Operación": 120
}

logger = logging.getLogger(__name__)

def authenticate_user(email: str, password: str, role: str) -> Optional[Dict[str, Any]]:
    """
    Verifica si un usuario existe con el email, contraseña y rol especificados.
    Devuelve los datos del usuario si las credenciales son correctas, o None en caso contrario.
    Nota: Se compara en texto plano la contraseña con `password_hash` por simplicidad
    del MVP, tal como se especificó.
    """
    connection = get_db_connection()
    if not connection:
        logger.error("No se pudo conectar a la base de datos para autenticar al usuario.")
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        # En la base de datos, el rol es ENUM('patient', 'doctor', 'admin')
        query = """
            SELECT id, email, rol 
            FROM usuarios 
            WHERE email = %s AND password_hash = %s AND rol = %s
        """
        cursor.execute(query, (email, password, role))
        user = cursor.fetchone()
        
        if user:
            # Recuperamos datos extra dependiendo del rol
            user_data = {
                "id": user["id"],
                "email": user["email"],
                "rol": user["rol"],
                "nombre": "Usuario" # Valor por defecto
            }
            
            if role == "patient":
                cursor.execute("SELECT id, nombre FROM pacientes WHERE usuario_id = %s", (user["id"],))
                paciente = cursor.fetchone()
                if paciente:
                    user_data["paciente_id"] = paciente["id"]
                    user_data["nombre"] = paciente["nombre"]
            elif role == "doctor":
                cursor.execute("SELECT id, nombre, especialidad FROM medicos WHERE usuario_id = %s", (user["id"],))
                medico = cursor.fetchone()
                if medico:
                    user_data["medico_id"] = medico["id"]
                    user_data["nombre"] = medico["nombre"]
                    user_data["especialidad"] = medico["especialidad"]
            elif role == "admin":
                user_data["nombre"] = "Control de Admin"
                    
            return user_data
        
        return None
    except Exception as e:
        logger.error(f"Error al autenticar usuario: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_patient(data: Dict[str, Any]) -> bool:
    """
    Crea un nuevo usuario con rol paciente y su correspondiente registro en la tabla pacientes.
    Lanza excepciones en caso de que el email o dni ya existan.
    """
    connection = get_db_connection()
    if not connection:
        logger.error("No se pudo conectar a la base de datos para registrar al paciente.")
        raise Exception("Error de conexión a la base de datos")

    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # Insertar en tabla usuarios
        query_usuario = "INSERT INTO usuarios (email, password_hash, rol) VALUES (%s, %s, 'patient')"
        cursor.execute(query_usuario, (data['email'], data['password']))
        usuario_id = cursor.lastrowid
        
        # Insertar en tabla pacientes
        query_paciente = "INSERT INTO pacientes (usuario_id, nombre, dni, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(query_paciente, (usuario_id, data['nombre'], data['dni'], data['telefono']))
        
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error al registrar paciente: {e}")
        raise e
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_patient_profile(usuario_id: int) -> Optional[Dict[str, Any]]:
    """Obtiene los datos completos de un paciente uniendo usuarios y pacientes."""
    connection = get_db_connection()
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT p.*, u.email 
            FROM pacientes p 
            JOIN usuarios u ON p.usuario_id = u.id 
            WHERE u.id = %s
        """
        cursor.execute(query, (usuario_id,))
        return cursor.fetchone()
    except Exception as e:
        logger.error(f"Error al obtener perfil: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_patient_profile(usuario_id: int, data: Dict[str, Any]) -> bool:
    """Actualiza el email en usuarios y el resto en pacientes."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # Actualizar email en usuarios
        cursor.execute("UPDATE usuarios SET email = %s WHERE id = %s", (data['email'], usuario_id))
        
        # Actualizar datos en pacientes
        query_paciente = """
            UPDATE pacientes 
            SET nombre = %s, telefono = %s, direccion = %s, grupo_sanguineo = %s, alergias = %s 
            WHERE usuario_id = %s
        """
        cursor.execute(query_paciente, (
            data['nombre'], data['telefono'], data['direccion'], 
            data['grupo_sanguineo'], data['alergias'], usuario_id
        ))
        
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error al actualizar perfil: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_all_doctors() -> List[Dict[str, Any]]:
    """Obtiene todos los médicos registrados."""
    connection = get_db_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT m.*, u.email, DATE_FORMAT(u.creado_en, '%Y-%m-%d') as fecha
            FROM medicos m
            JOIN usuarios u ON m.usuario_id = u.id
            ORDER BY m.nombre ASC
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error al obtener médicos: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_doctor(data: Dict[str, Any]) -> bool:
    """Crea un usuario médico y su perfil correspondiente."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # 1. Crear usuario
        cursor.execute(
            "INSERT INTO usuarios (email, password_hash, rol) VALUES (%s, %s, 'doctor')",
            (data['email'], data['password'])
        )
        usuario_id = cursor.lastrowid
        
        # 2. Crear médico
        cursor.execute(
            "INSERT INTO medicos (usuario_id, nombre, especialidad, estado) VALUES (%s, %s, %s, %s)",
            (usuario_id, data['nombre'], data['especialidad'], data['estado'])
        )
        
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error al crear médico: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_appointment(data: Dict[str, Any]) -> bool:
    """Crea una nueva cita en la base de datos."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        medico_id = data.get('medico_id') # Puede ser None (Pendiente de asignar por Admin)

        query = """
            INSERT INTO citas (paciente_id, medico_id, fecha_hora, motivo, sintomas, prioridad_alta)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['paciente_id'],
            medico_id,
            data['fecha_hora'],
            data['motivo'],
            data.get('sintomas'),
            data.get('prioridad_alta', False)
        ))
        connection.commit()
        return True
    except Exception as e:
        if connection:
            connection.rollback()
        logger.error(f"Error al crear cita: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_pending_appointments() -> List[Dict[str, Any]]:
    """Obtiene todas las citas con estado 'Pendiente'."""
    connection = get_db_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT c.*, p.nombre as paciente_nombre 
            FROM citas c
            JOIN pacientes p ON c.paciente_id = p.id
            WHERE c.estado = 'Pendiente'
            ORDER BY c.prioridad_alta DESC, c.fecha_hora ASC
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error al obtener citas pendientes: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_appointment_status(appointment_id: int, status: str, medico_id: int = None) -> bool:
    """Actualiza el estado de una cita y opcionalmente el médico asignado."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        if medico_id:
            query = "UPDATE citas SET estado = %s, medico_id = %s WHERE id = %s"
            cursor.execute(query, (status, medico_id, appointment_id))
        else:
            query = "UPDATE citas SET estado = %s WHERE id = %s"
            cursor.execute(query, (status, appointment_id))
        connection.commit()
        return cursor.rowcount > 0
    except Exception as e:
        if connection:
            connection.rollback()
        logger.error(f"Error al actualizar cita: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_all_appointments() -> List[Dict[str, Any]]:
    """Obtiene todas las citas (incluyendo aceptadas) para mostrar en el calendario."""
    connection = get_db_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT c.*, p.nombre as paciente_nombre, m.nombre as medico_nombre
            FROM citas c
            JOIN pacientes p ON c.paciente_id = p.id
            JOIN medicos m ON c.medico_id = m.id
            WHERE c.estado = 'Aceptada'
            ORDER BY c.fecha_hora ASC
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error al obtener todas las citas: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_active_appointments_by_patient(paciente_id: int) -> List[Dict[str, Any]]:
    """Obtiene todas las citas de un paciente específico, incluyendo datos del médico."""
    connection = get_db_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT c.*, m.nombre as medico_nombre, m.especialidad as medico_especialidad
            FROM citas c
            JOIN medicos m ON c.medico_id = m.id
            WHERE c.paciente_id = %s AND c.estado IN ('Pendiente', 'Aceptada')
            ORDER BY c.prioridad_alta DESC, c.fecha_hora ASC
        """
        cursor.execute(query, (paciente_id,))
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error al obtener citas del paciente: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_all_appointments_by_patient(paciente_id: int) -> List[Dict[str, Any]]:
    """Obtiene el historial completo de citas de un paciente."""
    connection = get_db_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT c.*, m.nombre as medico_nombre, m.especialidad as medico_especialidad
            FROM citas c
            JOIN medicos m ON c.medico_id = m.id
            WHERE c.paciente_id = %s
            ORDER BY c.fecha_hora DESC
        """
        cursor.execute(query, (paciente_id,))
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error al obtener historial de citas: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_doctor_appointments_by_day(medico_id: int, fecha: str) -> List[Dict[str, Any]]:
    """
    Obtiene las citas de un médico para un día específico, con detalles del paciente.
    Si la cita actual no tiene informe, hereda los vitales del último informe disponible del paciente.
    """
    connection = get_db_connection()
    if not connection:
        return []
    try:
        cursor = connection.cursor(dictionary=True)
        # Usamos COALESCE para traer los vitales del informe actual o del último histórico disponible
        query = """
            SELECT 
                c.id, c.fecha_hora, c.motivo, c.estado, c.paciente_id,
                p.nombre as paciente_nombre, p.grupo_sanguineo, p.alergias,
                COALESCE(ip.vitals_altura, h.vitals_altura) as vitals_altura,
                COALESCE(ip.vitals_peso, h.vitals_peso) as vitals_peso,
                COALESCE(ip.vitals_respiracion, h.vitals_respiracion) as vitals_respiracion,
                COALESCE(ip.vitals_presion, h.vitals_presion) as vitals_presion,
                ip.observaciones
            FROM citas c
            JOIN pacientes p ON c.paciente_id = p.id
            LEFT JOIN informe_paciente ip ON c.id = ip.cita_id
            LEFT JOIN (
                SELECT i1.*
                FROM informe_paciente i1
                JOIN (
                    SELECT paciente_id, MAX(id) as max_id
                    FROM informe_paciente
                    GROUP BY paciente_id
                ) i2 ON i1.id = i2.max_id
            ) h ON p.id = h.paciente_id
            WHERE c.medico_id = %s AND DATE(c.fecha_hora) = %s
            ORDER BY c.fecha_hora ASC
        """
        cursor.execute(query, (medico_id, fecha))
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error al obtener citas del médico con herencia de vitales: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_or_update_patient_report(data: Dict[str, Any]) -> bool:
    """Crea o actualiza el informe médico de una cita."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        cursor = connection.cursor()
        # Verificar si ya existe un informe para esta cita
        cursor.execute("SELECT id FROM informe_paciente WHERE cita_id = %s", (data['cita_id'],))
        exists = cursor.fetchone()

        if exists:
            query = """
                UPDATE informe_paciente 
                SET vitals_altura = %s, vitals_peso = %s, vitals_respiracion = %s, 
                    vitals_presion = %s, observaciones = %s
                WHERE cita_id = %s
            """
            params = (
                data['vitals_altura'], data['vitals_peso'], data['vitals_respiracion'],
                data['vitals_presion'], data['observaciones'], data['cita_id']
            )
        else:
            # Recuperar paciente_id de la cita para cumplir con la restricción de la BD
            cursor.execute("SELECT paciente_id FROM citas WHERE id = %s", (data['cita_id'],))
            cita = cursor.fetchone()
            if not cita:
                logger.error(f"No se encontró la cita {data['cita_id']} para crear el informe.")
                return False
            
            # Dependiendo del conector, cita puede ser una tupla o un diccionario
            p_id = cita[0] if isinstance(cita, (tuple, list)) else cita.get('paciente_id')

            query = """
                INSERT INTO informe_paciente 
                (cita_id, paciente_id, vitals_altura, vitals_peso, vitals_respiracion, vitals_presion, observaciones)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                data['cita_id'], p_id, data['vitals_altura'], data['vitals_peso'], 
                data['vitals_respiracion'], data['vitals_presion'], data['observaciones']
            )
        
        cursor.execute(query, params)
        connection.commit()
        return True
    except Exception as e:
        logger.error(f"Error al guardar informe del paciente: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_available_slots(fecha: str, motivo: str) -> List[str]:
    """
    Calcula los huecos horarios disponibles de forma global en la clínica.
    Un hueco es disponible si hay al menos un médico libre para la duración del motivo.
    """
    connection = get_db_connection()
    if not connection:
        return []
    
    duracion_minutos = DURATIONS.get(motivo, 30)
    delta_cita = timedelta(minutes=duracion_minutos)
    
    try:
        inicio_jornada = datetime.strptime(f"{fecha} 08:00:00", "%Y-%m-%d %H:%M:%S")
        fin_jornada = datetime.strptime(f"{fecha} 18:00:00", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return []

    try:
        cursor = connection.cursor(dictionary=True)
        
        # 1. Obtener todos los médicos activos
        cursor.execute("SELECT id FROM medicos WHERE estado = 'Activo'")
        medicos = [m['id'] for m in cursor.fetchall()]
        if not medicos:
            return []

        # 2. Obtener todas las citas que ocupan espacio (Aceptadas y Completadas)
        query = """
            SELECT fecha_hora, motivo 
            FROM citas 
            WHERE DATE(fecha_hora) = %s AND estado IN ('Aceptada', 'Completado')
            ORDER BY fecha_hora ASC
        """
        cursor.execute(query, (fecha,))
        todas_citas = cursor.fetchall()
        
        # 3. Mapear intervalos ocupados globalmente
        ocupados = []
        for c in todas_citas:
            inicio = c['fecha_hora']
            if isinstance(inicio, str):
                inicio = datetime.strptime(inicio, "%Y-%m-%d %H:%M:%S")
            dur = DURATIONS.get(c['motivo'], 30)
            fin = inicio + timedelta(minutes=dur)
            ocupados.append((inicio, fin))
            
        # 4. Generar huecos disponibles
        huecos_disponibles = []
        actual = inicio_jornada
        
        while actual + delta_cita <= fin_jornada:
            fin_propuesto = actual + delta_cita
            
            # Verificamos si este intervalo solapa con CUALQUIER cita de la clínica
            hay_solape = False
            for (o_inicio, o_fin) in ocupados:
                if actual < o_fin and fin_propuesto > o_inicio:
                    hay_solape = True
                    break
            
            if not hay_solape:
                huecos_disponibles.append(actual.strftime("%H:%M:%S"))
            
            actual += timedelta(minutes=30)
            
        return huecos_disponibles
    except Exception as e:
        logger.error(f"Error al calcular huecos: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_latest_report_by_patient(paciente_id: int) -> Optional[Dict[str, Any]]:
    """Obtiene el último informe médico de un paciente específico."""
    connection = get_db_connection()
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT ip.*, DATE_FORMAT(c.fecha_hora, '%d/%m/%Y %H:%i') as fecha_cita, m.nombre as medico_nombre
            FROM informe_paciente ip
            JOIN citas c ON ip.cita_id = c.id
            JOIN medicos m ON c.medico_id = m.id
            WHERE ip.paciente_id = %s
            ORDER BY c.fecha_hora DESC
            LIMIT 1
        """
        cursor.execute(query, (paciente_id,))
        return cursor.fetchone()
    except Exception as e:
        logger.error(f"Error al obtener el último informe: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_doctor(medico_id: int, data: Dict[str, Any]) -> bool:
    """Actualiza los datos de un médico y su usuario asociado."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # 1. Obtener usuario_id
        cursor.execute("SELECT usuario_id FROM medicos WHERE id = %s", (medico_id,))
        res = cursor.fetchone()
        if not res: return False
        usuario_id = res[0] if isinstance(res, tuple) else res.get('usuario_id')
        
        # 2. Actualizar email y contraseña (si se proporciona)
        if data.get('password'):
            cursor.execute(
                "UPDATE usuarios SET email = %s, password_hash = %s WHERE id = %s",
                (data['email'], data['password'], usuario_id)
            )
        else:
            cursor.execute(
                "UPDATE usuarios SET email = %s WHERE id = %s",
                (data['email'], usuario_id)
            )
            
        # 3. Actualizar médico
        cursor.execute(
            "UPDATE medicos SET nombre = %s, especialidad = %s, estado = %s WHERE id = %s",
            (data['nombre'], data['especialidad'], data['estado'], medico_id)
        )
        
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error al actualizar médico: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_doctor(medico_id: int) -> bool:
    """Elimina un médico y su usuario asociado."""
    connection = get_db_connection()
    if not connection:
        return False
    try:
        connection.start_transaction()
        cursor = connection.cursor()
        
        # 1. Obtener usuario_id
        cursor.execute("SELECT usuario_id FROM medicos WHERE id = %s", (medico_id,))
        res = cursor.fetchone()
        if not res: return False
        usuario_id = res[0] if isinstance(res, tuple) else res.get('usuario_id')
        
        # 2. Eliminar médico y luego usuario
        cursor.execute("DELETE FROM medicos WHERE id = %s", (medico_id,))
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error al eliminar médico: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
