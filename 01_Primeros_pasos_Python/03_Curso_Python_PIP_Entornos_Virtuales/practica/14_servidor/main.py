import uvicorn
import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

#Nuestro Decorador generamos al ruta 
@app.get('/')
def get_list():
      return [1,2,3]

@app.get('/contactos')
def get_list():
      return [
            {'Nombre':'Kenny', 'telefono':123456789}, 
            {'Nombre':'Leo', 'telefono':123456789}, 
            {'Nombre':'mamá', 'telefono':123456789}, 
            {'Nombre':'papá', 'telefono':123456789}, 
        ]

@app.get('/web', response_class=HTMLResponse)
async def read_items():
    return """
    <html>
    <head>
    <title>Hola Soy Pagina Web en Servidor Python </title>
    </head>
    <body>
        <h1 style="color:red">Hola Soy Pagina Web en Servidor PythonL!</h1>
        <h3>Me sorprende lo <b>rapido</b> y comodo!</h2>
    </body>
    </html>
"""


def run():
    store.get_categorias()
    uvicorn.run("main:app", reload=True, port=8034)

if __name__ == '__main__':
        run()