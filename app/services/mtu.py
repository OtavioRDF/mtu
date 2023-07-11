from fastapi import APIRouter, Request, HTTPException, Depends
from app.use_cases.validate_infos import validate_infos
from app.use_cases.turing_machine import tm

from app.entities.schemas import History

router = APIRouter()


@router.post("/dtm", status_code=200)
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

    if result == True:
        return{
            "message": "Accepted"
        }
    
    raise HTTPException(
            status_code= 400,
            detail= "Rejected",
            headers= {"400": "Bad Request"}
        )