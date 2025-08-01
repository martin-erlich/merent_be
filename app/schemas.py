from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    name: str
    last_name: str
    phone: Optional[str] = None
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

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
    owner_ids: List[int] = []

class Property(PropertyBase):
    id: int
    owners: List[User] = []

    class Config:
        orm_mode = True

class ContractBase(BaseModel):
    property_id: int
    landlord_id: int
    tenant_id: int
    monthly_rent: float
    deposit: float
    start_date: date
    end_date: date
    include_taxes: bool
    include_fees: bool
    status: str

class ContractCreate(ContractBase):
    pass

class Contract(ContractBase):
    id: int
    property: Property
    landlord: User
    tenant: User

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    contract_id: int
    amount: float
    date: date
    due_date: datetime
    paid_at: Optional[datetime] = None
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
