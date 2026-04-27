import logging
import mysql.connector
from mysql.connector import Error
from .config import settings

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_server_connection():
    """Establece conexión al servidor MySQL sin especificar la base de datos."""
    try:
        connection = mysql.connector.connect(
            host=settings.db_host,
            user=settings.db_user,
            password=settings.db_password,
            port=settings.db_port
        )
        if connection.is_connected():
            return connection
    except Error as e:
        logger.error(f"Error al conectar al servidor MySQL: {e}")
        return None

def initialize_database():
    """Crea la base de datos si no existe."""
    connection = get_server_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.db_name}")
            logger.info(f"Base de datos '{settings.db_name}' verificada/creada exitosamente.")
            cursor.close()
        except Error as e:
            logger.error(f"Error al inicializar la base de datos: {e}")
        finally:
            connection.close()

def get_db_connection():
    """Devuelve una conexión a la base de datos de la clínica."""
    try:
        connection = mysql.connector.connect(
            host=settings.db_host,
            database=settings.db_name,
            user=settings.db_user,
            password=settings.db_password,
            port=settings.db_port
        )
        if connection.is_connected():
            return connection
    except Error as e:
        logger.error(f"Error al conectar a la base de datos '{settings.db_name}': {e}")
        return None
