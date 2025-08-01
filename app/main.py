from fastapi import FastAPI
from .database import engine, Base
from .routers import properties, contracts, payments, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Property Management POC", version="0.1.0")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(properties.router, prefix="/properties", tags=["properties"])
app.include_router(contracts.router, prefix="/contracts", tags=["contracts"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Property Management API"}
