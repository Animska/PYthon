# Esqueleto inicial FastAPI

Proyecto base para comenzar una API con FastAPI en Python.

## Requisitos

- Python 3.10 o superior

## Crear y activar entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar servidor en desarrollo

```bash
uvicorn app.main:app --reload
```

## Verificación básica

- Endpoint raíz: `http://127.0.0.1:8000/`
- Documentación automática: `http://127.0.0.1:8000/docs`
