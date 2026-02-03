import requests

def hacer_peticion_simple():
    """
    Función que hace una petición GET simple y muestra los resultados
    """
    print("Iniciando petición a JSONPlaceholder...")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Estado de la petición: {response.status_code}")
    if response.ok:
        posts = response.json()
        print(f"\nPetición exitosa")
        print(f"Se recibieron {len(posts)} posts")
        print(f"Tiempo de respuesta: {response.elapsed.total_seconds():.2f}s")
        print("\nPrimeros 3 posts:")

        for i, post in enumerate(posts[:3], 1):
            print(f"\n{i}. {post['title']}")
            print(f" Usuario: {post['userId']}")
            print(f" Contenido: {post['body'][:50]}...")
    else:
        print(f"\n✗ Error en la petición: {response.status_code}")

if __name__ == "__main__":
    hacer_peticion_simple()