import requests
# Datos a enviar
nuevo_post = {
"title": "Mi primer post desde Python",
"body": "Este es el contenido de mi post. Estoy aprendiendo requests.",
"userId": 1
}
# URL del endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Hacer petición POST
response = requests.post(url, json=nuevo_post)
print(f"Status code: {response.status_code}")

# Verificar si fue exitoso
if response.status_code == 201: # 201 = Created
    print("Post creado exitosamente")
    # Obtener el post que devolvió el servidor
    post_creado = response.json()
    print(f"\nID asignado por el servidor: {post_creado['id']}")
    print(f"Título: {post_creado['title']}")
    print(f"Contenido: {post_creado['body']}")
    print(f"Usuario: {post_creado['userId']}")
else:
    print(f"Error: {response.status_code}")