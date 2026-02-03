import requests

def obtener_clima(ciudad: str, api_key: str, unidades: str = 'metric', idioma: str = 'es'):
    """
    Obtener el clima de una ciudad usando la API de OpenWeatherMap
    
    Args:
        ciudad: ciudad de que buscamos el clima
        api_key: la api_key de OpenWeatherMap
        unidades: unidades de medicion del clima
        idioma: idioma en el que haremos la peticion
    """
    #Geocoding API
    url_geo = 'http://api.openweathermap.org/geo/1.0/direct'
    parametros_geo = {
        'q': ciudad,
        'appid': api_key,
        'limit': 1  # Solo queremos 1 resultado
    }
    response_geo = requests.get(url_geo, params=parametros_geo)
    response_geo.raise_for_status()
    
    data_geo = response_geo.json()
    if not data_geo:
        print(f"Ciudad '{ciudad}' no encontrada.")
        return
    
    lat = data_geo[0]['lat']
    lon = data_geo[0]['lon']
    pais = data_geo[0]['country']
    
    #Weather API
    url_weather = 'https://api.openweathermap.org/data/2.5/weather'
    parametros_weather = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': unidades,
        'lang': idioma
    }
    
    response_weather = requests.get(url_weather, params=parametros_weather)
    response_weather.raise_for_status()  # Verifica errores HTTP
    
    data = response_weather.json()
    
    print(f"Clima en {ciudad}, {pais}")
    print("====================================================")
    print(f"Temperatura: {data['main']['temp']}°C")
    print(f"Sensación térmica: {data['main']['feels_like']}°C")
    print(f"Descripción: {data['weather'][0]['description']}")
    print(f"Humedad: {data['main']['humidity']}%")
    print(f"Viento: {data['wind']['speed']} m/s")

# Prueba
api_key = 'f43b8301f20144dd417e7d90aa3f97b7'
obtener_clima('zafra', api_key)