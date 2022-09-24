import typing
from pydantic import BaseModel

class Record(BaseModel):
    key: str 
    value: typing.Any
    
class Update_Record_Dto:
    id: str
    value: typing.Any
    