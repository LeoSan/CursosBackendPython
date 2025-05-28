# Curso de FastAPI
> Crea y conecta APIs modernas con FastAPI y Python. Estructura proyectos, valida datos, organiza modelos, añade autenticación, relaciones y pruebas, y optimiza consultas y rendimiento usando SQLModel y Pydantic.

- Profesor: Luis Martínez
- Fecha Inicio: 23/Mayo/2025  
- Fecha Fin: 

## Clase 1: Creación de APIs rápidas y eficientes con FastAPI

## ¿Por qué FastAPI es revolucionario en la creación de APIs?
FastAPI permite desarrollar APIs de alto rendimiento sin complicaciones de configuración, lo que la convierte en una herramienta ideal para aplicaciones que demandan velocidad y escalabilidad. Con este framework, Python puede competir con los lenguajes más rápidos, ofreciendo una experiencia de desarrollo sencilla y poderosa. Algunas características que lo hacen destacar incluyen:

- Velocidad: Utiliza las capacidades de Python y aprovecha tipado y optimización de datos para maximizar el rendimiento.
- Simplicidad: Gracias a su diseño intuitivo y buena documentación, se adapta tanto a principiantes como a expertos.
- Escalabilidad: Ideal para aplicaciones de misión crítica, soporta grandes volúmenes de tráfico, usado por empresas de alto nivel.

## 
- enlace -> https://fastapi.tiangolo.com/
```Python

```


## Clase 2: Creación de APIs con FastAPI: Framework Rápido y Versátil


## ¿Cómo funciona FastAPI internamente?
FastAPI está basado en dos frameworks principales:

- Starlette: Gestiona las solicitudes HTTP, permitiendo a la API recibir y responder peticiones de manera eficiente.
- Pydantic: Facilita la creación de modelos de datos. Con estos modelos, puedes estructurar la información para agregar, modificar o eliminar datos en la API de forma controlada y validada.

```Python

```

## Clase 3: Creación de Entornos Virtuales y Configuración de FastAPI


## Pasos 
- Paso 1: Primero generamos un entorno -> ´python3 -m venv fastapivenv´ -> ´source fastapivenv/bin/activate´
- Paso 2: Instalamos fastAPI -> 'pip3 install "fastapi[standar]"'
- Paso 2: Instalamos fastAPI -> 'pip install uvicorn'
- Paso 4: creamos un repositorio para gestionar el API -> ´mkdir curso-fastapi-project´ -> cd curso-fastapi-project
- Paso 5: creamos el archivo main.py dentro del repositorio creado del proyecto -> ´touch main.py´
- Paso 6: este archivo es tu server 

```Python

## Ejemplo 
import arrow
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/time")
async def time():
    return {"curren_time": arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```
- Paso 6: ejecutar el api -> ´uvicorn main:app --reload´
- Paso 7: podemos acceder de manera local
    -  swangger ->  http://127.0.0.1:8000/docs 
    - local     ->  http://127.0.0.1:8000/


## Clase 4: Crear un Endpoint Dinámico con FastAPI para Obtener Hora por País y Formato
> Manera de pasar variables usando el decorador 


```Python

import arrow
import zoneinfo
from datetime import datetime
import uvicorn
from fastapi import FastAPI

app = FastAPI()

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

```

## Clase 5: Validación de datos con Pydantic en FastAPI: Creación de endpoints
> Para crear un endpoint dinámico y seguro en FastAPI, es fundamental validar la información recibida, especialmente si el contenido se envía en el cuerpo de la solicitud.

## ¿Cómo estructurar un modelo de datos en FastAPI?
Para definir un modelo de datos, FastAPI emplea Pydantic, que permite usar clases para representar un esquema y validar la información que ingresa. Los pasos iniciales incluyen:

