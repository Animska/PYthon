from fastapi import FastAPI


app = FastAPI(
    title="API Base FastAPI",
    description="Esqueleto inicial de API con FastAPI.",
    version="0.1.0",
)


@app.get("/")
async def estado_api() -> dict[str, str]:
    """Devuelve el estado básico de la API."""
    return {"mensaje": "API FastAPI operativa"}
