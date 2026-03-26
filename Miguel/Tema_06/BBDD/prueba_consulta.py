from typing import Any
from mysql.connector import Error
from connection import obtener_conexion, cerrar_conexion

def listar_libros_sin_filtro():
    """
    SELECT sin parámetros: recupera toda la tabla.
    cursor.execute() recibe únicamente la cadena SQL.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT id, titulo, autor, precio FROM libro"
        cursor.execute(sql)
        libros: list[Any] = cursor.fetchall()
        print(f"Total de libros: {len(libros)}")
        for libro in libros:
            print(f" [{libro['id']}] {libro['titulo']}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
            cerrar_conexion(conexion)

def buscar_libros_por_autor(autor: str):
    """ 
    SELECT con un parámetro: filtra por autor.
    La tupla de un solo elemento requiere la coma final: (valor,)
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT id, titulo, autor, precio FROM libro WHERE autor LIKE %s"
        cursor.execute(sql, (f"%{autor}%",))
        libros = cursor.fetchall()
        if not libros:
            print(f"No se encontraron libros del autor '{autor}'.")
            return
        
        for libro in libros:
            print(f"[{libro['id']}] {libro['titulo']} — {libro['autor']} "
            f"({libro['precio']:.2f} €)")
    except Error as e:
        print(f"Error en la búsqueda: {e}")
    finally:
        if cursor:
            cursor.close()
            cerrar_conexion(conexion)

def buscar_libros_por_rango_de_precio(precio_min: float, precio_max: float):
    """
    SELECT con dos parámetros: filtra por rango de precio.
    Los %s se sustituyen en el orden en que aparecen en la tupla.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = """
            SELECT id, titulo, autor, precio
            FROM libro
            WHERE precio >= %s AND precio <= %s
            ORDER BY precio ASC
        """
        cursor.execute(sql, (precio_min, precio_max))
        libros: list[Any] = cursor.fetchall()
        if not libros:
            print(f"No hay libros entre {precio_min:.2f} € y {precio_max:.2f} €.")
            return
        print(f"Libros entre {precio_min:.2f} € y {precio_max:.2f} €:")
        for libro in libros:
            print(f" [{libro['id']}] {libro['titulo']} {libro['precio']} €")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
            cerrar_conexion(conexion)

def buscar_libro_por_id(libro_id: int):
    """
    SELECT por clave primaria: como máximo devuelve una fila.
    fetchone() es la elección natural en este caso.
    """
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT id, titulo, autor, año, precio FROM libro WHERE id = %s"
        cursor.execute(sql, (libro_id,))
        libro = cursor.fetchone()
        if libro:
            print(f"Libro encontrado: {libro}")
        else:
            print(f"No existe ningún libro con id={libro_id}.")
    except Error as e:
        print(f"Error al buscar el libro: {e}")
    finally:
        if cursor:
            cursor.close()
            cerrar_conexion(conexion)

if __name__ == "__main__":
    print("=== SELECT sin parámetros ===")
    listar_libros_sin_filtro()

    print("\n=== SELECT con un parámetro: autor 'Martin' ===")
    buscar_libros_por_autor("Martin")

    print("\n=== SELECT con dos parámetros: precio entre 30 € y 50 € ===")
    buscar_libros_por_rango_de_precio(30.00, 50.00)
    
    print("\n=== SELECT por clave primaria: id=2 ===")
    buscar_libro_por_id(2)