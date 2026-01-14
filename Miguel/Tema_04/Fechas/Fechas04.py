# Ejercicio 4 – Dias hasta Enero
# Crea un programa que:
# 1. Pida al usuario una fecha de evento (DD/MM/YYYY)
# 2. Calcule cuántos días faltan para ese evento
# 3. Si el evento ya pasó, mostrar "El evento ya ocurrió hace X días"
# 4. Si el evento es hoy, mostrar "¡El evento es hoy!"
# 5. Si el evento es en el futuro, mostrar "Faltan X días para el event

from datetime import datetime

# Ejercicio 4 – Días hasta evento
def dias_hasta_evento():
    # 1. Pedir fecha al usuario
    fecha_str = input("Introduce la fecha del evento (DD/MM/YYYY): ")

    # 2. Convertir a datetime
    evento = datetime.strptime(fecha_str, "%d/%m/%Y")  # [web:21]
    hoy = datetime.now()  # [web:23]

    # Nos quedamos solo con la parte de fecha (sin hora)
    evento = evento.date()
    hoy = hoy.date()

    # 2. Calcular diferencia en días
    diferencia = (evento - hoy).days  # [web:22]

    # 3, 4 y 5. Mostrar mensaje según el caso
    if diferencia < 0:
        print(f"El evento ya ocurrió hace {-diferencia} días")
    elif diferencia == 0:
        print("¡El evento es hoy!")
    else:
        print(f"Faltan {diferencia} días para el evento")

# Llamar a la función principal
dias_hasta_evento()
