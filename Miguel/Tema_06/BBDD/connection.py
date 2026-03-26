import mysql.connector
from mysql.connector import Error
def obtener_conexion():
    """
    Devuelve una conexión activa a la base de datos MySQL.
    Lanza una excepción si la conexión no se puede establecer.
    """
    conexion = mysql.connector.connect(
        host="localhost",
        port=3307,
        database="libreria",
        user="root",
        password=""
    )
    return conexion

def cerrar_conexion(conexion):
    """
    Cierra la conexión solo si está activa.
    """
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    conexion = None
    try:
        conexion = obtener_conexion()
        print(f"Conectado al servidor MySQL "
            f"(versión: {conexion.server_info})")
    except Error as e:
        print(f"Error al conectar: {e}")
    finally:
        cerrar_conexion(conexion)