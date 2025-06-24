## Curso de Flask
> Crea aplicaciones web completas con Flask: rutas, vistas, formularios, bases de datos con SQLAlchemy, autenticación, plantillas con Jinja, pruebas unitarias y mejoras visuales con TailwindCSS.

- Profesor: Luis Martínez
- Fecha Inicio: 28/Mayo/2025  
- Fecha Fin: 19/Junio/2025
- Guia : https://github.com/platzi/curso-flask/ 
- Curso Viejo -> https://platzi.com/clases/old/flask-19/ -> flask viejo curso 

## Clase 01: Creación de una Aplicación de Notas con Flask y Tailwind
> Flask es un micro framework de Python que ofrece una base sólida para construir aplicaciones web con flexibilidad y control. Su diseño minimalista permite agregar extensiones según las necesidades específicas del proyecto, convirtiéndolo en una herramienta poderosa para desarrolladores que buscan personalización y eficiencia en sus aplicaciones.

## ¿Qué es Flask y por qué utilizarlo?
Imagina que construir una aplicación web es como construir una casa. Tienes todos los elementos y, al unirlos, vas construyendo muros, techos y suelos. Eso es Flask en esencia: una base sólida sobre la cual puedes agregar componentes según tus necesidades específicas.

Flask es un micro framework de Python que te permite tener control total sobre tu aplicación web. A diferencia de otros frameworks más robustos, Flask no impone una estructura rígida, sino que te da la libertad de diseñar tu aplicación como mejor te parezca.

## Las principales ventajas de Flask incluyen:

- Configuración minimalista que facilita comenzar proyectos rápidamente
- Comunidad extensa que ha desarrollado numerosas extensiones reutilizables
- Curva de aprendizaje accesible especialmente si ya conoces Python
- Herramientas de desarrollo integradas como un servidor web y una shell para ejecutar código Python en el contexto de la aplicación

## ¿Qué empresas utilizan Flask en producción?
Flask no es solo para pequeños proyectos o desarrolladores independientes. Grandes empresas confían en este framework para sus aplicaciones:

- Netflix utiliza Flask para crear herramientas internas que apoyan sus procesos de desarrollo
- Spotify implementa características importantes de su aplicación de streaming musical con Flask
- Estas empresas de clase mundial han elegido Flask por su flexibilidad, rendimiento y capacidad de adaptación a necesidades específicas.

## ¿Cómo extender Flask según tus necesidades?
Una de las características más poderosas de Flask es su capacidad de extensión. Puedes agregar funcionalidades específicas según lo requiera tu proyecto:

## Extensiones para manejar sesiones de usuario
- Componentes para gestionar consultas e inserciones en bases de datos
- Herramientas para autenticación y autorización
- Módulos para procesamiento de formularios
- Esta modularidad te permite mantener tu aplicación ligera, incluyendo solo lo que realmente necesitas, sin el peso de componentes innecesarios que podrían ralentizar tu aplicación.


## Notas Mentales 
- Es un Microfram,ework luego para agregar base solidas deacuerdo  a las peticiones del usuario 
- Configurtacion rapida
- Curva de aprendizaje muy facil 
- Set de herramientas
- Comunidad activa
- Usar shell o servidor web 
- https://platzi.com/clases/old/flask-19/ -> flask viejo curso 

## Clase 2: Creación de una Aplicación de Notas con Flask Paso a Paso
> 
## ¿Cómo configurar un entorno de desarrollo para Flask?
Antes de comenzar a programar con Flask, es fundamental establecer un entorno de desarrollo adecuado. El uso de entornos virtuales es una práctica recomendada que nos permite aislar las dependencias de cada proyecto y evitar conflictos entre versiones de paquetes.

## Pasos: 

- Paso 1: Para crear nuestro entorno de trabajo, seguiremos estos pasos:
    Crear una carpeta para nuestro proyecto:

```bash
mkdir notes-app
cd notes-app
```

- Paso 2: Generar un entorno virtual dentro de esta carpeta:
```bash
python -m venv venv
```
- Paso 3: Activar el entorno virtual:

En sistemas Unix/Linux/MacOS:

```bash
source venv/bin/activate
```

En sistemas Windows (el comando específico estará disponible en los recursos adicionales)

- Paso 4: Instalar Flask usando pip:
```bash
pip install Flask
```

