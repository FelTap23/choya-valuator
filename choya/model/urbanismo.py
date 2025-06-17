from pydantic import BaseModel, field_validator, model_validator
from pydantic_core.core_schema import FieldValidationInfo # Importar FieldValidationInfo
from typing import Optional

#TODO agregar validaciones a cada campo

class ServicioPublico(BaseModel):
    codigo: str
    ponderacion: float
    comentario: str
    
    
    #Para cosas sencillas
    @field_validator('codigo')
    @classmethod
    def validate_codigo(cls, codigo: str, info : FieldValidationInfo):
        print(f"Show details {info}")
        return codigo
    
    #Para cosas custom :p
    @model_validator(mode="after")
    def custom(self ):
        print(f"Date grassa")
        return self


    
class ServiciosPublicos(BaseModel):
    agua_potable: ServicioPublico
    drenaje_Y_alcantarillado: ServicioPublico
    red_electrificacion: ServicioPublico
    alumbrado: ServicioPublico
    vialidades: ServicioPublico
    banquetas: ServicioPublico
    vialidades: ServicioPublico
    pavimentos: ServicioPublico
    camellones: ServicioPublico
    
class CaracteristicasUrbanas(BaseModel):
    zona: str
    construccion_dominante: str
    saturacion : int
    uso_de_suelo: str
    poblacion: str
    via_accesso: str
    ejemplito: ServicioPublico
    
    