from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field, confloat

class Pintura(BaseModel):
    tipo: Literal[
        "Interior",
        "Exterior",
        "Esmalte",
        "Impermeabilizante",
        "Anticorrosiva",
        "Texturizada",
        "Vinilica",
        "Otro"
    ] = Field(..., description="Tipo de pintura aplicada")
    
    acabado: Optional[Literal[
        "Mate",
        "Satinado",
        "Brillante",
        "Texturizado",
        "Otro"
    ]] = Field(None, description="Acabado superficial de la pintura")
    
    color: Optional[str] = Field(None, description="Color de la pintura (nombre o código hexadecimal)")
    
    area_m2: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Área pintada en metros cuadrados")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual de la pintura")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales sobre la pintura")