- Paso 5: Verificar la instalación:
```bash
flask --help
```

## ¿Cómo ejecutar nuestra aplicación Flask?
Existen dos formas principales de ejecutar una aplicación Flask:

Usando Python directamente:

python app.py

Usando el comando Flask (recomendado):

flask run

## comando 
- flask run --help
- flask run --debug # activa el debugin 

## Notas Mentales 
- igual o parecido que node.js usamos un archivo principal para este caso es app.py tiene elementos que se van configurando pero es el archivo de arranque dejo ejemplo 

```Python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True) # Esto es importante ya que no hay qiue recargar el servidor 

```


## Clase 3: Manejo de Decoradores y Métodos HTTP en Flask
> El decorador @route en Flask es una herramienta poderosa que permite definir cómo nuestras aplicaciones web responden a diferentes tipos de solicitudes HTTP. Dominar este decorador es fundamental para crear APIs robustas y aplicaciones web interactivas que puedan procesar diversos tipos de peticiones de los usuarios. En este artículo, exploraremos cómo extender nuestro uso del decorador @route para manejar diferentes métodos HTTP y retornar varios tipos de datos.

```Python

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"


@app.route('/acerca-de') #Url
def about():
    return "Hello"

@app.route("/contacto", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente", 201
    return "Pagina de contacto"


@app.route("/api/info")
def api_info():
    data = {
        "nombre": "Notes App",
        "version": "1.1.1"
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True) # Esto es importante ya que no hay qiue recargar el servidor 

```


## Clase 4: Uso de Jinja para Plantillas HTML Dinámicas en Flask
> La integración de Jinja en Flask revoluciona la forma en que creamos aplicaciones web dinámicas, permitiéndonos incorporar lógica de programación directamente en nuestros archivos HTML. Esta potente combinación nos brinda la flexibilidad necesaria para desarrollar interfaces de usuario interactivas y personalizadas sin sacrificar la estructura y semántica del HTML. Descubramos cómo Jinja transforma el desarrollo web con Flask y cómo podemos aprovechar sus capacidades para crear aplicaciones más robustas y dinámicas.

## ¿Qué es Jinja y por qué es importante en Flask?
Jinja es un motor de plantillas para Python que permite incorporar variables, condicionales, bucles y otras estructuras de programación directamente en archivos HTML. A diferencia del HTML estático, Jinja nos permite crear contenido dinámico que se genera en tiempo de ejecución.

## Características principales de Jinja:

- Uso de variables dentro del HTML
- Estructuras condicionales (if-else)
- Bucles (for)
- Herencia de plantillas
- Filtros para manipular datos

```Python

## App.py 
@app.route('/notas')
def home():
    notes = [
        {"title": "Nota uno", "description": "Descripción de la nota uno", "created_at": "2023-01-01"},
        {"title": "Nota dos", "description": "Descripción de la nota dos", "created_at": "2023-01-02"},
        {"title": "Nota tres", "description": "Descripción de la nota tres", "created_at": "2023-01-03"}
    ]
    return render_template('home.html', notes=notes)

## templates/home.html

<ul>
    {% for note in notes %}
        <li>
            <h3>{{ note.title }}</h3>
            <p>{{ note.description }}</p>
            <small>Creado el: {{ note.created_at }}</small>
        </li>
    {% endfor %}
</ul>

```

## Clase 5: Creación y Manejo de Formularios en Aplicaciones Web
> Los formularios son una parte esencial en el desarrollo web, ya que permiten la comunicación entre usuarios y servidores. Dominar el manejo de formularios en Flask te permitirá crear aplicaciones web interactivas y funcionales que respondan a las necesidades de tus usuarios. En este contenido, exploraremos cómo implementar formularios en Flask, procesar la información enviada y realizar redirecciones efectivas entre diferentes vistas.

## notas mentales 
- Para hacer el algoritmo nos apoyamos de los siguientes aditamentos: 
    - render_template => genera la plantilla y puede recibir valores
    - request => es el pedido que viene de get o post 
    - redirect => nos permite redirecciona con ayuda de url_for claro previamente tiene que exisir confirmation como route 
    - url_for => realiza match con la url que este establecida en algun router


