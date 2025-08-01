from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import crud, schemas, database

router = APIRouter()

@router.get("/contract/{contract_id}", response_model=List[schemas.Payment])
def read_payments(contract_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_payments_for_contract(db, contract_id, skip, limit)

@router.get("/{payment_id}", response_model=schemas.Payment)
def read_payment(payment_id: int, db: Session = Depends(database.get_db)):
    payment = crud.get_payment(db, payment_id)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.put("/{payment_id}/status")
def update_payment_status(
    payment_id: int, 
    status: str, 
    paid_at: datetime = None, 
    receipt_filename: str = None,
    db: Session = Depends(database.get_db)
):
    """Update payment status, paid_at timestamp, and receipt_filename"""
    payment = crud.update_payment_status(db, payment_id, status, paid_at, receipt_filename)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": f"Payment {payment_id} status updated to {status}", "payment": payment}

@router.post("/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(database.get_db)):
    return crud.create_payment(db, payment)
