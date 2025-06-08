import yaml

from choya.model.avaluo import AvaluoCaractetistica
from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import List

CARACTERISTICAS_URBANAS = ".avaluo_caracteristicas/caracteristicas_urbanas.yml"
SERVICIOS_PUBLICOS = ".avaluo_caracteristicas/servicios_publicos.yml"

class ChoyaAvaluoConfiguracion(BaseSettings): 
    AVALUO_CARACTERSITICAS_LIST : List[AvaluoCaractetistica]
    
@lru_cache
def load_app_properties() ->  ChoyaAvaluoConfiguracion:
    # Carga manual desde YAML
    with open(CARACTERISTICAS_URBANAS, "r") as f:
        config_data = yaml.safe_load(f)
    return ChoyaAvaluoConfiguracion(**config_data)


def load_yaml_second_approach() -> ChoyaAvaluoConfiguracion:
    with open(SERVICIOS_PUBLICOS, "r") as f:
        config_data= yaml.safe_load(f)
        #Utilizando compression de listas
        servicios_publicos = [  {**item, "tipo": tipo} for (tipo,sublista) in config_data["AVALUO_CARACTERISTICAS_LIST"].items() for item in sublista  ]
        avaluo_caracteristica_list = [ AvaluoCaractetistica(id=None ,tipo=s["tipo"],titulo=s["titulo"],descripcion=s["descripcion"],ponderacion=s["ponderacion"]) for s in servicios_publicos]
        return ChoyaAvaluoConfiguracion( AVALUO_CARACTERSITICAS_LIST= avaluo_caracteristica_list)
        
        
            
        
        
        