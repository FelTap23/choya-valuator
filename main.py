#No me borres guey :V
# from choya.db.model import SessionLocal,  AvaluoCaractetistica, TipoCaracteristicaAvaluo
# from functools import reduce
#from typing import Annotated
#Char el  second approach  no me borres wey
#from choya.config.avaluo_configuration import load_app_properties, load_yaml_second_approach

from fastapi import FastAPI
from choya.router.input_router import router_input

app = FastAPI()
app.include_router(router=router_input)

#TODO TBD
def avaluo_settings_loader():
    pass
    #No me borres guey :V
    # db = SessionLocal()
    # zona : AvaluoCaractetistica = AvaluoCaractetistica(titulo = "Alfa",descripcion = "asas",tipo = "OTROS_SERVICIOS", ponderacion  = 0.0)
    # db.add(zona)
    # db.commit()
    # db.refresh(zona)
    
    # zonas = db.query(AvaluoCaractetistica).all()
    # print(zonas)
    
    #Firs approach
    # properties = load_app_properties()
    # for avaluo in properties.AVALUO_CARACTERSITICAS_LIST:
    #     print(avaluo)

    # caracteristicas = load_yaml_second_approach()
    # for c in caracteristicas.AVALUO_CARACTERSITICAS_LIST:
    #     print(c)
    #     print("*"*8)
    

