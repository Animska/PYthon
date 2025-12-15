from influxdb import InfluxDBClient
import config

# --- Configuración acceso a InfluxDB ---
INFLUX_HOST = config.HOST
INFLUX_PORT = config.PORT
INFLUX_USER = config.USER
INFLUX_PASS = config.PASS 
INFLUX_DB = config.DB 

# =================================================================
# RESÚMENES DIARIOS (DÍA DE AYER COMPLETO)
# =================================================================
def diario_huerto_humedad():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Construir la consulta InfluxQL
    # Consultando datos desde hoy - 2d para obtener todos los datos del día anterior
    # Agrupamos por time(1d). 
    # Nos devolverá 3 líneas
        # Estadísticas de algunas medidas de anteayer
        # Estadísticas de todas las medidas de ayer
        # Estadísticas de algunas medidas del día actual
    query = (
        f'SELECT MEAN("value"), MIN("value"), MAX("value") FROM "%" '  
        f'WHERE "entity_id" = \'agsex_sdf_huerto_lht65n_humedad\' '
        f'AND time >= now() - 2d '
        f'GROUP BY time(1d)')

    # Ejecutar la consulta 
    result = client.query(query)
    # Guardar los puntos (filas) del resultado en una lista
    points = list(result.get_points()) 
    if not points:
        print(f"\n⚠️ No se encontraron puntos.") # Para hacer algo de loggin
        # Si no hay datos 
        return None
    else:
        # Tenemos 3 points ordenados: anteayer, ayer, hoy.
        # Los datos que deseamos son points[1]
        datos = points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos = list(datos.values())
        # Retornamos como tupla la media, máxima y mínima
        # datos[0] es la marca de tiempo, el resto de posiciones son los datos
        media = round(float(datos[1]), 1)
        min = round(float(datos[2]), 1)
        max = round(float(datos[3]), 1)
        # Devolvemos los datos en un diccionario con claves mean, min, max
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result
    
def diario_huerto_temperatura():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Construir la consulta InfluxQL
    # Es la misma que la anterior, cambiando la tabla y el entity_id
    query = (
        f'SELECT MEAN("value"), MIN("value"), MAX("value") FROM "°C" '  
        f'WHERE "entity_id" = \'agsex_sdf_huerto_lht65n_temperatura\' '
        f'AND time >= now() - 2d '
        f'GROUP BY time(1d)')

    # Ejecutar la consulta 
    result = client.query(query)
    # Guardar los puntos del resultado en una lista
    points = list(result.get_points()) 
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        # Si no hay datos 
        return None
    else:
        # Tenemos 3 points (anteayer, ayer, hoy)
        # Los datos que deseamos son points[1]
        datos = points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos = list(datos.values())
        # Retornamos como tupla la media, máxima y mínima
        # datos[0] es la marca de tiempo, el resto de posiciones son los datos
        media = round(float(datos[1]), 1)
        min = round(float(datos[2]), 1)
        max = round(float(datos[3]), 1)
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result

# TODO
# hardcodeado por motivos de prueba para comprobar que funciona en telegram
def diario_invernadero_humedad():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Construir la consulta InfluxQL
    # Consultando datos desde hoy - 2d para obtener todos los datos del día anterior
    # Agrupamos por time(1d). 
    # Nos devolverá 3 líneas
        # Estadísticas de algunas medidas de anteayer
        # Estadísticas de todas las medidas de ayer
        # Estadísticas de algunas medidas del día actual
    query = (
        f'SELECT MEAN("value"), MIN("value"), MAX("value") FROM "%" '  
        f'WHERE "entity_id" = \'agsex_sdf_invernadero_lht65n_humedad\' '
        f'AND time >= now() - 2d '
        f'GROUP BY time(1d)')

    # Ejecutar la consulta 
    result = client.query(query)
    # Guardar los puntos (filas) del resultado en una lista
    points = list(result.get_points()) 
    if not points:
        print(f"\n⚠️ No se encontraron puntos.") # Para hacer algo de loggin
        # Si no hay datos 
        return None
    else:
        # Tenemos 3 points ordenados: anteayer, ayer, hoy.
        # Los datos que deseamos son points[1]
        datos = points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos = list(datos.values())
        # Retornamos como tupla la media, máxima y mínima
        # datos[0] es la marca de tiempo, el resto de posiciones son los datos
        media = round(float(datos[1]), 1)
        min = round(float(datos[2]), 1)
        max = round(float(datos[3]), 1)
        # Devolvemos los datos en un diccionario con claves mean, min, max
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result
    
