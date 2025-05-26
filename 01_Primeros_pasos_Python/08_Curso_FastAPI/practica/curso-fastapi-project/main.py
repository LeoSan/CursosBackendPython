import arrow
import zoneinfo
from datetime import datetime
import uvicorn
from fastapi import FastAPI
from db_postgresql import SessionDep, create_all_tables
from sqlmodel import select 

from models import Customer, Transaction, Invoice, CustomerCreate



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

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)## Ejecuta la sentencia 
    session.commit()## Aplica los cambios 
    session.refresh(customer)##refresca el modelo con lo nuevo 
    return customer


@app.get("/customers", response_model=list[Customer])
async def list_customer(session: SessionDep):
    customers = session.execute(select(Customer)).scalars().all()
    return customers


@app.post("/transaction")
async def create_customer(transaction_data: Transaction):
    """
        Una forma sencilla para documentar tu método 
    """
    return transaction_data

@app.post("/invoice")
async def create_customer(invoice_data: Invoice):
    """
        Una forma sencilla para documentar tu método 
    """
    return invoice_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    