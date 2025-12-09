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


¿Qué son los f-strings en Python y por qué usarlos?
Los f-strings se crean anteponiendo una letra f al inicio de las comillas. Con eso, puedes colocar expresiones dentro de llaves y Python las evalúa al imprimir. Según se comenta, fueron agregados desde Python 3.6 y funcionan en versiones actuales como 3.13, con mejoras de rendimiento y legibilidad frente a .format.

Mejor legibilidad: ves variables y lógica en el lugar donde se imprimen.
Mejor rendimiento: el formateo es más rápido en versiones modernas de Python.
Sintaxis directa: basta con escribir f"... {expresión} ...".
¿Cómo verificar la versión de Python?
Confirma que Python sea 3.6 o superior. El ejemplo menciona 3.13 como versión instalada, por lo que es compatible con f-strings.

¿Qué ventaja tienen sobre format?
Con .format las variables quedan lejos del texto, lo que dificulta leer qué se inserta. Con f-strings, la interpolación es inmediata y el código se entiende de un vistazo.

Ejemplo equivalente con .format que resulta menos claro:

nombre = "Ana"
texto = "Hola, {}".format(nombre)
print(texto)
¿Qué precaución con el editor?
Si antepones la f pero no usas llaves, algunos editores o linters como “Ruf” podrían eliminar la f automáticamente por no aportar nada. Asegúrate de incluir al menos una expresión entre llaves.

¿Cómo insertar variables, operaciones y funciones dentro de f-strings?
Dentro de las llaves puedes colocar variables, operaciones matemáticas y llamadas a métodos o funciones. Esto reduce errores y concentra la lógica donde se muestra el texto.

¿Cómo interpolar variables?
nombre = "Ana"
saludo = f"Hola, {nombre}"
print(saludo)
Interpola el valor de una variable entre llaves.
Mantiene el texto y los datos juntos.
¿Cómo ejecutar operaciones y cálculos?
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
¿Cómo llamar métodos y funciones?
Puedes invocar métodos de cadenas como .upper directamente en el f-string.

nombre = "Ana"
texto = f"Hola, {nombre.upper()}"
print(texto)  # Hola, ANA
También puedes llamar funciones propias si lo necesitas.
El editor puede autocompletar porque estás escribiendo código Python normal dentro de las llaves.
¿Cómo usar condicionales y otros recursos dentro de f-strings?
Los f-strings aceptan expresiones, incluyendo condicionales tipo if/else en línea. Además, permiten acceder a estructuras como diccionarios y, de forma avanzada, aplicar formateadores con el operador dos puntos.

¿Cómo escribir condicionales inline?
nombre = "Ana"
edad = 20
msg = f"Hola, {nombre}, eres {'mayor de edad' if edad >= 18 else 'menor de edad'}"
print(msg)
Útil para pluralizar o ajustar textos según cantidades.
Mantiene la lógica condicional cercana al mensaje.
¿Dónde aplicar plural o singular?
Cuando generas textos con conteos.
Para diferenciar “mayor”/“menor”, “elemento”/“elementos”, según el número.
Validando la cantidad directamente en las llaves.
Ejemplo de patrón:

cantidad = 1
info = f"Tienes {cantidad} {'elemento' if cantidad == 1 else 'elementos'}"
print(info)
¿Qué más puedes integrar?
Acceso a diccionarios para mostrar valores.
datos = {"ciudad": "Lima"}
texto = f"Vives en {datos['ciudad']}"
print(texto)



## CLASE 06:  Argumentos dinámicos *args en funciones Python
¿Cómo dar formato a números con FStrings?
Los modificadores de formato se aplican tras los dos puntos. Esto permite generar salidas más legibles para personas, como separar miles con coma, limitar decimales con redondeo y rellenar con ceros a la izquierda.

¿Cómo aplicar separador de miles?
Usa la coma para miles: más legible para valores grandes.
Inserta el modificador tras el valor: dos puntos y coma.


