#Ejemplo 1: Filtrar posts por usuario
import requests

#sin parametros
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()
print(f"Total de posts sin filtrar: {len(posts)}")

#con parametros
url = "https://jsonplaceholder.typicode.com/posts"
parametros = {
'userId': 1
}
response = requests.get(url, params=parametros)
posts = response.json()
print(f"Total de posts del usuario 1: {len(posts)}")
print(f"URL final construida: {response.url}")
# Salida:
# Total de posts del usuario 1: 10
# URL final construida: https://jsonplaceholder.typicode.com/posts?userId=1