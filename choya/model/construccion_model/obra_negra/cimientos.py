from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

PositiveFloat = Annotated[float, Field(gt=0)]

class Dimensiones(BaseModel):
    ancho_m: Optional[PositiveFloat] = Field(None, description="Ancho promedio en metros")
    largo_m: Optional[PositiveFloat] = Field(None, description="Largo total en metros, si aplica")
    espesor_losa_m: Optional[PositiveFloat] = Field(None, description="Espesor de losa en metros, solo si aplica")

class Concreto(BaseModel):
    resistencia_fc: Literal[
        "150kg/cm²", "200kg/cm²", "250kg/cm²", "300kg/cm²", "350kg/cm²"
    ] = Field(..., description="Resistencia del concreto")
    armado: bool = Field(..., description="Indica si lleva acero de refuerzo")

class Suelo(BaseModel):
    tipo: Literal[
        "Arena", "Grava", "Arcilloso", "Limoso", "Roca", "Mixto", "Otro"
    ] = Field(..., description="Tipo de suelo según estudio geotécnico")
    capacidad_portante_ton_m2: PositiveFloat = Field(..., description="Capacidad portante en toneladas por metro cuadrado")

class Cimentacion(BaseModel):
    tipo: Literal[
        "Zapata_Aislada",
        "Zapata_Corrida",
        "Losa_de_Cimentacion",
        "Pilotes",
        "Pilas_y_Cilindros",
        "Muros_de_Cimentacion",
        "Cimentacion_Mixta",
        "Otro"
    ] = Field(..., description="Tipo técnico de cimentación")
    
    sistema: Literal["Cimentacion_Superficial", "Cimentacion_Profunda"] = Field(..., description="Clasificación general de la cimentación")
    
    profundidad_m: PositiveFloat = Field(..., description="Profundidad desde el nivel de desplante en metros")
    
    dimensiones: Optional[Dimensiones] = Field(None, description="Dimensiones físicas de la cimentación si aplican")
    
    concreto: Concreto = Field(..., description="Datos del concreto utilizado")
    
    suelo: Suelo = Field(..., description="Características del suelo")
    
    drenaje: bool = Field(..., description="Indica si existe sistema de drenaje subterráneo")
    
    aislamiento: bool = Field(..., description="Indica si tiene impermeabilización o aislamiento térmico")
    
    año_construccion: Annotated[int, Field(ge=1800, le=2100, description="Año de construcción de la cimentación")]
    
    estado: Literal["Bueno", "Regular", "Dañado"] = Field(..., description="Estado actual de la cimentación")
    
    observaciones: Optional[str] = Field(None, description="Comentarios o detalles técnicos adicionales")
