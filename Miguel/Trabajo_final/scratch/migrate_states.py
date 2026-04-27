import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def migrate():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "clinica_funeraria")
        )
        cursor = conn.cursor()
        print("Cambiando ENUM de estado en la tabla citas...")
        cursor.execute("ALTER TABLE citas MODIFY COLUMN estado ENUM('Pendiente', 'Aceptada', 'Rechazada', 'Completado', 'Cancelado') DEFAULT 'Pendiente';")
        conn.commit()
        print("Migración completada exitosamente.")
    except Exception as e:
        print(f"Error durante la migración: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    migrate()
