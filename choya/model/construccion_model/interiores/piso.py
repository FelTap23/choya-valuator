from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Piso(BaseModel):
    tipo: Literal[
        "Ceramica",
        "Porcelanato",
        "Madera_y_Derivados_Duela",
        "Madera_y_Derivados_Laminado",
        "Piso_Vinilico",
        "Cemento_Pulido_y_Concreto_Estampado",
        "Cemento_Escobillado",
        "Artesanal",
        "Granito",
        "Marmol",
        "Epoxico"
    ] = Field(..., description="Tipo de piso")

    calidad: Optional[Literal[
        "Baja",
        "Media",
        "Alta"
    ]] = Field(None, description="Calidad del piso")

    tamano_mosaico_cm: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Tamaño promedio del mosaico o loseta en centímetros")

    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual del piso")

    observaciones: Optional[str] = Field(None, description="Comentarios adicionales sobre el piso")
