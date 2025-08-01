from sqlalchemy.orm import Session
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()

def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Property).offset(skip).limit(limit).all()

def create_property(db: Session, prop: schemas.PropertyCreate):
    # Extract owner_ids from the schema
    owner_ids = prop.owner_ids
    property_data = prop.dict(exclude={'owner_ids'})
    
    db_prop = models.Property(**property_data)
    db.add(db_prop)
    db.commit()
    db.refresh(db_prop)
    
    # Add owners to the property
    if owner_ids:
        owners = db.query(models.User).filter(models.User.id.in_(owner_ids)).all()
        db_prop.owners = owners
        db.commit()
        db.refresh(db_prop)
    
    return db_prop

def create_monthly_payments(db: Session, contract_id: int, monthly_rent: float, start_date: date, end_date: date):
    """Create monthly payments for the entire contract duration"""
    print(f"Creating payments for contract {contract_id}")
    print(f"Monthly rent: {monthly_rent}")
    print(f"Start date: {start_date}")
    print(f"End date: {end_date}")
    
    current_date = start_date
    payment_number = 1
    payments_created = 0
    
    while current_date <= end_date:
        # Set due date to the 10th of the month
        due_date = current_date.replace(day=10)
        
        # If the 10th has already passed this month, move to next month
        if due_date < current_date:
            due_date = (current_date + relativedelta(months=1)).replace(day=10)
        
        print(f"Creating payment {payment_number}: due {due_date}")
        
        # Create payment record
        payment = models.Payment(
            contract_id=contract_id,
            amount=monthly_rent,
            date=current_date,
            due_date=due_date,
            paid_at=None,  # Not paid yet
            method="",
            reference=f"Rent {payment_number}",
            receipt_filename="",
            status="pending"
        )
        
        db.add(payment)
        payments_created += 1
        current_date = current_date + relativedelta(months=1)
        payment_number += 1
    
    db.commit()
    print(f"Created {payments_created} payments for contract {contract_id}")

def get_contracts_for_property(db: Session, property_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Contract).filter(models.Contract.property_id == property_id).offset(skip).limit(limit).all()

def create_contract(db: Session, contract: schemas.ContractCreate):
    print(f"Creating contract with monthly rent: {contract.monthly_rent}")
    print(f"Contract dates: {contract.start_date} to {contract.end_date}")
    
    # Validate that end date is after start date
    if contract.end_date <= contract.start_date:
        raise ValueError("End date must be after start date")
    
    db_contract = models.Contract(**contract.dict())
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    
    print(f"Contract created with ID: {db_contract.id}")
    
    # Create monthly payments for the entire contract duration
    create_monthly_payments(
        db=db,
        contract_id=db_contract.id,
        monthly_rent=contract.monthly_rent,
        start_date=contract.start_date,
        end_date=contract.end_date
    )
    
    return db_contract

def get_payments_for_contract(db: Session, contract_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).filter(models.Payment.contract_id == contract_id).offset(skip).limit(limit).all()

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
