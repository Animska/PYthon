import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 1. Crea una función guardar_en_cache(ciudad, datos) que guarde datos en
# cache_{ciudad}.json. Retorna True si todo va bien y False en caso contrario.
def guardar_en_cache(ciudad:str,datos:dict)->bool:
    try:
        filename = BASE_DIR / f"cache_{ciudad}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print("\n--- Datos guardados en cache ---")
        return True   
    
    except Exception as e:
        print(f'ERROR! {e}')
    
    return False
        

# 2. Crea una función cargar_desde_cache(ciudad) que cargue datos si existen. Si
# el archivo no existe, devolver None. Debe retornar los datos de la caché.
def cargar_desde_cache(ciudad: str):
    filename = BASE_DIR / f"cache_{ciudad}.json"
    if filename.exists():  # Reemplaza os.path.isfile
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                datos_cargados = json.load(f)
                return datos_cargados
            
        except Exception as e:
            print(f'ERROR! {e}')
            
    return None

# 3. Crea la función mostrar_datos_ciudad, que reciba los datos de caché como
# parámetro de entrada y muestre los datos meteorológicos de la ciudad
def mostrar_datos_ciudad(cache_datos:dict):
    print(f"La temperatura hoy en {cache_datos['ciudad']} es de {cache_datos['temperatura']}º, hace un tiempo {cache_datos['descripcion']}")

# 4. Prueba guardando datos de Madrid y Barcelona

# 5. Verifica que puedes cargar ambos caches

if __name__ == "__main__":
    #1.-
    datos_madrid = { 'ciudad': 'Madrid', 'temperatura': 18.5, 'descripcion': 'Soleado' }
    guardar_en_cache('madrid', datos_madrid)
    #2.-
    cache = cargar_desde_cache('madrid')
    print(cache['temperatura']) # 18.5
    #3.-
    print("\n3. Mostrando datos de Madrid:")
    mostrar_datos_ciudad(cache)
    #4.-
    datos_madrid = {'ciudad': 'Madrid', 'temperatura': 18.5, 'descripcion': 'Soleado'}
    datos_barcelona = {'ciudad': 'Barcelona', 'temperatura': 20.2, 'descripcion': 'Parcialmente nublado'}
    guardar_en_cache('madrid', datos_madrid)
    guardar_en_cache('barcelona', datos_barcelona)
    #5.-
    cache_madrid = cargar_desde_cache('madrid')
    cache_barcelona = cargar_desde_cache('barcelona')

    if cache_madrid:
        print(f"Madrid cargado correctamente: {cache_madrid['temperatura']}ºC")
    else:
        print("❌ Error cargando Madrid")

    if cache_barcelona:
        print(f"Barcelona cargado correctamente: {cache_barcelona['temperatura']}ºC")
    else:
        print("❌ Error cargando Barcelona")

    print("\n=== MOSTRANDO DATOS ===")
    mostrar_datos_ciudad(cache_madrid)
    mostrar_datos_ciudad(cache_barcelona)
