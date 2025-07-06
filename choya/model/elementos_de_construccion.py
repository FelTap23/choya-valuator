from pydantic import BaseModel
from typing import Optional
from choya.model.construccion_model.obra_negra.cimientos import Cimentacion
from choya.model.construccion_model.obra_negra.estructura import Estructura
from choya.model.construccion_model.obra_negra.techo import Techo
from choya.model.construccion_model.obra_negra.entrepisos import Entrepisos
from choya.model.construccion_model.obra_negra.muro import Muros
from choya.model.construccion_model.obra_negra.azotea import Azotea
from choya.model.construccion_model.obra_negra.barda import Barda

from choya.model.construccion_model.interiores.aplanado import Aplanado
from choya.model.construccion_model.interiores.carpinteria import Carpinteria
from choya.model.construccion_model.interiores.escalera import Escalera
from choya.model.construccion_model.interiores.lambrin import Lambrin

from choya.model.construccion_model.interiores.pintura import Pintura
from choya.model.construccion_model.interiores.piso import Piso
from choya.model.construccion_model.interiores.plafon import Plafon
from choya.model.construccion_model.interiores.zoclo import Zoclo

from choya.model.construccion_model.instalacion_electrica import InstalacionElectrica
from choya.model.construccion_model.instalacion_hidraulica import InstalacionHidraulica
from choya.model.construccion_model.ventanas_herrajes_y_cerrajeria import Ventanas, Cerrajeria

class ObraNegra(BaseModel):
    estrutura: Estructura
    cimentacion : Cimentacion
    techos : Optional[Techo]
    azotea: Optional[Azotea]
    entre_pisos: Optional[Entrepisos]
    muros: Optional[Muros]
    barda: Optional[Barda]

class Interiores(BaseModel):
    aplanado : Aplanado
    carpinteria : Optional[Carpinteria]
    escalera: Optional[Escalera]
    lambrin: Optional[Lambrin]
    pintura: Optional[Pintura]
    piso: Optional[Piso]
    plafon: Optional[Plafon]
    zoclo: Optional[Zoclo]
    
    
    
class ElementosConstruccion(BaseModel):
    obra_negra : Optional[ObraNegra]
    interiores: Optional[Interiores]
    instalacion_electrica: Optional[InstalacionElectrica]
    instalacion_hidraulica: Optional[InstalacionHidraulica]
    ventanas : Optional[Ventanas]
    cerrajeria : Optional[Cerrajeria]
    