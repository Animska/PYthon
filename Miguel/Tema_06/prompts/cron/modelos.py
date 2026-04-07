from typing import Literal
from pydantic import BaseModel, Field


class AnalisisPlanta(BaseModel):
    nombre:       str
    descripcion:  str
    salud_pct:    int = Field(ge=0, le=100)
    nivel_alerta: Literal["BUENO", "MEDIO", "PELIGRO"]


class AnalisisInvernadero(BaseModel):
    plantas: list[AnalisisPlanta]