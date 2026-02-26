from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator
from typing import Optional
from datetime import datetime

class CrearProducto(BaseModel):
    nombre:str = Field(min_length=3, max_length=10, description="Nombre del producto")
    precio:float = Field(default=0.00, description="descripción: Precio en euros(debe ser positivo)")
    descripcion:Optional[str]
    categorias:list[str] = Field(default=[], description="Lista de categorias")
    stock:int = Field(default=0, gt=0, description="Cantidad de stock")

    @field_validator('precio')
    @classmethod
    def validar_decimales_precio(cls, valor: float) -> float:
        if round(valor, 2) != valor:
            raise ValueError('El precio solo puede tener 2 decimales')
        return valor

    @field_validator('nombre')
    @classmethod
    def validar_nombre_texto(cls, valor: str) -> str:
        if any(c.isdigit() for c in valor):
            raise ValueError('El nombre no puede contener números')
        return valor.strip()
    
class Producto(BaseModel):
    id:int
    fecha:datetime

class Config()
