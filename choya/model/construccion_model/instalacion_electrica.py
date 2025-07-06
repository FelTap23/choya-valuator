from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field

class Luminarias(BaseModel):
    cantidad: Annotated[int, Field(ge=0)] = Field(0, description="Número estimado de lámparas/luminarias instaladas")
    calidad: Optional[Literal["Baja", "Media", "Alta"]] = Field(None, description="Calidad general de las luminarias")

class Apagadores(BaseModel):
    cantidad: Annotated[int, Field(ge=0)] = Field(0, description="Número de apagadores o interruptores")
    calidad: Optional[Literal["Baja", "Media", "Alta"]] = Field(None, description="Calidad de los apagadores")

class Contactos(BaseModel):
    cantidad: Annotated[int, Field(ge=0)] = Field(0, description="Número de contactos eléctricos (enchufes)")

class InstalacionElectrica(BaseModel):
    tipo_instalacion: Literal["Oculta", "A_la_vista", "Mixta"] = Field(..., description="Tipo de instalación eléctrica")

    tipo_cableado: Optional[Literal["Cobre", "Aluminio", "Mixto", "Desconocido"]] = Field(None, description="Material predominante del cableado")

    luminarias: Optional[Luminarias] = Field(None, description="Detalles de las luminarias instaladas")

    apagadores: Optional[Apagadores] = Field(None, description="Detalles de los apagadores instalados")

    contactos: Optional[Contactos] = Field(None, description="Detalles de los contactos eléctricos")

    tiene_red_datos: Optional[bool] = Field(False, description="Indica si cuenta con red de datos estructurada")

    tiene_interruptor_termomagnetico: Optional[bool] = Field(False, description="Indica si cuenta con tablero de interruptores termomagnéticos")

    tiene_interruptor_diferencial: Optional[bool] = Field(False, description="Indica si cuenta con protección diferencial")

    estado: Literal["Bueno", "Regular", "Deteriorado"] = Field(..., description="Estado general del sistema eléctrico interior")

    observaciones: Optional[str] = Field(None, description="Comentarios técnicos adicionales o condiciones particulares")
