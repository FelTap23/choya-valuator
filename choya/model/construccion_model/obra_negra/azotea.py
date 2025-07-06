from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Azotea(BaseModel):
    tipo: Literal[
        "Azotea_de_Concreto",
        "Azotea_con_Lamina",
        "Azotea_Habitable_Terraza_Jardin"
    ] = Field(..., description="Tipo de azotea según su construcción y uso")
    
    impermeabilizada: Optional[bool] = Field(False, description="Indica si la azotea tiene impermeabilización")
    
    uso: Optional[Literal[
        "Técnico_Servicio",  # Ej. tendederos, tanques, etc.
        "Recreativo",         # Jardines, terrazas, roof garden
        "Sin_Uso_Definido"
    ]] = Field(None, description="Uso actual de la azotea")
    
    accesible: Optional[bool] = Field(True, description="Indica si la azotea es accesible desde el interior")
    
    barandales_o_muros: Optional[bool] = Field(None, description="Indica si la azotea cuenta con protección perimetral")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado físico de la azotea")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales sobre la azotea")
