from pydantic import BaseModel
from datetime import date
from typing import Optional

class PrisioneroBase(BaseModel):
    fecha_publicacion: Optional[date]
    pais_prision: Optional[str]
    consulado: Optional[str]
    delito: Optional[str]
    extraditado: Optional[str]
    situacion_juridica: Optional[str]
    genero: Optional[str]
    grupo_edad: Optional[str]
    cantidad: Optional[int]
    latitud: Optional[float]
    longitud: Optional[float]

class PrisioneroCreate(PrisioneroBase):
    pass

class Prisionero(PrisioneroBase):
    id: int

    class Config:
        orm_mode = True
