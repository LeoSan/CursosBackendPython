import arrow
import zoneinfo
from datetime import datetime
import uvicorn
from fastapi import FastAPI
from db_postgresql import create_all_tables
from .routers import customers

app = FastAPI(lifespan=create_all_tables) 

app.include_router(customers.router)


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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    