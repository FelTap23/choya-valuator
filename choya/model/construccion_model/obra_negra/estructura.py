from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Estructura(BaseModel):
    tipo: Literal[
        "Concreto_Reforzado",
        "Acero",
        "Mamposteria_Block",
        "Mamposteria_Tabique",
        "Madera",
        "Mixta",
        "Otro"
    ] = Field(..., description="Tipo principal de estructura")
    
    calidad_material: Optional[Literal[
        "Alta",
        "Media",
        "Baja"
    ]] = Field(None, description="Calidad del material principal")
    
    sistema_estructural: Optional[Literal[
        "Columnas_y_Vigas",
        "Muros_de_Carga",
        "Entremado_Metalico",
        "Entremado_Madera",
        "Otro"
    ]] = Field(None, description="Sistema estructural empleado")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual de la estructura")
    
    año_construccion: Annotated[int, Field(ge=1800, le=2100, description="Año de construcción")]
    
    pisos: Annotated[int, Field(gt=0)] = Field(..., description="Número de pisos o niveles")
    
    sistema_antisismico: Optional[bool] = Field(False, description="Presencia de sistemas antisísmicos o refuerzos")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales o detalles técnicos")
