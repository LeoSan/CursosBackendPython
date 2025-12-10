# NotiNews 📰🤖

**NotiNews** (anteriormente Platzi News) es una aplicación de línea de comandos (CLI) moderna desarrollada en Python. Permite buscar noticias en tiempo real y enriquecerlas mediante inteligencia artificial para responder preguntas contextuales.

**Características Principales:**
- 🔍 **Búsqueda Global**: Integra **NewsAPI** para buscar titulares en miles de fuentes internacionales.
- 🧠 **Análisis con IA**: Utiliza **Google Gemini** (gemini-2.5-flash) para leer, resumir y responder preguntas sobre las noticias encontradas.
- 🚀 **Tecnología Moderna**: Construido con Python 3.13+, `uv`, Pydantic y Rich para una experiencia de desarrollo y uso profesional.

## Requisitos Previos

- **Python 3.13** o superior.
- **uv** (Gestor de paquetes moderno). [Instalar uv](docs/SETUP_UV.md).
- Claves de API válidas:
    - **News API**: [Obtener clave gratis](https://newsapi.org/)
    - **Google AI Studio**: [Obtener clave de Gemini](https://aistudio.google.com/)

## Instalación Rápida

Sigue nuestra guía detallada en [SETUP_UV.md](docs/SETUP_UV.md) o ejecuta:

```bash
# 1. Crear entorno virtual
uv venv

# 2. Instalar dependencias y el proyecto
uv pip install -e .
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto copiando el siguiente formato:

```env
# Claves OBLIGATORIAS
NEWSAPI_API_KEY=tu_clave_de_newsapi_aqui
GOOGLE_API_KEY=tu_clave_de_google_aqui

# Configuración Opcional (valores por defecto mostrados)
# GEMINI_MODEL=gemini-2.5-flash
# MAX_ARTICLES=10
# REQUEST_TIMEOUT=15
```

## Uso

Una vez instalado, usa el comando `uv run noti-news`.

### 1. Buscar Noticias
Obtén un listado de los artículos más recientes sobre un tema.

```bash
# Uso básico
uv run noti-news search "Python 3.13"

# Ver logs detallados (útil para depuración)
uv run noti-news --log-level DEBUG search "Inteligencia Artificial"
```

### 2. Preguntar a la IA
Combina la búsqueda con el poder de Gemini. La IA leerá los artículos por ti y responderá tu pregunta basándose únicamente en esa información reciente.

```bash
# Sintaxis: ask "TEMA_BUSQUEDA" "PREGUNTA"
uv run noti-news ask "Cambio Climático" "¿Cuáles son las soluciones más mencionadas?"
```

## Estructura del Proyecto

Para más detalles técnicos, consulta [docs/TECHNICAL_DETAILS.md](docs/TECHNICAL_DETAILS.md).

```
src/noti_news/
├── analysis/       # Lógica con Google Gemini
├── core/           # Modelos y excepciones (Dominio)
├── io/             # CLI y visualización (Rich)
└── sources/        # Integración con NewsAPI
```

## Desarrollo y Pruebas

Para ejecutar la suite de pruebas automatizadas (30 tests):

```bash
# Opción 1: Script de ayuda
python run_tests.py

# Opción 2: Usando uv
uv run python -m unittest discover tests
```

---
*Desarrollado con fines educativos para el Curso de Python Profesional.*