```Python

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route("/confirmacion", methods=["GET", "POST"])
def confirmation():
    print(request)
    valor:str = request.args.get("note", "No encontrada") ## Forma de leer desde la url 
    data = {
        "status":"OKI",
        "valor": valor
    }
    return jsonify(data), 200

@app.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        note = request.form.get("note", "No encontrada") # Forma de capturas datos post
        return redirect(url_for("confirmation", note=note)) ## Forma de redireccionar 
    return render_template("note_form.html")# renderizar plantilla

if __name__ == '__main__':
    app.run(debug=True) # Esto es importante ya que no hay qiue recargar el servidor 

```

## Clase 6: Integración de SQLAlchemy en Flask para Bases de Datos
> La integración de bases de datos en aplicaciones Flask representa un paso fundamental para desarrollar soluciones web robustas y escalables. 

## Pasos 
- Paso 1: Debemos instalar sqlalchemy, recuerda esto nos permite crear motor y secciones de base de datos ademas de interactuar usando el ORM ´pip install flask-sqlalchemy´

- Paso 2: luego de instalar podemo usar el shell de flask ´flask shell´
    - podemos agregar a esa linea de comando lo siguiente -> from flask_sqlalchemy import SQLAlchemy si no menciona un error nos indica que se instalo de manera correcta 

- Paso 3: Para configurar nuestra base de datos SQLite, necesitamos modificar nuestro archivo principal de la aplicación (app.py):

```Python

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la ruta del archivo de base de datos
db_filepath = os.path.join(os.path.dirname(__file__), 'notes.sqlite')

# Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_filepath}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instancia de SQLAlchemy
db = SQLAlchemy(app)

```
1. Importamos la librería os para manejar rutas de archivos
2. Definimos la ruta donde se creará el archivo SQLite
3. Configuramos la URI de la base de datos con el formato requerido por SQLAlchemy
4. Desactivamos el seguimiento de modificaciones para reducir la verbosidad de los logs
5. Creamos una instancia de SQLAlchemy vinculada a nuestra aplicación


## ¿Cómo crear modelos y tablas con SQLAlchemy?
Los modelos en SQLAlchemy son clases de Python que representan tablas en la base de datos. Cada atributo de la clase corresponde a una columna en la tabla.

Para nuestro ejemplo, crearemos un modelo Note para almacenar notas con título y contenido:


```Python
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'Note {self.id}: {self.title}'
```

## Creación de las tablas en la base de datos
Una vez definido el modelo, necesitamos crear las tablas correspondientes en la base de datos. Para esto, utilizamos el método create_all() de SQLAlchemy:
```bash
flask shell -> 1
from app import db -> 2
db.create_all()   -> 3
```

## Validar en SQLite3
- Para validar en sqlite podemos ejecutar el siguiente comando 
- sqlite3 notes.sqlite => nos abre un entorno para ejecuctar comando sql para tener nuestra data 
- .schema

## Clase 7: Creación y Gestión de Notas con SQLAlchemy y Vistas en Python
> La gestión de datos en aplicaciones web es un componente fundamental para crear experiencias interactivas y funcionales. En este artículo, exploraremos cómo implementar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una aplicación Flask utilizando SQLAlchemy, centrándonos específicamente en la creación y visualización de notas. Dominar estas técnicas te permitirá desarrollar aplicaciones web robustas con persistencia de datos, una habilidad esencial para cualquier desarrollador web moderno.

```Python

```


## Clase 8: Edición de Contenidos en Bases de Datos con Formularios
> La edición de contenidos en bases de datos es una funcionalidad esencial en cualquier aplicación web moderna. Aprender a implementar formularios de edición en Flask nos permite crear aplicaciones más completas y funcionales, donde los usuarios pueden modificar la información previamente almacenada. Este proceso, aunque parece complejo, se simplifica enormemente cuando entendemos los conceptos fundamentales de rutas dinámicas, manipulación de modelos y redirecciones.

## ¿Cómo crear un formulario para editar contenido en Flask?
Para implementar la funcionalidad de edición en nuestra aplicación Flask, necesitamos crear un nuevo formulario que nos permita modificar una nota existente en la base de datos. Este proceso implica varios pasos importantes:

Crear una nueva ruta que acepte el ID de la nota como parámetro.
Recuperar la información existente de la base de datos.
Mostrar esa información en un formulario para su edición.
Procesar los cambios y actualizarlos en la base de datos.

