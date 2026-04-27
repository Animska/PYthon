from typing import Optional, Dict, Any, List
import logging
from .database import get_db_connection

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
        query = """
            INSERT INTO citas (paciente_id, medico_id, fecha_hora, motivo, sintomas, prioridad_alta)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['paciente_id'],
            data['medico_id'],
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
