import typing
from pydantic import BaseModel

class Record(BaseModel):
    key: str 
    value: typing.Any
    