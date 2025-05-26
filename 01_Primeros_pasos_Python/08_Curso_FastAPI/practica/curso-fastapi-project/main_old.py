import arrow
import zoneinfo
from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException, status
from db_postgresql import SessionDep, create_all_tables
from sqlmodel import select 

from models import Customer, Transaction, Invoice, CustomerCreate, CustomerUpdate 



app = FastAPI(lifespan=create_all_tables) ## Metodo ejeucta esto al comienzo o al final 

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time-with-arrow")
async def time(iso_code:str):
    return {"curren_time": arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")}

@app.get("/time-with-datetime/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}

@app.get("/customers", response_model=list[Customer])
async def list_customer(session: SessionDep):
    """
        End Point para listar todos los clientes
    """
    customers = session.execute(select(Customer)).scalars().all()
    return customers

@app.get("/customers/{customer_id}", response_model=Customer)
async def read_customer(customer_id: int, session: SessionDep):
    """
        End Point para buscar por id
    """
    customer_db = session.get(Customer, customer_id)
    if not  customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return customer_db

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    """
        End Point para crear cliente
    """
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)## Ejecuta la sentencia 
    session.commit()## Aplica los cambios 
    session.refresh(customer)##refresca el modelo con lo nuevo 
    return customer

@app.delete("/customers/{customer_id}")
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



@app.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
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



@app.post("/transaction")
async def create_customer(transaction_data: Transaction):
    """
        Una forma sencilla para documentar tu método 
    """
    return transaction_data

@app.post("/invoice")
async def create_customer(invoice_data: Invoice):
    return invoice_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    