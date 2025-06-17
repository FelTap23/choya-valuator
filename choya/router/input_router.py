from fastapi import APIRouter
from choya.model.terreno import  Terreno
from choya.model.urbanismo import CaracteristicasUrbanas


router_input = APIRouter()


@router_input.post("/terreno")
def terreno_endpoint( payload : Terreno):
    return { "status": True}

@router_input.post("/urbanismo")
def terreno_endpoint( payload : CaracteristicasUrbanas):
    print("Reaching this endpoint urbanismo")
    return { "status": True}