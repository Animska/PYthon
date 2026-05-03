from api.database import get_db_connection

def fix_table():
    conn = get_db_connection()
    if not conn:
        print("No se pudo conectar")
        return
    try:
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE citas MODIFY medico_id INT NULL;")
        conn.commit()
        print("Tabla citas modificada: medico_id ahora es NULLABLE")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    fix_table()
