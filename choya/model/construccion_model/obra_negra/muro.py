from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Muros(BaseModel):
    tipo: Literal[
        "Concreto",
        "Tabique_Rojo",
        "Tabique_Gris",
        "Tabique_Comun",
        "Tabicon_Ligero",
        "Tabicon_Pesado",
        "Drywall",
        "Acero",
        "Madera",
        "Piedra"
    ] = Field(..., description="Tipo de muro")
    
    acabado_exterior: Optional[Literal[
        "Estuco",
        "Pintura",
        "Revestimiento",
        "Sin_Acabado"
    ]] = Field(None, description="Acabado exterior del muro")
    
    grosor_cm: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Grosor aproximado del muro en centímetros")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Deteriorado"
    ] = Field(..., description="Estado actual del muro")
    observaciones: Optional[str] = Field(None, description="Comentarios o detalles adicionales sobre el muro")
