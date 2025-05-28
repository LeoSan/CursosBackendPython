import pytest # Lobreria 
from fastapi.testclient import TestClient # Emula acciones de HTTP get,post, Etc 
from sqlalchemy import create_engine # Nos permite crear seccion y motores de bases de datos 
from sqlalchemy.pool import StaticPool# Permite generar base de datos en memoria 
from sqlmodel import Session, SQLModel

from app.main import app
from db_postgresql import get_db

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine( ## Aqui creamos el motor de base de datos 
    sqlite_url,
    connect_args={"check_same_thread": False},## Evitar que se ejecuten codigo de manera simultanea
    poolclass=StaticPool, ## Crear la base de datos en manera temporal y en memoria 
) ## Entorno 


@pytest.fixture(name="session") ## configuración de pruebas fixture Que hace: nos va devolver lo que rretorne yield, nos permite conectar con la base de datos es nuestro conex 
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session ## Seder esta variable para la proxima funcion que esta delegando
    SQLModel.metadata.drop_all(engine)## Ojo con esto usamos la de SQLmodel no la de pytes 


@pytest.fixture(name="client") ##  se pueden reutilizar fixture en otras 
def client_fixture(session: Session):
    def get_db_override():
        return session

    app.dependency_overrides[get_db] = get_db_override # impprtamos nuestra app de creada de app = FastAPI(lifespan=create_all_tables) que esta en APP/main.py
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()