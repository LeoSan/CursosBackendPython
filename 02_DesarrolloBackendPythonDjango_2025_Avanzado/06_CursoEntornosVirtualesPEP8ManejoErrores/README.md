# Curso Entornos virtuales, PEP8 y Manejo de Errores 🚀

> Domina el código Python intermedio con proyectos reales. Aprende a escribir funciones limpias, usar type hints y manejar errores profesionales. Mejora tu lógica con comprensiones, F-strings y módulos organizados para crear sistemas escalables y elegantes.

| Detalle | Información |
| :--- | :--- |
| **Publicado el** | Publicado el 11 de octubre de 2025 |
| **Profesor** | Luis MArtinez |
| **Fecha de Inicio** | 22/10/2025 |
| **Fecha de Fin** | 30/10/2025 |

## CLASE 01: INTRO

**¿Qué significa escribir código pythónico?**
Es escribir con claridad y coherencia con el lenguaje: nombres descriptivos, estructuras concisas y convenciones que mejoran la lectura y el mantenimiento.

**¿Qué habilidades y prácticas profesionales dominarás?**
El avance a intermedio incluye conceptos que fortalecen tu criterio técnico y tu estilo de código.

- PEP 8: guía de estilo para mantener un código consistente y legible.
- Entornos virtuales: aislamiento de dependencias para proyectos organizados.
- Comprensiones: creación concisa de colecciones con intención clara.
- Funciones built-in: uso de utilidades del lenguaje para simplificar tareas.
- Literal strings: formateo directo y expresivo para generar texto.
- Manejo de errores: captura y control de fallos para robustez.
- Excepciones personalizadas: señalización precisa de situaciones especiales.
- Modularización: organización del código en módulos reutilizables y mantenibles.
- Integración con AI: aplicación de inteligencia artificial en un flujo real de datos.


## CLASE 02: Configuración de PEP 8 y formateo automático con Ruff en Python


🐍✨ PEP 8 + Ruff + VS Code
🎯 Propósito
💡 Escribir código Python limpio, legible y escalable usando las buenas prácticas de PEP 8 y la automatización de Ruff.

🧱 1️⃣ Inicio del archivo
📜 Documentación al principio

"""

Sistema de análisis de noticias con APIs múltiples.

"""

🔤 Constantes

En MAYÚSCULAS_CON_GUION_BAJO
Usa comillas dobles siempre DEFAULT_LANGUAGE = "español"

🧭 Mantén el mismo formato en todo el proyecto.

🧩 2️⃣ Nombres y estilo
🐍 Funciones y variables: snake_case ✏️ Ejemplo:

def clean_text(texto: str) -> str:

    """Limpia y formatea texto."""

    pass

📏 Reglas visuales

🔹 4 espacios de indentación (no tabuladores)
🔹 2 líneas en blanco entre funciones
🔹 Máximo 88 caracteres por línea
🧠 Usa nombres descriptivos y coherentes.

⚙️ 3️⃣ Estructura lógica del código
1️⃣ Funciones utilitarias

2️⃣ Funciones principales

3️⃣ Bloque de ejecución →

if __name__ == "__main__":

    ...

🌍 Código en inglés

📝 Documentación en español (opcional)

📦 4️⃣ Orden correcto de imports
📚 Sigue este orden PEP 8:

🐍 Estándar de Python → import json
🌐 Terceros → import requests
📁 Locales → from utils.helpers import formatear_datos
✅ Orden explícito y consistente 🚫 Elimina imports no usados

💬 5️⃣ Comillas y espacios
💎 Usa un único tipo de comillas

➡️ Recomendado: dobles "texto"

🔍 En VS Code activa:

Settings → JSON → Editor Render White Space → All para visualizar espacios y tabulaciones.

🧰 6️⃣ Automatiza con Ruff
🚀 Ruff (hecho en Rust) aplica PEP 8 automáticamente:

