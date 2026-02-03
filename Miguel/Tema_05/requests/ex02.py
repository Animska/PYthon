#Múltiples parámetros
import requests

url = "https://jsonplaceholder.typicode.com/posts"
parametros = {
'userId': 1,
'_sort': 'id',
'_order': 'desc',
'_limit': 3
}
response = requests.get(url, params=parametros)
posts = response.json()
print(f"URL construida: {response.url}")
print(f"\nPrimeros 3 posts del usuario 1 (orden descendente):")
print('='*60)
for post in posts:
    print(f"ID: {post['id']} | Título: {post['title'][:40]}...")
# Salida
# URL construida: https://jsonplaceholder.typicode.com/posts?userId=1&_sort=id&_order=desc&_limit=3
# Primeros 3 posts del usuario 1 (orden descendente):
# ============================================================
# ID: 10 | Título: optio molestias id quia eum...
# ID: 9 | Título: nesciunt iure omnis dolorem tempora et...
# ID: 8 | Título: dolorem dolore est ipsam...