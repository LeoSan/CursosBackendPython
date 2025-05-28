from enum import Enum
from pydantic import BaseModel, EmailStr, field_validator
from sqlmodel import Field, SQLModel, Relationship, Session, select
from db_postgresql import engine
from typing import List, Optional

## llave valor 
class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

## Plan 

class CustomerPlan(SQLModel, table=True):## Tabla pivote 
    id: int = Field(primary_key=True)
    plan_id: int = Field(foreign_key="plan.id")
    customer_id: int = Field(foreign_key="customer.id")
    status:StatusEnum = Field(default=StatusEnum.ACTIVE)


class Plan(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default=None)
    price: int = Field(default=None)
    descripcion: str = Field(default=None)
    customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan) ## Relacion de muchos a muchos

## Clientes 

class CustomerBase(SQLModel):  
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):## usamos cls ya que el self es usaod para metodos de instancias para este aso pasamos a cls y aplicamos decorador @classmethod
        session = Session(engine)
        query = select(Customer).where(Customer.email == value)
        result = session.exec(query).first()
        if result:
            raise ValueError("Este correo ya esta registrado")
        return value


class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass 

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")
    plans: list[Plan] = Relationship(
        back_populates="customers", link_model=CustomerPlan
    )


## Transacciones 
class TransactionBase(SQLModel):
    ammount: int
    description: str

class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: Customer = Relationship(back_populates="transactions")

class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id")

class PaginatedTransactionsResponse(SQLModel):
    total_count: int  # Total de elementos
    total_pages: int   # Total de páginas
    current_page: int  # Página actual
    limit: int         # Límite de elementos por página
    transactions: List["Transaction"]  #

# Modelo para la respuesta de Transaction
class TransactionRead(TransactionBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


## Facturas 
class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property## Visiviliza esta variable como variable de clase 
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)