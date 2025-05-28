from fastapi import APIRouter, HTTPException, Query, status
from sqlmodel import select

from db_postgresql import SessionDep
from models import (
    Customer,
    CustomerCreate,
    CustomerPlan,
    CustomerUpdate,
    Plan,
    StatusEnum,
)

router = APIRouter()

@router.get("/customers", response_model=list[Customer], tags=['customers'])
async def list_customer(session: SessionDep):
    """
        End Point para listar todos los clientes
    """
    customers = session.execute(select(Customer)).scalars().all()
    return customers

@router.get("/customers/{customer_id}", response_model=Customer, tags=['customers'])
async def read_customer(customer_id: int, session: SessionDep):
    """
        End Point para buscar por id
    """
    customer_db = session.get(Customer, customer_id)
    if not  customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return customer_db

@router.post("/customers", response_model=Customer, tags=['customers'])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    """
        End Point para crear cliente
    """
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)## Ejecuta la sentencia 
    session.commit()## Aplica los cambios 
    session.refresh(customer)##refresca el modelo con lo nuevo 
    return customer

@router.delete("/customers/{customer_id}", tags=['customers'])
async def delete_customer(customer_id: int, session: SessionDep):
    """
        End Point para eliminar cliente por ID
    """
    customer_db = session.get(Customer, customer_id)
    if not  customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    session.delete(customer_db)## Ejecuta la sentencia 
    session.commit()## Aplica los cambios 
    return {"detail":"OKI"}

@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED, tags=['customers'])
async def put_customer(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):  
    """
        End Point para modificar cliente por ID 
    """  
    customer_db = session.get(Customer, customer_id)
    if not  customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")

    customer = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer)
    session.add(customer_db)## Ejecuta la sentencia 
    session.commit()## Aplica los cambios 
    session.refresh(customer_db)##refresca el modelo con lo nuevo 
    return customer_db


@router.post('/customers/{customer_id}/plans/{plan_id}', tags=['customers'])
async def subscribe_customer_to_plan(customer_id: int, plan_id: int, session: SessionDep, plan_status:StatusEnum=Query() ):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)

    if not customer_db or not plan_db:
        raise HTTPException(status_code=404, detail="El customer o plan no existe")

    customer_plan_db = CustomerPlan(plan_id=plan_db.id, customer_id=customer_db.id, status=plan_status)
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_db)

    return customer_plan_db

@router.get("/customers/{customer_id}/plans")
async def subscribe_customer_to_plan(
    customer_id: int, session: SessionDep, plan_status: StatusEnum = Query()
):
    customer_db = session.get(Customer, customer_id)

    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    query = (
        select(CustomerPlan)
        .where(CustomerPlan.customer_id == customer_id)
        .where(CustomerPlan.status == plan_status)
    )
    plans = session.execute(query).all()
    return plans
##{"detail":"OKI"}