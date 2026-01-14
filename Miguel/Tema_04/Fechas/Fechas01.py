# Crea una función es_fin_de_semana que reciba una fecha y devuelva true si es fin de
# semana. Otra función es_dia_laborable que reciba una fecha y devuelva true si es día
# laborable.
from datetime import datetime

def es_fin_de_semana(hoy):
    if hoy.strftime("%a") in ['Sat','Sun']:
        return True
    

#Prueba
hoy = datetime.now()
if es_fin_de_semana(hoy):
    print("¡Es fin de semana!")
else:
    print("Es día laborable")