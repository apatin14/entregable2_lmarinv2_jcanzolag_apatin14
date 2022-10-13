from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from serialize import serialize
import typing

_serilize = serialize()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Record(BaseModel):
    key: str
    value: typing.Any
    
class Path(BaseModel):
    path_name: str


@app.post("/create", response_model=Record)
def create(record: Record):
    print(record)
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
        return {"data": records}

    except Exception as e:
        return e


@app.put("/update")
def update(record: Record):
    try:
        # OPERATION CACHE
        return _serilize.update_record(record.key, record.value)

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

@app.post("/setPath")
def create(path: Path):
    try:
        _serilize.set_path(path)
        return {
            "message": "Success"
        }

    except Exception as e:
        return e