Formatea código
Ordena imports
Detecta errores antes de ejecutar
🪄 Cómo configurarlo en VS Code
1️⃣ Instala la extensión Ruff

2️⃣ Clic derecho → Formatear documento

3️⃣ En settings.json agrega:

{

  "format_on_save": true

}

💾 Al guardar → Ruff corrige comillas, espacios y estilo. ✨ Tu código siempre limpio.

🔄 7️⃣ Organización automática de imports
💡 Configura VS Code para:

Ordenar imports (estándar → terceros → locales)
Eliminar imports sin uso
🔥 Todo sucede automáticamente al guardar.

🧮 8️⃣ Comandos Ruff esenciales
🧩 Formatear proyecto completo: ruff format

📘 Ayuda detallada: ruff format help

🧹 Linter activo: Detecta variables no usadas y posibles errores. 👉 Lo muestra directamente en el editor.

## CLASE 03: Sintaxis de list, dict y set comprehensions en Python

🐍💡Comprehensions en Python
🔍 ¿Qué son?
Forma compacta, legible y elegante de crear listas, diccionarios o conjuntos en una sola línea.

📦 En una comprehension puedes combinar:

🔁 Iteración → recorrer elementos
🔧 Mapeo → transformar valores
🚫 Filtro (if) → incluir o excluir
Ventajas principales:

 ✅ Mismo resultado que un for clásico

 ✅ Menos código y más claridad

 ✅ Condiciones integradas directamente

🧠 Estructura general
[expresión for elemento in iterable if condición]

🔹 Expresión: qué quieres devolver

🔹 Iteración: recorre los datos

🔹 Filtro: opcional, decide qué incluir

🔄 De un for tradicional a una comprehension
🧩 Código clásico
```Python
def extract_titles_traditional(articles):

    titles = []

    for article in articles:

        titles.append(article["title"])

    return titles
```
⚡ Versión pythónica
```Python
def extract_titles(articles):

    return [a["title"] for a in articles]
```
➡️ Mismo resultado.

➡️ Menos ruido visual.

➡️ Intención clara: obtener títulos.

🚀 Beneficios de la sintaxis compacta
✨ Menos errores por variables intermedias

🧩 Código más expresivo: “qué hago”, no “cómo lo hago”

🧹 Compatible con herramientas como Ruff (mejor legibilidad automática)

🔎 Filtros con if dentro de la comprehension
def extract_titles_long(articles):
```Python
    return [a["title"] for a in articles if len(a["title"]) > 10]
```
🎯 Solo incluye títulos con más de 10 caracteres.

🧠 El if siempre va al final.

🧱 Crear diccionarios (dict comprehension)
🎯 Ideal cuando quieres pares clave → valor.
```Python
long_desc_by_title = {

    a["title"]: a["description"]

    for a in articles

    if len(a["description"]) > 20

}
```
💬 Resultado: Diccionario con títulos y descripciones largas.

📏 Si el filtro es muy estricto, puedes ajustar el número:
```Python
by_title_min5 = {

    a["title"]: a["description"]

    for a in articles

    if len(a["description"]) > 5

}
```

```Python

sample_articles = [
    {'title': 'Python logra nuevo éxito', 'source': {'name': 'TechNews'}, 'description': 'Gran noticia', 'category': 'Tecnología'},
    {'title': 'Mercado en crisis', 'source': {'name': 'Finance'}, 'description': 'Análisis completo', 'category': 'Economía'},
    {'title': 'Nueva tecnología', 'source': {'name': 'TechNews'}, 'description': 'Innovación', 'category': 'Tecnología'},
    {'title': 'Deportes hoy', 'source': {'name': 'Sports'}, 'description': 'Resultados', 'category': 'Deportes'},
    {'title': 'Política actual', 'source': {'name': 'News'}, 'description': 'Actualidad', 'category': 'Política'},
    {'title': 'Ciencia avanza', 'source': {'name': 'Science'}, 'description': 'Descubrimientos', 'category': 'Ciencia'}
]


def extract_unique_source_list(articles):
    return list({article["source"]["name"] for article in articles if "source" in article and "name" in article["source"]})

```

