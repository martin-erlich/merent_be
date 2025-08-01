from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float, Table, DateTime
from sqlalchemy.orm import relationship
from .database import Base

# Association table for many-to-many relationship between users and properties
property_owners = Table(
    'property_owners',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('property_id', Integer, ForeignKey('properties.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    phone = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)

    # Many-to-many relationship with properties (as owner)
    owned_properties = relationship('Property', secondary=property_owners, back_populates='owners')
    
    # One-to-many relationship with contracts (as landlord)
    landlord_contracts = relationship('Contract', foreign_keys='Contract.landlord_id', back_populates='landlord')
    
    # One-to-many relationship with contracts (as tenant)
    tenant_contracts = relationship('Contract', foreign_keys='Contract.tenant_id', back_populates='tenant')

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    type = Column(String)
    rooms = Column(Integer)
    size = Column(Float)
    neighborhood = Column(String)
    floor = Column(Integer)
    unit = Column(String)
    estimated_value = Column(Float)

    # Many-to-many relationship with users (owners)
    owners = relationship('User', secondary=property_owners, back_populates='owned_properties')
    
    # One-to-many relationship with contracts
    contracts = relationship('Contract', back_populates='property')

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    landlord_id = Column(Integer, ForeignKey('users.id'))
    tenant_id = Column(Integer, ForeignKey('users.id'))
    monthly_rent = Column(Float)
    deposit = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    include_taxes = Column(Boolean)
    include_fees = Column(Boolean)
    status = Column(String)

    # Relationships
    property = relationship('Property', back_populates='contracts')
    landlord = relationship('User', foreign_keys=[landlord_id], back_populates='landlord_contracts')
    tenant = relationship('User', foreign_keys=[tenant_id], back_populates='tenant_contracts')
    payments = relationship('Payment', back_populates='contract')

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    amount = Column(Float)
    date = Column(Date)
    due_date = Column(DateTime)
    paid_at = Column(DateTime, nullable=True)
    method = Column(String)
    reference = Column(String)
    receipt_filename = Column(String)
    status = Column(String)

    contract = relationship('Contract', back_populates='payments')
