from fastapi import APIRouter
from router_server.routing import routingTier
from schemas.record import Record, update_hash, update_record_dto

_routingTier = routingTier()
routes_record = APIRouter()


@routes_record.post("/create")
def create(record: Record):
    try:
        # OPERATION CACHE
        return _routingTier.create_key_value(record.key, record.value)

    except Exception as e:
        return e


@routes_record.get("/get/{id}")
def get(id: str):
    try:
        # OPERATION CACHE
        return _routingTier.find_by_id(id)

    except Exception as e:
        return e


@routes_record.put("/update")
def update(record: update_record_dto):
    try:
        # OPERATION CACHE
        return _routingTier.update_by_id(record.id, record.value)

    except Exception as e:
        return e


@routes_record.delete("/delete/{id}")
def delete(id: str):
    try:
        return _routingTier.delete_by_id(id)
    except Exception as e:
        return e


@routes_record.post("/setHash")
def set_hash(hash: update_hash):
    try:
        # OPERATION CACHE
        return _routingTier.set_hash(hash)

    except Exception as e:
        return e
