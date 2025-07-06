from typing import Literal, Optional
from pydantic import BaseModel, Field

class Ventanas(BaseModel):
    tipo: Literal[
        "Corrediza",
        "Abatible",
        "Fija",
        "Oscilobatiente",
        "Plegable",
        "Otro"
    ] = Field(..., description="Tipo de ventana")

    material_marco: Literal[
        "Aluminio",
        "Madera",
        "PVC",
        "Herreria",
        "Mixto",
        "Otro"
    ] = Field(..., description="Material predominante del marco de la ventana")

    tipo_vidrio: Literal[
        "Sencillo",
        "Doble",
        "Templado",
        "Laminado",
        "Reflectivo",
        "Otro"
    ] = Field(..., description="Tipo de vidrio utilizado")

    tiene_herreria: bool = Field(False, description="Indica si tiene herrería o rejas de seguridad")

    tipo_herreria: Optional[Literal[
        "Forjada",
        "Tubular",
        "Electrosoldada",
        "Otro"
    ]] = Field(None, description="Tipo de herrería o rejas, si aplica")

    aislamiento_termico: bool = Field(False, description="Indica si tiene aislamiento térmico")
    aislamiento_acustico: bool = Field(False, description="Indica si tiene aislamiento acústico")
    tiene_tragaluces: bool = Field(False, description="Indica si tiene tragaluces")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Deteriorado"
    ] = Field(..., description="Estado general de la ventana")

    observaciones: Optional[str] = Field(None, description="Comentarios adicionales o detalles técnicos")


class Cerrajeria(BaseModel):
    tipo: Literal[
        "Cilindro",
        "Palanca",
        "Electrónica",
        "Biométrica",
    ] = Field(..., description="Tipo de cerrajería")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Deteriorado"
    ] = Field(..., description="Estado general")

    observaciones: Optional[str] = Field(None, description="Detalles adicionales")