## Router y proceso update
```Python

@app.route('/editar-nota/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id) ## Realiza la consulta en la tabla 
    
    if request.method == 'POST':## Valido que sea un post aqui update 
        title = request.form.get('title')
        content = request.form.get('content')
        
        note.title = title
        note.content = content
        
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit_note.html', note=note) ## en caso de get mostramos el formulario con el valor note 

```

## Formulario  
```html

<form method="post">
    <div>
        <label for="title">Título</label>
        <input type="text" name="title" value="{{ note.title }}">
    </div>
    <div>
        <label for="content">Contenido</label>
        <textarea name="content">{{ note.content }}</textarea>
    </div>
    <button type="submit">Guardar nota</button>
</form>

```

## Formulario  Home boton editar
```python

{% for note in notes %}
    <div>
        <h3>{{ note.title }}</h3>
        <p>{{ note.content }}</p>
        <a href="{{ url_for('edit_note', id=note.id) }}">✏️ Editar</a>
    </div>
{% endfor %}

```

## Clase 9: Eliminar notas en una aplicación web usando SQLAlchemy
> para eliminar usamos db.session.delete(note)

## Router y proceso delete
```Python

@app.route('/delete-note/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.query.get(id)
    
    if not note:
        # Si la nota no existe, no tiene sentido intentar borrarla
        return redirect(url_for('home'))
    
    db.session.delete(note)
    db.session.commit()
    
    return redirect(url_for('home'))
```

## Formulario  
```html

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Página de Inicio</title>
</head>

<body>
    <h1>Bienvenido a Flask Notes</h1>
    <ul>
        {% for note in notes %}
        <li>
            <div>
                <h3>{{ note.title }}</h3>
                <p>{{ note.content }}</p>
                <a href="{{ url_for('edit_note', id=note.id) }}">✏️ Editar</a>
                <form method="post" action="/delete-note/{{ note.id }}">
                    <button type="submit">Eliminar</button>
                </form>
            </div>
        </li>
        {% else %}
        Aun no se han creado notas
        {% endfor %}
    </ul>

    <a href="{{ url_for('create_note') }}">agregar una nueva nota</a>
</body>

</html>

```

## Clase 10: Refactorización y Organización de Proyectos en Flask
>a refactorización de código es una práctica esencial para cualquier desarrollador que busque mantener sus proyectos escalables y fáciles de mantener. Cuando trabajamos con frameworks como Flask, organizar adecuadamente nuestro código no solo mejora la legibilidad, sino que también facilita el trabajo en equipo y la implementación de pruebas unitarias. En este artículo, exploraremos cómo transformar una aplicación Flask básica en una estructura más profesional y mantenible.




```Python

```


## Clase 11: Refactorización de Rutas y Blueprints en Flask
> 

**¿Cómo preparar nuestro repositorio para un desarrollo profesional?**
Antes de comenzar a refactorizar nuestro código, es importante asegurarnos de que nuestro repositorio esté correctamente configurado. Uno de los primeros pasos es crear un archivo .gitignore para evitar subir archivos innecesarios al repositorio. 


**¿Qué son los blueprints en Flask y por qué son importantes?**
Los blueprints en Flask son una forma de organizar aplicaciones a gran escala, permitiéndonos agrupar endpoints o URLs de acuerdo a su dominio o funcionalidad. Esta modularización facilita enormemente el mantenimiento del código y permite una mejor separación de responsabilidades dentro de nuestra aplicación.

Cuando trabajamos con aplicaciones Flask que crecen en complejidad, mantener todas las rutas en un solo archivo se vuelve inmanejable. Los blueprints nos permiten:

Organizar el código en módulos lógicos.
Reutilizar componentes en diferentes partes de la aplicación.
Facilitar la migración de funcionalidades a nuevas aplicaciones.
Mejorar la colaboración en equipos de desarrollo.

```Python

```

## Clase 12: Implementación de Flash Messages en Aplicaciones Web con Flask
> ¿Qué son los Flash Messages y por qué son importantes?
Los Flash Messages son mensajes temporales que se muestran al usuario después de realizar una acción específica. Estos mensajes viajan entre solicitudes (requests) a través de sesiones, permitiendo mostrar información relevante sobre acciones completadas o errores ocurridos.

Características principales:

Persisten entre solicitudes para el mismo usuario
Se almacenan en cookies encriptadas
Desaparecen después de ser mostrados una vez
Pueden categorizarse (éxito, error, advertencia)
La importancia de estos mensajes radica en que proporcionan retroalimentación inmediata al usuario, mejorando la usabilidad de la aplicación y reduciendo la confusión sobre si una acción se completó correctamente.

¿Cómo implementar Flash Messages en una aplicación Flask?
La implementación de mensajes flash en Flask es relativamente sencilla gracias a que esta funcionalidad viene integrada en el framework. Veamos paso a paso cómo hacerlo:

Configuración inicial
Primero, necesitamos configurar una clave secreta para encriptar las cookies que transportarán nuestros mensajes:

# Configuración de la clave secreta para encriptar cookies
app.secret_key = "cualquier_valor_secreto"
Esta clave es fundamental para la seguridad, ya que sin ella Flask no podrá manejar la información de sesión de forma segura.

Importación y uso de Flash
Para utilizar los mensajes flash, necesitamos importar la función correspondiente:

from flask import flash
Luego, podemos crear mensajes flash en cualquier punto de nuestro código, especialmente después de acciones importantes:

# Después de crear una nota exitosamente
flash("Nota creada", "success")
El primer parámetro es el mensaje que queremos mostrar, y el segundo es la categoría. Las categorías son útiles para aplicar diferentes estilos según el tipo de mensaje (éxito, error, advertencia).

Mostrando los mensajes en la plantilla
Para mostrar los mensajes en nuestra plantilla HTML, utilizamos la función get_flashed_messages() de Jinja2:



```Python
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
            {% for category, message in messages %}
                <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
```


## Clase 13: Plantillas Jinja en Flask: Reutilización de Código HTML
> ¿Qué es Jinja y cómo mejora nuestro desarrollo frontend?
Jinja es el manejador de plantillas integrado en Flask que ofrece grandes ventajas para el desarrollo frontend. Su principal beneficio es evitar la duplicación de código HTML, permitiéndonos mantener nuestro código organizado en diferentes archivos y reutilizarlo según sea necesario.

Para trabajar con Jinja de manera más eficiente, podemos instalar la extensión "Better Jinja" en nuestro editor de código, lo que facilita la escritura y el autocompletado de código Jinja.

Creando una plantilla base con Jinja
El primer paso para implementar Jinja en nuestra aplicación es crear una plantilla base que contendrá la estructura común a todas nuestras páginas:

Creamos un archivo llamado base.html en la carpeta templates
Definimos la estructura básica de HTML5
Agregamos bloques que serán redefinidos en las plantillas hijas
<!-- Seleccionamos Jinja HTML como lenguaje -->
{% block app_notas %}{% endblock %}

<body style="background-color: aqua;">
    {% block content %}{% endblock %}
</body>
Los bloques ({% block nombre %}{% endblock %}) son áreas que pueden ser sobrescritas por las plantillas que extiendan de esta base.

Extendiendo la plantilla base
Para utilizar nuestra plantilla base en otras vistas, usamos la directiva {% extends %}:

{% extends "base.html" %}

{% block content %}
<div>
    Lorem ipsum dolor sit amet...
</div>
{% endblock %}
Es importante entender que solo el contenido dentro de los bloques definidos será visible en la página final. Todo el contenido que no esté dentro de un bloque redefinido será ignorado.

¿Cómo implementar elementos comunes en todas las páginas?
Una de las ventajas de usar plantillas base es la capacidad de definir elementos que aparecerán en todas las páginas de nuestra aplicación, como barras de navegación, pies de página o sistemas de mensajes.

Sistema de mensajes flash
Para implementar un sistema de mensajes que aparezca en todas las páginas, podemos colocar el código correspondiente en la plantilla base:
```Python
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}

{% block content %}{% endblock %}
```

De esta manera, los mensajes flash se mostrarán en cualquier página que extienda de nuestra plantilla base.

Mejorando la apariencia con Tailwind CSS
Para mejorar la apariencia de nuestra aplicación, podemos utilizar frameworks CSS como Tailwind. En nuestra plantilla base mejorada, incluimos:

La integración de Tailwind CSS mediante un script
Fuentes personalizadas desde Google Fonts
Una barra de navegación (navbar)
Un sistema de mensajes con colores según la categoría (success, error, warning)
Un contenedor principal con márgenes y padding adecuados
Un pie de página


