# Crea una función llamada contar_dias_laborales, con parámetros de entrada
# fecha_inicio y fecha_fin que cuente los días laborales (no fin de semana) entre dos
# fechas
from datetime import datetime

def contar_dias_laborales(fecha_inicio,fecha_final):
    




#Prueba
inicio = datetime(2025, 12, 1)
fin = datetime(2025, 12, 31)
dias_laborables = contar_dias_laborables(inicio, fin)
print(f"Días laborables en diciembre: {dias_laborables}")