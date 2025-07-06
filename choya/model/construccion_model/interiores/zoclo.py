from typing import Literal, Optional
from pydantic import BaseModel, Field

class Zoclo(BaseModel):
    tipo: Literal[
        "Ceramico_o_Porcelanato",
        "Madera",
        "Poliestireno",
        "Metal_Aluminio_o_Acero",
        "Marmol",
        "Piedra"
    ] = Field(..., description="Tipo de material del zoclo")
    
    calidad: Optional[Literal[
        "Baja",
        "Media",
        "Alta"
    ]] = Field(None, description="Calidad del zoclo")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual del zoclo")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales sobre el zoclo")