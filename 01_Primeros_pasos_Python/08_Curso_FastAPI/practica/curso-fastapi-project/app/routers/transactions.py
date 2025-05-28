from fastapi import APIRouter, HTTPException, status, Query
from sqlmodel import select
#from fastapi_pagination import Page, paginate
from db_postgresql import SessionDep

from models import Customer, PaginatedTransactionsResponse, Transaction, TransactionCreate, TransactionRead

router = APIRouter()

@router.get("/transactions", tags=["transactions"])
async def list_transaction(session: SessionDep):
    """
        End Point para listar todas los transacciones 
    """
    transactions = session.execute(select(Transaction)).scalars().all()
    return transactions

@router.get("/transactions-paginado-manita", tags=["transactions"])
async def list_transaction_paginado_manita(
    session: SessionDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Número de registros"),
):
    """
        End Point para listar todas los transacciones paginado
    """
    # Consulta de transacciones con paginación
    query = select(Transaction).offset(skip).limit(limit)
    transactions = session.execute(query).scalars().all()## aqui era mi problema claro como estamos en postgresql se usa scalars
    return transactions


 # Endpoint usando fastapi-pagination

@router.get("/transactions-paginado-mejorado", response_model=PaginatedTransactionsResponse, tags=["transactions"])
async def list_transactions(
    session: SessionDep,
    skip: int = Query(0, description="Registros a omitir"),
    limit: int = Query(10, description="Número de registros por página"),
):
    # Consulta de transacciones con paginación
    query = select(Transaction).offset(skip).limit(limit)
    transactions = session.execute(query).scalars().all()

    print(transactions)
    # Obtener el total de registros en la base de datos (sin paginación)
    total_count_query = select(Transaction)
    total_count = len(session.execute(total_count_query).all())  # Contamos los registros

    # Calcular el total de páginas
    total_pages = (total_count + limit - 1) // limit  # Redondear hacia arriba

    # Crear la respuesta paginada
    response = PaginatedTransactionsResponse(
        total_count=total_count,
        total_pages=total_pages,
        current_page=(skip // limit) + 1,  # Calcular la página actual
        limit=limit,
        transactions=transactions
    )
    return response

"""
@router.get("/transactions-paginado-plugin", name="Obtiene todas las transacciones", tags=["transactions"], response_model=Page[Transaction])
def list_transaction_paginado(session: SessionDep):
    query = select(Transaction)
    return paginate(session, query)
"""

@router.post("/transactions", status_code=status.HTTP_201_CREATED, tags=["transactions"])
async def create_transation(transaction_data: TransactionCreate, session: SessionDep):
    """
        End Point para crear una transaccion
    """
    transaction_data_dict = transaction_data.model_dump()
    customer = session.get(Customer, transaction_data_dict.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )

    transaction_db = Transaction.model_validate(transaction_data_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)

    return transaction_db


