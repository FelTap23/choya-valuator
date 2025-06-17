
from fastapi import FastAPI
from choya.router.input_router import router_input
from antecedentes import Antecedentes

app = FastAPI()

app.include_router(router=router_input)
@app.post("/antecedentes")
def antecedentes(antecedente : Antecedentes):
    return True