from datetime import datetime, date
from typing import List, Optional
from sqlalchemy import String, Integer, Float, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(30), nullable=False)
    
    sales: Mapped[List["Sale"]] = relationship("Sale", back_populates="user")

class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    company_name: Mapped[str] = mapped_column(String(100), nullable=False)
    tax_id: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    
    batches: Mapped[List["MedicineBatch"]] = relationship("MedicineBatch", back_populates="supplier")

class Medicine(Base):
    __tablename__ = "medicines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    barcode: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    trade_name: Mapped[str] = mapped_column(String(100), nullable=False)
    active_ingredient: Mapped[str] = mapped_column(String(100), nullable=False)
    laboratory: Mapped[str] = mapped_column(String(100), nullable=False)
    requires_prescription: Mapped[bool] = mapped_column(Boolean, default=False)
    min_stock: Mapped[int] = mapped_column(Integer, default=10)
    
    batches: Mapped[List["MedicineBatch"]] = relationship("MedicineBatch", back_populates="medicine")

class MedicineBatch(Base):
    __tablename__ = "medicine_batches"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    medicine_id: Mapped[int] = mapped_column(ForeignKey("medicines.id"), nullable=False)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
    batch_number: Mapped[str] = mapped_column(String(50), nullable=False)
    expiration_date: Mapped[date] = mapped_column(Date, nullable=False)
    available_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    purchase_price: Mapped[float] = mapped_column(Float, nullable=False)

    medicine: Mapped["Medicine"] = relationship("Medicine", back_populates="batches")
    supplier: Mapped["Supplier"] = relationship("Supplier", back_populates="batches")

class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)
    payment_method: Mapped[str] = mapped_column(String(30), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="sales")