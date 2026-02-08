from datetime import datetime, timedelta
from typing import Optional

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, fecha_publicacion: datetime) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.fecha_publicacion = fecha_publicacion

    def es_prestable(self) -> bool:
        """
        Retorna True si han pasado al menos 180 días desde la publicación.
        """
        # Es más preciso usar días totales para evitar errores de fin de mes
        diferencia = (datetime.now() - self.fecha_publicacion).days
        return diferencia >= 180
    
    def __str__(self) -> str:
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"

class Prestamo:
    DIAS_PRESTAMO = 15
    MULTA_RETRASO_DIA = 0.50

    def __init__(self, libro: Libro, usuario: str, fecha_prestamo: Optional[datetime] = None) -> None:
        if not libro.es_prestable():
            raise ValueError(f"El libro '{libro.titulo}' no es prestable: requiere más de 6 meses de antigüedad.")
        
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo or datetime.now()
        self.fecha_devolucion_limite = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        self.fecha_devolucion_real: Optional[datetime] = None

    def calcular_dias_retraso(self, fecha_devolucion: Optional[datetime] = None) -> int:
        fecha_entrega = fecha_devolucion or datetime.now()
        diferencia = (fecha_entrega - self.fecha_devolucion_limite).days
        return max(0, diferencia) # Retorna 0 si no hay retraso
    
    def devolver_libro(self, fecha_devolucion: Optional[datetime] = None) -> dict:
        fecha_entrega = fecha_devolucion or datetime.now()
        self.fecha_devolucion_real = fecha_entrega
        retraso = self.calcular_dias_retraso(fecha_entrega)
        
        return {
            'libro': self.libro.titulo,
            'usuario': self.usuario,
            'fecha_devolucion': fecha_entrega,
            'dias_retraso': retraso,
            'multa': retraso * self.MULTA_RETRASO_DIA
        }
    
    def __str__(self) -> str:
        # CORREGIDO: Si real es None, el préstamo sigue activo.
        estado = "[ACTIVO]" if self.fecha_devolucion_real is None else "[DEVUELTO]"
        return f"Préstamo {estado} - {self.libro} - Usuario: {self.usuario} - Límite: {self.fecha_devolucion_limite.date()}"
    
class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.prestamos_activos = []
        self.historial_prestamos = []

    def realizar_prestamo(self, libro: Libro, usuario: str) -> bool:
        try:
            prestamo = Prestamo(libro, usuario)
            self.prestamos_activos.append(prestamo)
            self.historial_prestamos.append(prestamo)
            print(f"ÉXITO! Tienes hasta el {prestamo.fecha_devolucion_limite.date()} para devolverlo")
            return True
        except ValueError as e:
            print(f"ERROR: {e}")
            return False
        
    def devolver_libro(self, isbn: str, fecha_devolucion: Optional[datetime] = None) -> Optional[dict]:
        prestamo = next((p for p in self.prestamos_activos if p.libro.isbn == isbn), None)

        if prestamo:
            datos_prestamo = prestamo.devolver_libro(fecha_devolucion)
            self.prestamos_activos.remove(prestamo)
            return datos_prestamo
        
        print("No se encontró un préstamo activo con ese ISBN.")
        return None
        
    def listar_prestamos_activos(self) -> None:
        if not self.prestamos_activos:
            print("No hay préstamos activos.")
            return
        
        print('-' * 40)
        print(f"{self.nombre:^40}")
        print('-' * 40)
        for p in self.prestamos_activos:
            retraso = p.calcular_dias_retraso()
            aviso = "¡AVISO!" if retraso > 0 else ""
            multa = retraso * p.MULTA_RETRASO_DIA
            print(f"{p} | Retraso: {retraso}d | {aviso} Multa: ${multa:.2f}")

    def generar_estadisticas(self) -> dict:
        # CORREGIDO: Lógica completa de estadísticas
        total = len(self.historial_prestamos)
        activos = len(self.prestamos_activos)
        total_retrasos = sum(1 for p in self.historial_prestamos if p.calcular_dias_retraso(p.fecha_devolucion_real) > 0)
        
        return {
            'total_prestamos': total,
            'prestamos_activos': activos,
            'prestamos_finalizados': total - activos,
            'prestamos_con_retraso':total_retrasos
        }

        
        
    

