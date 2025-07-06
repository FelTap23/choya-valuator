from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Plafon(BaseModel):
    tipo: Literal[
        "Yeso",
        "Drywall",
        "PVC",
        "Lamina_Acustica",
        "Madera"
    ] = Field(..., description="Material principal del plafón")
    
    uso: Optional[Literal[
        "Decorativo",
        "Acústico",
        "Funcional",
        "Mixto"
    ]] = Field("Funcional", description="Función principal del plafón")
    
    altura_libre_m: Optional[Annotated[float, Field(gt=0)]] = Field(None, description="Altura libre desde el piso hasta el plafón, en metros")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado físico del plafón")
    
    con_iluminacion_integrada: Optional[bool] = Field(False, description="Indica si el plafón tiene iluminación empotrada o integrada")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales o particularidades del plafón")
