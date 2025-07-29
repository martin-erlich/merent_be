from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

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

    contracts = relationship('Contract', back_populates='property')

class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    tenant_name = Column(String)
    monthly_rent = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    include_taxes = Column(Boolean)
    include_fees = Column(Boolean)
    status = Column(String)

    property = relationship('Property', back_populates='contracts')
    payments = relationship('Payment', back_populates='contract')

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    amount = Column(Float)
    date = Column(Date)
    method = Column(String)
    reference = Column(String)
    receipt_filename = Column(String)
    status = Column(String)

    contract = relationship('Contract', back_populates='payments')
