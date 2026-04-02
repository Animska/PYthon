from checks import cpu_met, disk_met, memory_met, temperatures_met, net_met
from pathlib import Path
import datetime
import requests

# CONSTANTES de telegram
TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""

def enviar_telegram(mensaje):
    """Envía un mensaje de texto a un chat de Telegram mediante la API de Bots."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': mensaje,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Error enviando a Telegram: {e}")
        return False
    
BASE_DIR = Path(__file__).resolve().parent
directorio_logs = Path(BASE_DIR / "Logs")


def control_cpu(log=False, umbral=80, verbose=False):
    data = cpu_met()
    if data['CPU_usage'] > umbral:
        msg = f"⚠️ *AVISO CPU*: El uso actual es del {data['CPU_usage']}% (Umbral: {umbral}%)"
        enviar_telegram(msg)
        if verbose: print(msg)
    if log:
        logging(data,'cpu')
    return data

def control_disk(log=False, umbral=80, verbose=False):
    data = disk_met()
    if data["percent"] > umbral:
        msg = f"💽 *AVISO DISCO*: Espacio ocupado al {data['percent']}%"
        enviar_telegram(msg)
    if log:
        logging(data,'disk')
    return data

def control_memory(log=False, umbral=80, verbose=False):
    data = memory_met()
    ram_pct = data["ram_usage_percent"]
    swap_pct = data["swap_usage_percent"]
     
    if ram_pct > umbral or swap_pct > umbral:
        msg = f"🚨 *AVISO MEMORIA*: RAM al {ram_pct}% y SWAP al {swap_pct}%"
        enviar_telegram(msg)
        if verbose: print(msg)

    if log:
        logging(data,'memory')
    return data

def control_temperatures(log=False, umbral=40):
    data = temperatures_met()
    for sensor, valor in data.items():
        if valor > umbral:
            msg = f"🔥 *AVISO TEMP*: Sensor {sensor} a {valor}ºC (Máx: {umbral}ºC)"
            enviar_telegram(msg)

    if log:
        logging(data,'temperatures')
    return data

def control_net(log=False, puertos=[]):
    data = net_met()
    data['open_ports'] = [p for p in data['open_ports'] if p not in puertos]
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