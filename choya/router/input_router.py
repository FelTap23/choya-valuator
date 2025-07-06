from fastapi import APIRouter
from choya.model.terreno import  Terreno
from choya.model.caracteristicas_urbanas import CaracteristicasUrbanas
from choya.model.antecedentes import Antecedentes
from choya.model.elementos_de_construccion import ElementosConstruccion
#This class is just to quick validation
router_input = APIRouter()


@router_input.post("/terreno")
async def terreno_endpoint( payload : Terreno):
    return { "status": True}

@router_input.post("/urbanismo")
async def terreno_endpoint( payload : CaracteristicasUrbanas):
    print("Reaching this endpoint urbanismo")
    return { "status": True}

@router_input.post("/antecedentes")
async def antecedentes_endpoint( payload : Antecedentes):
    print("Endpoint antecedentes reached.")
    return { "status" : True }


@router_input.post("/elementos_construccion")
async def elementos_construccion_endpoint( payload : ElementosConstruccion):
    print("Endpoint antecedentes reached.")
    return { "status" : True }