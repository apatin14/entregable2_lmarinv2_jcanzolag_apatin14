from fastapi import FastAPI
from routes.record_routes import routes_record

app = FastAPI()

app.include_router(routes_record, prefix="/records")