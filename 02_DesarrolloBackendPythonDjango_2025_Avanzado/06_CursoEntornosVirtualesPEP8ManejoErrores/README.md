# Curso Entornos virtuales, PEP8 y Manejo de Errores 🚀

> Domina el código Python intermedio con proyectos reales. Aprende a escribir funciones limpias, usar type hints y manejar errores profesionales. Mejora tu lógica con comprensiones, F-strings y módulos organizados para crear sistemas escalables y elegantes.

| Detalle | Información |
| :--- | :--- |
| **Publicado el** | Publicado el 11 de octubre de 2025 |
| **Profesor** | Luis Martinez |
| **Fecha de Inicio** | 22/10/2025 |
| **Fecha de Fin** |  |



## Tabla de Contenidos
- [CLASE 01: INTRO](#clase-01-intro)
- [CLASE 02: Configuración de PEP 8 y formateo automático con Ruff en Python](#clase-02-configuracion-de-pep-8-y-formateo-automatico-con-ruff-en-python)
- [CLASE 03: Sintaxis de list, dict y set comprehensions en Python](#clase-03-sintaxis-de-list,-dict-y-set-comprehensions-en-python)
- [CLASE 04: Comprensiones anidadas para agrupar y filtrar datos en Python](#clase-04-comprensiones-anidadas-para-agrupar-y-filtrar-datos-en-python)
- [CLASE 05:  Argumentos dinámicos *args en funciones Python](#clase-05--argumentos-dinamicos-*args-en-funciones-python)
- [CLASE 06:  Argumentos dinámicos *args en funciones Python](#clase-06--argumentos-dinamicos-*args-en-funciones-python)
- [CLASE 07:  Argumentos dinámicos *args en funciones Python](#clase-07--argumentos-dinamicos-*args-en-funciones-python)
- [CLASE 08: Uso de kwargs para crear un cliente de APIs flexible](#clase-08-uso-de-kwargs-para-crear-un-cliente-de-apis-flexible)
- [CLASE 09: Integración de Python con News API usando parámetros dinámicos](#clase-09-integracion-de-python-con-news-api-usando-parametros-dinamicos)
- [CLASE 10: Control de errores en Python con try y except](#clase-10-control-de-errores-en-python-con-try-y-except)
- [CLASE 11: Uso del bloque finally para liberar recursos en Python](#clase-11-uso-del-bloque-finally-para-liberar-recursos-en-python)
- [Clase 13 : Anotaciones de tipo con type hints en Python](#clase-13--anotaciones-de-tipo-con-type-hints-en-python)
- [Clase 14 : Tipado de funciones y estructuras de datos en Python](#clase-14--tipado-de-funciones-y-estructuras-de-datos-en-python)
- [Clase 15: Documentación en Python con docstrings y PEP 257](#clase-15-documentacion-en-python-con-docstrings-y-pep-257)
- [Clase 16: Entornos virtuales en Python: qué son y por qué los necesitas](#clase-16-entornos-virtuales-en-python-que-son-y-por-que-los-necesitas)
- [Clase 17: Creación y gestión de entornos virtuales con venv en Python](#clase-17-creacion-y-gestion-de-entornos-virtuales-con-venv-en-python)
- [Clase 18: Creación de entornos virtuales en Windows con Python](#clase-18-creacion-de-entornos-virtuales-en-windows-con-python)
- [Clase 19: Gestión moderna de dependencias Python con UV y pyproject](#clase-19-gestion-moderna-de-dependencias-python-con-uv-y-pyproject)
- [Clase 20: Modularización de código Python con responsabilidad única](#clase-20-modularizacion-de-codigo-python-con-responsabilidad-unica)
- [Clase 21: Paquetes Python: de estructura plana a código modular](#clase-21-paquetes-python-de-estructura-plana-a-codigo-modular)
- [Clase 22: Función enumerate en Python para indexar listas automáticamente](#clase-22-funcion-enumerate-en-python-para-indexar-listas-automaticamente)
- [Clase 23: Filtrado de listas con filter en Python](#clase-23-filtrado-de-listas-con-filter-en-python)
- [Clase 24: Función map para calcular tiempo de lectura en Python](#clase-24-funcion-map-para-calcular-tiempo-de-lectura-en-python)
- [Clase 25: Conexión de OpenAI API con variables de entorno en Python](#clase-25-conexion-de-openai-api-con-variables-de-entorno-en-python)


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
```Python
def get_sources(articles):

    return {

        a['source']['name']

        for a in articles

        if a.get('source') and a['source'].get('name')

    }
```
📘 Lectura:

{ expresión for elemento in iterable if condición }

Más limpia, menos código, misma lógica.
💡 Comprobación: Imprime ambos resultados: si hay fuentes repetidas, el set mostrará una sola vez cada una.

🧩 3. Categorizar artículos por fuente
Queremos agrupar artículos según su fuente → cada fuente será una clave con una lista de artículos.

🔸 Versión tradicional
def categorize_traditional(articles):
```Python
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
```
🔍 Lógica paso a paso:

Obtiene fuentes únicas.
Inicializa el diccionario.
Recorre artículos y los agrega a su fuente correspondiente.
⚡ Versión con dict y list comprehension
```Python
def categorize(articles):

    return {

        source: [

            article

            for article in articles

            if article.get('source') and article['source'].get('name') == source

        ]

        for source in get_sources(articles)

    }
```
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


## CLASE 05:  Argumentos dinámicos *args en funciones Python


**¿Qué son los f-strings en Python y por qué usarlos?**
Los f-strings se crean anteponiendo una letra f al inicio de las comillas. Con eso, puedes colocar expresiones dentro de llaves y Python las evalúa al imprimir. Según se comenta, fueron agregados desde Python 3.6 y funcionan en versiones actuales como 3.13, con mejoras de rendimiento y legibilidad frente a .format.

Mejor legibilidad: ves variables y lógica en el lugar donde se imprimen.
Mejor rendimiento: el formateo es más rápido en versiones modernas de Python.
Sintaxis directa: basta con escribir f"... {expresión} ...".


**¿Cómo verificar la versión de Python?**
Confirma que Python sea 3.6 o superior. El ejemplo menciona 3.13 como versión instalada, por lo que es compatible con f-strings.



**¿Qué ventaja tienen sobre format?**
Con .format las variables quedan lejos del texto, lo que dificulta leer qué se inserta. Con f-strings, la interpolación es inmediata y el código se entiende de un vistazo.

Ejemplo equivalente con .format que resulta menos claro:

nombre = "Ana"
texto = "Hola, {}".format(nombre)
print(texto)



**¿Qué precaución con el editor?**
Si antepones la f pero no usas llaves, algunos editores o linters como “Ruf” podrían eliminar la f automáticamente por no aportar nada. Asegúrate de incluir al menos una expresión entre llaves.



**¿Cómo insertar variables, operaciones y funciones dentro de f-strings?**
Dentro de las llaves puedes colocar variables, operaciones matemáticas y llamadas a métodos o funciones. Esto reduce errores y concentra la lógica donde se muestra el texto.


**¿Cómo interpolar variables?**
nombre = "Ana"
saludo = f"Hola, {nombre}"
print(saludo)
Interpola el valor de una variable entre llaves.
Mantiene el texto y los datos juntos.



**¿Cómo ejecutar operaciones y cálculos?**
Operaciones aritméticas simples en línea.
suma = f"La suma es {1 + 1}"
print(suma)  # La suma es 2
Cálculos más expresivos, como una edad a partir del año de nacimiento.
nombre = "Ana"
anio_nacimiento = 2020
anio_actual = 2025  # ejemplo de año actual
mensaje = f"Hola, {nombre}, tu edad es {anio_actual - anio_nacimiento} años"
print(mensaje)
Ventaja: legibilidad y menor propensión a errores, porque el cálculo vive en la misma línea del texto.


**¿Cómo llamar métodos y funciones?**
Puedes invocar métodos de cadenas como .upper directamente en el f-string.

nombre = "Ana"
texto = f"Hola, {nombre.upper()}"
print(texto)  # Hola, ANA
También puedes llamar funciones propias si lo necesitas.
El editor puede autocompletar porque estás escribiendo código Python normal dentro de las llaves.


**¿Cómo usar condicionales y otros recursos dentro de f-strings?**
Los f-strings aceptan expresiones, incluyendo condicionales tipo if/else en línea. Además, permiten acceder a estructuras como diccionarios y, de forma avanzada, aplicar formateadores con el operador dos puntos.


**¿Cómo escribir condicionales inline?**
nombre = "Ana"
edad = 20
msg = f"Hola, {nombre}, eres {'mayor de edad' if edad >= 18 else 'menor de edad'}"
print(msg)
Útil para pluralizar o ajustar textos según cantidades.
Mantiene la lógica condicional cercana al mensaje.



**¿Dónde aplicar plural o singular?**
Cuando generas textos con conteos.
Para diferenciar “mayor”/“menor”, “elemento”/“elementos”, según el número.
Validando la cantidad directamente en las llaves.
Ejemplo de patrón:

cantidad = 1
info = f"Tienes {cantidad} {'elemento' if cantidad == 1 else 'elementos'}"
print(info)


**¿Qué más puedes integrar?**
Acceso a diccionarios para mostrar valores.
datos = {"ciudad": "Lima"}
texto = f"Vives en {datos['ciudad']}"
print(texto)



## CLASE 06:  Argumentos dinámicos *args en funciones Python


**¿Cómo dar formato a números con FStrings?**
Los modificadores de formato se aplican tras los dos puntos. Esto permite generar salidas más legibles para personas, como separar miles con coma, limitar decimales con redondeo y rellenar con ceros a la izquierda.




**¿Cómo aplicar separador de miles?**
Usa la coma para miles: más legible para valores grandes.
Inserta el modificador tras el valor: dos puntos y coma.


bank_balance = 1234567890
texto = f"Tu saldo en la cuenta bancaria es {bank_balance:,}."
print(texto)
# Tu saldo en la cuenta bancaria es 1,234,567,890.





**¿Cómo controlar decimales y redondeo?**
Limita decimales con f: redondea automáticamente.
Cambia la precisión: .1f, .2f, etc.
stock_price = 1.405
texto = f"El valor del stock es {stock_price:.1f}."
print(texto)
# El valor del stock es 1.4.

texto2 = f"El valor del stock es {stock_price:.2f}."
print(texto2)
# El valor del stock es 1.41.



**¿Cómo agregar ceros a la izquierda?**
Define el ancho mínimo con ceros: 03, 04, etc.
Indicado para IDs y códigos fijos.
user_id = 1
texto = f"Su ID es {user_id:03d}."
print(texto)
# Su ID es 001.

user_id = 100
texto = f"Su ID es {user_id:04d}."
print(texto)
# Su ID es 0100.



**¿Cómo alinear texto y crear tablas legibles?**
Los FStrings permiten alinear valores con un ancho fijo, ideal para tablas simples con pipeline y sumarios más claros. Puedes alinear a la izquierda o a la derecha cambiando el indicador de alineación.



**¿Cómo alinear columnas con anchura fija?**
Especifica ancho tras los dos puntos: 15, 10, etc.
Alinea texto a la izquierda o números a la derecha para facilitar lectura.

product = "laptop"
price = 1000
print(f"producto | precio")
print(f"{product:<15} | {price:>10,}")
# producto       |      1,000


**¿Cómo concatenar filas con un salto de línea?**
Usa el backslash n para un retorno de línea: \n.
Duplica líneas con el mismo formato para simular una tabla.
product = "laptop"
price = 1000
linea = f"{product:<15} | {price:>10,}"
tabla = f"producto         | precio\n{linea}\n{linea}"
print(tabla)


**¿Cómo formatear fechas y mejorar el debugging?**
Una fecha en su forma por defecto sale en formato ISO. Con modificadores, puedes mostrar día, número, mes, año y hora en una versión más legible. Además, los FStrings permiten imprimir variables y mensajes para encontrar errores más rápido.



**¿Cómo mostrar una fecha completa legible?**
Crea la fecha con datetime: año, mes, día y hora.
Aplica códigos de formato para nombre del día, día, mes, año y hora.
from datetime import datetime
fecha = datetime(2024, 12, 5, 10, 10)
print(f"La fecha completa es {fecha}.")  # formato ISO por defecto

formato = f"La fecha completa es {fecha:%A, %d de %B del %Y a las %I y %M %p}."
print(formato)
# La fecha completa es jueves, 05 de diciembre del 2024 a las 10 y 10 A.M.


**¿Cómo usar FStrings para debugging rápido?**
Inserta variables directamente en el mensaje: más contexto.
Combina texto y valores calculados en una sola línea.
Útil para verificar estados y entradas del usuario.
user = "ana"
items = ["A", "B", "C"]
print(f"debug: usuario={user}, total_items={len(items)}, items={items}")



## CLASE 07:  Argumentos dinámicos *args en funciones Python



**¿Qué son los argumentos dinámicos args en Python?**
Los argumentos dinámicos permiten recibir un número variable de parámetros posicionales. En Python se definen con un asterisco y el nombre convencional args. Internamente, args es una tupla: inmutable, ordenada y accesible por índice.

Se definen con un asterisco antes del nombre del parámetro.
Se almacenan como tupla inmutable.
El orden de los argumentos posicionales es crucial.



**¿Cómo se usan args con ejemplos de código?**
def ejemplo_args(*args):
    print(f"args: {args}")
    print(f"type: {type(args)}")

# Llamadas de ejemplo
Ejemplo = ejemplo_args
Ejemplo(1, 2, 3)
Ejemplo("Hola", "mundo")
Ejemplo()  # sin parámetros




## CLASE 08: Uso de kwargs para crear un cliente de APIs flexible


**¿Qué son keywords y por qué combinarlos con args?**
Los keywords se envían con nombre y se reciben con doble asterisco: kwargs. A diferencia de args, que solo capturan valores posicionales, kwargs agrupa parámetros nombrados en un diccionario. Esto permite pasar pares key-value y trabajar con ellos de forma dinámica y clara.

kwargs es un diccionario. Permite inspeccionar keys y valores de entrada.
Key-value nombrado. Claridad al invocar funciones y reutilizarlas.
Combinación con args. Flexibilidad total con parámetros posicionales y nombrados.
Ejemplo base de impresión de keywords:

def ejemplo_keywords(**keywords):
    print(type(keywords))  # dict
    print(keywords)        # {'llave': 'valor', ...}
    print('---')

# llamada de ejemplo
# ejemplo_keywords(llave='valor', api_key='demo')


**¿Cómo implementar kwargs en una función flexible?**
La idea central: crear una función única que, según el nombre de la API, seleccione el API client correcto, mezcle una configuración base con parámetros dinámicos, y ejecute la llamada. El resultado es una función robusta y reutilizable.

def fetch_news(api_name, *args, **keywords):
    """
    función flexible para conectar con la API.
    """
    # configuración base común a múltiples APIs
    base_config = {
        "timeout": ...,  # por defecto
        "retries": ...,  # por defecto
    }

    # fusión de configuración: base + parámetros nombrados entrantes
    config = {**base_config, **keywords}

    # selección de cliente por nombre
    api_clients = {
        "newsAPI": news_api_client,   # referencia a cliente de News API
        "Guardian": guardian_client,  # referencia a cliente de Guardian
    }

    client = api_clients[api_name]
    return client(*args, **config)



**¿Cómo funcionan los diccionarios y el doble asterisco?**
Desempaquetado con :** copiar pares key-value dentro de otro diccionario.
Mezcla de configuraciones: {**base_config, **keywords} agrega y sobrescribe de forma limpia.
Invocación con :** client(*args, **config) pasa parámetros de forma explícita.



**¿Qué orden de parámetros es correcto en Python?**
Obligatorios primero: por ejemplo, api_name al inicio.
Luego args: parámetros posicionales variables.
Al final kwargs:** parámetros nombrados y dinámicos.




**¿Cómo se selecciona el cliente por nombre?**
Mapa de clientes: un diccionario api_clients con el nombre como clave.
Búsqueda directa: client = api_clients[api_name] elige el ejecutor correcto.
Una sola función: orquesta múltiples fuentes como News API y Guardian.



**¿Cómo usarlo con News API y Guardian?**
Con una misma función puedes enviar parámetros distintos y obtener resultados de diferentes orígenes. La clave está en pasar keywords específicos de cada servicio, manteniendo una base_config con timeout y retries.

Ejemplo con News API.
Ejemplo con Guardian con sección y fecha.
Misma función, distintos parámetros, mismo flujo.
Invocaciones ilustrativas:

# News API
fetch_news(
    "newsAPI",
    api_key="demo",
    query="noticias de Python",
)

# Guardian
fetch_news(
    "Guardian",
    api_key="Demoguardian",
    section="sports",
    from_date="2020-10-10",
)
Conceptos y habilidades que te llevas: - kwargs como diccionario para parámetros nombrados. - args para valores posicionales flexibles. - Key-value explícito para legibilidad y mantenimiento. - Desempaquetado con ** para fusionar configuraciones. - Configuración base con timeout y retries reutilizable. - Selección de cliente por nombre mediante diccionario de API clients. - Orden correcto de parámetros: obligatorios, args, kwargs.

¿Tienes dudas sobre cómo adaptar los parámetros de tu API favorita o cómo estructurar tu base_config? Deja tu pregunta y cuéntanos tu caso para ayudarte a concretarlo.



## CLASE 09: Integración de Python con News API usando parámetros dinámicos


**¿Cómo obtener y proteger tu API key de News API?**

Obtener la API key es el primer paso. Se solicita en newsapi.org completando un formulario y pulsando submit. Cópiala y úsala por ahora como constante en el código.

No hacerla pública ni subirla al repositorio.
Tratarla como una llave de acceso.
Guardarla temporalmente como constante para fines educativos.
La documentación oficial (Get Started, Searching for news articles) indica la URL base y que la API key se pasa como parámetro. Esa guía define el formato correcto del request.



**¿Cómo construir la URL y el query string en Python?**

La recomendación es evitar concatenar cadenas a mano. Usa las herramientas de Python: urllib.parse.urlencode para formatear parámetros y urllib.request para abrir la URL con un timeout controlado. Así la URL final es válida y el servidor entiende el GET.

Usar urllib.parse para generar el query string.
Añadir parámetros como la q de búsqueda y la apiKey.
Construir la URL final uniendo base y parámetros.



**¿Qué hace urllib.parse.urlencode?**

Convierte un diccionario de parámetros en un query string seguro para una URL. Evita errores de encoding y respeta el formato esperado por la API.

import json
from urllib import parse, request

API_KEY = "TU_API_KEY"
BASE_URL = "BASE_URL_DE_NEWS_API"  # URL base indicada en la documentación de búsqueda.

def fetch_news(api_key: str, query: str, timeout: int = 10):
    params = {
        "q": query,
        "apiKey": api_key,
    }
    query_string = parse.urlencode(params)
    url = f"{BASE_URL}?{query_string}"

    # Enviar el request con administrador de contexto.
    with request.urlopen(url, timeout=timeout) as resp:
        data_bytes = resp.read()  # Respuesta cruda en bytes.

    # Decodificar y parsear json.
    data_text = data_bytes.decode("utf-8")
    data = json.loads(data_text)
    return data

    

**¿Cómo enviar el request con urllib.request y with?**

Con el administrador de contexto with se maneja el response y se lee el contenido con seguridad. El timeout evita esperas indefinidas.

Abrir la URL con request.urlopen y pasar timeout.
Leer los bytes con .read().
Mantener el código claro y cercano a la función de fetch.



**¿Cómo decodificar la respuesta y procesar artículos en json?**
La respuesta llega como bytes. Hay que aplicar decode('utf-8') y luego json.loads para obtener un diccionario. Desde ahí, acceder a llaves como status, totalResults y especialmente articles para listar títulos.

Decodificar a texto con UTF-8.
Convertir a diccionario con json.loads.
Inspeccionar llaves con keys() para entender la estructura.
Iterar articles y mostrar title.

# Ejecución de prueba
response_data = fetch_news(API_KEY, "Python")
print(list(response_data.keys()))  # Ver llaves disponibles.

articles = response_data["articles"]  # Acceso a la lista de artículos.
for article in articles:
    print(article["title"])  # Imprimir solo el título.
Consejos prácticos que marcan diferencia:

Imprimir solo los primeros caracteres al inicio para validar el formato.
Mostrar el query string y la URL final para depurar.
Usar herramientas estándar de Python en lugar de armar URLs a mano.
Limpiar prints una vez que el flujo funcione.



## CLASE 10: Control de errores en Python con try y except



**¿Qué problema resuelve try/except en Python?**

Cuando conviertes o recibes datos, algo puede fallar: un servidor puede estar caído o la entrada del usuario puede ser inválida. Con try/except, Python permite interceptar estas situaciones y definir una acción segura: mostrar un mensaje, asignar un valor por defecto o frenar la ejecución si estás dentro de una función.

Un ejemplo base: pedir dos números y dividirlos. Si el usuario digita cero para el divisor, ocurre un ZeroDivisionError; si escribe texto, aparece ValueError. Con manejo de excepciones, puedes informar al usuario de forma clara y continuar el flujo del programa cuando tiene sentido.

# try_except.py
# Entrada del usuario y división
A = int(input("Digita un número: "))
B = int(input("Digita otro número: "))
resultado = A / B
print(resultado)


**¿Cómo implementar try y except paso a paso?**
Primero, identifica la línea que puede fallar y envuélvela en try. Luego maneja el error con except. Puedes comenzar capturando una excepción general con Exception, observar el tipo real y después especializar el manejo.

try:
    A = int(input("Digita un número: "))
    B = int(input("Digita otro número: "))
    resultado = A / B
    print(resultado)
except Exception as e:
    print("Ocurrió un error:", e)
    print("Tipo de error:", type(e))
Esto te mostrará mensajes como "invalid literal for int()" (propio de ValueError) o "division by zero" (propio de ZeroDivisionError).


**¿Cómo capturar ZeroDivisionError sin ocultar otros errores?**
Sé específico cuando conoces el problema esperado: dividir entre cero. Así evitas atrapar errores no relacionados.

try:
    A = int(input("Digita un número: "))
    B = int(input("Digita otro número: "))
    resultado = A / B
    print(resultado)
except ZeroDivisionError:
    print("No está permitido dividir por cero.")


**¿Cómo validar entradas y capturar ValueError?**
Si el usuario escribe "hola" en lugar de un número, int() lanza ValueError. Captúralo y guía al usuario.

try:
    A = int(input("Digita un número: "))
    B = int(input("Digita otro número: "))
    resultado = A / B
    print(resultado)
except ValueError:
    print("El valor digitado no es un número válido.")
except ZeroDivisionError:
    print("No está permitido dividir por cero.")
Puedes imprimir el error concreto con as e si necesitas más detalle para diagnóstico.



**¿Cómo evitar múltiples try innecesarios?**
En lugar de anidar varios try, concentra el bloque de riesgo y usa múltiples except específicos. Esto mantiene el código claro y mantenible.



**¿Qué buenas prácticas debes aplicar al manejar excepciones en Python?**

Además de proteger el código contra entradas inválidas o divisiones por cero, aplica criterios de calidad para que tu manejo de errores aporte valor real en desarrollo y producción.

No exageres: agrega try/except solo donde esperas errores. Evita rodear todo el programa.
Sé específico: prefiere ValueError y ZeroDivisionError a usar Exception genérica.
Muestra mensajes útiles: informa al usuario con claridad y sin tecnicismos.
Registra el error: haz logging o imprime el error en consola para facilitar el debugging.
Controla el flujo: si estás en una función, usa return tras manejar el error para evitar efectos secundarios.
Prueba escenarios reales: por ejemplo, al conectarte a una News API, cambia la API key por una inválida y captura el fallo del request. Muestra un mensaje: "La conexión a la News API está fallando porque la API es inválida".


## CLASE 11: Uso del bloque finally para liberar recursos en Python


**¿Qué es finally y cuándo se ejecuta en Python?**

El bloque finally se ejecuta siempre, ocurra o no una excepción. A diferencia de poner un print después del try y los except, el código dentro de finally corre incluso si el programa va a romperse por una excepción no manejada. Es ideal para liberar recursos, cerrar archivos o desconectarte de servicios antes de que la ejecución termine abruptamente.

Se ejecuta tras los except, con o sin error previo.
Sirve para liberar recursos y cerrar archivos.
Permite registrar mensajes justo antes del bloqueo.
Aporta robustez al flujo de la aplicación.



**¿Cómo se estructura el bloque try/except/finally?**

try:
    a = int(input("Número A: "))
    b = int(input("Número B: "))
    print(a / b)
except ValueError:
    print("Error: debes ingresar números enteros.")
except ZeroDivisionError:
    print("Error: B no puede ser cero.")
except KeyboardInterrupt:
    print("Ejecución cancelada por el usuario.")
finally:
    print("print desde finally")

print("Este es otro print")
ValueError: cuando se ingresan letras en vez de números.
ZeroDivisionError: cuando B es 0.
KeyboardInterrupt: cuando el usuario interrumpe con Ctrl+C o Delete.
El mensaje en finally aparece siempre; el de después del bloque puede no mostrarse si el programa se interrumpe antes.


**¿Cómo identificar y capturar excepciones específicas?**

Python ofrece una jerarquía de errores con BaseException como raíz y excepciones comunes como ImportError, IndexError y KeyboardInterrupt. Una práctica efectiva es reproducir el error para observar cuál excepción lanza Python y luego capturar esa clase específica con except.

Observa el rastro del error no manejado.
Copia la clase de excepción que aparece.
Agrega un except con esa excepción específica.
Evita capturar genéricamente si puedes precisar el tipo de error.



**¿Por qué capturar KeyboardInterrupt en aplicaciones interactivas?**

Permite mostrar un mensaje claro al usuario.
Evita trazas largas e innecesarias.
Asegura que se ejecute finally para liberar recursos.


**¿Cómo manejar una API key inválida en un client de noticias?**
En una implementación con un client de noticias como NewsAPI, cuando la API key es inválida Python lanza una excepción. La estrategia recomendada es capturar la excepción exacta que se muestra, registrar un mensaje y retornar una estructura segura para que el resto de la aplicación no falle, por ejemplo un diccionario con articles vacío.



**¿Cómo aplicar try/except/finally en Fetch News?**

def fetch_news(client):
    try:
        # Llama al método de tu client (p. ej., top_headlines)
        response = client.top_headlines()
        return response  # Estructura válida cuando todo sale bien.
    except Exception:  # Reemplaza con la excepción específica que te muestre Python.
        print("La API key es inválida")
        return {"articles": []}  # Entrega una respuesta segura para el resto del sistema.
    finally:
        # Libera recursos o desconéctate de servicios si aplica.
        print("Liberando recursos en finally")
Captura la excepción que obtuviste al ejecutar con la API key dañada.
Muestra un mensaje claro: "La API key es inválida".
Retorna {"articles": []} para evitar errores aguas arriba.
Usa finally para cerrar conexiones o liberar memoria.



**¿Qué habilidades y conceptos refuerzas con este patrón?**
Manejo de excepciones con try, except y finally.
Identificación de errores específicos: ValueError, ZeroDivisionError, KeyboardInterrupt.
Diseño de respuestas seguras: diccionarios vacíos en fallos de API key.
Liberación de recursos y cierre ordenado del flujo.

##  CLASE 12 : Creación de excepciones personalizadas en Python


Excepciones personalizadas en Python
Crear tus propias excepciones te permite nombrar el problema y facilitar su captura precisa. En lugar de devolver una lista vacía, puedes lanzar un error explícito para que quien consuma la funcionalidad decida el mensaje a mostrar.


**¿Cómo funciona raise para detener la ejecución?**

Usa raise para lanzar un error y frenar el flujo.
El bloque finally se ejecuta siempre, incluso si hay error.
Mensajes claros orientan al desarrollador: "no está permitido el cálculo por dos".

# Ejemplo inicial con la excepción genérica

def dividir(a, b):
    if b == 2:
        raise Exception("No está permitido el cálculo por dos")
    return a / b

try:
    dividir(100, 2)
except Exception as e:
    print(e)
finally:
    print("finally siempre se ejecuta")



**¿Por qué crear una excepción específica y no usar Exception?**

Para capturar solo lo que importa y no "todo" con Exception.
Para documentar la intención del error mediante nombre y docstring.
class DivisionError(Exception):
    """Error en operación."""
    pass

def dividir(a, b):
    if b == 2:
        raise DivisionError("No está permitido el cálculo por dos")
    return a / b

try:
    dividir(100, 2)
except DivisionError as e:  # captura específica
    print(e)
finally:
    print("finally siempre se ejecuta")
Patrón try, except y finally
El flujo de manejo de errores se apoya en cuatro cláusulas usadas con intención: colocar lo frágil en try, decidir cuándo fallar con raise, capturar con except y garantizar limpieza con finally.


**¿Qué hace cada cláusula en el flujo de errores?**

try: bloque con código que podría fallar.
raise: detiene la ejecución y lanza un tipo de error específico.
except: captura un tipo de error concreto o todos si usas Exception.
finally: se ejecuta siempre, ocurra o no un error.


**¿Cómo capturar y mostrar mensajes claros?**
Captura el tipo correcto para evitar silencios o excesos.
Muestra el mensaje de la excepción con print(e).
Evita duplicar mensajes en consola.
try:
    # operación sensible
    resultado = dividir(100, 2)
except DivisionError as e:
    print(e)  # mensaje claro y suficiente
finally:
    print("limpieza de recursos, si aplica")
Caso aplicado con News API client
En lugar de retornar arrays vacíos, lanza errores que expresen el fallo real. Define una jerarquía de excepciones para tu cliente y maneja los errores donde consumes la funcionalidad.



**¿Cómo definir una jerarquía de excepciones para la app?**

Crea una base para agrupar errores de la aplicación.
Hereda casos específicos como ApiKey inválida.
Documenta con docstrings para guiar a otros.
class NewsSystemError(Exception):
    """Error general en la app."""
    pass

class ApiKeyError(NewsSystemError):
    """ApiKey inválida."""
    pass

# En el cliente, en lugar de devolver lista vacía

def fetch_articles():
    # ... si falla la conexión con la API
    raise NewsSystemError("Ocurrió un error, no se pudo conectar con la API")


**¿Dónde y cómo manejar el error en el consumo?**
Maneja el error donde llamas al cliente, con try/except.
Inicializa variables como response_data en None para evitar referencias no definidas.
Muestra solo el mensaje de la excepción para evitar repeticiones.
response_data = None

try:
    response_data = fetch_articles()
except NewsSystemError as e:
    print(e)  # "Ocurrió un error, no se pudo conectar con la API"

if response_data is not None:
    # continuar con el flujo cuando hay datos válidos
    pass
Ideas clave para aplicar hoy: - Excepciones personalizadas: nombres claros y captura específica. - raise: decide cuándo detener el flujo con un mensaje útil. - Jerarquía de errores: una base común más casos concretos. - Manejo en el consumidor: try/except cerca del uso real. - Estados seguros: inicializa a None y valida antes de usar.


## Clase 13 : Anotaciones de tipo con type hints en Python



**¿Qué es el tipado dinámico y por qué usar type hints en Python?**
Python es dinámicamente tipado: cada variable recibe su tipo según el valor asignado. La metáfora de los frascos con azúcar y sal ayuda: puedes saber el contenido al abrirlos, pero con etiquetas es más claro. Los type hints son esas “etiquetas”. Indican el tipo esperado, aunque Python no obliga a cumplirlo en tiempo de ejecución. Aun así, aportan documentación, legibilidad y mejor soporte del editor.

Tipado dinámico: el tipo cambia según el valor asignado.
Type hints: anotaciones que orientan al desarrollador y a herramientas de chequeo.
No imponen el tipo en ejecución: ayudan a evitar errores antes de correr el programa.


**¿Cómo se agregó el typing a Python 3.5?**
Según se cuenta, el módulo typing llegó en la versión 3.5. Guido van Rossum tenía dudas por la complejidad añadida, pero una persona insistió para que se incorporara. Desde entonces, puedes anotar tipos sin cambiar la naturaleza dinámica del lenguaje.



**¿Cómo anotar variables y revisar su tipo en código?**
Primero, observa cómo Python asigna tipos automáticamente y cómo los type hints documentan la intención. La función type revela el tipo actual.

# Variable sin tipo explícito
variable = 42
print("variable:", variable, "tipo:", type(variable))

# Cambio de entero a texto: Python lo permite
variable = "Texto de prueba"
print("variable:", variable, "tipo:", type(variable))
La variable pasa de entero a string sin error: tipado dinámico.
Usar type() te muestra el tipo real en ejecución.
Ahora, anota el tipo con el operador dos puntos. Es la “etiqueta” del frasco:

# Anotación de tipo (type hint)
variable: int = 44
print("variable:", variable, "tipo:", type(variable))

# Python no fuerza el tipo en tiempo de ejecución
variable = "texto"  # Un validador de tipos marcará incompatibilidad.
variable: int = 44: indica que debería ser entero.
Python permite reasignar un string, pero un chequeador lo reportará.
Para permitir que una variable esté vacía, usa el operador pipeline | con None:

# Entero que también puede estar vacío
user_id: int | None = None
int | None comunica: puede ser entero o estar vacío.
Útil cuando aún no existe en la base de datos.
Habilidades y conceptos que practicas: - Usar el operador dos puntos para anotar tipos en variables. - Verificar el tipo en ejecución con la función type. - Entender que los type hints no imponen tipos en tiempo de ejecución. - Permitir valores vacíos con int | None usando el operador pipeline.


**¿Qué errores evitar con nombres de archivo y módulos?**
Evita nombrar archivos como types o typing: ya existen módulos con esos nombres y verás un warning. Usa nombres como type_hints.py para prevenir conflictos.


**¿Cómo validar tipos automáticamente con MyPy en el editor?**
Instala la extensión MyPy desde Extensiones. Tras activarla, aparecerán líneas con errores cuando una asignación no coincida con la anotación de tipo. Al pasar el mouse, verás mensajes como: tipo incompatible, la expresión era STR y luego se envía un entero.

Pasos prácticos: - Instalar la extensión MyPy en el editor. - Escribir anotaciones: variable: int = 44. - Reasignar un valor incompatible para ver el reporte. - Corregir según el mensaje de tipo incompatible.

Beneficios inmediatos: - Detectas errores mientras escribes, no al ejecutar. - Mantienes consistencia entre lo esperado y lo asignado. - Mejoras la legibilidad del código para todo el equipo.

**Enlace**
- https://lcmartinez.com/python-typing


**Ejemplos**

# Con anotaciones
- task_id: int = 1
- title: str = "Buy groceries"
- completed: bool = False
- due_date: str | None = "2023-12-31" # Usando sintaxis moderna (Python 3.10+)
- metadata: dict[str, str] = {"priority": "high"} # Sintaxis moderna (Python 3.9+)
- tags: list[str] = ["shopping", "important"] # Sintaxis moderna (Python 3.9+)


**Funciones**
Se anotan los tipos de los parámetros y el tipo de retorno después de ->.

# tasks debe estar definido previamente, p.ej. tasks: list[dict] = []
tasks: list[dict] = []

def create_task(title: str, due_date: str | None = None) -> dict:
    task = {
        "id": len(tasks) + 1, # Asume un mecanismo simple de ID
        "title": title,
        "completed": False,
        "due_date": due_date
    }
    tasks.append(task)
    return task



**Clases**
Se pueden anotar los atributos en el cuerpo de la clase o en __init__.


import random # Necesario para generate_id
def generate_id() -> int: return random.randint(1000, 9999) # Ejemplo simple

class Task:
    # Anotaciones de atributos de instancia
    id: int
    title: str
    completed: bool
    due_date: str | None # str o None
    tags: list[str]

    def __init__(self, title: str, due_date: str | None = None) -> None:
        self.id = generate_id()
        self.title = title
        self.completed = False
        self.due_date = due_date
        self.tags = [] # Inicializa como lista vacía

    # Anotación del tipo de retorno (referencia a la propia clase)
    def mark_complete(self) -> "Task":
        self.completed = True
        return self # Permite encadenar métodos



## Clase 14 : Tipado de funciones y estructuras de datos en Python




**¿Cómo tipar funciones en Python con parámetros y retorno?**
Anotar funciones hace explícito qué datos reciben y devuelven. Se usan dos puntos para parámetros y el operador flecha para el retorno. Así, el editor identifica tipos y ofrece autocompletado.

# función tipada: parámetros y retorno

def suma_clara(a: int, b: int) -> int:
    return a + b
Parámetros tipados con ":" y su tipo: int, str, etc.
Retorno con "->" y el tipo esperado.
El editor muestra tipos y autocompleta según las anotaciones.




**¿Qué ventaja práctica ofrece el tipado en proyectos grandes?**
Entiendes qué enviar a cada función sin abrir su archivo.
Reduces errores al integrar módulos en muchos archivos.
Documentas el código de forma viva y verificable.



**¿Cómo tipar listas, diccionarios y estructuras anidadas?**
Para colecciones, usa genéricos con corchetes. Con list indicas que es una lista; con tipos internos, restringes su contenido. Esto habilita autocompletado correcto y validaciones de incompatibilidad.

# lista de artículos: cada elemento es un diccionario con datos como title
articles: list[dict] = [
    {"title": "Primer post"},
    {"title": "Segundo post"},
]

# lista de listas restringida a strings
matriz: list[list[str]] = [
    ["artículos", "otro"],
    ["más", "items"],
]
Usa list[...] para tipar listas con su contenido.
El editor solo sugiere métodos válidos de lista tras el punto.
Anida tipos: list[list[str]] para listas de listas de strings.
Tipos básicos disponibles: int, str, list, dict y tuple.




**¿Qué ocurre si agregas un tipo incompatible?**
El editor marca el item como incompatible con el tipo declarado.
Evitas errores al momento de construir o ejecutar.
Corriges de inmediato antes de que el fallo se propague.




**¿Cuándo usar any y cómo apoyarte en mypy?**
Cuando migras código sin tipado, any permite avanzar mientras decides los tipos reales. Úsalo con moderación para no perder los beneficios del tipado.

# uso controlado de any
from typing import any

articulos3: list[any] = [
    "texto",
    123,
    {"title": "válido"},
]
any acepta cualquier tipo de dato.

- Útil al mover un proyecto sin typing a código tipado.
- No sobreabusar: mejor sin tipado que llenarlo de any en todos los archivos.
- Instala la extensión MyPy para detectar errores y empezar a limpiar el código mientras construyes el proyecto.




## Clase 15: Documentación en Python con docstrings y PEP 257




**¿Qué es un docstring en Python y por qué documentar código?**
Documentar evita confusiones al releer código. La mayoría de las veces no vuelves a cambiar el código: lo vuelves a leer. Un docstring es un texto entre tres comillas que describe módulos, funciones o clases.

Tres comillas permiten múltiples líneas en una sola cadena de texto.
Cada archivo puede empezar con un docstring de módulo claro.
Funciones y clases deben tener docstrings que expliquen propósito y uso.



**¿Cómo iniciar con triple comillas?**
"""
Explicación de docstrings en Python.
Permite escribir documentación multilínea para archivos, funciones y clases.
"""

# Ejemplo sin docstring
def saludo():
    return "Hola"

# Ejemplo con docstring
def saludo_doc():
    """Esta función devuelve un saludo.

    Retorno:
        str: un saludo en español.
    """
    return "Hola"
Usa múltiples líneas para dar claridad.
Evita textos crípticos: sé directo y específico.



**¿Cómo se escriben y consultan docstrings según PEP 257?**
El PEP 257 propone la anatomía de una buena documentación. Empieza con una descripción corta, luego opcionalmente una explicación larga, parámetros, retorno, excepciones y ejemplos. Además, puedes consultar esa ayuda desde consola o el editor.


**¿Cómo estructurar el docstring según PEP 257?**
def limpiar_texto(texto: str) -> str:
    """Limpia y normaliza el texto removiendo espacios y convirtiendo a minúsculas.

    Descripción:
        esta función toma la cadena de texto y realiza operaciones de limpieza.

    Parámetros:
        texto (str): cadena de texto que se va a limpiar y normalizar.

    Retorno:
        str: texto limpio y normalizado.

    Excepciones:
        TypeError: si texto no es de tipo str.

    Ejemplos:
        >>> limpiar_texto("  Hola, mundo  ")
        'hola, mundo'
    """
    if not isinstance(texto, str):
        raise TypeError("texto debe ser str")
    return texto.strip().lower()
Tipos explícitos ayudan al editor y a quien lee (ver typing y anotaciones como texto: str y -> str).
Ejemplos tipo doctest (>>>) muestran entradas y salidas esperadas.




**¿Cómo consultar la documentación en consola y editor?**
print(saludo_doc.__doc__)   # Accede al atributo protegido __doc__
help(saludo_doc)            # Abre la guía interactiva; presiona Q para salir
Con __doc__ obtienes el texto del docstring directamente.
Con help() ves firma, retorno y la ayuda completa.
En el editor, al pasar el cursor, se muestra la firma, el retorno y la documentación con tipos.




**¿Cómo usar IA y buenas prácticas para documentar?**
Puedes aprovechar Cloud Code u otro entorno para pedir a un LLM que redacte docstrings completos. Proporciona el código y el contexto del PEP 257 para que genere descripción, parámetros, retorno, excepciones y ejemplos en español cuando lo necesites.



**¿Qué prompt usar para generar un docstring?**
Genera un docstring completo en español. Sigue el PEP 257 para esta función.
Incluye: descripción, parámetros, retorno, excepciones y ejemplos.
Recomendación general: se sugiere inglés, pero usar español facilita para hispanohablantes.
Verifica la salida: debe reflejar lo que realmente hace la función.



**¿Qué buenas prácticas elevan la calidad?**
- Sé conciso y claro: pide menos relleno y más precisión.
- Mantén la documentación actualizada: ajusta cuando cambie la funcionalidad.
- Documenta ejemplos: facilitan entender el comportamiento real.



## Clase 16: Entornos virtuales en Python: qué son y por qué los necesitas



**¿Qué problema resuelven los entornos virtuales en Python?**
Los conflictos aparecen cuando dos proyectos requieren versiones distintas de la misma librería. Instalar una versión nueva de Pandas sobre otra puede romper un proyecto anterior. La solución en Python es clara: usar entornos virtuales, formalizados como Virtual Environments and Packages.

Evitan dañar instalaciones previas al probar versiones nuevas de paquetes.
Permiten usar varias versiones del mismo paquete en un mismo equipo.
Cada entorno es una carpeta independiente con una instalación real de Python.
Puedes crear, borrar y recrear entornos sin afectar otros proyectos.
Idea clave: cada entorno incluye su propio ejecutable de Python. Al activarlo, todo se ejecuta con esa versión y sus dependencias.




**¿Qué significa activar un entorno virtual?**
Activar es lograr que, al ejecutar Python, se use el ejecutable del entorno seleccionado. Si activas el entorno equivocado o no activas ninguno y haces un import, puede aparecer un error de “el módulo no fue encontrado”.

Confirma siempre qué entorno está activo antes de trabajar.
Python genera un script para activar el entorno de forma automática.
Un entorno nuevo se crea sin paquetes: empieza vacío.



**¿Cómo instalar y verificar paquetes con pip?**
Dentro del entorno, gestiona dependencias con PIP: instala o desinstala y consulta detalles. Puedes ver la información de una librería específica, como su versión y metadatos.

pip show request
Instala y desinstala paquetes según lo requiera el proyecto.
Revisa la lista de dependencias del entorno cuando necesites auditar tu configuración.



**¿Cómo compartir dependencias y trabajar en distintos sistemas?**
Para que tu código no falle en manos de otra persona, comparte siempre las dependencias. La práctica recomendada es usar requirements.txt, un archivo de texto con todas las librerías y sus versiones específicas.

Establece la versión exacta compatible con tu código (ejemplo mencionado: 1.9.2).
Entrega al equipo un requirements.txt para asegurar el mismo entorno.
Sobre sistemas operativos, hay diferencias relevantes al crear y activar entornos:

En Mac y Linux, los pasos suelen ser similares por ser entornos Unix.
En Windows cambian incluso las rutas: usan contrabarra en vez de barra.
Tendrás guías separadas por sistema para crear y activar sin complicaciones.

**ENLACE**
- https://docs.python.org/3/tutorial/venv.html



## Clase 17: Creación y gestión de entornos virtuales con venv en Python



**¿Cómo verificar Python y ubicar el ejecutable con which?**
Antes de crear un entorno virtual, confirma que Python está instalado y localiza el ejecutable correcto. Verlo es clave cuando hay múltiples versiones o un alias a python3.


**¿Qué comandos confirman la instalación?**
Usa estos comandos en la terminal para verificar versión y ruta del ejecutable.

python --version
which python
which python3
Confirma la versión de Python instalada.
Identifica si python apunta a python3 como alias.
Comprueba el ejecutable real (por ejemplo, instalado con Homebrew en macOS).



**¿Por qué importa el path cuando hay varios ejecutables?**
Porque al activar un entorno virtual, el path del ejecutable cambia para apuntar al Python del entorno. Así evitas ejecutar paquetes del sistema por error. Verifica con which python3 antes y después de activar el entorno para notar la diferencia.



**¿Cómo crear y activar un entorno virtual con venv?**
Crear un entorno con -m venv aísla dependencias, manteniendo tu proyecto limpio y reproducible. Al ejecutarlo, se genera una carpeta con scripts y configuraciones propias del entorno.


**¿Qué crea python -m venv y qué hay en las carpetas?**
Ejecuta el módulo venv y nómbralo, por ejemplo newsemv.

python -m venv newsemv
Tras crearlo, verás:

bin/: ejecutables de Python, ejecutables de pip y scripts de activación para Linux y Windows.
include/: cabeceras de Python usadas durante instalaciones con pip.
lib/: librerías instaladas dentro del entorno; comienza vacío con solo pip.
Archivo de configuración: ruta del home y versión usados al ejecutar Python.
Idea clave: cada entorno nuevo inicia sin paquetes, listo para instalar solo lo necesario.



**¿Cómo activar y desactivar el entorno virtual?**
Activa y verifica que cambió el ejecutable a la ruta del entorno. Luego desactiva cuando termines.

# activar (Linux/macOS)
source newsemv/bin/activate

# verificar rutas
which python
which python3

# desactivar
deactivate
Al activar, which muestra el path dentro de newsemv.
Al desactivar, which vuelve al ejecutable global (ejemplo: Homebrew).
Mantén claridad sobre qué entorno está activo para evitar errores.



**¿Cómo ayuda Visual Studio Code con entornos?**
La extensión de Python y el panel de Python Environments permiten seleccionar el entorno, ver dependencias e incluso activar automáticamente el entorno al abrir la terminal integrada. Útil para no equivocarte de intérprete.


**¿Cómo instalar dependencias desde PyPI y fijar versiones con requirements.txt?**
Instala paquetes desde PyPI, lista dependencias con pip y fija versiones con requirements.txt. Así otras personas pueden replicar tu entorno sin sorpresas.



**¿Cómo instalar y listar paquetes con pip?**
Busca en PyPI y copia el comando de instalación. Ejemplo con ruff (formateador de código):

pip install ruff

# verificar paquetes instalados
override
pip list
Instala desde PyPI la versión disponible.
Visualiza los paquetes presentes en tu entorno virtual.



**¿Cómo compartir dependencias con requirements.txt?**
Usa pip freeze para capturar la versión exacta instalada y compártela en un archivo.

# generar el archivo con versiones fijadas
pip freeze > requirements.txt

# instalar desde el archivo
pip install -r requirements.txt

# desinstalar un paquete específico
pip uninstall ruff -y
pip freeze exporta en formato paquete==versión para asegurar reproducibilidad.
pip install -r instala exactamente las versiones definidas.
Puedes reinstalar tras desinstalar para validar el flujo.



**¿Qué buenas prácticas debes aplicar?**
No subas la carpeta del entorno virtual al repo. Agrega el nombre del entorno a .gitignore.
Mantén versiones fijadas en requirements.txt para evitar roturas por actualizaciones.
Considera usar python-dotenv para gestionar tu API key fuera del código y protegerla.



## Clase 18: Creación de entornos virtuales en Windows con Python



**¿Qué resuelve un entorno virtual en Windows?**
Los entornos virtuales permiten separar paquetes y versiones de Python por proyecto. Así evitas conflictos, reproduces instalaciones y mantienes cada proyecto limpio. Una vez creado, el entorno inicia sin paquetes instalados: es un espacio independiente y controlado.

Aislamiento de dependencias por proyecto.
Versiones separadas de Python por entorno.
Instalaciones reproducibles con un archivo de requerimientos.



**¿Cómo verificar Python y su instalación?**
Confirma que Python está disponible y dónde se ubica en tu sistema.

python --version
where python
Verás rutas distintas: una del sistema y otra de tu instalación manual.
En PowerShell, para ejecutar un comando de CMD:
cmd /c where python
Esto muestra el orden de búsqueda del ejecutable: primero el del entorno activo, luego otras rutas del sistema.




**¿Cómo crear el entorno con venv y qué carpetas trae?**
Crea el entorno con el módulo venv. Puedes usar un nombre corto y descriptivo.

python -m venv MuseEnv
Al finalizar, aparece una nueva carpeta con elementos clave:

Carpeta Scripts: activadores y desactivadores del entorno, como activate.bat y Activate.ps1.
Ejecutable de Python: python.exe propio del entorno.
Archivo de configuración: “pyenv config” con rutas y ajustes del entorno.
Carpeta Lib: paquetes instalados solo para este entorno.



**¿Cómo activar y solucionar errores en PowerShell?**
Para activar en PowerShell, usa el script de la carpeta Scripts. Si ves un error por ejecución de scripts deshabilitada, habilita según la nota para Windows en la documentación de Python y vuelve a activar.

# Activar en PowerShell (ruta relativa dentro de Scripts)
./Scripts/Activate.ps1
Si hay restricción de ejecución, copia el comando sugerido en la documentación oficial y ejecútalo.
Al activarse, la terminal cambia indicando el nombre del entorno.
Para desactivar:
deactivate
Útil para validar el ejecutable activo desde PowerShell:
cmd /c where python
Primero se usará el python.exe del entorno. Si falla, se intentan otras rutas listadas.



**¿Cómo identificar el contenido de Scripts y Lib?**
Al explorar la estructura notarás:

Scripts: contiene Activate.ps1, activate.bat y utilidades del entorno.
Lib: refleja paquetes instalados con pip. Inicia vacío al crear el entorno.
Archivo “pyenv config”: define rutas y variables para que el entorno sepa qué usar.



**¿Cómo instalar paquetes y congelar dependencias con pip?**
Busca paquetes en PyPI, copia el comando de instalación y ejecútalo con el entorno activo. El ejemplo usa el paquete “roof” para formateo de código.

# Instalar un paquete desde PyPI
pip install roof

# Listar paquetes del entorno
pip list
Para ver reflejo en la carpeta del entorno, revisa Lib después de instalar.
Si desactivas el entorno y ejecutas pip list, ya no verás los paquetes del entorno.


**¿Cómo generar y usar requirements.txt?**
Estándar para compartir dependencias con tu equipo: requirements.txt.

# Con el entorno activo, “congela” versiones exactas
pip freeze > requirements.txt

# Desinstalar un paquete del entorno
pip uninstall roof

# Instalar desde requirements.txt
pip install -r requirements.txt
pip freeze guarda paquetes y versiones exactas para instalaciones reproducibles.
pip install -r lee el archivo y reinstala lo necesario sin escribir cada paquete a mano.


**¿Cómo aprovechar Visual Studio Code con entornos virtuales?**
Al abrir un archivo de Python, Visual Studio Code muestra el entorno activo en la barra inferior. Es práctico cuando la terminal está cerrada: confirmas el intérprete seleccionado a simple vista.

Ver el entorno activo sin abrir la terminal.
Cambiar de entorno desde el selector de intérprete.



## Clase 19: Gestión moderna de dependencias Python con UV y pyproject



**¿Qué es V y por qué acelera la gestión de dependencias en Python?**
V es una herramienta de Astral para instalar Python, crear entornos virtuales y gestionar dependencias con comandos simples. Al usar Rust bajo el capó, las instalaciones son notablemente más rápidas. Además, estandariza el uso de pyproject para definir dependencias y configura un entorno virtual llamado .vm que los editores de código detectan fácilmente.

Compatible con macOS y Windows: mismos comandos en ambos sistemas operativos.
Integración con pyproject: dependencias definidas en un único archivo.
Mejor rendimiento: instalaciones más rápidas gracias a Rust.
Flujo claro: comandos como help, init, add, remove y sync.
Buenas prácticas: no subir la carpeta .vm al repositorio.
Ejecuta la instalación desde PyPI con pip.

pip install V
V help


**¿Cómo iniciar un proyecto con V y pyproject?**
El comando init crea la estructura base del proyecto y evita configuraciones manuales. Se generan tres archivos clave, incluyendo el estándar pyproject con una sección dependencies lista para usar.

V init
Python version: define la versión de Python del proyecto para asegurar consistencia.
readme: archivo inicial para documentación futura.
pyproject: archivo central para dependencias y configuración del proyecto.
Para agregar una dependencia como ruff (formateador estilo PEP ocho), usa add. El sistema escribe la versión adecuada en pyproject y genera Vlock, que fija versiones exactas, incluyendo las transitivas, para evitar incompatibilidades.

V add ruff
Si aparece un warning por desajuste de entornos, es porque V crea y usa un entorno .vm por defecto. Conviene borrar el entorno anterior y, si la terminal sigue apuntando al viejo entorno, cerrarla y abrirla de nuevo para que el warning desaparezca.



**¿Qué comandos de V optimizan el flujo de trabajo?**
Una vez configurado el entorno .vm, el flujo diario se simplifica con comandos que actualizan pyproject, limpian dependencias no usadas y sincronizan el entorno virtual para alinearlo con la configuración declarada.



**¿Cómo agregar o quitar dependencias con V add y V remove?**
Agrega paquetes y escríbelos en pyproject con su versión compatible.
Genera o actualiza Vlock con bloqueos de versiones.
Al eliminar, limpia dependencias transitivas que ya no se necesitan.
V add request
V remove requests
Claves a considerar: - pyproject se actualiza en cada operación. - Vlock asegura reproducibilidad del entorno. - El borrado es inteligente: quita lo innecesario automáticamente.


**¿Cómo sincronizar el entorno con V sync?**
Alinea el entorno .vm con lo declarado en pyproject y Vlock.
Útil tras borrar o agregar dependencias, o al cambiar de rama.
Ideal para otros desarrolladores que descargan el proyecto y necesitan replicar el entorno exacto.
V sync
Consejos prácticos: - tras cambios de dependencias, ejecuta sync para evitar desajustes. - si quitaste una librería, sync removerá también su huella del entorno.



**¿Cómo gestionar el entorno virtual .vm y evitar conflictos?**
Cada vez que usas V, se activa el entorno .vm automáticamente.
Si ves un warning de entorno, cierra y abre la terminal para refrescarlo.
No subas .vm al repositorio: es específico de tu sistema.

**cOMANDOS DE V**
- pip install uv => instala uv
- uv help => muestra ayuda
- uv init => crea la estructura base del proyecto y evita configuraciones manuales. Se generan tres archivos clave, incluyendo el estándar pyproject con una sección dependencies lista para usar.
- uv add ruff => instala paquetes y los agrega a pyproject 
- uv add request => instalo otro paquete y lo agrega a pyproject
- uv remove requests => quito paquete y lo quita de pyproject
- uv sync => alinea el entorno .vm con lo declarado en pyproject y Vlock sincronica todas las dependencias en tu entorno actual 




## Clase 20: Modularización de código Python con responsabilidad única


**¿Por qué modularizar en Python para escalar?**
Modularizar significa dividir la aplicación en archivos de Python que agrupan funciones o clases relacionadas. La regla central: cada módulo debe manejar una sola responsabilidad. Así puedes abrir un archivo y entender solo autenticación, configuración o el cliente de la API, sin perderte en cientos de líneas.


**¿Qué es un módulo y cuál es su responsabilidad?**
Archivo de Python con funciones, clases o utilidades relacionadas.
Una sola responsabilidad por módulo.
Facilita leer y modificar partes específicas, como autenticación o config.



**¿Qué beneficios aporta al mantenimiento y a LLMs?**
Menos fricción al hacer mantenimiento. No más archivos gigantes difíciles de seguir.
Mejor colaboración: cada quien toca solo lo necesario.
Compatibilidad con LLMs. Pueden importar y modificar solo el módulo relevante.



**¿Cómo nombrar e importar módulos sin conflictos en Python?**
Nombrar bien evita errores y sorpresas al importar. Además, entender cómo funciona el sistema de imports en Python evita chocar con módulos estándar como datetime.


**¿Cómo usar snake case para nombres válidos?**
Usa snake case para archivos: nombres en minúsculas con guiones bajos.
Corrige nombres no válidos para que el módulo sea importable.



**¿Cómo evitar chocar con módulos estándar de Python?**
No llames a tu archivo igual que uno del lenguaje. Ejemplo: si haces from datetime, Python buscará primero el módulo estándar y no el tuyo.
Regla práctica: evita nombres de la biblioteca estándar para tus módulos.



**¿Cómo funcionan import y from import con docstrings?**
Puedes importar con el nombre del archivo: importar el módulo y acceder a su contenido.
El editor suele autocompletar y mostrar la documentación de docstrings.
También puedes usar from docstring import elemento definido adentro, como “ejemplo con docstring”.
Coloca los imports arriba para evitar el warning del editor y úsalo para que desaparezca el aviso.



**¿Cómo dividir el proyecto en módulos prácticos?**
Partiendo de un main.py con todo junto, el objetivo es separar ejemplos, clientes externos y configuración en módulos claros. Así el proyecto crece sin perder orden.




**¿Qué mover de main.py a example.py?**
Los ejemplos del curso deben ir en un módulo dedicado: example.py.
Esto crea un “módulo de ejemplos” accesible y fácil de consultar.
Deja en main.py solo lo esencial de la aplicación.



**¿Cómo crear un módulo news-api-client para la API?**
Crea un archivo llamado news-api-client con todo lo relacionado al client de la API.
Importa lo necesario para la conexión, por ejemplo URL if y el módulo JSON.
Si existe un “API key error” en main, considera mover su definición a un módulo común para mejores imports.
Usa el quick fix del editor para agregar imports, verificando que sean los correctos.



**¿Cómo inspeccionar un módulo con dir en la terminal?**
Abre la terminal y ejecuta Python.
Importa un módulo, por ejemplo datetime.
Usa la función integrada dir(módulo) para listar sus funcionalidades.
Útil para explorar qué ofrece un módulo antes de usarlo.
Ideas clave y habilidades prácticas: - Modularización con responsabilidad única. - Convención de nombres en snake case. - Evitar conflictos con la biblioteca estándar como datetime. - Importar con import y from import según convenga. - Uso de docstrings para documentación en el editor. - Exploración con dir en consola para conocer funcionalidades. - Separación en archivos como example.py, main.py y news-api-client. - Gestión de imports de URL if, JSON y manejo de “API key error”. - Beneficios para mantenimiento y LLMs al aislar cambios.

**Enlace**
- https://docs.python.org/3/tutorial/modules.html



## Clase 21: Paquetes Python: de estructura plana a código modular



**¿Cómo pasar de estructura plana a paquetes escalables?**
Transformar módulos sueltos en una estructura de paquetes hace el proyecto más claro y fácil de mantener. La lógica de negocio queda en un paquete principal y los ejemplos en otro, con un main mínimo que solo orquesta imports.

Crear el paquete examples con init.py.
Crear el paquete news_analyzer con init.py.
Mover módulos de la app: api_client, config, exceptions, utils.
Mantener main.py en el root para ejecutar: python main.py.
Confirmar que la app no depende de los ejemplos para funcionar.
Estructura sugerida:

.
├── main.py
├── examples/
│   ├── __init__.py
│   ├── ejemplo_1.py
│   └── ejemplo_2.py
└── news_analyzer/
    ├── __init__.py
    ├── api_client.py   # antes: news_api_client.py (renombrado durante el refactor)
    ├── config.py       # contiene API key y base URL
    ├── exceptions.py
    └── utils.py

Resultado: el main solo importa lo necesario para mostrar artículos desde la API, y el paquete news_analyzer concentra la aplicación. Así, el antiguo monolito se convierte en módulos y paquetes listos para crecer.


**¿Por qué dejar main.py en el root?**
Facilita ejecutar desde la línea de comandos: python main.py.
Evita rutas confusas de imports al ejecutar.
Mantiene una entrada clara a la aplicación.


**¿Cómo ayuda Pylance en el refactor?**
Actualiza imports al renombrar archivos dentro del paquete.
Reduce errores por nombres desactualizados.
Acelera el refactor al mover muchos módulos a la vez.


**¿Qué es un paquete en Python y cómo se inicializa?**
Un paquete es una carpeta con un archivo especial init.py. Ese archivo se ejecuta cuando se importa el paquete: se puede usar para inicializar variables o una configuración única.

Ejemplo de init.py mínimo:

# news_analyzer/__init__.py
# Inicialización del paquete: configura lo necesario una sola vez.
Los paquetes anidados son comunes: cada nivel requiere su propio init.py. Puedes tener un padre con varios hijos y, dentro de cada hijo, más paquetes y módulos. Esto permite separar la app de los tutoriales y, en proyectos grandes, organizar dominios y funcionalidades sin mezclar responsabilidades.

Práctica recomendada: en examples, crea paquetes anidados y prueba sus imports desde un archivo Python para entrenar la mecánica.


**¿Qué beneficios trae una estructura por paquetes?**
Separación clara entre app y ejemplos.
Escalabilidad: añadir nuevas funcionalidades es más simple.
Imports organizados y predecibles.
Código más profesional y colaborativo.


**¿Cómo organizar imports y evitar errores al refactor?**
Al mover archivos, es común ver errores de “no se encuentra el módulo”. Lee el traceback, identifica desde dónde busca Python y corrige la ruta de importación.



**¿Cuándo usar importación relativa con punto?**
Si un módulo importa a otro del mismo paquete, usa importación relativa con un punto para indicar el paquete actual.

# news_analyzer/api_client.py

# imports locales (mismo paquete): usar importación relativa
from .config import API_KEY, BASE_URL
from .exceptions import AppError  # ejemplo de clase de excepción dentro del paquete

# recomendación PEP 8: los imports locales van al final del bloque de imports
Si importas desde fuera del paquete, usa ruta absoluta con el nombre del paquete:

# main.py (en el root)
from news_analyzer.config import API_KEY, BASE_URL
from news_analyzer import api_client, exceptions
Caso real tras mover archivos: el módulo api_client buscaba config en el root y falló. Solución: cambiar a importación relativa (from .config import ...) dentro de api_client. Aplica lo mismo a exceptions.


**¿Cómo ordenar imports según PEP 8?**
Primero estándar de Python.
Luego terceros.
Al final los imports locales del paquete, separados por una línea en blanco.


## Clase 22: Función enumerate en Python para indexar listas automáticamente

Por qué usar enumerate en Python para listas e iterables?
Usar un contador dentro de un for añade complejidad y riesgo de errores. Enumerate simplifica: toma una lista o iterable, produce una tupla con el índice y el elemento, y acepta un inicio personalizado con start. Esta función es más rápida, mejora la claridad y es menos propensa a bugs.


**¿Qué problema resuelve con for y contador manual?**
Código tradicional con contador explícito:

counter = 1
for article in sample_articles:
    print(f"{counter}. {article}")
    counter = counter + 1
Inconvenientes: - Más líneas y lógica extra para el contador. - Mayor probabilidad de errores. - Itera toda la lista incluso si no se necesita de inmediato.


**¿Cómo luce la solución con enumerate y start?**
Con enumerate, el índice y el elemento llegan juntos, y puedes definir el inicio:

for index, article in enumerate(sample_articles, start=1):
    print(f"{index}. {article}")
Incluso puedes iniciar en otro valor, por ejemplo 10:

for index, article in enumerate(sample_articles, start=10):
    print(f"{index}. {article}")
Beneficios clave: - Tupla (índice, elemento) lista para usar. - start configurable. - Evaluación perezosa: el objeto se materializa al iterar.


**¿Cómo se implementa enumerate paso a paso en el proyecto?**
Primero, ver la representación de enumerate y cómo produce tuplas al iterar:

enum_articles = enumerate(sample_articles)
print(enum_articles)  # representación del objeto en memoria
for item in enum_articles:
    print(item)  # (índice, article)
Luego, aplicar enumerate a una necesidad real: listar fuentes únicas de noticias. Se parte de una función que devuelve un set sin duplicados.



**¿Cómo obtener fuentes únicas con set y getSources?**
Generar el conjunto de fuentes y luego enumerarlo desde 1:

# suponiendo que ya cuentas con la función getSources
source_set = getSources(articles)  # devuelve un set sin duplicados
for index, source in enumerate(source_set, start=1):
    print(f"{index}. {source}")
Observaciones prácticas: - Se mostró un set con todas las fuentes sin repetidos. - Al enumerarlas, se obtuvo un listado numerado claro. - En el ejemplo, se contaron 38 fuentes únicas.


**¿Cómo nombrar mejor para legibilidad del código?**
Renombrar para expresar intención mejora el mantenimiento:

# antes
source_set = getSources(articles)

# después
unique_sources = get_unique_sources(articles)
for idx, src in enumerate(unique_sources, start=1):
    print(f"{idx}. {src}")


**¿Qué conceptos y habilidades refuerzas con este patrón?**
Adoptar enumerate fortalece competencias básicas de Python y buenas prácticas.

Enumerate: función integrada que produce índice y elemento como tupla.
Índice y elemento: desempaquetado directo en el for para mayor claridad.
Parámetro start: define el inicio del conteo sin lógica adicional.
Evaluación perezosa: el objeto de enumerate no recorre hasta iterar, eficiente con colecciones grandes.
Tupla: estructura inmutable que agrupa el índice y el valor.
Iterable: cualquier objeto que puede recorrerse en un for.
Set: colección sin duplicados para obtener fuentes únicas de forma directa.
Legibilidad y mantenimiento: nombres como get_unique_sources comunican intención y evitan errores.
Rendimiento: enumerate está optimizado y suele ser más rápido que manejar contadores manuales.
Evitar bugs: menos estado mutable (sin counter) implica menos puntos de fallo.


🔍 ¿Qué es enumerate()?

📘 Es una función integrada de Python que permite:

➡️ Recorrer listas o iterables añadiendo un índice automáticamente.

➡️ Devolver pares (índice, elemento) listos para usar.

➡️ Definir el índice inicial con start.

➡️ Evaluarse solo al iterar, lo que mejora la eficiencia.

🧩 Ideal para trabajar con listas grandes o donde se necesite numerar elementos.

⚡ Ventajas principales

✨ Legibilidad: el código se entiende de inmediato.

⚙️ Eficiencia: se ejecuta más rápido que usar contadores manuales.

💬 Simplicidad: elimina variables extra como counter.

🧱 Seguridad: menos riesgo de errores (sin estado mutable).

📈 Escalabilidad: funciona bien con millones de elementos.

⚠️ El problema del contador manual



## Clase 23: Filtrado de listas con filter en Python


**¿Cómo filtrar números pares con un for y operador módulo?**
Empezamos con una lista del 1 al 10 y un filtrado manual. La clave es el operador módulo: si num % 2 == 0, el número es par. Así construimos una nueva lista con los pares.

# filter_pairs.py
numbers = list(range(1, 11))
pairs = []

for num in numbers:
    if num % 2 == 0:  # operador módulo con 2
        pairs.append(num)

print(numbers)
print(pairs)
Uso de operador módulo para evaluar pares.
Construcción de una lista a partir de otra.
Impresión de lista original y lista filtrada.


**¿Qué hace filter en Python y por qué retorna un iterador?**
La función filter recibe dos argumentos: una función que retorna booleano y un iterable (por ejemplo, list, set o las llaves de un diccionario). Al aplicarla, devuelve un iterador que se evalúa bajo demanda, útil con muchos datos porque solo “se calcula” al consumirlo.

def is_pair(n: int) -> bool:
    return n % 2 == 0

pairs_iter = filter(is_pair, numbers)  # retorna un iterador

for pair in pairs_iter:
    print(pair)
Si se necesita la colección completa, conviene convertir el iterador a list.

pairs_list = list(filter(is_pair, numbers))
print(pairs_list)
filter requiere función que retorne True/False y un iterable.
Retorna un iterador, no una lista directa.
Conversión con list(...) cuando se desea materializar resultados.
Evaluación perezosa: solo se procesa cuando se consume, ideal si luego usarás pocos elementos.


**¿Cómo integrar filter para seleccionar artículos por fuente en un sistema de noticias?**
Se implementa una utilidad getarticles_by_source que recibe una lista de diccionarios y un str con la fuente. Se usa filter con lambda para comparar el nombre de la fuente en cada artículo y se convierte el resultado a lista para mantener el typing esperado.

from typing import List, Dict

def getarticles_by_source(articles: List[Dict], source: str) -> List[Dict]:
    filtered = filter(
        lambda article: article["source"]["name"].lower() == source.lower(),
        articles
    )
    return list(filtered)
Uso de lambda como función anónima para el criterio de filtrado.
Acceso a campos anidados: article['source']['name'].
Comparación case-insensitive con .lower() en ambos lados para evitar discrepancias de mayúsculas/minúsculas.
Conversión a list para cumplir con el tipo de retorno y evitar errores de typing.


**¿Cómo depurar la fuente correcta disponible?**
Si el resultado es una lista vacía, imprime las fuentes únicas para verificar nombres exactos (por ejemplo, diferencias entre “GitHub” y “github.com”). Un “set comprimido” ayuda a inspeccionar rápidamente.

sources = {article["source"]["name"] for article in articles}
print(sources)
Inspección rápida con comprensión de conjuntos.
Verificación de valores reales presentes en source.name.
Ajuste del criterio: coincidencia exacta o normalizada con .lower().


**¿Cómo presentar los resultados sin for condicionales adicionales?**
Tras filtrar, se pueden imprimir campos específicos como el título.

github_articles = getarticles_by_source(articles, "github.com")
for a in github_articles:
    print(a["title"])  # mostrar solo el título
Mantén el filtrado en una sola expresión con filter.
Evita bucles condicionales redundantes que consumen CPU o memoria.
Muestra la información clave que necesitas, como el title.


## Clase 24: Función map para calcular tiempo de lectura en Python



**¿Cómo convertir un for en map en Python?**
Usar map te permite aplicar una función a cada elemento de una list sin recorrerla manualmente. Primero, se parte de un enfoque clásico con for para obtener los cuadrados y luego se reemplaza por map, que es más expresivo y perezoso en su evaluación: solo calcula cuando accedes a los elementos.

Código con for:

numbers = [1, 2, 3, 4, 5]
cuadrados = []
for num in numbers:
    cuadrados.append(num ** 2)
print(numbers, cuadrados)
Código con map y función nombrada:

def cuadrado(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]
cuadrados_map = list(map(cuadrado, numbers))  # map es perezoso, por eso list(...)
print(cuadrados_map)
Claves prácticas: - map recibe primero una función y luego un iterable. - map, como filter, no materializa resultados hasta que los consumes. - Convertir a list fuerza el cálculo inmediato para imprimir o depurar.


**¿Cómo calcular el tiempo de lectura con map en una app de noticias?**
El objetivo es agregar a cada artículo un campo reading_time. Para ello, se crea una función utilitaria en utils que recibe un diccionario de artículo, calcula minutos con base en su content y devuelve el mismo diccionario modificado. Se corrigió el tipo de retorno de stream a dict para alinear con lo que realmente se retorna.

Función en utils:

# utils.py
def get_reading_time(article: dict) -> dict:
    """
    Calcula el tiempo de lectura.
    """
    minutos = len(article["content"]) // 200 + 1  # ~200 caracteres por minuto
    article["reading_time"] = minutos
    return article
Integración en main con map y conversión a list para ver resultados de inmediato:

# main.py
from utils import get_reading_time

# articles: lista de diccionarios con al menos "title" y "content"
articulos_con_tiempo = list(map(get_reading_time, articles))

# Imprimir título y tiempo de lectura
for art in articulos_con_tiempo:
    print(art["title"], "-", art["reading_time"], "min")
Qué observar en la salida: - Verás los campos originales como source y description, y el nuevo reading_time en minutos. - Puedes imprimir un solo elemento o iterar para mostrar título y tiempo de lectura.


**¿Por qué map mejora el rendimiento y la mantenibilidad?**
map aporta rendimiento porque es perezoso: no procesa toda la lista de una vez, solo cuando accedes a cada elemento. Además, usar una función nombrada en lugar de una lambda facilita entender la transformación, hacer pruebas unitarias y mantener un código más declarativo.

Buenas prácticas y palabras clave que aplican: - map y su parentesco con filter para transformar y filtrar colecciones. - Uso de una función con nombre para transformaciones complejas: más legible y testeable. - Evaluación perezosa: eficiencia al trabajar con listas grandes. - Tipos y contratos claros: retorno como dict cuando modificas un diccionario. - Utilidades modulares: separar lógica en utils y orquestación en main. - Métrica definida: aproximadamente 200 caracteres por minuto para reading_time y sumar uno para asegurar un mínimo. - Conceptos de iteradores: base de herramientas rápidas en Python, como las de la documentación de itertools.


## Clase 25: Conexión de OpenAI API con variables de entorno en Python


**¿Cómo proteger la API key con .env y variables de entorno?**
Guardar llaves de la API en el código es un riesgo. La solución es .env y python-dotenv, cargando variables de entorno con seguridad y sin subirlas al repositorio.

Usa un archivo .env para llaves y contraseñas.
Instala python-dotenv con v: v add python-dotenv.
Carga variables con load_dotenv y os.environ.get.
Evita exponer la key en el código y en el control de versiones.
Código base:

# Instalación
v add python-dotenv
# config.py
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# print(OPENAI_API_KEY)  # Úsalo solo para probar; luego elimínalo.
# .env (ejemplo)
OPENAI_API_KEY=tu_llave_secreta
Puntos clave: - variables de entorno con os.environ.get. - No subir API keys al repositorio. - Imprimir solo para probar y luego borrar el print.


**¿Cómo instalar la librería de OpenAI y configurar el cliente?**
OpenAI ofrece una librería oficial en PyPI. Se integra creando un client y usando un model como GPT-4 (requiere saldo para su uso).

Instala la librería desde PyPI.
Crea un archivo OpenAI.py para centralizar la configuración.
El client toma la key desde el entorno ya cargado.
Usa instructions y input para controlar la respuesta.
# Instalación de la librería oficial
v add openai
# OpenAI.py
from openai import OpenAI

client = OpenAI()  # Toma la API key desde el entorno

def analyze_news_withIA(articles, query):
    # Implementación mostrada abajo: construir *prompt* con contexto y consultar la API.
    pass
Notas: - La librería incluye ejemplos claros de uso. - Si usas v como gestor, puedes prescindir de un archivo de requerimientos y mantener una única fuente de dependencias. - El endpoint de ejemplo utiliza instructions, input y selección de model.


**¿Cómo construir el prompt con artículos y hacer la consulta?**
La estrategia es pasar a la IA un contexto con títulos y descripciones de artículos, y luego una pregunta concreta. Para controlar costos, limita a los primeros diez artículos y recorta la descripción a cien caracteres.

Extrae título y descripción con una lista por comprensión.
Limita a 10 artículos para reducir costos en el LLM.
Recorta descripciones a 100 caracteres.
Redacta un prompt claro: “Responde de forma concisa en español”.
# Construcción de contexto y prompt

def analyze_news_withIA(articles, query):
    context = "\n".join([
        f"- Título: {a['title']}. Descripción: {a['description'][:100]}."
        for a in articles[:10]
    ])

    prompt = (
        "Basándote en estas noticias:\n"
        f"{context}\n"
        f"Pregunta: «{query}». Responde de forma concisa en español."
    )

    # Ejemplo de uso del *client* con *model*, *instructions* e *input*.
    response = client.responses.create(
        model="gpt-4",
        instructions="eres un agente que lee en contexto y responde brevemente",
        input=prompt
    )

    # Puede devolver un *stream* o quizás no haya respuesta; maneja ambos casos.
    return response or None

**¿Cómo integrarlo en el flujo principal?**
Importa la función en el archivo principal.
Pasa la lista de artículos y la query.
Imprime la respuesta.
from OpenAI import analyze_news_withIA

articulos = [...]  # Lista de artículos ya obtenidos.
pregunta = "¿Qué piensas de Python?"

respuesta = analyze_news_withIA(articulos, pregunta)
print(respuesta)

**¿Cómo verificar el contexto enviado?**
Imprime el prompt para auditar qué recibe la IA.
Observa la salida. Ejemplo de respuesta: “Python es un lenguaje versátil y popular…”.
# Dentro de analyze_news_withIA, temporalmente:
print(prompt)  # Útil para depurar qué se está enviando a la IA.
Habilidades y conceptos que practicas: lenguaje natural, API de OpenAI, .env, python-dotenv, variables de entorno, os.environ.get, lista por comprensión, control de costos en LLM, prompt conciso, impresión y pruebas en terminal, integración en main, manejo de posibles None o stream, y mención del modelo GPT-4 que requiere saldo. Próximos pasos sugeridos: programación orientada a objetos y publicación en un repositorio de GitHub aplicando buenas prácticas.

**Cuestionario**


