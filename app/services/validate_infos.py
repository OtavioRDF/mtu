from fastapi import Request
import logging

async def validate_infos(info: Request):    
    request_values = {
        "states": set(info.get("states", [])),
        "input_symbols": set(info.get("input_symbols", [])),
        "tape_symbols": set(info.get("tape_symbols", [])),
        "transitions": dict(info.get("transitions", {})),
        "initial_state": info.get("initial_state", ""),
        "blank_symbol": info.get("blank_symbol", ""),
        "final_states": set(info.get("final_states", [])),
        "input": info.get("input", "")
    }

    response = {}

    if request_values.get("blank_symbol") == "":
        logging.error("Blank symbol cannot be empty")
        response.update({"code": 400, "message": "blank_symbol cannot be empty string"})

    elif request_values.get("initial_state") == "":
        logging.error("Initial state cannot be empty")
        response.update({"code": 400, "message": "initial_state cannot be empty string"})

    elif request_values.get("input") == "":
        logging.error("Input cannot be empty")
        response.update({"code": 400, "message": "input cannot be empty string"})
    
    
    if len(request_values.get("states")) == 0:
        logging.error("States cannot be empty")
        response.update({"code": 400, "message": "states cannot be empty"})
    
    elif len(request_values.get("input_symbols")) == 0:
        logging.error("input symbols cannot be empty")
        response.update({"code": 400, "message": "input_symbols cannot be empty"})
    
    elif len(request_values.get("tape_symbols")) == 0:
        logging.error("Tape symbols cannot be empty")
        response.update({"code": 400, "message": "tape_symbols cannot be empty"})

    elif len(request_values.get("final_states")) == 0:
        logging.error("Final states cannot be empty")
        response.update({"code": 400, "message": "final_states cannot be empty"})

    elif len(request_values.get("transitions")) == 0:
        logging.error("Transitions cannot be empty")
        response.update({"code": 400, "message": "final_states cannot be empty"})

    return response, request_values