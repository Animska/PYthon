#Parámetros opcionales
import requests

def buscar_posts(user_id=None, limite=None, ordenar_por=None):
    """
    Busca posts con filtros opcionales
    Args:
        user_id: ID del usuario (opcional)
        limite: Número máximo de resultados (opcional)
        ordenar_por: Campo para ordenar (opcional)
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    # Construir diccionario de parámetros
    parametros = {}
    if user_id is not None:
        parametros['userId'] = user_id
    if limite is not None:
        parametros['_limit'] = limite
    if ordenar_por is not None:
        parametros['_sort'] = ordenar_por
    print(f"Parámetros enviados: {parametros}")
    response = requests.get(url, params=parametros)
    print(f"URL generada: {response.url}")
    return response.json()

# Prueba 1: Solo user_id
print("\n--- Búsqueda 1: Solo user_id ---")
posts1 = buscar_posts(user_id=2)
print(f"Resultados: {len(posts1)} posts")
# Prueba 2: user_id y límite
print("\n--- Búsqueda 2: user_id + límite ---")
posts2 = buscar_posts(user_id=2, limite=5)
print(f"Resultados: {len(posts2)} posts")
# Prueba 3: Todos los parámetros
print("\n--- Búsqueda 3: Todos los parámetros ---")
posts3 = buscar_posts(user_id=1, limite=3, ordenar_por='id')
print(f"Resultados: {len(posts3)} posts")
# Prueba 4: Sin parámetros (todos los posts)
print("\n--- Búsqueda 4: Sin filtros ---")
posts4 = buscar_posts()
print(f"Resultados: {len(posts4)} posts")
# Salida
# --- Búsqueda 1: Solo user_id ---
# Parámetros enviados: {'userId': 2}
# URL generada: https://jsonplaceholder.typicode.com/posts?userId=2
# Resultados: 10 posts
# --- Búsqueda 2: user_id + límite ---
# Parámetros enviados: {'userId': 2, '_limit': 5}
# URL generada: https://jsonplaceholder.typicode.com/posts?userId=2&_limit=5
# Resultados: 5 posts
# --- Búsqueda 3: Todos los parámetros ---
# Parámetros enviados: {'userId': 1, '_limit': 3, '_sort': 'id'}
# URL generada: https://jsonplaceholder.typicode.com/posts?userId=1&_limit=3&_sort=id
# Resultados: 3 posts
# --- Búsqueda 4: Sin filtros ---
# Parámetros enviados: {}
# URL generada: https://jsonplaceholder.typicode.com/posts
# Resultados: 100 posts