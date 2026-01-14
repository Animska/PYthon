# Ejercicio 5 – Validador de reservas
# Crea un sistema de validación de reservas de hotel:
# 1. Función validar_reserva(fecha_entrada, fecha_salida)
# 2. Verificar que fecha_entrada sea futura (al menos mañana)
# 3. Verificar que fecha_salida sea posterior a fecha_entrada
# 4. Verificar que la estancia sea mínimo 1 noche, máximo 30 noches
# 5. Calcular número de noches y precio (70€/noche entre semana, 100€/noche fin de
# semana)
# 6. Devolver diccionario con: válido (bool), mensaje (str), noches (int), precio_total
# (float)

from datetime import datetime, timedelta

PRECIO_ENTRE_SEMANA = 70
PRECIO_FIN_SEMANA = 100

def validar_reserva(fecha_entrada, fecha_salida):
    """
    fecha_entrada y fecha_salida deben ser objetos datetime.date
    o datetime (en cuyo caso se usará solo la parte de fecha).
    """
    hoy = datetime.now().date()
    
    # Asegurar que trabajamos con date (sin hora)
    if isinstance(fecha_entrada, datetime):
        fecha_entrada = fecha_entrada.date()
    if isinstance(fecha_salida, datetime):
        fecha_salida = fecha_salida.date()

    # 2. Verificar que fecha_entrada sea futura (al menos mañana)
    if fecha_entrada <= hoy:
        return {
            "valido": False,
            "mensaje": "La fecha de entrada debe ser al menos mañana.",
            "noches": 0,
            "precio_total": 0.0
        }

    # 3. Verificar que fecha_salida sea posterior a fecha_entrada
    if fecha_salida <= fecha_entrada:
        return {
            "valido": False,
            "mensaje": "La fecha de salida debe ser posterior a la fecha de entrada.",
            "noches": 0,
            "precio_total": 0.0
        }

    # 4. Verificar estancia mínima 1 noche, máxima 30 noches
    noches = (fecha_salida - fecha_entrada).days
    if noches < 1:
        return {
            "valido": False,
            "mensaje": "La estancia mínima es de 1 noche.",
            "noches": 0,
            "precio_total": 0.0
        }
    if noches > 30:
        return {
            "valido": False,
            "mensaje": "La estancia máxima es de 30 noches.",
            "noches": noches,
            "precio_total": 0.0
        }

    # 5. Calcular nº de noches y precio por tipo de día
    precio_total = 0.0
    fecha_actual = fecha_entrada

    while fecha_actual < fecha_salida:
        # weekday(): lunes=0 ... domingo=6
        if fecha_actual.weekday() < 5:  # Lunes a viernes
            precio_total += PRECIO_ENTRE_SEMANA
        else:  # Sábado y domingo
            precio_total += PRECIO_FIN_SEMANA
        fecha_actual += timedelta(days=1)

    return {
        "valido": True,
        "mensaje": "Reserva válida.",
        "noches": noches,
        "precio_total": float(precio_total)
    }

# Ejemplo de uso:
if __name__ == "__main__":
    # Entradas como strings DD/MM/YYYY
    entrada_str = "20/02/2026"
    salida_str = "25/02/2026"

    fecha_entrada = datetime.strptime(entrada_str, "%d/%m/%Y")
    fecha_salida = datetime.strptime(salida_str, "%d/%m/%Y")

    resultado = validar_reserva(fecha_entrada, fecha_salida)
    print(resultado)
