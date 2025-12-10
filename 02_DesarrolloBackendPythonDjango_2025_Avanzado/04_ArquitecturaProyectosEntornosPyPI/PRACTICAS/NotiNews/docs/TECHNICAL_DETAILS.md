# Documentación Técnica de NotiNews

## 1. Introducción
**NotiNews** es una aplicación de línea de comandos (CLI) moderna diseñada para buscar noticias en tiempo real y enriquecerlas mediante análisis de Inteligencia Artificial. Su objetivo principal es demostrar una arquitectura robusta, modular y profesional utilizando las últimas tecnologías del ecosistema Python.

## 2. Tecnologías y Herramientas Utilizadas

Este proyecto ha sido construido seleccionando cuidadosamente herramientas que representan el estado del arte en el desarrollo con Python en 2025.

### 🐍 Python 3.13+
Utilizamos la versión más reciente de Python para aprovechar las últimas mejoras de rendimiento y características del lenguaje. Python es el lenguaje estándar para IA y scripting debido a su legibilidad y vasto ecosistema.

### ⚡ uv (Universal Python Package Manager)
En lugar de usar `pip` y `venv` tradicionales, utilizamos **uv**.
-   **¿Por qué?**: Es extremadamente rápido (escrito en Rust), gestiona dependencias de manera determinista y simplifica la creación de entornos virtuales.
-   **Función**: Reemplaza a `pip`, `pip-tools` y `virtualenv` en un solo comando unificado.

### 🤖 Google Gemini (Generative AI)
El "cerebro" de la aplicación.
-   **Modelo**: `gemini-2.5-flash` (configurable).
-   **Librería**: `google-generativeai`.
-   **Uso**: Analiza el contenido de los artículos obtenidos para responder preguntas naturales del usuario (ej. "¿Qué opinan los expertos sobre este tema?").
-   **Ventaja**: Ofrece un balance excepcional entre velocidad, costo y calidad de razonamiento comparado con modelos anteriores.

### 📰 NewsAPI
La fuente de datos.
-   **Función**: Provee acceso programático a titulares y artículos de miles de fuentes de noticias a nivel mundial.
-   **Integración**: Se conecta vía HTTP para traer JSONs con metadatos de noticias.

### 🛡️ Pydantic (Validación de Datos)
-   **Clase `Settings`**: Gestiona la configuración (API Keys, modelos) validando que existan y tengan el formato correcto al inicio.
-   **Clase `Article`**: Define la estructura de datos de un artículo, asegurando que siempre tengamos título, descripción y URL válidos, evitando errores en tiempo de ejecución.

### 🎨 Rich (Interfaz de Usuario)
-   **Función**: Transforma la terminal aburrida en una experiencia visual rica.
-   **Características**: Tablas formateadas, colores, spinners de carga y renderizado de Markdown directamente en la consola.

## 3. Arquitectura del Sistema

El proyecto sigue una arquitectura modular para facilitar el mantenimiento y la escalabilidad.

```
src/noti_news/
├── analysis/       # Lógica de IA
│   └── analyzer.py # Clase GeminiAnalyzer
├── core/           # Dominio y Reglas de Negocio
│   ├── models.py   # Definiciones de datos (Article)
│   ├── services.py # Orquestador (NewsService)
│   └── exceptions.py # Manejo de errores personalizados
├── io/             # Entrada/Salida
│   ├── cli.py      # Interfaz de Línea de Comandos (Click/Argparse)
│   └── display.py  # Renderizado con Rich
├── sources/        # Conectores a APIs Externas
│   └── newsapi.py  # Cliente HTTP para NewsAPI
└── config.py       # Gestión de configuración (Variables de entorno)
```

## 4. Flujo de Funcionamiento (Workflow)

Cuando un usuario ejecuta un comando como `uv run noti-news ask "Python" "¿Es popular?"`, sucede lo siguiente:

1.  **Inicialización (`main.py` -> `cli.py`)**:
    -   Se carga la configuración (`config.py`) y se validan las API Keys.
    -   Se instancia el `NewsService`.

2.  **Búsqueda (`NewsService` -> `NewsAPI`)**:
    -   El servicio solicita noticias sobre "Python" al cliente `NewsAPI`.
    -   `NewsAPI` hace una petición HTTP GET.
    -   Los datos JSON crudos se convierten en objetos `Article` validados por Pydantic.

3.  **Análisis (`NewsService` -> `GeminiAnalyzer`)**:
    -   Si el usuario hizo una pregunta, el servicio envía los objetos `Article` y la pregunta al `GeminiAnalyzer`.
    -   Se construye un "prompt" que incluye el contexto de las noticias.
    -   Se envía a Google Gemini para generar una respuesta en lenguaje natural.

4.  **Visualización (`cli.py` -> `display.py`)**:
    -   La librería `Rich` recibe los objetos y la respuesta.
    -   Imprime una tabla elegante con los artículos y la respuesta de la IA formateada en la terminal.

## 5. Calidad de Código y Pruebas
El proyecto incluye una suite de pruebas automatizadas (`tests/`) que utiliza `unittest.mock`. Esto permite verificar el funcionamiento de todo el sistema sin gastar créditos reales de las APIs ni requerir conexión a internet durante el desarrollo.



## aditamentos para el desarrollo 
- RUFF:  se instala ruff para reglas pep8 de python se isntala ´uv add ruff´ se usa ´uv run ruff format .´ -> https://docs.astral.sh/ruff/configuration/ => https://docs.astral.sh/ruff/configuration/#python-file-discovery