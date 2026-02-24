from datetime import date
from pydantic import BaseModel, Field


class RegistroTemperatura(BaseModel):
    fecha:date = Field(description="Fecha del registro")
    temperatura_max:float = Field(gt=-100, lt=60,description="Temperatura máxima (entre -100 y 60)")
    temperatura_min:float = Field(gt=-100, lt=60,description="Temperatura máxima (entre -100 y 60)")
    ciudad:str

    @classmethod
    def desde_dict(cls, datos:dict):
        if isinstance(datos["fecha"], str):
            datos["fecha"] = date.fromisoformat(datos["fecha"])

        datos["temperatura_max"] = float(datos["temperatura_max"])
        datos["temperatura_min"] = float(datos["temperatura_min"])
        
        return cls(**datos)
    
    def __str__(self) -> str:
        return f"[{self.fecha}] {self.ciudad}: {self.temperatura_min}ºC - {self.temperatura_max}°C"
    



#PRUEBAS
if __name__ == "__main__":
    # Ejemplo de uso
    datos_ejemplo = {
        "fecha": "2026-06-01",
        "temperatura_max": "30.5",
        "temperatura_min": "20.0",
        "ciudad": "Madrid"
    }
    
    registro = RegistroTemperatura.desde_dict(datos_ejemplo)
    print(registro)