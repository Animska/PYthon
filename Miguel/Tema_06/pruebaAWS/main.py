from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
# Middleware CORS: permite que el navegador haga peticiones
# desde el frontend (Apache puerto 80) hacia la API (Uvicorn puerto 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def root():
    return {'mensaje': 'Aplicacion FastAPI desplegada en AWS EC2'}

@app.get('/saludo/{nombre}')
def saludo(nombre: str):
    return {'mensaje': f'Hola, {nombre}!'}

@app.get('/productos')
def productos():
    return {
        'productos': [
            {'id': 1, 'nombre': 'Teclado', 'precio': 49.99},
            {'id': 2, 'nombre': 'Monitor', 'precio': 299.99},
            {'id': 3, 'nombre': 'Raton', 'precio': 29.99},
        ]
    }
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)