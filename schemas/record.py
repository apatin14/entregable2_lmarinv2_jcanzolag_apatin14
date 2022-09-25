import typing
from pydantic import BaseModel

class Record(BaseModel):
    key: str 
    value: typing.Any
    
class update_record_dto:
    id: str
    value: typing.Any
    