from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.get("/contract/{contract_id}", response_model=List[schemas.Payment])
def read_payments(contract_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_payments_for_contract(db, contract_id, skip, limit)

@router.post("/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(database.get_db)):
    return crud.create_payment(db, payment)
