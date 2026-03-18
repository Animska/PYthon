from control import control_cpu, control_disk, control_memory, control_temperatures, control_net
import time
from datetime import datetime, timedelta

def main():
    datetime_ultimo_log = datetime.now()
    
    print("Iniciando monitorización cada 30 segundos...")

    while True:
        datetime_actual = datetime.now()

        # 2. Comprobamos si la diferencia es mayor o igual a 30 segundos
        if (datetime_actual - datetime_ultimo_log).total_seconds() >= 30:
            control_cpu(True)
            control_disk(True)
            control_memory(True)
            control_temperatures(True)
            control_net(True)
            
            datetime_ultimo_log = datetime_actual
            print(f"Log generado a las: {datetime_actual.strftime('%H:%M:%S')}")
        else:
            control_cpu()
            control_disk()
            control_memory()
            control_temperatures()
            control_net()
        # Un pequeño descanso para no saturar el procesador con el bucle while
        time.sleep(1)

if __name__ == '__main__':
    main()