## Importar BaseModel de Pydantic.
Crear una clase llamada Customer que herede de BaseModel.
Definir campos dentro de la clase con sus tipos, por ejemplo, name: str para el nombre y age: int para la edad.
Utilizar typing para permitir múltiples tipos de datos, como en el campo description, que podría ser de tipo str o None (opcional).

En FastAPI, se utiliza async para definir endpoints con el fin de aprovechar la programación asíncrona. Esto permite manejar múltiples solicitudes de manera concurrente sin bloquear el hilo principal. Al realizar operaciones que pueden tardar, como consultas a bases de datos o llamadas a APIs externas, async ayuda a mejorar el rendimiento y la capacidad de respuesta de la aplicación,

```Python
# main.py

import arrow
import zoneinfo
from datetime import datetime
import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel 

class Customer(BaseModel):
    name:str
    descripcion:str|None
    email:str 
    age:int 

@app.post("/customers")
async def create_customer(customer_data: Customer):
    """
        Una forma sencilla para documentar tu método 
    """
    return customer_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```


## Clase 6: Modelado de Datos y Conexión de Modelos en FastAPI
> Para diseñar una API robusta, es esencial modelar correctamente los datos, especialmente al crear nuevos modelos que organicen y relacionen la información eficientemente. En esta guía, exploraremos cómo crear modelos en FastAPI para estructurar datos, conectar modelos y optimizar la funcionalidad de nuestra API

## Pasos: 
- Paso 1: Podemos aplicar la estructuración MVC para manejar nuestro FASTAPI iniciamos creando el archivo modelo.py y ahí anexamos nuestros modelos. 

- Paso 2: Creamos nuestro  modelo en nuestro model.py 

```Python
from pydantic import BaseModel


class Customer(BaseModel):
    id: int
    name: str
    description: str | None
    email: str
    age: int

class Transaction(BaseModel):
    id: int
    ammount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property## Visiviliza esta variable como variable de clase 
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)

```
- Paso 3: importamos desde main.py los modelos y en nuestros endpoint podemos aplicar y usar nuestro modelo 

```Python

@app.post("/customers")
async def create_customer(customer_data: Customer):
    """
        Una forma sencilla para documentar tu método 
    """
    return customer_data

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

```

## Clase 7: Validación de Datos y Modelos en Endpoints de FastAPI
> La validación de datos y la gestión de modelos en FastAPI permite crear endpoints seguros y eficientes. En este ejemplo, mostramos cómo manejar un modelo para recibir y devolver datos sin exponer identificadores innecesarios

## Notas: 
- Podemos usar el metodo de pydantic para crear validaciones sencillas desde el modelo ´model_validate´

```Python

db_customers: list[Customer] = []

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump()) ## Aqui la magia 
    # Ausmiendo que hace base de datos
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer

```


## Clase 8: Conexión de FastAPI con SQLite usando SQLModel
> Para conectar FastAPI con una base de datos real, primero configuraremos una base de datos SQLite utilizando la librería SQLModel, que facilita la integración sin necesidad de escribir SQL. SQLModel combina Pydantic y SQLAlchemy, permitiendo que nuestros modelos se almacenen directamente en bases de datos con una sintaxis simplificada

## PASOS

## ¿Cómo instalar y configurar SQLModel?
1. Instalación: Abre la terminal y ejecuta:

    pip install sqlmodel

También es recomendable registrar las dependencias en un archivo requirements.txt, como SQLModel y FastAPI con sus respectivas versiones. Esto ayuda a instalar todas las dependencias en otros entornos fácilmente.

2. Creación del archivo de configuración:

Crea un archivo db.py.
Importa las clases Session y create_engine de SQLModel para gestionar la conexión.
Define las variables para la conexión, como la URL de la base de datos, en este caso sqlite:///database_name.db.

3. Creación del engine:

Utiliza create_engine con la URL de la base de datos para crear el motor que gestionará las sesiones.
```Python

from fastapi import FastAPI
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

```

4. Importamos la conexion donde deseamos usarlo 

