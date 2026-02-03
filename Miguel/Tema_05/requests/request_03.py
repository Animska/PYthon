import requests
def crear_post(titulo:str, contenido:str, user_id:int):
    """
    Crea un post en https://jsonplaceholder.typicode.com/posts con validación completa.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": titulo,
        "body": contenido,
        "userId": user_id
    }
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()  # Lanza excepción si status != 2xx
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Timeout de 10 segundos excedido")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
        return None


post = crear_post(
            titulo="Python requests es genial",
            contenido="Después de aprender urllib, requests es un alivio. Todo es más simple y limpio.",
            user_id=1
        )
if post:
    print("\n" + "="*60)
    print("OPERACIÓN COMPLETADA")
    print("="*60)