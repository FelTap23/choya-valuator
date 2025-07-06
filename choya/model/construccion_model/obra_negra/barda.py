from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Barda(BaseModel):
    tipo: Literal[
        "Block_de_Concreto",
        "Tabique_Rojo",
        "Malla_Ciclonica",
        "Piedra",
        "Madera",
        "Metal",
        "No_tiene"
    ] = Field(..., description="Tipo de material principal de la barda")
    
    altura_m: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Altura aproximada en metros")
    
    estado: Literal[
        "Buena",
        "Regular",
        "Dañada"
    ] = Field(..., description="Estado físico de la barda")
    
    completa: Optional[bool] = Field(True, description="Indica si la barda delimita completamente el terreno")
    
    con_refuerzo: Optional[bool] = Field(False, description="Indica si la barda tiene castillos, columnas o refuerzos estructurales")
    
    con_proteccion_adicional: Optional[Literal[
        "Alambre_de_Puas",
        "Electricificada",
        "Cristal_Roto",
        "Ninguna"
    ]] = Field("Ninguna", description="Medidas adicionales de seguridad sobre la barda")
    
    observaciones: Optional[str] = Field(None, description="Comentarios o detalles adicionales")
