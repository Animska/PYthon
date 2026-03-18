from checks import cpu_met, disk_met, memory_met, temperatures_met, net_met
from pathlib import Path
import datetime

BASE_DIR = Path(__file__).resolve().parent
directorio_logs = Path(BASE_DIR / "Logs")


def control_cpu(log=False):
    data = cpu_met()
    if log:
        logging(data,'cpu')
    return data

def control_disk(log=False):
    data = disk_met()
    if log:
        logging(data,'disk')
    return data

def control_memory(log=False):
    data = memory_met()
    if log:
        logging(data,'memory')
    return data

def control_temperatures(log=False):
    data = temperatures_met()
    if log:
        logging(data,'temperatures')
    return data

def control_net(log=False):
    data = net_met()
    if log:
        logging(data,'net')
    return data

def logging(data,componente):
    directorio_logs.mkdir(exist_ok=True)
    # Obtenemos la fecha y hora actual para el registro
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(directorio_logs / f'{componente}_log.log', "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        for k,v in data.items():
            f.write(f'\t[{k}]: {v}\n')
        f.write('\n')


