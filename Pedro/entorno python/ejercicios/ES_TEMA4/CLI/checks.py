import psutil

def cpu_met():
    return {
        "CPU_usage" : psutil.cpu_percent(interval=None)
        }

def disk_met(path="/"):
    disk = psutil.disk_usage(path)
    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "used_gb": round(disk.used / (1024**3), 2),
        "free_gb": round(disk.free / (1024**3), 2),
        "percent": disk.percent
    }

def memory_met():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    # Fórmula de ratio: Relación entre uso de Swap y RAM
    # Un valor alto indica que el sistema depende demasiado del disco
    swap_threshold_ratio = (swap.percent / mem.percent) if mem.percent > 0 else 0
    
    return {
        "ram_total_gb" : round(mem.total / (1024**3), 2),
        "ram_usage_percent" : mem.percent,
        "swap_usage_percent" : swap.percent,
        "pressure_warning" : mem.percent > 85 and swap.percent > 10,
        "swap_ratio" : round(swap_threshold_ratio, 2)
    }

def temperatures_met():
    temps = psutil.sensors_temperatures()
    if not temps:
        return {} # Es mejor devolver un dict vacío que un error aquí
    
    resumen_temps = {}
    for name, entries in temps.items():
        if entries:
            # Tomamos solo la temperatura de la primera entrada (.current)
            resumen_temps[name] = entries[0].current 
    return resumen_temps

def net_met():
    connections = psutil.net_connections(kind='inet')
    stats = {
        "total_connections": len(connections),
        "open_ports": []
    }
    
    for conn in connections:
        if conn.status == 'LISTEN':
            stats["open_ports"].append(conn.laddr.port)
        
    return stats


print(disk_met())