Procedimiento para usar Flask Migrate:

1. Ejecuta:

pip install Flask-Migrate

2. En app.py añadir:

from flask_migrate import Migrate

migrate = Migrate(app, db) # <--- Añade esta línea

3. Ejecuta:

flask db init (Inicializa una vez por proyecto)

4. Agrega el campos al modelo

created_at = db.Column(db.DateTime, default=db.func.now(), nullable=True) # tiene que aceptar nulo pq existen registros

5. Ejecuta el comando:

flask db migrate -m "Add created_at column to Note"

6. Ejecuta:

flask db upgrade


## Clase 14: Sistema Básico de Autenticación con Sesiones en Flask
> ¿Cómo funcionan las sesiones en Flask?
Las sesiones en Flask nos permiten almacenar información específica del usuario en cookies del navegador. Esto es particularmente útil cuando necesitamos mantener el estado de autenticación de un usuario mientras navega por nuestra aplicación.

Las sesiones funcionan de la siguiente manera:

Almacenan datos en cookies del navegador del cliente
La información se encripta utilizando una clave secreta
Permiten acceder a los datos del usuario en diferentes rutas de la aplicación
Mantienen la persistencia de la información entre solicitudes HTTP
Es importante destacar que Flask implementa un mecanismo de seguridad mediante la secret_key, que encripta la información almacenada en las cookies. Esto previene que, si alguien intercepta estas cookies, no pueda utilizarlas en otro navegador para suplantar la identidad del usuario original.

¿Por qué es importante la secret_key?
La secret_key es un componente crítico en la seguridad de las sesiones de Flask. Esta clave se utiliza para:

Encriptar la información almacenada en las cookies
Prevenir ataques de suplantación de identidad
Asegurar que las cookies solo funcionen en el navegador del usuario legítimo
Proteger datos sensibles que se comparten entre el cliente y el servidor
Sin una secret_key adecuada, cualquier persona con acceso a las cookies podría manipular la información y potencialmente acceder a recursos protegidos de la aplicación.

Implementando un sistema de autenticación básico
Para implementar nuestro sistema de autenticación, crearemos un nuevo Blueprint en Flask que manejará las rutas de login y logout. Este enfoque nos permite organizar mejor nuestro código y separar la lógica de autenticación del resto de la aplicación.

Creación del Blueprint de autenticación
Primero, debemos crear una nueva carpeta para nuestro Blueprint:

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
Luego, definimos la ruta de login que aceptará tanto solicitudes GET (para mostrar el formulario) como POST (para procesar la información del usuario):

from flask import Blueprint, request, render_template, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        
        if username == 'admin':
            session['user'] = username
            return redirect(url_for('notes.home'))
        else:
            flash('Usuario no permitido', 'error')
    
    return render_template('login.html')
En este código:

Verificamos si la solicitud es POST (envío del formulario)
Obtenemos el nombre de usuario del formulario
Validamos si el usuario es válido (en este caso, solo 'admin')
Si es válido, almacenamos el nombre de usuario en la sesión
Redirigimos al usuario a la página principal de notas
Si no es válido, mostramos un mensaje de error

```Python

```

## Clase 15: Implementación de Login y Logout con Validación de Sesiones
> ¿Cómo proteger rutas con autenticación en Flask?
Después de implementar un sistema de login básico, el siguiente paso lógico es proteger ciertas rutas para que solo sean accesibles por usuarios autenticados. En nuestro caso, queremos asegurarnos de que solo los usuarios que han iniciado sesión puedan ver el listado de notas.

Para lograr esto, necesitamos verificar si existe un usuario en la sesión actual. Si el usuario está presente, permitimos el acceso a la vista de notas; de lo contrario, redirigimos al usuario a la página de login con un mensaje informativo.

```Python
from flask import session, flash, redirect, url_for

@app.route('/notes')
def notes():
    if 'usuario' in session:
        # El usuario está autenticado, mostrar las notas
        return render_template('notes.html')
    else:
        # El usuario no está autenticado, redirigir al login
        flash('Para poder ver las notas debes iniciar sesión', 'error')
        return redirect(url_for('auth.login'))
```

