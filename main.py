
from fastapi import FastAPI
from choya.router.input_router import router_input


app = FastAPI()
    
app.include_router(router=router_input)

#To show the first error message
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
