import typing
from pydantic import BaseModel

class Record(BaseModel):
    key: str 
    value: typing.Any
    
class update_record_dto(BaseModel):
    id: str
    value: typing.Any
    
class update_hash(BaseModel):
    partition_number: int
    value: object
    