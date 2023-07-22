from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session

from typing import List

import pika 

from app.use_cases.validate_infos import validate_infos
from app.use_cases.turing_machine import tm
from jobs.sender import sent_to_queue

from app.entities.schemas import History
from app.entities import crud, schemas

from app.utils.deps import get_db

router = APIRouter()


@router.post("/dtm", status_code=200)
async def dtm(info: Request, db: Session = Depends(get_db)):
    info = await info.json()
    infos = await validate_infos(info)
    
    error_response, request_values = infos

    if len(error_response) != 0:
        raise HTTPException(
            status_code= error_response.get("code"),
            detail= error_response.get("message"),
            headers= {"400": "Bad Request"}
        )

    result = await tm(request_values, info)

    history = schemas.History(query=str(info), result=result)
    crud.create_history(db=db, history=history)

    if result == True:
        return{
            "message": "Accepted"
        }
    
    raise HTTPException(
            status_code= 400,
            detail= "Rejected",
            headers= {"400": "Bad Request"}
        )

@router.post("/dtm/multiple_mtu", response_model= None, status_code=200)
async def multiple_dtm(info: Request):
    list_info = await info.json()
    infos = []
    for info in list_info:
        response, request_values = await validate_infos(info)

        if not response:
            infos.append(request_values)

    sent_to_queue(infos)

    return {
        "message": "Processing your inputs...."
    }

@router.get("/dtm/get_history/{id}", status_code=200)
async def get_history(id: int, db: Session = Depends(get_db)):
    history = crud.get_history(db=db, id=id)
    if history is None:
        raise HTTPException(
            status_code= 400,
            detail= "Not found",
            headers= {"400": "Bad Request"}
        )
    return history


@router.get("/dtm/get_all_history", status_code=200)
async def get_all_history(db: Session = Depends(get_db)):
    history = crud.get_all_history(db=db)
    return history