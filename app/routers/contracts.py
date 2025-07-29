from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.get("/property/{property_id}", response_model=List[schemas.Contract])
def read_contracts(property_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_contracts_for_property(db, property_id, skip, limit)

@router.post("/", response_model=schemas.Contract)
def create_contract(contract: schemas.ContractCreate, db: Session = Depends(database.get_db)):
    return crud.create_contract(db, contract)