def diario_invernadero_temperatura():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Construir la consulta InfluxQL
    # Es la misma que la anterior, cambiando la tabla y el entity_id
    query = (
        f'SELECT MEAN("value"), MIN("value"), MAX("value") FROM "°C" '  
        f'WHERE "entity_id" = \'agsex_sdf_invernadero_lht65n_temperatura\' '
        f'AND time >= now() - 2d '
        f'GROUP BY time(1d)')

    # Ejecutar la consulta 
    result = client.query(query)
    # Guardar los puntos del resultado en una lista
    points = list(result.get_points()) 
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        # Si no hay datos 
        return None
    else:
        # Tenemos 3 points (anteayer, ayer, hoy)
        # Los datos que deseamos son points[1]
        datos = points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos = list(datos.values())
        # Retornamos como tupla la media, máxima y mínima
        # datos[0] es la marca de tiempo, el resto de posiciones son los datos
        media = round(float(datos[1]), 1)
        min = round(float(datos[2]), 1)
        max = round(float(datos[3]), 1)
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result

# =================================================================
# DATOS ACTUALES (ÚLTIMA MEDICIÓN)
# =================================================================
def actual_huerto_humedad():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Configura la query correcta aquí
    query = (
        f'SELECT "value" FROM "%" '  
        f'WHERE "entity_id" = \'agsex_sdf_huerto_lht65n_humedad\' '
        f'ORDER BY time DESC '
        f'LIMIT 1')

    # Ejecutar la consulta 
    result = client.query(query)

    # Guardar los puntos del resultado en una lista
    points = list(result.get_points())
    
    # Comprueba si no hay puntos
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        # Si no hay datos 
        return None
    # Retorna los datos como un diccionario, donde la clave es 'value'
    else:
        # Tenemos 3 points (anteayer, ayer, hoy)
        # Los datos que deseamos son points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos=points[0]
        valor=round(float(datos['value']), 1)
        return valor
    
def actual_huerto_temperatura():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Configura la query correcta aquí
    query = (
        f'SELECT "value" FROM "°C" '  
        f'WHERE "entity_id" = \'agsex_sdf_huerto_lht65n_temperatura\' '
        f'ORDER BY time DESC '
        f'LIMIT 1')

    # Ejecutar la consulta 
    result = client.query(query)

    # Guardar los puntos del resultado en una lista
    points = list(result.get_points())
    
    # Comprueba si no hay puntos
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        # Si no hay datos 
        return None
    # Retorna los datos como un diccionario, donde la clave es 'value'
    else:
        # Tenemos 3 points (anteayer, ayer, hoy)
        # Los datos que deseamos son points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos=points[0]
        valor=round(float(datos['value']), 1)
        return valor

# TODO
# No es obligatorio hacerlo, se hardcodea para probar en Telegram
def actual_invernadero_humedad():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Configura la query correcta aquí
    query = (
        f'SELECT "value" FROM "%" '  
        f'WHERE "entity_id" = \'agsex_sdf_invernadero_lht65n_humedad\' '
        f'ORDER BY time DESC '
        f'LIMIT 1')

    # Ejecutar la consulta 
    result = client.query(query)

    # Guardar los puntos del resultado en una lista
    points = list(result.get_points())
    
    # Comprueba si no hay puntos
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        # Si no hay datos 
        return None
    # Retorna los datos como un diccionario, donde la clave es 'value'
    else:
        # Tenemos 3 points (anteayer, ayer, hoy)
        # Los datos que deseamos son points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos=points[0]
        valor=round(float(datos['value']), 1)
        return valor

