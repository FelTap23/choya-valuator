from typing import Literal, Optional
from pydantic import BaseModel, Field

class CarpinteriaElemento(BaseModel):
    tipo: Literal[
        "Puerta",
        "Closet",
        "Ventana",
        "Mueble_empotrado",
        "Otro"
    ] = Field(..., description="Tipo de elemento de carpintería")
    
    calidad_madera: Optional[Literal[
        "Baja",
        "Media",
        "Alta"
    ]] = Field(None, description="Calidad general de la madera")
    
    estado: Optional[Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ]] = Field(None, description="Estado actual del elemento")
    
    observaciones: Optional[str] = Field(None, description="Comentarios o detalles adicionales")

class Carpinteria(BaseModel):
    elementos: Optional[list[CarpinteriaElemento]] = Field(None, description="Lista de elementos de carpintería")
    
    observaciones_generales: Optional[str] = Field(None, description="Observaciones generales sobre la carpintería")
