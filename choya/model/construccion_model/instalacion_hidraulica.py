from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Cisterna(BaseModel):
    tiene: bool = Field(..., description="Indica si la vivienda cuenta con cisterna")
    capacidad_litros: Optional[Annotated[int, Field(gt=0)]] = Field(None, description="Capacidad de la cisterna en litros")
    material: Optional[Literal[
        "Concreto",
        "Plastico",
        "Fibra_de_vidrio",
        "Otro"
    ]] = Field(None, description="Material de la cisterna")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Deteriorado"
    ] = Field(..., description="Estado de la cisterna")
    

class Tinaco(BaseModel):
    tiene: bool = Field(..., description="Indica si hay tinaco instalado")
    capacidad_litros: Optional[Annotated[int, Field(gt=0)]] = Field(None, description="Capacidad en litros")
    material: Optional[Literal[
        "Plastico",
        "Rotoplas",
        "Fibra_de_vidrio",
        "Metalico",
        "Otro"
    ]] = Field(None, description="Material del tinaco")

class Boiler(BaseModel):
    tiene: bool = Field(..., description="Indica si hay boiler instalado")
    tipo: Optional[Literal[
        "Gas",
        "Electrico",
        "Solar",
        "Instantaneo",
        "Otro"
    ]] = Field(None, description="Tipo de boiler")

class Tuberia(BaseModel):
    material: Literal[
        "PVC",
        "CPVC",
        "Cobre",
        "PEX",
        "Galvanizado",
        "Otro"
    ] = Field(..., description="Material predominante de la tuberia")
    estado: Literal[
        "Bueno",
        "Regular",
        "Deteriorado"
    ] = Field(..., description="Estado general de las tuberias")

class InstalacionHidraulica(BaseModel):
    cisterna: Optional[Cisterna] = Field(None, description="Detalles sobre la cisterna de almacenamiento")
    tinaco: Optional[Tinaco] = Field(None, description="Detalles sobre el tinaco de azotea")
    boiler: Optional[Boiler] = Field(None, description="Detalles sobre el boiler o calentador de agua")
    tuberias: Optional[Tuberia] = Field(None, description="Detalles sobre la red de tuberias")

    tiene_bomba_presion: bool = Field(..., description="Indica si hay bomba presurizadora o hidroneumático")
    
    estado: Literal[
        "Bueno",
        "Regular",
        "Deteriorado"
    ] = Field(..., description="Estado general del sistema hidráulico interior")
    
    observaciones: Optional[str] = Field(None, description="Comentarios técnicos adicionales o condiciones particulares")
