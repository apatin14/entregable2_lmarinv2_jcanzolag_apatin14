from fastapi import APIRouter
from db_client.serialize import serialize
from db_client.hashing256 import Hashing256
from schemas.record import Record

routes_record = APIRouter()

_hash256=Hashing256()
_serilize =serialize(_hash256)

@routes_record.post("/create", response_model=Record)
def create(record: Record):
    try:
        #OPERATION CACHE

        _serilize.write_record(record.key, record.value)
        return record

    except Exception as e:
        return e

@routes_record.get("/get/{id}")
def get(id: str):
    try:
        #OPERATION CACHE
        record = _serilize.search_record(id)
        return record

    except Exception as e:
        return e

@routes_record.get("/getall")
def get():
    try:
        #OPERATION CACHE
        records = _serilize.read_records()
        return records

    except Exception as e:
        return e

@routes_record.put("/update", response_model=Record)
def update(record: Record):
    try:
        #OPERATION CACHE

        _serilize.update_record(record.key, record.value)

        return record

    except Exception as e:
        return e

@routes_record.delete("/delete/{id}")
def delete(id: str):
    try:
        #OPERATION CACHE
        _serilize.delete_record(id)

        return{
            "message": "Success"
        }
    except Exception as e:
        return e