```Python

# main.py 

from db import SessionDep ## Paso 1

db_customers: list[Customer] = []


@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep): ## Paso 2
    customer = Customer.model_validate(customer_data.model_dump())
    # Ausmiendo que hace base de datos
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer

```
4. Debemos usar el SQLModel en nuestro modelo para generar las tablas deseadas 
## Ejemplo 
> Como podemos ver usamos la clase SQLModel que permite configurar nuestras clases para generar tablas lo primordial es enviar como parametro tambien table=True para que funcione  ->  Customer(SQLModel, table=True): 

```python

from pydantic import BaseModel
from sqlmodel import Field, SQLModel 


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None
    email: str
    age: int


```

## Clase 9: Integración de SQLModel en FastAPI para Manejo de Bases de Datos
> 

## Pasos 
- Paso 1: Debemos crear el metodo para generar la tablas en la base de datos 

```Python
def create_all_tables(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield ## Indicamos que use esta funcionalidad a otro llamado 



```

- Paso 2: Ubicamos main.py y en la configuración de app restablecemos lo que necesitamos -> lifespan=create_all_tables

```Python

app = FastAPI(lifespan=create_all_tables) ## lifespan nos permite ejecutar un metodo al comienzo o al final que se inicia el APP (server) para este caso -> create_all_tables() lo definimos en el archivo db_postgresql
```
- Paso 3: configuramos nuestro endpoint, notese que agregamos add(), commit(), refresh() esto nos permite interactuar ya con la base de datos 
```python 
#main.py 

@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)## Ejecuta la sentencia 
    session.commit()## Aplica los cambios 
    session.refresh(customer)##refresca el modelo con lo nuevo 
    return customer
```


## Clase 10 y 11: Find, Create, Update, Delete Gestión de Endpoints en FastAPI para CRUD de Clientes
> Dejo la manera de ejemplo de CRUD
- Archivo de referencia [Enlace](../08_Curso_FastAPI/practica/curso-fastapi-project/app/routers/customers.py)

## Buscar ID

```Python
@router.get("/customers/{customer_id}", response_model=Customer, tags=['customers'])
async def read_customer(customer_id: int, session: SessionDep):
    """
        End Point para buscar por id
    """
    customer_db = session.get(Customer, customer_id)
    if not  customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return customer_db

```

## Update 
```Python
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

```

## Delete 
```Python

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

```

## Clase 12: Estructuración de Aplicaciones con FastAPI y API Router
> Se sugiere una estructura muy baga, aquí un ejemplo practico 
- Se sugiere aplicar arquitectura Limpia
- Se sugiere aplicar arquitectura Exagonal 
- Imagen Muestra ![Ejemplo](../08_Curso_FastAPI/info/info_001.png)
- Se tomará este proyecto básico como referencia [Enlace Aqui](../08_Curso_FastAPI/practica/curso-fastapi-project/app/main.py)
- Haciendo esta estructura debemos cambiar la forma de ejeuctar el comando -> ´uvicorn app.main:app --reload´
- Se implementa la mejora de Router

```python

import arrow
import zoneinfo
from datetime import datetime
import uvicorn
from fastapi import FastAPI
from db_postgresql import create_all_tables
from .routers import customers

app = FastAPI(lifespan=create_all_tables) 

app.include_router(customers.router)

```

## Clase 13: Relaciones en FastAPI y SQL Model: Creación y Uso Práctico
> os modelos de datos en bases de datos relacionales permiten organizar y relacionar información sin duplicarla en múltiples tablas, optimizando así la gestión de datos. Al usar FastAPI y SQLModel, es posible configurar estas relaciones en los modelos que luego reflejarán las tablas en la base de datos, permitiendo un acceso eficiente y estructurado a los datos.

