import heapq

class GestorIncidencias:
    def __init__(self):
        # Listas para los heaps (colas de prioridad)
        self.cola_software = []
        self.cola_hardware = []
        # Conjunto para control de unicidad (tipo, descripción)
        self.pendientes = set()
        # Diccionario para el historial de tareas completadas
        self.historico = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    def agregar_incidencia(self, prioridad, tipo, descripcion):
        tipo = tipo.lower()
        id_unico = (tipo, descripcion)

        if id_unico in self.pendientes:
            print(f"Error: La tarea '{descripcion}' de tipo '{tipo}' ya esta pendiente.")
        
        else:
            # La tupla (prioridad, descripcion) permite a heapq ordenar por urgencia
            tarea = (prioridad, descripcion)
            
            if tipo == "software":
                heapq.heappush(self.cola_software, tarea)
            elif tipo == "hardware":
                heapq.heappush(self.cola_hardware, tarea)

            self.pendientes.add(id_unico)
            print(f"Incidencia añadida: [Nivel: '{prioridad}', Tipo: '{tipo}', Descripción: '{descripcion}']")

    def atender_siguiente(self, tipo):
        tipo = tipo.lower()
        # Obtenemos la cola según el tipo
        if tipo == "software":
            cola = self.cola_software
        elif tipo == "hardware":
            cola = self.cola_hardware
        else:
            print("Tipo no compatible")
            return None

        if not cola:
            print(f"No hay tareas pendientes en la cola de tipo '{tipo}'")
            return None

        # Extraer la tarea con menor numero de prioridad (mas urgente)
        prioridad, descripcion = heapq.heappop(cola)
        print(f"ATENDIENDO: [Nivel: '{prioridad}', Tipo: '{tipo}', Descripción: '{descripcion}']")
        
        # Actualizamos el conjunto de pendientes (tipo, descripción)
        self.pendientes.remove((tipo, descripcion))
        # Actualizamos el histórico según prioridad
        self.historico[prioridad] += 1
        
        
    

    def ver_proxima(self, tipo):
        tipo = tipo.lower()
        # Obtenemos la cola según el tipo
        if tipo == "software":
            cola = self.cola_software
        elif tipo == "hardware":
            cola = self.cola_hardware
        else:
            print("Tipo no compatible")
            return None

        if not cola:
            print(f"No hay tareas pendientes en la cola de tipo '{tipo}'")
            return None

        # El elemento mas pequeño siempre esta en el indice 0
        prioridad, descripcion = cola[0]
        print(f"PRÓXIMA EN COLA {tipo}: [Nivel: '{prioridad}', Descripción: '{descripcion}']")

    def resumen_estadistico(self):
        print("\n--- RESUMEN DE TAREAS COMPLETADAS ---")
        for prioridad, num in self.historico.items():
            print(f"Prioridad {prioridad}: {num} tareas")
        print("-------------------------------------\n")

# --- Prueba del sistema ---
def main():
    gestor = GestorIncidencias()

    # 1. Agregar incidencias
    gestor.agregar_incidencia(2, "software", "Error de base de datos")
    gestor.agregar_incidencia(1, "software", "Servidor caido")
    gestor.agregar_incidencia(3, "hardware", "Cambio de disco duro")
    gestor.agregar_incidencia(1, "hardware", "Fallo de alimentacion")
    
    # Intento de duplicado
    gestor.agregar_incidencia(5, "software", "Error de base de datos")

    # 2. Ver proximas
    gestor.ver_proxima("software")
    gestor.ver_proxima("hardware")

    # 3. Atender tareas
    gestor.atender_siguiente("software") # Deberia atender 'Servidor caido' (Prio 1)
    gestor.atender_siguiente("software") # Deberia atender 'Error de base de datos' (Prio 2)
    gestor.atender_siguiente("hardware") # Deberia atender 'Fallo de alimentacion' (Prio 1)

    # 4. Mostrar estadisticas
    gestor.resumen_estadistico()

if __name__ == "__main__":
    main()