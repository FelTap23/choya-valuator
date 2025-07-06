from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Techo(BaseModel):
    tipo_material: Literal[
        "Losa_Maciza_Concreto",
        "Losa_Nervada_o_Aligerada",
        "Membrana_Asfaltica",
        "Vigueta_y_Bovedilla",
        "Lamina_Galvanizada_o_Pintro",
        "Lamina_Termoacustica",
        "Lamina_Translucida",
        "Teja_de_Madera",
        "Par_y_Nudo",
        "Teja_de_Barro_Cocido",
        "Teja_de_Concreto",
        "Teja_Metalica"
    ] = Field(..., description="Tipo de material del techo")
    
    forma_techo: Literal[
        "Techo_Plano",
        "Techo_Inclinado_A_Dos_Aguas",
        "Techo_Inclinado_A_Cuatro_Aguas",
        "Techo_Inclinado_Mas_Aguas",
        "Techo_Curvo_Abovedado"
    ] = Field(..., description="Forma o tipo estructural del techo")
    
    techo_especial: Optional[Literal[
        "Techo_Verde",
        "Techo_Solar",
        "Techo_Tensado"
    ]] = Field(None, description="Tipo de techo especial, si aplica")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ] = Field(..., description="Estado actual del techo")
    
    aislamiento_termico: Optional[bool] = Field(False, description="Indica si cuenta con aislamiento térmico")
    
    aislamiento_acustico: Optional[bool] = Field(False, description="Indica si cuenta con aislamiento acústico")
    
    observaciones: Optional[str] = Field(None, description="Comentarios o detalles adicionales")