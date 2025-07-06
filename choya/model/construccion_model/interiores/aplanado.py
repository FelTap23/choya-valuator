from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Aplanado(BaseModel):
    tipo: Literal[
        "Mortero_Cemento_Arena",
        "Yeso",
        "Cal_Arena",
        "Con_Aditivos",
        "Barro_Paja_Arena"
    ] = Field(..., description="Tipo de mezcla usada en el aplanado")

    uso: Optional[Literal[
        "Interior",
        "Exterior",
        "Ambos"
    ]] = Field("Ambos", description="Dónde se aplicó el aplanado")

    espesor_cm: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Espesor promedio del aplanado en centímetros")

    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado físico del aplanado")

    acabado_final: Optional[Literal[
        "Liso",
        "Texturizado",
        "Rústico",
        "Sin_Acabado"
    ]] = Field(None, description="Tipo de acabado superficial del aplanado")

    observaciones: Optional[str] = Field(None, description="Observaciones técnicas o detalles adicionales")
