from sqlalchemy.orm import Session
from . import models, schemas

def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()

def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Property).offset(skip).limit(limit).all()

def create_property(db: Session, prop: schemas.PropertyCreate):
    db_prop = models.Property(**prop.dict())
    db.add(db_prop)
    db.commit()
    db.refresh(db_prop)
    return db_prop

def get_contracts_for_property(db: Session, property_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Contract).filter(models.Contract.property_id == property_id).offset(skip).limit(limit).all()

def create_contract(db: Session, contract: schemas.ContractCreate):
    db_contract = models.Contract(**contract.dict())
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

def get_payments_for_contract(db: Session, contract_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).filter(models.Payment.contract_id == contract_id).offset(skip).limit(limit).all()

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
