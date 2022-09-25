from fastapi import APIRouter
from router_server.routing import routingTier
from schemas.record import Record, update_record_dto

_routingTier = routingTier(5)
routes_record = APIRouter()


@routes_record.post("/create", response_model=Record)
def create(record: Record):
    try:
        # OPERATION CACHE
        _routingTier.create_key_value(record.key, record.value)
        return record

    except Exception as e:
        return e


@routes_record.get("/get/{id}")
def get(id: str):
    try:
        # OPERATION CACHE
        return _routingTier.find_by_id(id)

    except Exception as e:
        return e


@routes_record.put("/update", response_model=Record)
def update(record: update_record_dto):
    try:
        # OPERATION CACHE
        return _routingTier.update_by_key(record.id, record.value)

    except Exception as e:
        return e


@routes_record.delete("/delete/{id}")
def delete(id: str):
    try:
        return _routingTier.delete_by_id(id)
    except Exception as e:
        return e
