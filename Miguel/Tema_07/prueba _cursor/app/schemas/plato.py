from pydantic import BaseModel, Field


class Plato(BaseModel):
    """Modelo base de un plato del menu."""

    id: int = Field(..., ge=1, description="Identificador unico del plato")
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del plato")
    precio: float = Field(..., ge=0, description="Precio del plato")
