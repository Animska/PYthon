# Escribe una función calcular_edad(fecha_nacimiento) que:
# 1. Reciba una fecha de nacimiento como string en formato DD/MM/YYYY
# 2. La convierta a objeto datetime
# 3. Calcule la edad actual en años
# 4. Devuelva un mensaje: "Tienes X años"
# 5. Indique si es mayor o menor de edad

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    # 1 y 2. Convertir string DD/MM/YYYY a datetime
    nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")  # [web:12]

    # 3. Calcular edad en años (exacta considerando si ya cumplió años este año)
    hoy = datetime.now()  # [web:14]
    edad = hoy.year - nacimiento.year - (
        (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)
    )  # [web:14]

    # 4. Mensaje con la edad
    mensaje_edad = f"Tienes {edad} años"

    # 5. Indicar si es mayor o menor de edad
    if edad >= 18:
        mensaje_mayoria = "Eres mayor de edad"
    else:
        mensaje_mayoria = "Eres menor de edad"

    # Puedes devolver ambos mensajes juntos o por separado
    return f"{mensaje_edad}. {mensaje_mayoria}"

# Pruebas
print(calcular_edad("15/05/1990"))
print(calcular_edad("01/01/2010"))
print(calcular_edad("20/12/2024")) # Recién nacido cas
