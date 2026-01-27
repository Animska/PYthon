#Caracteres especiales - Codificación automática
import requests
# Búsqueda con espacios, acentos y caracteres especiales
parametros = {
'q': 'Python & Web Development',
'ciudad': 'São Paulo',
'email': 'usuario@ejemplo.com'
}
response = requests.get('https://httpbin.org/get', params=parametros)
print("Parámetros originales:")
print(parametros)
print("\nURL generada por requests:")
print(response.url)
print("\nRequests codificó automáticamente:")
print(" - Espacios → %20")
print(" - & → %26")
print(" - @ → %40")
print(" - ã → %C3%A3")
# Salida
# Parámetros originales:
# {'q': 'Python & Web Development', 'ciudad': 'São Paulo', 'email': 'usuario@ejemplo.com'}
# URL generada por requests:
#https://httpbin.org/get?q=Python+%26+Web+Development&ciudad=S%C3%A3o+Paulo&email=usuario%40ejemplo.com
# Requests codificó automáticamente:
# - Espacios → %20 (o +)
# - & → %26
# - @ → %40
# - ã → %C3%A3