bank_balance = 1234567890
texto = f"Tu saldo en la cuenta bancaria es {bank_balance:,}."
print(texto)
# Tu saldo en la cuenta bancaria es 1,234,567,890.


¿Cómo controlar decimales y redondeo?
Limita decimales con f: redondea automáticamente.
Cambia la precisión: .1f, .2f, etc.
stock_price = 1.405
texto = f"El valor del stock es {stock_price:.1f}."
print(texto)
# El valor del stock es 1.4.

texto2 = f"El valor del stock es {stock_price:.2f}."
print(texto2)
# El valor del stock es 1.41.

¿Cómo agregar ceros a la izquierda?
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

¿Cómo alinear texto y crear tablas legibles?
Los FStrings permiten alinear valores con un ancho fijo, ideal para tablas simples con pipeline y sumarios más claros. Puedes alinear a la izquierda o a la derecha cambiando el indicador de alineación.

¿Cómo alinear columnas con anchura fija?
Especifica ancho tras los dos puntos: 15, 10, etc.
Alinea texto a la izquierda o números a la derecha para facilitar lectura.

product = "laptop"
price = 1000
print(f"producto | precio")
print(f"{product:<15} | {price:>10,}")
# producto       |      1,000


¿Cómo concatenar filas con un salto de línea?
Usa el backslash n para un retorno de línea: \n.
Duplica líneas con el mismo formato para simular una tabla.
product = "laptop"
price = 1000
linea = f"{product:<15} | {price:>10,}"
tabla = f"producto         | precio\n{linea}\n{linea}"
print(tabla)
¿Cómo formatear fechas y mejorar el debugging?
Una fecha en su forma por defecto sale en formato ISO. Con modificadores, puedes mostrar día, número, mes, año y hora en una versión más legible. Además, los FStrings permiten imprimir variables y mensajes para encontrar errores más rápido.

¿Cómo mostrar una fecha completa legible?
Crea la fecha con datetime: año, mes, día y hora.
Aplica códigos de formato para nombre del día, día, mes, año y hora.
from datetime import datetime
fecha = datetime(2024, 12, 5, 10, 10)
print(f"La fecha completa es {fecha}.")  # formato ISO por defecto

formato = f"La fecha completa es {fecha:%A, %d de %B del %Y a las %I y %M %p}."
print(formato)
# La fecha completa es jueves, 05 de diciembre del 2024 a las 10 y 10 A.M.
¿Cómo usar FStrings para debugging rápido?
Inserta variables directamente en el mensaje: más contexto.
Combina texto y valores calculados en una sola línea.
Útil para verificar estados y entradas del usuario.
user = "ana"
items = ["A", "B", "C"]
print(f"debug: usuario={user}, total_items={len(items)}, items={items}")

## CLASE 07:  Argumentos dinámicos *args en funciones Python

¿Qué son los argumentos dinámicos args en Python?
Los argumentos dinámicos permiten recibir un número variable de parámetros posicionales. En Python se definen con un asterisco y el nombre convencional args. Internamente, args es una tupla: inmutable, ordenada y accesible por índice.

Se definen con un asterisco antes del nombre del parámetro.
Se almacenan como tupla inmutable.
El orden de los argumentos posicionales es crucial.


¿Cómo se usan args con ejemplos de código?
def ejemplo_args(*args):
    print(f"args: {args}")
    print(f"type: {type(args)}")

# Llamadas de ejemplo
Ejemplo = ejemplo_args
Ejemplo(1, 2, 3)
Ejemplo("Hola", "mundo")
Ejemplo()  # sin parámetros


## CLASE 08: Uso de kwargs para crear un cliente de APIs flexible

