from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.get("/", response_model=List[schemas.Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_properties(db, skip, limit)

@router.post("/", response_model=schemas.Property)
def create_property(prop: schemas.PropertyCreate, db: Session = Depends(database.get_db)):
    return crud.create_property(db, prop)
