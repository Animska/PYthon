from mysql.connector import Error
from connection import obtener_conexion, cerrar_conexion

def insertar_libro(titulo: str, autor: str, año: int, precio: float) -> int | None:
    """
    Inserta un nuevo libro y devuelve el id generado por AUTO_INCREMENT.
    Devuelve None si la operación falla.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO libro (titulo, autor, año, precio)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (titulo, autor, año, precio))
        conexion.commit()
        nuevo_id = cursor.lastrowid
        print(f"Libro insertado con id={nuevo_id}.")
        return nuevo_id
    except Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error al insertar. Transacción revertida. Detalle: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)

def actualizar_precio(libro_id: int, nuevo_precio: float) -> bool:
    """
    Actualiza el precio de un libro.
    Devuelve True si se modificó alguna fila, False en caso contrario.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE libro SET precio = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_precio, libro_id))
        conexion.commit()
        if cursor.rowcount:
            print(f"Precio actualizado (filas afectadas: {cursor.rowcount}).")
            return True
        else:
            print(f"No existe ningún libro con id={libro_id}.")
            return False
    except Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error al actualizar. Transacción revertida. Detalle: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)

def eliminar_libro(libro_id: int) -> bool:
    """
    Elimina un libro por su id.
    Devuelve True si se eliminó, False si no existía o hubo error.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM libro WHERE id = %s"
        cursor.execute(sql, (libro_id,))
        conexion.commit()
        if cursor.rowcount:
            print(f"Libro con id={libro_id} eliminado correctamente.")
            return True
        else:
            print(f"No existe ningún libro con id={libro_id}.")
            return False
    except Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error al eliminar. Transacción revertida. Detalle: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)

def demo_rollback_explicito():
    """
    Ilustra el comportamiento del rollback de forma deliberada:
    inserta un libro sin hacer commit y después revierte la transacción.
    Al final el libro no debe existir en la base de datos.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO libro (titulo, autor, año, precio) VALUES (%s, %s, %s, %s)",
            ("Libro temporal", "Autor Demo", 2024, 9.99)
        )
        # Dentro de la misma transacción el registro ya es visible
        cursor.execute("SELECT id, titulo FROM libro WHERE titulo = 'Libro temporal'")
        fila = cursor.fetchone()
        print(f"Dentro de la transacción, el libro existe: {fila}")
        
        # Revertimos intencionalmente sin hacer commit
        conexion.rollback()
        print("Rollback ejecutado.")
        
        # El registro ha desaparecido por completo
        cursor.execute("SELECT id, titulo FROM libro WHERE titulo = 'Libro temporal'")
        fila = cursor.fetchone()
        print(f"Tras el rollback, el libro existe: {fila}")  # None esperado
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)

if __name__ == "__main__":
    print("=== INSERT ===")
    nuevo_id = insertar_libro("Design Patterns", "Gang of Four", 1994, 48.50)
    
    print("\n=== UPDATE ===")
    if nuevo_id:
        actualizar_precio(nuevo_id, 44.00)
    
    print("\n=== DELETE ===")
    if nuevo_id:
        eliminar_libro(nuevo_id)
        
    print("\n=== DEMO rollback explícito ===")
    demo_rollback_explicito()