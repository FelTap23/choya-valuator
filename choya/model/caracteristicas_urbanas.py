from pydantic import BaseModel, field_validator, model_validator
from pydantic_core.core_schema import FieldValidationInfo 
from typing import Optional, ClassVar

from choya.validator.advanced_field_validator import AdvancedFieldValidator
from choya.validator.in_memory_validator import InMemoryValidator

class Servicio(BaseModel):
    codigo: str
    ponderacion: float
    comentario: str

class ServiciosPublicos(BaseModel):
    agua_potable: Servicio
    drenaje_Y_alcantarillado: Servicio
    red_electrificacion: Servicio
    alumbrado: Servicio
    vialidades: Servicio
    banquetas: Servicio
    pavimentos: Servicio
    camellones: Servicio

class OtrosServicios(BaseModel):
    red_telefonica: Optional[Servicio]
    servicio_de_limpia: Optional[Servicio]
    transporte_urbano: Optional[Servicio]

class EquipamientoUrbano(BaseModel):
    escuelas: Optional[Servicio]
    salud : Optional[Servicio]
    comercial: Optional[Servicio]

class CaracteristicasUrbanas(BaseModel):
    __advanced_validator : ClassVar[AdvancedFieldValidator]  = InMemoryValidator("AVALUO_CARACTERSITICAS", ".avaluo_caracteristicas/caracteristicas_urbanas.yml")
    #Closed values
    clasificacion_de_la_zona: str
    tipo_construccion_zona: str
    uso_de_suelo: str
    poblacion: str
    #Open values
    saturacion : int
    via_accesso: str
    
    servicios_publicos : ServiciosPublicos
    otros_servicios : OtrosServicios
    equipamiento_urbano: EquipamientoUrbano
        
    #TODO Include all the types with defaults to avoid to create Literals
    @field_validator('clasificacion_de_la_zona', 'tipo_construccion_zona', 'uso_de_suelo','poblacion')
    @classmethod
    def validate(cls, value: str, info : FieldValidationInfo):
        return cls.__advanced_validator.validate(info.field_name, value)