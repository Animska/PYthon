from datetime import datetime, timedelta
from clases import Biblioteca, Libro, Prestamo

def main():
    """Función principal de prueba del sistema."""

    # 1. Configuración inicial
    biblioteca = Biblioteca("Biblioteca Municipal Central")

    print(f"\n{'='*80}")
    print(f"SISTEMA DE GESTIÓN - {biblioteca.nombre}")
    print(f"{'='*80}\n")

    # 2. Creación de catálogo
    libro1 = Libro(
        "Clean Code",
        "Robert C. Martin",
        "978-0132350884",
        datetime(2023, 1, 15)  # Más de 6 meses
    )

    libro2 = Libro(
        "Python Crash Course",
        "Eric Matthes",
        "978-1593279288",
        datetime(2024, 11, 1)  # Menos de 6 meses
    )

    libro3 = Libro(
        "The Pragmatic Programmer",
        "David Thomas",
        "978-0201616224",
        datetime(2022, 5, 20)  # Más de 6 meses
    )

    # 3. Gestión de préstamos
    print("--- REALIZANDO PRÉSTAMOS ---\n")
    biblioteca.realizar_prestamo(libro1, "Ana García")
    biblioteca.realizar_prestamo(libro2, "Carlos López")  # Debería dar error por fecha
    biblioteca.realizar_prestamo(libro3, "María Rodríguez")

    print("\n")
    biblioteca.listar_prestamos_activos()

    # 4. Procesar devoluciones
    print("\n--- DEVOLUCIÓN A TIEMPO ---")
    fecha_devolucion_a_tiempo = datetime.now() + timedelta(days=10)
    info_dev = biblioteca.devolver_libro("978-0132350884", fecha_devolucion_a_tiempo)
    
    if info_dev:
        print(f"Libro: {info_dev['libro']}")
        print(f"Usuario: {info_dev['usuario']}")
        print(f"Días de retraso: {info_dev['dias_retraso']}")
        print(f"Multa: {info_dev['multa']:.2f}€\n")

    print("--- DEVOLUCIÓN CON RETRASO ---")
    fecha_devolucion_tarde = datetime.now() + timedelta(days=20)
    info_dev_tarde = biblioteca.devolver_libro("978-0201616224", fecha_devolucion_tarde)
    
    if info_dev_tarde:
        print(f"Libro: {info_dev_tarde['libro']}")
        print(f"Usuario: {info_dev_tarde['usuario']}")
        print(f"Días de retraso: {info_dev_tarde['dias_retraso']}")
        print(f"Multa: {info_dev_tarde['multa']:.2f}€\n")

    # 5. Reporte final
    print("--- ESTADÍSTICAS DE LA BIBLIOTECA ---")
    stats = biblioteca.generar_estadisticas()
    print(f"Total de préstamos realizados: {stats['total_prestamos']}")
    print(f"Préstamos activos:             {stats['prestamos_activos']}")
    print(f"Préstamos completados:         {stats['prestamos_finalizados']}")
    print(f"Préstamos con retraso:         {stats['prestamos_con_retraso']}")
    print(f"\n{'='*80}\n")

if __name__ == "__main__":
    main()