from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Entrepisos(BaseModel):
    tipo: Literal[
        "Losa_Maciza",
        "Losa_Aligerada_Reticular",
        "Losa_Aligerada_Nervada",
        "Losa_Prefabricada_Vigueta_y_Bovedilla",
        "Losa_Compuesta_Acero_y_Concreto",
        "Steel_Deck",
        "Madera_mas_Tablado",
        "Madera_Laminada",
        "Mixto_Acero_Madera",
        "Mixto_Concreto_Poliestireno"
    ] = Field(..., description="Tipo de entrepiso")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual del entrepiso")
    
    aislante_acustico: Optional[bool] = Field(False, description="Indica si cuenta con aislamiento acústico")
    
    observaciones: Optional[str] = Field(None, description="Comentarios o detalles adicionales")
