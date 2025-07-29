from datetime import date
from pydantic import BaseModel

class PropertyBase(BaseModel):
    address: str
    type: str
    rooms: int
    size: float
    neighborhood: str
    floor: int
    unit: str
    estimated_value: float

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int

    class Config:
        orm_mode = True

class ContractBase(BaseModel):
    property_id: int
    tenant_name: str
    monthly_rent: float
    start_date: date
    end_date: date
    include_taxes: bool
    include_fees: bool
    status: str

class ContractCreate(ContractBase):
    pass

class Contract(ContractBase):
    id: int

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    contract_id: int
    amount: float
    date: date
    method: str
    reference: str
    receipt_filename: str
    status: str

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True
