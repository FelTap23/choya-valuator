
from fastapi import FastAPI,Request
from choya.router.input_router import router_input
from choya.model.antecedentes import Antecedentes



from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY



app = FastAPI()
    
app.include_router(router=router_input)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     first_error = exc.errors()[0]
#     return JSONResponse(
#         status_code=HTTP_422_UNPROCESSABLE_ENTITY,
#         content={
#             "error": {
#                 "field": first_error.get("loc", []),
#                 "message": first_error.get("msg", "Invalid input"),
#                 "type": first_error.get("type", "")
#             }
#         }
#     )