def actual_invernadero_temperatura():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    # Configura la query correcta aquí
    query = (
        f'SELECT "value" FROM "°C" '  
        f'WHERE "entity_id" = \'agsex_sdf_invernadero_lht65n_temperatura\' '
        f'ORDER BY time DESC '
        f'LIMIT 1')

    # Ejecutar la consulta 
    result = client.query(query)

    # Guardar los puntos del resultado en una lista
    points = list(result.get_points())
    
    # Comprueba si no hay puntos
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        # Si no hay datos 
        return None
    # Retorna los datos como un diccionario, donde la clave es 'value'
    else:
        # Tenemos 3 points (anteayer, ayer, hoy)
        # Los datos que deseamos son points[1]
        # Cada fila es un diccionario
        # Los datos son los valores de cada diccionario.
        datos=points[0]
        valor=round(float(datos['value']), 1)
        return valor

# =================================================================
# RESÚMENES SEMANALES
# =================================================================
def semanal_huerto_humedad():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    query = (
        'SELECT MEAN("value") AS mean, MIN("value") AS min, MAX("value") AS max '
        'FROM "%" '
        'WHERE "entity_id" = \'agsex_sdf_huerto_lht65n_humedad\' '
        'AND time >= now() - 7d'
    )

    result = client.query(query)
    points = list(result.get_points()) 
    
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        return None
    else:
        p = points[0]  # Solo 1 fila con los agregados de toda la semana
        media = round(float(p['mean']), 1)
        min = round(float(p['min']), 1)
        max = round(float(p['max']), 1)
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result


def semanal_huerto_temperatura():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    query = (
        'SELECT MEAN("value") AS mean, MIN("value") AS min, MAX("value") AS max '
        'FROM "°C" '
        'WHERE "entity_id" = \'agsex_sdf_huerto_lht65n_temperatura\' '
        'AND time >= now() - 7d'
    )

    result = client.query(query)
    points = list(result.get_points()) 
    
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        return None
    else:
        p = points[0]  # Solo 1 fila con los agregados de toda la semana
        media = round(float(p['mean']), 1)
        min = round(float(p['min']), 1)
        max = round(float(p['max']), 1)
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result

# TODO
# No es obligatorio hacerlo, se hardcodea para probar en Telegram
def semanal_invernadero_humedad():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    query = (
        'SELECT MEAN("value") AS mean, MIN("value") AS min, MAX("value") AS max '
        'FROM "%" '
        'WHERE "entity_id" = \'agsex_sdf_temperature_lht65n_humedad\' '
        'AND time >= now() - 7d'
    )

    result = client.query(query)
    points = list(result.get_points()) 
    
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        return None
    else:
        p = points[0]  # Solo 1 fila con los agregados de toda la semana
        media = round(float(p['mean']), 1)
        min = round(float(p['min']), 1)
        max = round(float(p['max']), 1)
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result

def semanal_invernadero_temperatura():
    client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, 
                        password=INFLUX_PASS, database=INFLUX_DB)
    
    query = (
        'SELECT MEAN("value") AS mean, MIN("value") AS min, MAX("value") AS max '
        'FROM "°C" '
        'WHERE "entity_id" = \'agsex_sdf_invernadero_lht65n_temperatura\' '
        'AND time >= now() - 7d'
    )

    result = client.query(query)
    points = list(result.get_points()) 
    
    if not points:
        print(f"\n⚠️ No se encontraron puntos.")
        return None
    else:
        p = points[0]  # Solo 1 fila con los agregados de toda la semana
        media = round(float(p['mean']), 1)
        min = round(float(p['min']), 1)
        max = round(float(p['max']), 1)
        result = dict()
        result['mean'] = media
        result['min'] = min
        result['max'] = max
        return result

if __name__ == '__main__':
    # Aquí puedes hacer pruebas de acceso a datos sin invocar al bot

    print(semanal_huerto_temperatura())
    print(semanal_huerto_humedad())


