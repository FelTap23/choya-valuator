from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Lambrin(BaseModel):
    tipo: Literal[
        "Wood_Plastic_Composite",
        "PVC",
        "Melamina",
        "Enchapado",
        "Madera_Natural",
        "Ceramica",
        "Azulejo",
        "Piedra_Natural",
        "Yeso",
        "Metal",
        "Fibras_Naturales",
        "Marmol",
        "Granito"
    ] = Field(..., description="Tipo de material del lambrin")
    
    uso: Optional[Literal[
        "Interior",
        "Exterior",
        "Ambos"
    ]] = Field("Interior", description="Lugar de aplicación del lambrin")
    
    acabado: Optional[Literal[
        "Liso",
        "Texturizado",
        "Brillante",
        "Mate",
        "Rústico"
    ]] = Field(None, description="Acabado superficial del lambrin")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual del lambrin")
    
    altura_m: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Altura del lambrin instalado en metros")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales o detalles técnicos")
