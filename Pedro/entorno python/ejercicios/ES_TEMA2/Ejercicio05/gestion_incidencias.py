from collections import namedtuple
from collections import defaultdict
import heapq

Incidencia = namedtuple('Incidencia', ['prioridad', 'tipo', 'descripcion'])

class GestorIncidencias:
    def __init__(self):
        self._software = []
        self._hardware = []     
        self._incidencias_pendientes = set()
        self._historico = defaultdict(int)
    
    def agregar_incidencia(self, prioridad, tipo, descripcion):
        incidencia = Incidencia(prioridad, tipo.lower(), descripcion)
        if incidencia in self._incidencias_pendientes:
            print('Esta incidencia ya esta en pendientes')
            return None
        
        if tipo == 'software':
            heapq.heappush(self._software, incidencia)
        elif tipo == 'hardware':
            heapq.heappush(self._hardware, incidencia)
        else:
            print("Tipo inválido")
            return False
        
        self._incidencias_pendientes.add(incidencia)
        print(f"✓ Añadida {tipo}: {descripcion} (prioridad {prioridad})")
        return True
    
    def atender_siguiente(self, cola):
        heap = self._software if cola == 'software' else self._hardware
        
        if not heap:
            print(f"No hay incidencias pendientes en {cola}")
            return None
        
        inc = heapq.heappop(heap)
    
        self._incidencias_pendientes.discard((inc.tipo, inc.descripcion))
        
        self._historico[inc.prioridad] += 1
        
        print(f"✅ Completada {cola}: {inc.descripcion} (prioridad {inc.prioridad})")
        return inc
    
    def ver_proxima(self, cola):
        heap = self._software if cola == 'software' else self._hardware
        
        if not heap:
            print(f"No hay incidencias pendientes en {cola}")
            return None
        
        inc = heap[0]  # Peek sin extraer
        print(f"⏳ Próxima {cola}: {inc.descripcion} (prioridad {inc.prioridad})")
        return inc
    
    def resumen_estadistico(self):
        print("HISTÓRICO DE TAREAS COMPLETADAS POR PRIORIDAD:")
        print("-" * 50)
        for prioridad in sorted(self._historico, reverse=True):
            print(f"Prioridad {prioridad}: {self._historico[prioridad]} tareas")
        print(f"Total: {sum(self._historico.values())} tareas")


gestor = GestorIncidencias()


gestor.agregar_incidencia(1, 'hardware', 'Disco falla')
gestor.agregar_incidencia(3, 'software', 'Bug login')
gestor.agregar_incidencia(1, 'hardware', 'Disco falla')  # Duplicado -> rechazado


gestor.ver_proxima('hardware')
gestor.ver_proxima('software')


gestor.atender_siguiente('hardware')
gestor.resumen_estadistico()


