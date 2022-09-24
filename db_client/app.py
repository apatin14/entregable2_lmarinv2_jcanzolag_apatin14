from fastapi import FastAPI
from pydantic import BaseModel, Field
from serialize import serialize
import typing

_serilize = serialize()
app = FastAPI()
    
class Record(BaseModel):
    key: str
    value: typing.Any
    
@app.post("/create", response_model=Record)
def create(record: Record):
    try:
        _serilize.write_record(record.key, record.value)
        return record

    except Exception as e:
        return e


@app.get("/get/{id}")
def get(id: str):
    try:
        # OPERATION CACHE
        record = _serilize.search_record(id)
        return record

    except Exception as e:
        return e


@app.get("/getall")
def get():
    try:
        # OPERATION CACHE
        records = _serilize.read_records()
        return records

    except Exception as e:
        return e


@app.put("/update", response_model=Record)
def update(record: Record):
    try:
        # OPERATION CACHE

        _serilize.update_record(record.key, record.value)

        return record

    except Exception as e:
        return e


@app.delete("/delete/{id}")
def delete(id: str):
    try:
        # OPERATION CACHE
        _serilize.delete_record(id)

        return{
            "message": "Success"
        }
    except Exception as e:
        return e