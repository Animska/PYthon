from datetime import datetime,timedelta
from typing import Optional

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, fecha_publicacion: datetime) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.fecha_publicacion = fecha_publicacion

    def es_prestable(self) -> bool:
        """
        Retorna True si han pasado 180 días (6 meses) desde la publicación.
        """
        #diferencia = (datetime.now().date() - self.fecha_publicacion.date()).days
        diferencia = (datetime.now().year - self.fecha_publicacion.year) * 12 + (datetime.now().month - self.fecha_publicacion.month)
        if diferencia >= 6:
            return  True
        
        return False
    
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
        
        if fecha_prestamo is None:
            self.fecha_prestamo = datetime.now()
        else:
            self.fecha_prestamo = fecha_prestamo

        #fecha límite
        self.fecha_devolucion_limite = self.fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        
        # 5.fecha de devolucion(none por que no se ha devuelto aun)
        self.fecha_devolucion_real: Optional[datetime] = None

    def calcular_dias_retraso(self, fecha_devolucion: Optional[datetime] = None) -> int:
        """
        calcula los dias de retraso en la devolucion del libro
        Args:
            -fecha_devolucion: fecha en la que se devuelve, si es none sera la actual

        retorna el numero de dias con retraso a la fecha limite, 0 si es anterior
        a la devolucion
        """
        fecha_entrega = fecha_devolucion or datetime.now()
        diferencia = (fecha_entrega - self.fecha_devolucion_limite).days
        if diferencia <=0:
            return 0

        return diferencia
    
    def devolver_libro(self, fecha_devolucion: Optional[datetime] = None) -> dict:
        """
        Asignar fecha_devolucion al atributo fecha_devolucion_real
        Args:
            --fecha_devolucion: fecha en la que se devuelve, si es none sera la actual
        retorna un diccionario con los datos e la instancia del prestamo
        """
        fecha_entrega = fecha_devolucion or datetime.now()

        self.fecha_devolucion_real = fecha_entrega
        retraso = self.calcular_dias_retraso(fecha_entrega)
        dicc = {}
        dicc['libro'] = self.libro.titulo
        dicc['usuario'] = self.usuario
        dicc['fecha_devolucion'] = fecha_entrega
        dicc['dias_retraso'] = retraso
        dicc['multa'] = retraso * self.MULTA_RETRASO_DIA

        return dicc
    
    def __str__(self) -> str:
        if self.fecha_devolucion_real is None:
            return f"Préstamo [Devuelto] - {self.libro} - Usuario: {self.usuario} - Fecha límite: {self.fecha_devolucion_limite}"
        
        return f"Préstamo [Activo] - {self.libro} - Usuario: {self.usuario} - Fecha límite: {self.fecha_devolucion_limite}"
    
class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.prestamos_activos = []
        self.historial_prestamos = []

    def realizar_prestamo(self, libro: Libro, usuario: str) -> bool:
        """
        Añade un prestamo creado satisfactoriamente a las listas prestamos_activos
        y historial_prestamos e imprime la fecha limite

        Args:
            libro: instancia de libro para el prestamo
            usuario: usuario que realiza el prestamo

        Retorna un bool si se ha podido crear y añadir el prestamo
        """
        try:
            prestamo = Prestamo(libro,usuario)
            self.prestamos_activos.append(prestamo)
            self.historial_prestamos.append(prestamo)
            print(f"EXITO! Tienes hasta el {prestamo.fecha_devolucion_limite} para devolverlo")
            return True
        except ValueError as e:
                print(f"ERROR {e}")
                return False
        
    def devolver_libro(self, isbn: str, fecha_devolucion: Optional[datetime] = None) ->Optional[dict]:
        """
        Busca el prestamo en la lista de prestamos y lo elimina de la lista
        Args:
            -isbn: ISBN del libro que esta en el prestamo
            -fecha_devolucion: fecha donde se hizo la devolucion del prestamo

        Retorna un diccionario con los datos de la devolucion
        """
        fecha_entrega = fecha_devolucion or datetime.now()
        prestamo = None
        for prestamo_activo in self.prestamos_activos:
            if prestamo_activo.libro.isbn == isbn:
                prestamo = prestamo_activo
                break

        if prestamo:
            datos_prestamo = prestamo.devolver_libro(fecha_entrega)
            self.prestamos_activos.remove(prestamo)
            return datos_prestamo
        
        return None
        
    def listar_prestamos_activos(self) -> None:
        """
        Lista prestamos activos dentro de la lista de prestamos activos
        
        :
        """
        if len(self.prestamos_activos) == 0:
            print("No hay préstamos actvos")
            return
        
        print('-'*20)
        print(f"{self.nombre:^20}")
        print('-'*20)
        for prestamo_act in self.prestamos_activos:
            retraso = prestamo_act.calcular_dias_retraso()
            if retraso > 0:
                warning="¡AVISO!"
                multa= retraso * prestamo_act.MULTA_RETRASO_DIA
            else:
                warning=""
                multa=0
            print(f"{prestamo_act} |{retraso}|{warning}|{multa}")
            
    def generar_estadis2cas(self) -> dict:
        dicc_prestamos={}
        dicc_prestamos['total_prestamos'] = len(self.historial_prestamos)
        dicc_prestamos['prestamos_activos'] = len(self.prestamos_activos)
        dicc_prestamos['prestamos_completaso']
        dicc_prestamos['']

        return dicc_prestamos

        
        
    

