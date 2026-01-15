from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
directorio_logs = Path(BASE_DIR / "Logs")

def registar_logs(mensaje):
    directorio_logs.mkdir(exist_ok=True)
    fecha = datetime.now()
    fecha_log = f"app_{fecha.year}-{fecha.month}-{fecha.day}.log"
    fichero = directorio_logs / fecha_log
    with fichero.open("a", encoding="utf-8") as f:
        f.write(fecha.strftime(f"[%Y-%m-%d %H:%M:%S] {mensaje}\n"))

    return f"Fichero {fecha_log} creado"



def eliminar_logs(num_dias):
    if not directorio_logs.exists():
        return "No existe un directorio de Logs"
    
    for archivo in directorio_logs.glob("app_*.log"):
        fecha_str = archivo.stem.replace("app_", "")
        fecha_archivo = datetime.strptime("fecha_str","%Y-%m-%d")
        diferencia_dias =(datetime.now() - fecha_archivo).days

        if diferencia_dias > num_dias:
            archivo.unlink()
            print(f"Log eliminado: {archivo.name} con {diferencia_dias} de antigüedad.")

print(registar_logs('Inicio de sesion'))
print(registar_logs('Baneo de 4000 usuarios'))
eliminar_logs(3)