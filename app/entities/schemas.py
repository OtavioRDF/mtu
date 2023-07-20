from pydantic import BaseModel, EmailStr
from typing import List

class History(BaseModel): 
  query: str 
  result: str 


class EmailSchema(BaseModel):
  email: List[EmailStr]