¿Cómo implementar la funcionalidad de logout?
El logout es una funcionalidad esencial en cualquier sistema de autenticación. Permite a los usuarios cerrar su sesión de forma segura cuando terminan de usar la aplicación. En Flask, podemos implementar esta funcionalidad de manera sencilla utilizando el método pop() del objeto de sesión.

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Se ha deslogueado correctamente')
    return redirect(url_for('auth.login'))

¿Qué extensiones de Flask puedo usar para mejorar la seguridad?
Flask cuenta con varias extensiones que facilitan la implementación de sistemas de autenticación robustos:

Flask-Login: Maneja sesiones de usuario, incluyendo login, logout y recordar sesiones.
Flask-Security: Proporciona funcionalidades como registro de usuarios, confirmación de email, y restablecimiento de contraseñas.
Flask-User: Similar a Flask-Security pero con más opciones de personalización.
Flask-JWT-Extended: Para autenticación basada en tokens JWT, ideal para APIs.

## Clase 16: Validación de Formularios en Flask: Mensajes de Error y Reglas Básicas
> ¿Cómo validar información del lado del cliente en Flask?
Cuando desarrollamos aplicaciones web, es común que los usuarios ingresen información que puede no cumplir con nuestros criterios de validez. Por ejemplo, títulos demasiado cortos o contenidos sin suficiente información. La validación en el lado del servidor es esencial para garantizar que solo se procesen datos que cumplan con nuestros requisitos.

En Flask, podemos implementar validaciones manuales de manera relativamente sencilla. Estas validaciones se realizan antes de que los datos se guarden en la base de datos, lo que nos permite mostrar mensajes de error apropiados al usuario y evitar el procesamiento de información inválida.

Implementación de validaciones básicas en rutas de Flask
Para implementar validaciones básicas en nuestras rutas de Flask, podemos verificar las condiciones directamente en el código de la ruta. Veamos un ejemplo práctico:

```Python
@app.route('/notes/create', methods=['POST'])
def create_note():
    title = request.form['title']
    content = request.form['content']
    
    # Validación del título
    if len(title.strip()) > 10:
        # El título es válido, continuamos
        
        # Validación del contenido
        if len(content.strip()) > 300:
            # El contenido es válido, guardamos la nota
            # Código para guardar la nota en la base de datos
            flash('La nota fue creada correctamente', 'success')
            return redirect(url_for('notes'))
        else:
            flash('El contenido es muy corto, mínimo 300 caracteres', 'error')
    else:
        flash('El título es muy corto, mínimo 10 caracteres', 'error')
    
    # Si llegamos aquí, hubo un error de validación
    return render_template('create_note.html')
```


## Clase 17: Pruebas Unitarias en Flask: Creación y Configuración
¿Qué son las pruebas unitarias y por qué son importantes?
Las pruebas unitarias son una práctica esencial en el desarrollo de software que consiste en validar que cada componente individual de nuestro código funciona como esperamos. Esto es particularmente importante cuando nuestro código incluye lógica de negocio compleja.

Existen varios beneficios clave al implementar pruebas unitarias:

Validación constante: Nos permiten verificar que el código hace exactamente lo que esperamos.
Seguridad al realizar cambios: Podemos modificar nuestro código con la confianza de que no estamos rompiendo funcionalidades existentes.
Integración continua: Las pruebas pueden ejecutarse automáticamente en procesos de CI/CD (Integración Continua/Despliegue Continuo).
Documentación viva: Las pruebas sirven como documentación ejecutable de cómo debe comportarse nuestro código.
En Flask, tenemos herramientas específicas que nos facilitan la creación de pruebas para validar tanto nuestros modelos como nuestras vistas.

¿Cómo configurar un entorno de pruebas en Flask?
Para implementar pruebas unitarias en Flask, necesitamos configurar adecuadamente nuestro entorno. Esto implica varios pasos importantes:

Creación de una configuración específica para pruebas
Lo primero que debemos hacer es crear una configuración específica para nuestras pruebas:

class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_notes.db'
    SECRET_KEY = 'test_secret_key'
    TESTING = True
Esta configuración es similar a la de producción, pero con algunas diferencias clave:

Utilizamos una base de datos diferente (test_notes.db) para no afectar los datos de producción.
Establecemos TESTING = True para que Flask sepa que estamos en modo de prueba.
Podemos definir una clave secreta específica para pruebas.
Implementación del patrón Application Factory
Para poder cambiar la configuración durante las pruebas, necesitamos implementar el patrón Application Factory:

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Aquí va el resto de la configuración de la app
    # ...
    
    return app
