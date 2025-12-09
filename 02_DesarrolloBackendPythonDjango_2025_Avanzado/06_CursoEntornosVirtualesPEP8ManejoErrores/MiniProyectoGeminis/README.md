# MiniProyecto Geminis

Este proyecto es un cliente de consola escrito en Python que interactúa con la API de Google Gemini.

## Estructura del Proyecto

El proyecto sigue una estructura modular profesional:

- `src/`: Contiene el código fuente de la aplicación.
    - `gemini_client.py`: Lógica de conexión y configuración del modelo.
    - `main.py`: Punto de entrada de la aplicación.
- `tests/`: Contiene las pruebas unitarias.
- `requirements.txt`: Lista de dependencias.

## Requisitos

- Python 3.8+
- Una API Key de Google AI Studio.

## Instalación

1.  Crear entorno virtual:
    ```bash
    python -m venv api_gemi
    ```
2.  Activar entorno:
    - Windows: `.\api_gemi\Scripts\activate`
    - Unix: `source api_gemi/bin/activate`
3.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4.  Configurar variables de entorno:
    - Crear un archivo `.env` en la raíz.
    - Añadir: `GEMINI_API_KEY=tu_api_key_aqui`

## Ejecución

Para correr la aplicación principal desde la raíz del proyecto:

```bash

\MiniProyectoGeminis> => python ./src/main.py
```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
\MiniProyectoGeminis> => python -m unittest discover tests
```


## Enlace 
- https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419 => Aqui podemos ver las capacicades principales podemos validar como generar texto, generar imagenes, video, voz, etc. 