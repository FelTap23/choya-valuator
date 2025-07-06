from typing import Literal, Optional
from pydantic import BaseModel, Field

class Escalera(BaseModel):
    forma: Literal[
        "Escalera_recta",
        "Escalera_en_L_con_descanso",
        "Escalera_en_U",
        "Escalera_en_espiral_caracol",
        "Escalera_curva_caracol_amplia",
        "Escalera_compensada"
    ] = Field(..., description="Forma o tipo de la escalera")
    
    estructura: Literal[
        "Viga_central",
        "Dos_vigas_laterales",
        "Volada_o_flotante",
        "Metalica_o_modular"
    ] = Field(..., description="Tipo de estructura de la escalera")
    
    material: Literal[
        "Hormigon_armado",
        "Madera",
        "Metal",
        "Vidrio_templado"
    ] = Field(..., description="Material principal de la escalera")
    
    ubicacion: Literal[
        "Interior",
        "Exterior",
        "Emergencia"
    ] = Field(..., description="Ubicación o tipo funcional de la escalera")
    
    estado: Optional[Literal[
        "Bueno",
        "Regular",
        "Dañado"
    ]] = Field(None, description="Estado actual de la escalera")
    
    observaciones: Optional[str] = Field(None, description="Comentarios adicionales o detalles técnicos")
