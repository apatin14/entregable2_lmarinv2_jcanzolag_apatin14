from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.record_routes import routes_record

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_record, prefix="/records")
