FROM python:3.10.4

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", '/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/03_Curso_Python_PIP_Entornos_Virtuales/practica/14_servidor/main:app', "--host",  "--port", "8034"]