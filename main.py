
from fastapi import FastAPI
from choya.router.input_router import router_input
from choya.model.antecedentes import Antecedentes

app = FastAPI()

app.include_router(router=router_input)

