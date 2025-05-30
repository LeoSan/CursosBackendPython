## Curso de Flask
> Crea aplicaciones web completas con Flask: rutas, vistas, formularios, bases de datos con SQLAlchemy, autenticación, plantillas con Jinja, pruebas unitarias y mejoras visuales con TailwindCSS.

- Profesor: Luis Martínez
- Fecha Inicio: 28/Mayo/2025  
- Fecha Fin: 
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
- sqlite3 notes.sqlite => no abre un entorno para ejeuctar comando sql para tener nuestra data 
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
> 

```Python

```


## Clase 11: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```

## Clase 12: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```


## Clase 13: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```

## Clase 14: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```

## Clase 15: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```

## Clase 16: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```


## Clase 17: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```

## Clase 18: Creación de una Aplicación de Notas con Flask Paso a Paso
> 

```Python

```