Este patrón nos permite crear instancias de nuestra aplicación con diferentes configuraciones, lo que es esencial para las pruebas. En lugar de inicializar la aplicación directamente, creamos una función que la inicializa y la devuelve.

¿Cómo crear y ejecutar pruebas unitarias en Flask?
Una vez configurado nuestro entorno, podemos comenzar a escribir pruebas unitarias para nuestros modelos y vistas.

Creación de una clase de prueba
Creamos un archivo test_models.py con una clase que hereda de unittest.TestCase:

import unittest
from app import create_app
from config import TestConfig
from models import db, Note

class NoteModelTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
    
    def test_create_note(self):
        with self.app.app_context():
            note = Note(title="Título", content="Contenido")
            db.session.add(note)
            db.session.commit()
            
            saved_note = Note.query.first()
            
            self.assertEqual(saved_note.title, "Título")
            self.assertEqual(saved_note.content, "Contenido")
En este ejemplo:

El método setUp se ejecuta antes de cada prueba y configura el entorno necesario.
Creamos una instancia de nuestra aplicación con la configuración de prueba.
Inicializamos un cliente de prueba que nos permitirá simular solicitudes HTTP.
Creamos la estructura de la base de datos dentro del contexto de la aplicación.
En test_create_note, probamos que podemos crear una nota y que se guarda correctamente en la base de datos.
Uso del contexto de aplicación
Un aspecto crucial al trabajar con pruebas en Flask es el uso del contexto de aplicación. Muchas operaciones, como las interacciones con la base de datos, requieren este contexto:

with self.app.app_context():
    # Código que requiere el contexto de la aplicación
    db.create_all()
    # ...
Sin este contexto, recibiremos errores al intentar acceder a la base de datos u otros recursos de la aplicación.

Uso de assertions para validar resultados
Las assertions son el corazón de las pruebas unitarias. Nos permiten verificar que los resultados son los esperados:

self.assertEqual(saved_note.title, "Título")
Existen muchos tipos de assertions disponibles:

assertEqual: Verifica que dos valores son iguales
assertTrue/assertFalse: Verifica que un valor es verdadero o falso
assertIn: Verifica que un elemento está en una colección
assertRaises: Verifica que se lanza una excepción específica
Ejecución de las pruebas
Para ejecutar nuestras pruebas, utilizamos el módulo unittest de Python:

python -m unittest test_models.py
Si la prueba es exitosa, veremos un punto por cada prueba que pase. Si falla, veremos un mensaje de error detallado que nos ayudará a identificar el problema.



## Respuestas mentales 



1.
¿Cuál es la principal ventaja de usar Flask como framework web en Python?
Es un microframework ligero y flexible
2.
¿Qué comando necesitas ejecutar para iniciar un servidor de desarrollo Flask?
flask run
3.
¿Cómo defines una ruta en Flask que responda tanto a GET como a POST?
@app.route(’/’ , methods=[“POST”, “GET”])

4.
¿Qué método de SQLAlchemy se usa para crear todas las tablas en la base de datos?
create_all()
5.
¿Qué método se usa para obtener todos los registros de una tabla en SQLAlchemy?
query.all()
6.
¿Qué método HTTP se usa para actualizar datos existentes en una aplicación RESTful?
PUT
7.
¿Qué método de SQLAlchemy se usa para eliminar un registro de la base de datos?
db.session.delete()
8.
¿Cuál es la mejor práctica para organizar una aplicación Flask de mediano tamaño?
Usar una estructura modular con blueprints
9.
¿Qué método se usa para registrar un Blueprint en una aplicación Flask?
app.register_blueprint()
10.
¿Qué función de Flask se usa para mostrar mensajes flash al usuario?
flash()
11.
¿Dónde se debe incluir el CDN de TailwindCSS en una aplicación Flask?
En el template base HTML
12.
¿Qué configuración es necesaria para usar sesiones en Flask?
SECRET_KEY
13.
¿Qué método se usa para cerrar la sesión de un usuario en Flask?
session.clear()
14.
¿Qué método se usa para validar datos de un formulario en Flask?
request.form.get()
15.
¿Qué clase base se usa para crear pruebas en Flask?
unittest.TestCase