## CLASE 04: Comprensiones anidadas para agrupar y filtrar datos en Python

🧠Comprensiones en Python
🎯 Objetivo general
Aprender a usar list, set y dict comprehension para:

🔹 Escribir código más claro y conciso

🔹 Evitar duplicados con sets

🔹 Agrupar información sin perder legibilidad

🔹 Reducir líneas sin alterar la lógica

🔍 1. ¿Qué son las comprensiones?
> Son atajos sintácticos para crear listas, conjuntos o diccionarios a partir de bucles y condiciones.

💬 Piensa en ellas como una forma de decir: ➡️ “Toma cada elemento, filtra y transforma en una sola expresión.”

📦 Tipos:

list comprehension → crea listas [ ]
set comprehension → crea conjuntos { }
dict comprehension → crea diccionarios {clave: valor}


🧩 2. Extraer fuentes únicas con set comprehension
🟡 Concepto clave
Un set mantiene solo valores únicos → elimina duplicados automáticamente.

🔸 Versión tradicional
def get_sources_traditional(articles):

    sources = set()

    for article in articles:

        source = article.get('source')

        if source and source.get('name'):

            sources.add(source['name'])

    return sources

🧠 Lógica:

get() evita errores si falta la clave.
add() inserta la fuente en el conjunto.
Se eliminan duplicados de forma natural.
⚡ Versión con set comprehension
def get_sources(articles):

    return {

        a['source']['name']

        for a in articles

        if a.get('source') and a['source'].get('name')

    }

📘 Lectura:

{ expresión for elemento in iterable if condición }

Más limpia, menos código, misma lógica.
💡 Comprobación: Imprime ambos resultados: si hay fuentes repetidas, el set mostrará una sola vez cada una.

🧩 3. Categorizar artículos por fuente
Queremos agrupar artículos según su fuente → cada fuente será una clave con una lista de artículos.

🔸 Versión tradicional
def categorize_traditional(articles):

    sources = get_sources(articles)

    results = {}

    for source in sources:

        if source not in results:

            results[source] = []

        for article in articles:

            art_source = article.get('source')

            name = art_source.get('name') if art_source else None

            if name == source:

                results[source].append(article)

    return results

🔍 Lógica paso a paso:

Obtiene fuentes únicas.
Inicializa el diccionario.
Recorre artículos y los agrega a su fuente correspondiente.
⚡ Versión con dict y list comprehension
def categorize(articles):

    return {

        source: [

            article

            for article in articles

            if article.get('source') and article['source'].get('name') == source

        ]

        for source in get_sources(articles)

    }

🎯 Ventajas:

Código más compacto.
Agrupación directa sin bucles anidados.
Misma lógica, menos ruido visual.


🧭 4. Buenas prácticas
✅ Usa comprensiones para patrones de mapear y filtrar.

✅ Utiliza .get() para evitar errores de clave.

✅ Emplea set cuando necesites eliminar duplicados.

✅ Usa comprensiones anidadas para agrupar datos de forma clara.

✅ Verifica equivalencia con print() antes y después del refactor.

✅ Corrige advertencias del linter (como ruff).

✅ Comprueba que las funciones devuelvan datos correctos tras refactorizar.

## Ejemplo 

```Python
sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los titulos usando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 200:
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los titulos usando un comprehension"""
    return [article["title"] for article in articles if len(article["title"]) > 200]


def extract_article_summaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 5
    }


# print(extract_titles_traditional(sample_articles))
# print("======")
# print(extract_titles(sample_articles))
# print(extract_article_summaries(sample_articles))


def get_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def get_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def categorize_traditional(articles):
    sources = get_sources(articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []

        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)

    return results


def categorize(articles):
    sources = get_sources(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("===")
print(categorize(sample_articles))


```
