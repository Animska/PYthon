# Crea una función llamada contar_dias_laborales, con parámetros de entrada
# fecha_inicio y fecha_fin que cuente los días laborales (no fin de semana) entre dos
# fechas
from datetime import datetime, timedelta

def contar_dias_laborales(fecha_inicio, fecha_final):
    if fecha_inicio > fecha_final:
        fecha_inicio, fecha_final = fecha_final, fecha_inicio

    dias_laborales = 0
    fecha_actual = fecha_inicio

    while fecha_actual <= fecha_final:
        if fecha_actual.weekday() < 5:
            dias_laborales += 1
        fecha_actual += timedelta(days=1)

    return dias_laborales


# Prueba
inicio = datetime(2025, 12, 1)
fin = datetime(2025, 12, 31)
dias_laborables = contar_dias_laborales(inicio, fin)
print(f"Días laborables en diciembre: {dias_laborables}")