¿Qué son keywords y por qué combinarlos con args?
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
¿Cómo implementar kwargs en una función flexible?
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
¿Cómo funcionan los diccionarios y el doble asterisco?
Desempaquetado con :** copiar pares key-value dentro de otro diccionario.
Mezcla de configuraciones: {**base_config, **keywords} agrega y sobrescribe de forma limpia.
Invocación con :** client(*args, **config) pasa parámetros de forma explícita.
¿Qué orden de parámetros es correcto en Python?
Obligatorios primero: por ejemplo, api_name al inicio.
Luego args: parámetros posicionales variables.
Al final kwargs:** parámetros nombrados y dinámicos.
¿Cómo se selecciona el cliente por nombre?
Mapa de clientes: un diccionario api_clients con el nombre como clave.
Búsqueda directa: client = api_clients[api_name] elige el ejecutor correcto.
Una sola función: orquesta múltiples fuentes como News API y Guardian.
¿Cómo usarlo con News API y Guardian?
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

¿Cómo obtener y proteger tu API key de News API?
Obtener la API key es el primer paso. Se solicita en newsapi.org completando un formulario y pulsando submit. Cópiala y úsala por ahora como constante en el código.

No hacerla pública ni subirla al repositorio.
Tratarla como una llave de acceso.
Guardarla temporalmente como constante para fines educativos.
La documentación oficial (Get Started, Searching for news articles) indica la URL base y que la API key se pasa como parámetro. Esa guía define el formato correcto del request.

¿Cómo construir la URL y el query string en Python?
La recomendación es evitar concatenar cadenas a mano. Usa las herramientas de Python: urllib.parse.urlencode para formatear parámetros y urllib.request para abrir la URL con un timeout controlado. Así la URL final es válida y el servidor entiende el GET.

Usar urllib.parse para generar el query string.
Añadir parámetros como la q de búsqueda y la apiKey.
Construir la URL final uniendo base y parámetros.
¿Qué hace urllib.parse.urlencode?
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

    
¿Cómo enviar el request con urllib.request y with?
Con el administrador de contexto with se maneja el response y se lee el contenido con seguridad. El timeout evita esperas indefinidas.

Abrir la URL con request.urlopen y pasar timeout.
Leer los bytes con .read().
Mantener el código claro y cercano a la función de fetch.
¿Cómo decodificar la respuesta y procesar artículos en json?
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

¿Qué problema resuelve try/except en Python?
Cuando conviertes o recibes datos, algo puede fallar: un servidor puede estar caído o la entrada del usuario puede ser inválida. Con try/except, Python permite interceptar estas situaciones y definir una acción segura: mostrar un mensaje, asignar un valor por defecto o frenar la ejecución si estás dentro de una función.

Un ejemplo base: pedir dos números y dividirlos. Si el usuario digita cero para el divisor, ocurre un ZeroDivisionError; si escribe texto, aparece ValueError. Con manejo de excepciones, puedes informar al usuario de forma clara y continuar el flujo del programa cuando tiene sentido.

# try_except.py
# Entrada del usuario y división
A = int(input("Digita un número: "))
B = int(input("Digita otro número: "))
resultado = A / B
print(resultado)
¿Cómo implementar try y except paso a paso?
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

¿Cómo capturar ZeroDivisionError sin ocultar otros errores?
Sé específico cuando conoces el problema esperado: dividir entre cero. Así evitas atrapar errores no relacionados.

try:
    A = int(input("Digita un número: "))
    B = int(input("Digita otro número: "))
    resultado = A / B
    print(resultado)
except ZeroDivisionError:
    print("No está permitido dividir por cero.")
¿Cómo validar entradas y capturar ValueError?
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

¿Qué es finally y cuándo se ejecuta en Python?
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

¿Cómo funciona raise para detener la ejecución?
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
¿Por qué crear una excepción específica y no usar Exception?
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

¿Qué hace cada cláusula en el flujo de errores?
try: bloque con código que podría fallar.
raise: detiene la ejecución y lanza un tipo de error específico.
except: captura un tipo de error concreto o todos si usas Exception.
finally: se ejecuta siempre, ocurra o no un error.
¿Cómo capturar y mostrar mensajes claros?
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

¿Cómo definir una jerarquía de excepciones para la app?
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
¿Dónde y cómo manejar el error en el consumo?
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