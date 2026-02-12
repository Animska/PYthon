import requests
from pathlib import Path
import json

def generar_estadisticas():
    URL_API = "http://16.171.21.119:8000/alumnos"
    BASE_DIR = Path(__file__).resolve().parent
    FILE_DATA = Path(BASE_DIR / "estadisticas.json")

    try:
        #Conexion a API
        response = requests.get(URL_API)
        response.raise_for_status()
        data = response.json()
        alumnos = data.get("alumnos", [])

        estadis_alumnos = []
        cursos_data = {} # { "DAW": [lista_de_medias], ... }

        #Procesamiento de datos por alumno
        for alu in alumnos:
            nombre_completo = f"{alu['nombre']} {alu['apellidos']}"
            # Calculamos la media del alumno
            media_alu = round((alu['nota1'] + alu['nota2']) / 2, 2)
                
            # Guardamos para el JSON
            estadis_alumnos.append({
                "nombre": alu['nombre'],
                "apellidos": alu['apellidos'],
                "nota_media": media_alu
            })

            curso = alu['curso']
            if curso not in cursos_data:
                cursos_data[curso] = []
            cursos_data[curso].append(media_alu)
        
            print(f" {nombre_completo}: nota media = {media_alu}")

        #Procesamiento de datos por curso
        estadis_cursos = []
        print("--- Estadísticas por curso ---")
        for curso, medias in cursos_data.items():
            num_alumnos = len(medias)
            media_curso = round(sum(medias) / num_alumnos, 2)
                
            estadis_cursos.append({
                "curso": curso,
                "nota_media_curso": media_curso,
                "num_alumnos": num_alumnos
            })
                
            print(f" {curso}: nota media = {media_curso} ({num_alumnos} alumnos)")

        #Guardar en fichero JSON
            resultado_final = {
                "estadisticas_alumnos": estadis_alumnos,
                "estadisticas_cursos": estadis_cursos
            }
            
            with open(FILE_DATA, "w", encoding="utf-8") as f:
                json.dump(resultado_final, f, indent=4, ensure_ascii=False)
                
            print("Estadísticas guardadas en estadisticas.json")

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    generar_estadisticas()