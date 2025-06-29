Para validar clases

from pydantic import BaseModel, field_validator, model_validator
from pydantic_core.core_schema import FieldValidationInfo # Importar FieldValidationInfo

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