## Notas mentales 
- Para las relaciones podemos importar **Relationship** de nuestra libreria **sqlmodel**
- Para este ejempli es una relacion de un cliente puede tener muchas transacciones por lo que es 1..m 
- Como sabemos en la tabla hija va la id del padre como vemos en el ejemplo 
- foreign_key: Define la clave foránea en el modelo.
- Relationship: Establece una relación entre tablas.
- back_populates: Conecta las relaciones en ambas direcciones.

```python
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

```

## Clase 14: Relaciones Muchos a Muchos en Bases de Datos con SQLModel
> Las relaciones de muchos a muchos en bases de datos nos permiten asociar múltiples elementos de una tabla con muchos elementos de otra, utilizando una tabla intermedia. Esta tabla de enlace facilita las conexiones entre ambos elementos, permitiendo una mayor flexibilidad en la organización y gestión de los datos

## Notas mentales 
- Primer paso se genera una tabla pivote ver ejemplo 
- Segundo en la tabla Padre llevara esta nomeclatura -> customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan) ## Relacion de muchos a muchos
- Tercero la otra tabla Padre llevara la siguiente nomeclatura ->  plans: list[Plan] = Relationship(
        back_populates="customers", link_model=CustomerPlan
    )
- Para este Ejemplo la tabla pivote es CustomerPlan y esta tiene la ids de las tablas padres Plan y  Customer


```python
class CustomerPlan(SQLModel, table=True):## Tabla pivote 
    id: int = Field(primary_key=True)
    plan_id: int = Field(foreign_key="plan.id")
    customer_id: int = Field(foreign_key="customer.id")


class Plan(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default=None)
    price: int = Field(default=None)
    descripcion: str = Field(default=None)
    customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan) ## Relacion de muchos a muchos

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")
    plans: list[Plan] = Relationship(
        back_populates="customers", link_model=CustomerPlan
    )

```

## Clase 15: Creación y Suscripción de Planes y Clientes en FastAPI
> 
```python
from fastapi import APIRouter
from sqlmodel import select

from db_postgresql import SessionDep
from models import Plan

router = APIRouter()


@router.post("/plans")
async def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db


@router.get("/plans", response_model=list[Plan])
async def list_plan(session: SessionDep):
    # plans = session.execute(select(Plan)).all()
    plans =session.execute(select(Plan)).scalars().all()
    return plans
```

## Clase 16: Consultas Avanzadas con SQL Model y Filtrado de Estados en FastAPI
> Uso del Query
## nota mental
- from fastapi import  Query -> este hace la magia de enviar valores  por get 

```python
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

```

## Clase 17: Validación de Emails Únicos en Bases de Datos con Pydantic y FastAPI
> La validación efectiva de datos es crucial en el desarrollo de software, especialmente cuando se habla de correos electrónicos. Con herramientas como FastAPI y Pydantic, puedes asegurar no solo que tus e-mails tengan el formato adecuado, sino también que sean únicos dentro de tu base de datos.

## Notas mentales 
- from pydantic import EmailStr importar y usar en el modelo 
- https://docs.pydantic.dev/2.0/usage/types/string_types/#emailstr
- from pydantic import  field_validator =>  para realizar validaciones personalizadas 

```python

class CustomerBase(SQLModel):  
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

```

## Clase 18: Implementación de Paginación en FastAPI con SQLModel
> El profesor se paso de maniaco explica hacerlo manual el paginador cosa que ya con un plugin se puede hacer usaremos para este caso pip install fastapi-pagination

## Nota Mental 
- Sin embargo se dejan los ejemplos de hacer un paginador a manita y otro ejemplo usando el plugin [Enlace](../08_Curso_FastAPI/practica/curso-fastapi-project/app/routers/transactions.py)


## Pasos usando pip install fastapi-pagination
- Paso 1: instalar -> ´pip install fastapi-pagination´
- Paso 2:  

```python

```

## Clase 19: 
> 
```python

```
## Clase 20: 
> 
```python

```

## Clase 21: 
> 
```python

```

## Clase 22 : 
> 
```python

```