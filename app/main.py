from fastapi import FastAPI, Request, HTTPException
from services.validate_infos import validate_infos
from services.turing_machine import tm

app = FastAPI()


@app.post("/dtm", status_code=200)
async def dtm(info: Request):
    info = await info.json()
    infos = await validate_infos(info)
    
    error_response, request_values = infos

    if len(error_response) != 0:
        raise HTTPException(
            status_code= error_response.get("code"),
            detail= error_response.get("message"),
            headers= {"400": "Bad Request"}
        )

    result = tm(request_values)

    if result == "Accepted":
        return{
            "code": 200,
            "message": "Accepted"
        }
    
    raise HTTPException(
            status_code= 400,
            detail= "Rejected",
            headers= {"400": "Bad Request"}
        )