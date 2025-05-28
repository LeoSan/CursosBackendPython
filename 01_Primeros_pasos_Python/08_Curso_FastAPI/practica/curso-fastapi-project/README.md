.. image:: ./.github/assets/logo.png

|

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/API%20spec/badge.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/Tests/badge.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app

.. image:: https://github.com/nsidnev/fastapi-realworld-example-app/workflows/Styles/badge.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app

.. image:: https://codecov.io/gh/nsidnev/fastapi-realworld-example-app/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/nsidnev/fastapi-realworld-example-app

.. image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black

.. image:: https://img.shields.io/badge/style-wemake-000000.svg
   :target: https://github.com/wemake-services/wemake-python-styleguide

----------

""" 
Como parte de mis primeros pasos de conocer todo el entorno de Python estamos desarrollando practicas para aplicar lo aprendido realizando muchos minis proyectos este es mi primer avance en fastapi
"""
## Primero Explico la estructura 
> Como es mi primer avance esta una estructura sencilla se realiza así para comprender primero el uso de fastapi 
    app
    ├── router           - web routes.
    │   ├── dependencies - .
    │   └── main.py      - FastAPI aplicación creación y configuración.
    ├── db_postgresql.py - Conexion a la base de datos postgresql
    ├── requirements.txt - Documentación de las librerias instaladas.
    └── models.py        - Desarrollo de modelos y tablas para gestionar la base de datos.