
from pydantic import BaseModel,Field
from typing import Annotated,Literal
from datetime import date

class PeritoValuador(BaseModel):
    nombre : Annotated[str,Field(max_length=50),"Name of the perito"]
    credencial_bienes_inmuebles : Annotated[str,"Credencial de perito valuador"]
    registro_INADEJ : Annotated[str,"no. de INADEJ"]
    cedula_profesional : Annotated[str,"Cedula de perito valuador"]


class Antecedentes(BaseModel):
    solicitante : Annotated[str, Field(max_length=100), "Name of the person that requires the avaluo."]
    perito_valuador : Annotated[PeritoValuador,"Name of the professional perito"]
    asesor_valuador : Annotated[str, Field(max_length=100), "Name of the not professional asesor"]
    fecha_del_avaluo : Annotated[date, "The date when the avaluo is made"]
    tipo_inmueble_a_valuar : Literal["CASA_HABITACIÓN",	"CASA_HABITACIÓN_CON_COMERCIO_EN_PLANTA_BAJA", "DEPARTAMENTO", "BODEGA", "LOCAL_COMERCIAL", "INDUSTRIA", "NAVE_Y_OFICINAS", "EDIFICIO_DE_PRODUCTOS"]
    regimen_de_propiedad : Literal["PRIVADA_INDIVIDUAL", "EN_CONDOMINIO", "COPROPIEDAD"]
    propietario_del_inmueble : Annotated[str, Field(max_length=100), "person that owns the property and who is in the escrituras"]
    proposito_de_avaluo : Literal["ESTIMAR_SU_VALOR_COMERCIAL", "DETERMINAR_SU_VALOR_COMERCIAL"]
    ubicacion_del_inmueble : Annotated[str, Field(max_length=1000) ,"address where the residence is located"]
    numero_de_cuenta_predial : Annotated[str, Field(max_length=19) ,"this cannot be null value either it does not have or it hasnt been given"]
    numero_de_cuenta_de_agua : Annotated[str, Field(max_length=19) ,"this cannot be null value either it does not have or it hasnt been given"]

