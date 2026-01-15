#JSON a string
import json

datos_python = {
'nombre': 'Análisis Ventas Q3',
'productos': ['Software', 'Hardware', 'Servicios'],
'total_q3': 45000.75,
'activo': True
}
# Usamos dumps() para obtener la representación JSON como una CADENA de texto.
json_string = json.dumps(datos_python)
print(f"Tipo original: {type(datos_python)}")
print(f"Tipo JSON (string): {type(json_string)}")
print(json_string)