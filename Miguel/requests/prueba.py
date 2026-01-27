import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
print(len(posts))

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#obtiene el primer post

print(f"Status code: {response.status_code}")
#estatus