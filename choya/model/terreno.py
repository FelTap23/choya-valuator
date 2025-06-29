from pydantic import BaseModel, Field, confloat
from typing import Optional,Literal

class ColindanciaTerreno(BaseModel):
    medida : float = Field(..., gt=0.0)
    descripcion_colindancia  : str = Field(..., max_length=100)

class TopografiaTerreno(BaseModel):
    aspecto_topografico: Literal["RECTANGULO_REGULAR","POLIGONO_IRREGULAR","TRIANGULO_REGULAR"]
    incidencia: Literal["CON_MAS_DE_CUATRO_ANGULOS","NINGUNA"]
    caracteristicas_panoramicas: Literal[
        "SIN_RELEVANCIA",
        "CON_LIGERA_PENDIENTE_DESCENDENTE",
        "CON_PRONUNCIADA_PENDIENTE_DESCENDENTE",
        "CON_LIGERA_PENDIENTE_ASCENDENTE",
        "CON_PRONUNCIADA_PENDIENTE_ASCENDENTE"
    ]
    servidumbres_resctricciones : Optional[str] = None
    
    
class Terreno(BaseModel):
    descripcion : str = Field(..., max_length= 100)
    medidas_del_terreno_segun : Literal[
        "ESCRITURAS",
        "PLANO",
        "PLANO_CATASTRAL",
        "MEDIDAS_TOMADAS_EN_CAMPO",
        "DATOS_PROPORCIONADOS_POR_EL_CLIENTE",
        "PLANO_DE_SUBDIVISION",
        "CESION_DE_DERECHOS",
        "CONTRATO_PRIVADO_DE_COMPRA_VENTA",
        "NO_SE_PROPORCIONARON",
        "BOLETA_PREDIAL",
        "CEDULA_CATASTRAL"
    ]
    norte : ColindanciaTerreno
    sur: ColindanciaTerreno
    este: ColindanciaTerreno
    oeste: ColindanciaTerreno
    superficie_total_terreno : float = Field(..., gt=0.0)
    topografia : TopografiaTerreno
    