import uvicorn
from fastapi import FastAPI, Request
#from fastapi_pagination.middleware import PaginationMiddleware
from fastapi_pagination import Page, paginate, add_pagination
from db_postgresql import create_all_tables
from .routers import customers, transactions, plan

app = FastAPI(lifespan=create_all_tables)

# 1. Añade el middleware de paginación
#app.add_middleware(PaginationMiddleware)

# 2. Incluye tus routers
app.include_router(customers.router)
app.include_router(plan.router)
app.include_router(transactions.router)

# 3. Añade el soporte de paginación para SQLAlchemy/SQLModel
add_pagination(app)

@app.middleware("http") 
async def log_request_headers(request: Request, call_next):
    
    print("Request Headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")
    response = await call_next(request) 
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)