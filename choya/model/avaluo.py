from pydantic import BaseModel
from typing import Annotated,Literal, Optional

class AvaluoCaractetistica(BaseModel):
    id :  Annotated [Optional[int], "This could be null coz the ORM will assing the id"]
    titulo  : str
    descripcion : str 
    tipo : Literal[ "CLASIFICACION_DE_LA_ZONA" ,"TIPO_CONSTRUCCION_ZONA" ,"USO_DE_SUELO" , "POBLACION"   ,"ABASTECIMIENTO_DE_AGUA_POTABLE" ,"DRENAJE_Y_ALCANTARILLADO" ,"RED_DE_ELECTRIFICACION" ,"ALUMBRADO_PUBLICO" ,"GUARNICIONES","BANQUETAS", "VIALIDADES","PAVIMENTOS","CAMELLONES","SERVICIOS_MIXTOS_E_INFRAESTRUCTURA", "EQUIPAMIENTO_URBANO","INFRAESTRUCTURA_PRIVADA","   "]
    ponderacion : float
