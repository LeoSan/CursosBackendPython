# Curso de Django

> Construye aplicaciones web completas con Django. Crea modelos, vistas, plantillas, administra datos, usa relaciones, realiza pruebas, despliega en AWS y conecta con bases de datos y REST APIs.

## Clase 1:  Entornos Virtuales y Configuración de Django en Python
> Django es un framework para desarrollo web escrito en Python que inicialmente fue utilizado para crear blogs, pero ha evolucionado para soportar aplicaciones complejas, como las primeras versiones de Instagram y Spotify. 

## ¿Cuáles son los requerimientos previos para aprender Django?
- Conocer Python, ya que Django está construido en este lenguaje.
  - Sintaxis básica: if, for, definición de variables.
- Comprender la programación orientada a objetos.
  - Reutilización de código mediante clases y herencia.
- Conocer HTML para diseñar la interfaz de usuario.
- Conocimientos básicos de CSS para estilizar la aplicación.


## ¿Por qué es importante usar entornos virtuales en Django?
Los entornos virtuales permiten gestionar diferentes versiones de paquetes y librerías en un mismo equipo sin conflictos. Esto es crucial cuando se trabaja en múltiples proyectos que requieren distintas versiones de Django o cualquier otro paquete de Python.

## ¿Cómo se crea un entorno virtual en Python?
- Abre la terminal en tu editor de código preferido, como Visual Studio Code.
- Crea una carpeta para tu proyecto y ábrela en el editor.
- Usa la librería venv de Python para crear un entorno virtual:
    - python -m venv ~/path_to_your_folder/.venvs/my_first_env -> python3 -m venv django_one
- Verifica la creación del entorno con ls en la carpeta especificada.

## ¿Cómo se activa un entorno virtual?
- Para activar el entorno virtual y asegurarte de que los comandos se ejecuten en este entorno específico:
    - source ~/path_to_your_folder/.venvs/my_first_env/bin/activate -> source django_one/bin/activate
- Notarás que el nombre del entorno virtual aparece en la terminal, indicando que está activo.

## ¿Qué significa tener un entorno virtual activo?
Significa que cualquier comando que ejecutes utilizará las librerías instaladas en ese entorno específico, evitando conflictos con otras versiones de librerías que puedas tener en tu sistema. Esta práctica es esencial para evitar colisiones y mantener un entorno de desarrollo limpio y manejable


## Clase 2: 
>

## Pasos para instalar Django 
- Paso 0: se recomienda generar el entorno -> python3 -m venv django_one -> source django_one/bin/  
- Paso 1: pip3 install Django
![Ejemplo](../06_Curso_Django/info/info_001.png)
- Paso 2: debemos validar los comandos instalados en Django este comando es ´django-admin --help´
![Ejemplo](../06_Curso_Django/info/info_002.png)
- Paso 3: Ejecutamos el comando para iniciar el protecto ´django-admin startproject miPrimerDjango5´ Nombre del proyecto no debe estar separado usemos camelCase
- Paso 4: ya dentro del proyecto podemos ejeuctar este comando para validar los comandos del proyecto -> ´ python3 manage.py --help´
- Paso 5: para correr el servidor de django es de la siguiente manera ´python3 manage.py runserver´
![Ejemplo](../06_Curso_Django/info/info_003.png)
- paso 6: ´pip3 install -r requiriments.txt´

## Clase 3: Arquitectura MBT en Frameworks Web: Model, View y Template
> La arquitectura del framework está diseñada para ser reutilizable y organizar todas tus tareas. Utiliza el modelo MVT (Model, View, Template).

## ¿Qué es el modelo en MVT (Model, View, Template)?
El modelo es la parte de los datos:

Guarda y procesa los datos.
Contiene la lógica del negocio, como una calculadora que suma 2 más 2.

## ¿Qué es la vista en MTV?
La vista actúa como un conector:

Accede y dirige los datos.
Controla el flujo de peticiones y respuestas.
Verifica permisos y realiza comprobaciones necesarias.


## ¿Qué es el template en MTV?
El template maneja la parte gráfica:

Usa HTML y CSS para mostrar los datos.
Por ejemplo, muestra una lista de zapatos almacenada en el modelo.

## ¿Cómo interactúan modelo, vista y template?
El flujo de datos es el siguiente:

El modelo pasa datos a la vista en un array.
La vista pasa esos datos al template en un contexto.
El template muestra los datos gráficos.
En sentido contrario:

Un usuario busca en el template.
La vista recibe la búsqueda y consulta al modelo.
El modelo devuelve los resultados a la vista.
La vista envía los datos al template para mostrarlos.

## estructura tus archivos 

![Ejemplo](../06_Curso_Django/info/info_004.png)



> Nota: No debe haber conexión directa entre template y model. Siempre usa la vista para asegurar verificaciones y permisos.


## Clase 4: Modelo, Vista y Plantilla en Django: Creación y Conexión Básica
>
## ¿Cómo se definen los modelos en Django?

## Pasos 
- Paso 1: se ejecuta el comando para crear nuestra primera app ´python3 manage.py startapp my_first_app´ OJO esto debe estar al mismo nivel de MiPrimerDjango5 ya que se usa este repositorio para configurar nuestra app. este comando genera un directorio nuevo con archivos que podemos editar para dar forma a nuestra app 

    - Debe quedar así 
    - ![Ejemplo](../06_Curso_Django/info/info_005.png)

- Paso 2: Debemos ir al archivo setting.py de nuestro gestor de proyectos para este caso se llama ´miPrimerDjango5´ y agregar el nombre de la app previamente del paso 1 ->  ´python3 manage.py startapp my_first_app´
    - Debe quedar así 
    - ![Ejemplo](../06_Curso_Django/info/info_006.png)

- Paso 3: Podemos generar nuestros template de la siguiente forma debemos ir a nuestro **desarrollo app** recuerda es lo generado del paso 1, y crear el siguiente directorio template/nombre_app/nombre_del_html.html -> 'template/my_first_app/car_list.html' 
    - Debe quedar así 
    - ![Ejemplo](../06_Curso_Django/info/info_007.png)

- Paso 4: Debemos crear nueva rutas para esto debemos editar el archivo ´/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/06_Curso_Django/practica/miPrimerDjango5/miPrimerDjango5/urls.py´
    - Debe quedar así 
    - ![Ejemplo](../06_Curso_Django/info/info_008.png)

- Paso 5: Debemos ahora trabajar en la app y hacer los ajustes necesarios siguiente el MVT 
    - View 
    ```python
        from django.shortcuts import render

        # Create your views here.
        def my_view(request):
            return render(request, "my_first_app/car_list.html")

    ```
    - model
    ```python
        from django.db import models

        # Create your models here.
        class Car(models.Model):
            title = models.TextField(max_length=250)

    ```
    - template 
    ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Lista de Coches </title>
        </head>
        <body>
            <h1>Esta es la lista de coches</h1>
            
        </body>
        </html>

    ```
- Paso 6: Podemos ejeuctar el runserver ´python3 manage.py runserver´

## Clase 5: Modelos y Migraciones en Django ORM
>La “M” en el patrón MVC se refiere al Modelo, que es crucial para manejar datos de la base de datos en Django. En lugar de utilizar listas con datos estáticos en las vistas, ahora trabajaremos con datos provenientes del modelo, aprovechando el ORM de Django.

## ¿Qué es el ORM en Django?
El ORM (Object-Relational Mapping) en Django nos permite definir clases de Python que se relacionan directamente con las tablas de la base de datos. De esta forma, evitamos escribir sentencias SQL, ya que todo se maneja mediante Python.

## ¿Cómo se define una clase de modelo en Django?
Para definir un modelo, creamos una clase en el archivo models.py. Cada clase de modelo se corresponde con una tabla en la base de datos. Por ejemplo, si definimos la clase Car, esta se convertirá en una tabla con el nombre Car en la base de datos.

## ¿Qué son las migraciones en Django?
Las migraciones son un sistema que Django usa para aplicar y revertir cambios en la base de datos. Cuando creamos o modificamos un modelo, generamos migraciones que se pueden aplicar para crear o actualizar tablas en la base de datos.

- Aplicar una migración
- Creamos la clase Car con un atributo title.
- Ejecutamos la migración hacia adelante para crear la tabla Car en la base de datos.
- Si agregamos un campo year a la clase Car, otra migración aplicará este cambio a la tabla.
- Revertir una migración

Si es necesario, podemos revertir una migración para volver al estado anterior de la tabla.
Por ejemplo, al revertir la migración del campo year, la tabla Car quedará como antes de agregar dicho campo.

## Clase 6: Migraciones en Django: Creación de Tablas en la Base de Datos
> La migración de modelos en Django es un proceso fundamental para mantener la base de datos en sincronía con las clases del proyecto. Este artículo explora el uso de comandos para migrar modelos en Django, específicamente cómo manejar la migración de un modelo llamado “carro”.

## ¿Cómo identificar migraciones pendientes en Django?
Al ejecutar el comando python manage.py runserver, puedes encontrar un error que indica migraciones pendientes. Este mensaje significa que las tablas correspondientes a tus clases de Django no están creadas en la base de datos, lo que impide el correcto funcionamiento del proyecto.

## ¿Cómo crear migraciones en Django?
Para crear migraciones, usa el comando ´python manage.py makemigrations´ Este comando genera un archivo en la carpeta de migraciones con la creación de la tabla correspondiente al modelo “carro”.

## ¿Cómo aplicar migraciones en Django?
Una vez creadas las migraciones, se deben aplicar usando ´python manage.py migrate´. Esto ejecuta todas las migraciones y crea las tablas necesarias en la base de datos.

## ¿Cómo verificar la base de datos en Django?
Puedes revisar la base de datos usando ´python manage.py dbshell´ Este comando te conecta a la base de datos definida en el archivo settings.py. En este caso, se utilizó SQLite, que es fácil de usar pero no ideal para producción debido a su baja concurrencia.

## ¿Cómo configurar la base de datos en Django?
La configuración de la base de datos se encuentra en el archivo settings.py bajo el diccionario DATABASES. Django soporta múltiples motores de base de datos como PostgreSQL, MariaDB, MySQL, Oracle y SQLite. En este curso, se utilizará PostgreSQL.


## Clase 7 - 8: Creación y Gestión de Campos en Tablas de Django ORM
>

## ¿Qué pasos se siguen después de modificar el modelo?
Después de agregar el nuevo campo al modelo, sigue estos pasos:
- Guardar los cambios en el archivo del modelo: No olvides guardar el archivo después de realizar modificaciones.
- Crear nuevas migraciones: Ejecuta el comando ´python3 manage.py makemigrations´. Si no detecta cambios, verifica si guardaste el archivo. ejecutalo dentro del app del proyecto. 
- Aplicar las migraciones: Ejecuta python ´python3 manage.py migrate´. Este comando actualiza la base de datos con la nueva estructura.
- Podemos usar el shell de python para interactuar con la base de datos ´python3 manage.py shell´ => Es como tinker en laravel
- Podemos usar el shell de python para interactuar con la base de datos ´python3 manage.py dbshell´ podemos acceder a la base de datos -> .tables -> select * from my_first_app_book;
-  podemos instalar este paquete para ayudarnos en comsola para auto completar -> ´pip3 install ipython´

## Clase 9: Relaciones de Tablas Uno a Muchos con Django
> Manera de crear nuevas clases del modelo y como relacionar de 1 - 1 

```python

class Publisher(models.Model):
    name = models.TextField(max_length=250, null=True, default='n/a')
    direccion = models.TextField(max_length=250, null=True, default='n/a')

    def __str__(self):
        return f"{self.name} - {self.direccion} "
    
class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

## Clase 10: Relaciones de Muchos a Muchos en Modelos de Base de Datos
> 
## Notas mentales 
- Lo importante resaltar es el orden de las classes 
- La propiedad en la clase hija [authors = models.ManyToManyField(Autor, related_name="authors") ]
- si lo hacemos por consola impportante 
    - In [15]: autor_list = [danny, audry2]
    - In [16]: book.authors.set(autor_list)

```python

class Publisher(models.Model):
    name = models.TextField(max_length=250, null=True, default='n/a')
    direccion = models.TextField(max_length=250, null=True, default='n/a')

    def __str__(self):
        return f"{self.name} - {self.direccion} "
    
class Autor(models.Model):
    nombre = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.nombre

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Autor, related_name="authors") ## Muy importante el orden por eso el Autor esta en la parte superior

    def __str__(self):
        return self.title

```
## Clase 11:  Relaciones 1 a 1 en Django: Creación y Gestión de Perfiles de Autor

## Notas mentales 
- Lo importante resaltar es el orden de las classes 
- La propiedad en la clase hija [author = models.OneToOneField(Autor, on_delete=models.CASCADE) ]
- si lo hacemos por consola impportante 


## Clase 12: Uso de Managers en Django para Consultas de Base de Datos
> Los managers en Django son una herramienta poderosa que permite realizar diversas acciones dentro de las listas de objetos de un modelo, como contar, traer el primero o el último elemento, crear nuevos registros y mucho más.

## Notas Mentales 
-  autor1 = Autor.objects.first() -> Nos trae el primero 
-  autor1 = Autor.objects.count()  -> Cuenta el total de autores 
-  autor1 = Autor.objects.last() -> Nos trae el ultimo 
-  Autor?? -> Nos indica como esta definida la clase dento del model 
-  Autor.objects.create(nombre='Leonard', birth_date='1988-01-20') -> Crea un objeto directo en la base 
-  Autor.objects.all() -> Nos devuelve una lista de los autores 
-  Autor.objects.filter(nombre='Leonard')-> Podemos filtrar datos con el filter
-  Autor.objects.filter(nombre='Leonard').delete()-> Podemos concatenar metodos para este caso filtro y elimino
-  Autor.objects.all().order_by('nombre') -> Podemos ordenarlos 

## Clase 13 - 14: URLs Dinámicas en Django: Creación y Gestión Eficiente
> Podemos generar nuestro propio archivo de url para este caso seguiremos los pasos 

## Paso 
- Paso 1: Podemos generar archivos en nuestras app sin depender del project para este caso podemos crear un urls.py en la ruta raiz -> my_first_app/urls.py
- Paso 2: Podemos generar la misma estructura del miPrimerDjango5/urls.py en el nuevo archivo my_first_app/urls.py
- Paso 3: Podemos revisar views para generar las views correspondientes-> 
    - Claro pasos previos como lo indica debemos tener formadas los Modelos
    - Tambien tener listo los template -> book_list.html
```python

def view_autores(request, *args, **kwargs):
    author = Autor.objects.get(id=kwargs['id'])
    context = {"autor": author}
    return render(request, 'my_first_app/autor_list.html', context)

def view_books(request):
    books = Book.objects.all() 
    context = {"book_list": books}
    return render(request, 'my_first_app/book_list.html', context)
```



## Clase 15: Templates y Tags en Django: Creación de Aplicaciones Web
> Resumen

Exploraremos los templates en Django y sus funcionalidades avanzadas que los diferencian del HTML estándar. Aprenderemos cómo los templates nos permiten mostrar contenido dinámico en el navegador, validar variables, recorrer listas y aplicar filtros para modificar valores antes de mostrarlos. También veremos cómo reutilizar contenido común mediante el archivo base HTML.

## ¿Qué son los templates en Django?
Los templates en Django son archivos HTML que incluyen funcionalidades adicionales para mostrar contenido dinámico. A diferencia del HTML puro, los Django templates permiten:

Mostrar variables
Realizar validaciones con if
Recorrer listas con for

## ¿Cómo se muestran variables en un template?
Para mostrar variables, se encierran en dobles llaves {{ }}. Por ejemplo, para mostrar una variable llamada var del contexto, se usaría:

{{ var }}


## ¿Qué son y cómo se utilizan los filtros en Django?
Los filtros permiten modificar el valor de una variable antes de mostrarla. Se usan con un pipe | seguido del nombre del filtro. Por ejemplo, para mostrar solo el día y mes de una fecha:

{{ fecha_nacimiento|date:"m/d" }}
Los filtros pueden concatenarse. Por ejemplo, convertir el resultado en minúsculas:

{{ fecha_nacimiento|date:"m/d"|lower }}

## ¿Qué son los tags en Django y cómo se utilizan?
Los tags agregan funcionalidades adicionales al código HTML. Se abren con {% %} y pueden incluir:

if: para validaciones
for: para recorrer listas
url: para mostrar URLs dinámicas
Algunos tags requieren una etiqueta de cierre. Por ejemplo, if y for:

{% if condition %}
    <!-- contenido -->
{% endif %}

## ¿Qué es el archivo base HTML en Django?
El archivo base.html permite definir contenido común para ser reutilizado en la aplicación. Se crean bloques que pueden extenderse en otros archivos. Por ejemplo:

<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <div id="content">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
Para reutilizar este contenido:

<!-- new_template.html -->
{% extends "base.html" %}
{% block content %}
    <!-- contenido específico -->
{% endblock %}


## Clase 16: Configuración de Proyecto Django: Entorno, Extensiones y Repositorio
> Para este caso vamos a crear una app de coffe_shop 

## Notas mentales 
- cuando se crea un proyecto en Django se genera un repo con el nombre del proyecto y nuestro desarrollo son las app donde podrá ir el modelo los migrate y entre otras funcionalidades 


```python


```

## Clase 17: 
> 

```python


```

## Clase 18: 
> 

```python


```



## Clase 20: Configurar plantillas 
>

## Pasos 
- Paso 1: Se debe configurar en en el seeting del proyecto NO en la app DEL PROYECTO de esta manera

```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates' )],## Es donde va buscar los templates
        'APP_DIRS': True, ## hay que activarlo 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

- Paso 2: se debe crear un repositorio llamado 'templates' es aqui donde iran nuestras base.html 
    - de esta forma 
    - ![imagen](../06_Curso_Django/info/info_009.png)
    - congiguramos nuestra plantilla base.html de esta manera PLANTILLA PADRE 
    ```python
        HEAD
        BODY
        {% block content %} 

        {% endblock content %}
        FOOTER
    ```


- Paso 3: nuestra plantilla HIJA PARA ESTE ejemplo usamos list_products.html uso usamos las propiedades extend y block  

```html
{% extends "base.html" %}

{% block content %}
<section class="bg-white p-6 rounded-md shadow-md">
    <h2 class="text-xl font-semibold mb-4">Listado de Productos</h2>
    <ul>
        {% for product in products  %}
            <li>
                {{product.name}}
                <b>${{product.price}}</b>
                {% if product.photo %}
                    <img src="{{product.photo.url}}" alt="{{product.name}}" style="max-height:100px" />
                
                {% endif %}
            </li>
        
        {% endfor %}
    </ul>                
</section>
{% endblock content %}
```
- Paso 4: si no funciona por favor valida nombre de plantillas, la configuracion de urls.py y los nombre de las plantillas hijos el cambio es casi instantaneo 



## Clase 21: Administración de Modelos en Django: Configuración y Uso de Django
> Explorar la funcionalidad del Django Admin es esencial para aprovechar al máximo el potencial de Django en la gestión de aplicaciones web.

## ¿Cómo accedemos al Django Admin?
Primero, asegúrate de que el proyecto de Django esté corriendo. Luego, accede a la URL “/admin”. Aparecerá una página de inicio de sesión con el título “Django Administration”.

## ¿Cómo creamos un superusuario?
Para acceder al admin, necesitas un superusuario. Detén el servidor y ejecuta el comando createsuperuser. Proporciona un nombre de usuario, correo electrónico y contraseña. Reinicia el servidor y usa estas credenciales para iniciar sesión en el admin.

## ¿Cómo registramos un modelo en el Django Admin?
Abre el archivo admin.py dentro de tu aplicación.
Crea una nueva clase que herede de admin.ModelAdmin.
Importa tu modelo con from .models import Product.
Registra el modelo usando admin.site.register(Product, ProductAdmin).

## ¿Cómo personalizamos la vista de lista en el Django Admin?
Puedes añadir campos a la lista de visualización usando list_display:

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
Esto muestra los campos name y price en la lista de productos.

## ¿Cómo agregamos funcionalidad de búsqueda?
Añade el atributo search_fields en la clase del administrador:

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
Esto permite buscar productos por nombre.

## ¿Cómo editamos y guardamos productos?
Desde la lista de productos, haz clic en un producto para abrir el formulario de edición. Realiza los cambios necesarios y selecciona una de las opciones de guardado.

## ¿Cómo añadimos imágenes a los productos?
Asegúrate de tener un campo de imagen en tu modelo.
Sube una imagen a través del formulario de edición.
Configura las URLs para servir archivos estáticos agregando la configuración en urls.py:
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## ¿Cómo administramos múltiples productos?
Selecciona varios productos usando los checkboxes y aplica acciones en masa, como eliminar.

## ¿Cómo configuramos la visualización de imágenes en la lista de productos?
Configura las URLs de los archivos estáticos y media para que Django sepa dónde encontrarlas. Asegúrate de importar y utilizar correctamente static y settings en tu archivo urls.py.

## ¿Cómo agregamos un nuevo campo al modelo?
Para agregar un nuevo campo, como la fecha de creación, modifica el modelo y actualiza la clase del administrador para mostrarlo en la lista:

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')

## Notas mentales Comandos 
- Crear usuario admin -> ´python3 manage.py createsuperuser´ -> Te pide unos pasos para seguir adelante 
- Podemos generar adminitración de nuestros modelos es se hace de esta manera podemos ingresar al repositorio del proyecto para este caso cofee_shop y buscar el archivo admin.py  
```python
from django.contrib import admin
from .models import Products

# Register your models here.
# Paso 1: genero la clase que podra administrar el modelo esto se hace para genrar un CRUD
class ProductAdmin(admin.ModelAdmin):
    model = Products 

# Paso 2: registramos y relacionamos modelo, con la clase que se genero aqui para el admin del modelo 
admin.site.register(Products, ProductAdmin)
```

## Clase  23 - 24 : Detalle de Orden y Personalización de Vistas en Django

"""

admin.TabularInline: Esto indica que la clase OrderProductInlineAdmin hereda de la clase TabularInline que se encuentra 
dentro del módulo admin. 

TabularInline es una clase de Django que permite mostrar modelos relacionados (en este caso, OrderProduct) 
directamente dentro de la página de edición de otro modelo (en este caso, Order), presentándolos en un formato de tabla.
"""
class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


"""
inlines = [OrderProductInlineAdmin]: Este atributo dentro de OrderAdmin es una 
lista que contiene otras clases InlineAdmin. 

En este caso, incluye OrderProductInlineAdmin. Esto es lo que permite que los objetos 
relacionados del modelo OrderProduct se muestren y se puedan editar directamente dentro 
de la página de administración del modelo Order
"""

## clase 27: Creación de APIs con Django REST Framework
> La separación de la lógica de backend y frontend es una práctica común en el desarrollo de software moderno, con el frontend generalmente escrito en JavaScript y la conexión al backend manejada a través de APIs. Django REST es una librería de Python que facilita la creación de estas APIs, permitiendo una integración eficiente entre frontend y backend

# ¿Cómo instalar Django REST Framework?
Para instalar Django REST Framework, utilizamos el siguiente comando:

- pip install django-rest-framework

## ¿Cómo configurar un Serializer en Django REST?
Los Serializers en Django REST convierten modelos de Django en JSON. Para crear un nuevo Serializer, sigue estos pasos:

Crea un archivo llamado serializers.py en la aplicación correspondiente.
Importa ModelSerializer desde rest_framework:
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

## ¿Cómo crear una vista en Django REST?
Para crear una vista que devuelva datos en formato JSON:

Crea una vista heredando de APIView:

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductListAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
Define la URL para esta vista en urls.py:

from django.urls import path
from .views import ProductListAPI

urlpatterns = [
    ...
    path('api/products/', ProductListAPI.as_view(), name='product-list-api'),
]

## ¿Cómo manejar permisos y autenticación en Django REST?
Dependiendo de tu caso de uso, puedes configurar permisos y autenticación. Para esta vista, vamos a desactivarlos:

from rest_framework.permissions import AllowAny

class ProductListAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


## Implementación de Django REST Framework en un Proyecto Django
## Pasos 

- Paso 1:  Instalación:**

   Ejecuta el siguiente comando en la terminal dentro del directorio de tu proyecto:

```bash
    pip install djangorestframework
```

- Paso 2: Agregar a INSTALLED_APPS:

Edita el archivo settings.py de tu proyecto y agrega 'rest_framework' a la lista INSTALLED_APPS:

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Tus otras aplicaciones
    'tu_app',
    'rest_framework',
]
```

- Paso 3: Crear Serializadores (tu_app/serializers.py):

Define un serializador para tu modelo. Ejemplo para un modelo Producto:

```python

# tu_app/serializers.py
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        # O campos específicos:
        # fields = ('id', 'nombre', 'precio')
```
- Paso 4: Crear Vistas de API (tu_app/views.py):

Define las vistas que manejarán las solicitudes. Ejemplo usando vistas basadas en clases:

```python

# tu_app/views.py
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductoLista(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
```

- Paso 5: Configurar URLs (tu_app/urls.py y mi_proyecto/urls.py):

Crea o edita tu_app/urls.py:

```python
# tu_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoLista.as_view(), name='producto-lista'),
    path('productos/<int:pk>/', views.ProductoDetalle.as_view(), name='producto-detalle'),
]
Incluye las URLs de tu aplicación en el urls.py principal de tu proyecto:

Python

# mi_proyecto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tu_app.urls')),
]
```
- Paso 6: Ejecutar el Servidor:

```Bash
python manage.py runserver
```

- Paso 7: Probar la API:

Puedes usar herramientas como curl, 1  Postman o tu navegador para interactuar con las siguientes URLs (asumiendo que tu servidor se ejecuta en http://127.0.0.1:8000 y has usado el prefijo /api/

## Clase 28: Configuración de Bases de Datos con Django y AWS RDS

## Pasos 
- Paso 1: Instalar el Adaptador de PostgreSQL para Python**

Activa tu entorno virtual y ejecuta:

```bash
pip install psycopg2
```

- Paso 2: Configurar Django para Usar PostgreSQL
    - Validar conexion de manera local 
    - ![Video Tutorial](../06_Curso_Django/info/info_013.png)
    - Modifica la sección DATABASES en settings.py:

```Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<nombre_basededatos>',
        'USER': '<nombre_usuario>',
        'PASSWORD': '<contraseña>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- Paso 3: Aplicar las Migraciones de Django

Asegúrate de estar en el directorio de tu proyecto Django y ejecuta:

```Bash

python manage.py makemigrations
python manage.py migrate
```
Paso 4: Crear un Superusuario (Opcional)

```Bash
python manage.py createsuperuser
```
- Paso 5: Ejecutar el Servidor de Desarrollo de Django

```Bash

python manage.py runserver
```

## Muestra del Logro 
![Ejemplo](../06_Curso_Django/info/info_010.png)

## Crear una Base de datos en amazon web server 


1. Crear una Instancia de Base de Datos PostgreSQL en Amazon RDS:
2. Accede a la Consola de AWS: Inicia sesión en tu cuenta de AWS y dirígete a la consola de administración.
3. Busca RDS: En la barra de búsqueda, escribe "RDS" y selecciona el servicio "Relational Database Service".
4. Crea una Base de Datos: Haz clic en el botón "Crear base de datos".
    - Elige el Motor de Base de Datos: Selecciona "PostgreSQL".
    - Selecciona la Plantilla: Elige la plantilla que mejor se adapte a tus necesidades (por ejemplo, "Nivel gratuito" para pruebas o "Producción" para entornos reales).
5. Configuración:
    - Nombre de la Instancia de Base de Datos: Elige un nombre único para tu instancia.
    - Nombre de Usuario Maestro: Define un nombre de usuario para el administrador de la base de datos (por ejemplo, django_user).
    - Contraseña Maestra: Establece una contraseña segura para el usuario maestro. Confírmala.
6. Configuración de la Instancia:
    - Clase de Instancia: Selecciona el tipo de instancia según tus requerimientos de rendimiento.
    - Almacenamiento: Define el tamaño del almacenamiento.
    - Tipo de Almacenamiento: Elige el tipo de almacenamiento (por ejemplo, "Propósito general SSD").

7. Conectividad:
    - Nube Virtual Privada (VPC): Selecciona la VPC donde deseas lanzar la instancia. Si no tienes una, AWS creará una por defecto.
    - Grupo de Subredes: Elige un grupo de subredes dentro de tu VPC.
    - Accesibilidad Pública: Decide si quieres que la base de datos sea accesible públicamente (generalmente no se recomienda por seguridad para producción). Si la eliges, deberás configurar los grupos de seguridad adecuadamente.
    - Grupo de Seguridad de VPC: Configura un nuevo grupo de seguridad o elige uno existente. Es crucial configurar las reglas de entrada para permitir el tráfico desde tu dirección IP o desde la instancia donde se ejecuta tu aplicación Django (si está en AWS EC2 u otro servicio). Asegúrate de permitir el tráfico en el puerto predeterminado de PostgreSQL (5432).
    - Parámetros Adicionales: Revisa y configura otros parámetros según tus necesidades (copias de seguridad, mantenimiento, etc.).
    - Revisa y Crea: Revisa la configuración y haz clic en "Crear base de datos".

- [Video Tutorial](https://mega.nz/file/RNNwRb5I#vD5gSXoO0Kw2jg4HZ_h7zY_4ewA6NqDhg78aBrY9Y3E)

## Configuración de redes de AWS 
> Esto nos permite en el setting de configuración de DJango conectarnos con nuestra base AWS 

- [Video Tutorial](https://mega.nz/file/xMEgEBjR#V1ghgXp2IgZOj06bDm4eo4I1JZqOBFJvuC_YSut82co)

**Importante**
- De aqui vamos extraer los datos para ingresarlo en el setting.py
 ![Video Tutorial](../06_Curso_Django/info/info_012.png)


## Conectando nuestra base de datos AWS a nuestro proyecto 
> Es información sensible si no funciona es porque borre la base de datos de AWS 

- Validar Conexion AWS 
 ![Video Tutorial](../06_Curso_Django/info/info_014.png)


## Clase 29: Uso de Django Environ para Manejar Credenciales Seguras

## Pasos 
- Paso 1: Necesitamos instalar un paquete para crear un archivo .env y poder ocultar nuestras credenciales -> ´pip3 install django-environ´
- Paso 2: En la seccion suiperior del archivo setting.py realizamos la importacion de nuestra libreria
 
```Python

import os
from pathlib import Path
import environ # Paso 1


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env() # Paso 2
environ.Env.read_env(os.path.join(BASE_DIR, ".env")) # paso 3

```
- Paso 3: Creamos nuestro archivo en raiz llamado ´.env´ y cramos en mayusculas nuetras variables que vamos usar 
```Python
DJANGO_DB_PASSWORD=TUCLAVEES
```
- Paso 4: en el archivo setting usamos nuestras variables creadas 
```Python
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        #"ENGINE": "django.db.backends.postgresql",
        #"NAME": "mongodb_base",
        #"USER": "leonard",
        #"PASSWORD": "admin",
        #"HOST": "localhost",
        #"PORT": "5432",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "HOST": "dbdjango.c74aegummz7m.us-east-2.rds.amazonaws.com",
        "PORT": "5432",
        "USER": "postgres",
        "PASSWORD": env.str('DJANGO_DB_PASSWORD'),  
    }
}
```
- Paso 5: Debemos montar en nuestro entorno la variable de entorno para que funcione -> ´export DJANGO_DB_PASSWORD="tucalve"´
- Paso 6: ejecutamos comando para volver validar si todo bien -> ´python3 manage.py dbshell´ 
    - Validar Conexion AWS 
    - ![Video Tutorial](../06_Curso_Django/info/info_015.png)

## Clase 30: Testing de Aplicaciones Django con Unit Tests

## Pasos 
- Paso 1: Dentro de nuestras app existe un archivo test.py aqui podemos generar nuestros TDD Usaremos products/test.py para generar una prueba 
```Python
from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductListViewTests(TestCase):

    def test_should_return_200(self):
        url = reverse("list_product")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 0)

    def test_should_return_200_with_products(self):
        url = reverse("list_product")
        Product.objects.create(
            name="test", description="test description", price="5", available=True
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["products"].count(), 1)
```

- Paso 2: Corremos nuestras pruebas ejecutamos el siguiente codigo ´python3 manage.py test´
    - nos indicará si la prueba fue exitosa 

## Clase 31-32: Despliegue de Proyectos Django en AWS: Configuración y Mejora de

## Pasos 
- Paso 1: Validamos el requirememnts.txt -> ´pip3 install -r requirements.txt´
- Paso 2: validamos el formateo de python con black esto nos permite cambiar el ese error comun de comillas dobles en donde no se debe usar realiza el acambio de manera automatica y con las reglas pip8 -> pip3 install black -> luego ejecutar -> black . -> o formatear archivo especificos -> black archivo.py
- Paso 3: En AMW Creamos una Persona Para configurar los Acceso  
    - Accedemos a Amazon [Login](https://us-east-2.console.aws.amazon.com/console/home?nc2=h_m_mc&region=us-east-2)  
    - Buscamos en el Buscador Superior **AIM** 
    - De la barra del menu izquierdo buscamos **Personas**
    - Clic Boton **Crear Persona**
    - Ingresamos ene el input un **nombre** -> cursodjango -> clic boton siguiente
    - Escogemos Opciones de permisos -> **Adjuntar politicas directamente** clic aquí y abajo en el check box escogemos **AdministrarAcces**
    - AWS nos muestra una interfaz para validar los datos y para finalizar boton **Crear Persona**
    - Nos indica que se creo exitosamente 
    - Anexo Video-> [Paso 3](https://mega.nz/file/gINAXbZQ#tfGpwQRYanm0dD1QWIaiIGGOmbR1p4g5xYJ_YOIkbvM)
- Paso 4: Generar credenciales 
    - Luego de seguir el paso3 podemos continuar 
    - Accedemos a nuestra persona creada dando clic **cursodjango**
    - En la parte superior de la pagina ubicamos **Crear clave de acceso** clic aquí
    - Clic en la opción **Interfaz de línea de comandos (CLI)**
    - clic  **Entiendo la recomendación anterior y deseo proceder a la creación de una clave de acceso.**
    - Valor de etiqueta de descripción es opcional para este caso no vamos generar tag 
    - clic boton **Crear clave de acceso**
    - Es importante copiar y pegar estas claves ya que no hay manera de volver acceder a ellas 
    - Anexo Video-> [Paso 4](https://mega.nz/file/QUllyLxJ#hHZGm_EEoQ1tGWcf3R6_jkXNidaI3IM4DEKhdC-fjHs)
- Paso 5: Debemos instalar **eb** es la manera de como aws se comonica via consola con nuestro proyectos.
    - Para instalar eb en MAC hay que ejecutar el siguiente comando -> ´brew install awsebcli´
    - Para comprobar la instalacion -> ´eb --version´
    - ejecutamos el comando -> ´eb init´
    - debemos escoger las opciones que nos indican: 
    - la ciudad Ohio : 14 
    - colocamos la clave secreta -> la que se genero en el paso 4
    - Colocamos clave secreta -> la que se genero en el paso 4
    - Decimos que si nombre dle proyecto igual
    - indicamos que yes Clave SSH 
    - enter  
    - enter 
    - Te genera clave
    - Dejo evidencia de los pasos en consola: 
        - ![Evidencia 1](../06_Curso_Django/info/info_016.png)   
        - ![Evidencia 1](../06_Curso_Django/info/info_017.png)   

- Paso 6: Debemos validar en AWS si se genero la aplicación
    - Debes loguearte 
    - Buscar en el buscador superior **Elastic Beanstalk**
    - La barra de Menu Izquierdo buscar **Aplicaciones**
    - Debe salir el nombre de la aplicación que generamos en la línea de comandos
    - ![Evidencia 1](../06_Curso_Django/info/info_018.png) 
- Paso 7: Creamos nuestro environment por consola: 
    - Ejecutamos ´eb create {nombre-environment}´ -> ´eb status coffe-shop-production´ este comando demora unos minutos 
    - El servicio creará la infraestructura necesaria, incluyendo instancias y configuraciones de seguridad.
    - ![Evidencia 2](../06_Curso_Django/info/info_019.png) 
    - Valida como van los parametros de nuestra aplicacion ´eb status {nombre-environment}´ -> ´eb status coffe-shop-production´
    - Leyendo los estatus hay que validar que el Health: Red -> esto indica que no esta corriendo hay que validar porque no esta corriendo 
    - Podemos ver los logs ejecutando el siguiente comando ´eb logs {nombre-environment}´ -> ´eb logs coffe-shop-production´
    - Para este caso tenemos el siguiente error -> ModuloNotfound -> quiere decir que esta buscando el archivo wsgi.py pero no lo encuentra podemos ejecutar un comando para reconfigurar el entorno
    - Comando de reconfiguración -> ´eb config´
    - Ubicamos la secci´pn llamada -> aws:elasticbeanstalk:container:python:
    - Luego la sección WSGIPath: application debemos pasar -> WSGIPath: cofee_shop.wsgi:application
    - Explicación como el archivo wsgi.py esta dentro de la carpeta cofee_shop esta no lo esta encontrando por lo que le estamos indicando que debe entrar en ese direcctorio, al realizar el ajuste notece que hay que dejar un espacio esto es importante ya que no te permite editar 
    - "WSGIPath:-coffee_shop.wsgi:application" Indico con guion(-) el espacio que debe tener
    - Podemos ver los logs tambien en wn AWS checar imagen debemos descargar: 
    - ![Evidencia 2](../06_Curso_Django/info/info_020.png)
    - Para el siguiente error debemos configurar la URL_BASE ejecutamos el siguiente comando -> ´postgres://miusuario:micontraseña@mihost.amazonaws.com:5432/mibasededatos´
    - Ejemplo -> eb setenv DJANGO_DB_URL="postgres://miusuario:micontraseña@mihost.amazonaws.com:5432/mibasededatos"
    - Tambien debemos congigurar en el setting el ALLOWED_HOSTS anexando el CNAME -> coffe-shop-production.eba-wbpfxpgp.us-east-2.elasticbeanstalk.com que podemos extraer usando el ´eb status´ 
    - Como hicimos cambios en el proyecto debemos subirlos 
        - git status
        - git add . 
        - git commit -am"Ajuste"    
        - eb deploy coffe-shop-production --staged
    - Configuramos los static creando en el setting.py -> STATIC_ROOT = "static"
    - ejecutamos el comando ´python3 manage.py collectstatic´ -> si no funciona valida que tengas el **entorno activo** para este caso el django_one
    - el comando anterior genera un compilado del front de Django ahora hay que subir esos cambios 
    -  git add static/
    - eb deploy coffe-shop-production --staged

https://github.com/aws/aws-elastic-beanstalk-cli-setup?tab=readme-ov-file#2-quick-start
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html

https://github.com/platzi/django/blob/main/coffee_shop/settings.py


> La CLI de EB es una interfaz de línea de comandos para AWS Elastic Beanstalk que proporciona comandos interactivos que simplifican la creación, actualización y monitorización de entornos desde un repositorio local. Utilice la CLI de EB como parte de su ciclo diario de desarrollo y pruebas como alternativa a la consola de Elastic Beanstalk.




## Refinar 


Resumen

Desplegar una aplicación en AWS puede ser sencillo utilizando Elastic Beanstalk, un servicio que automatiza la infraestructura necesaria.

¿Qué es Elastic Beanstalk y cómo funciona?
Elastic Beanstalk es un servicio de AWS que permite desplegar y gestionar aplicaciones rápidamente. Basta con enviar el código, y el servicio se encarga de crear y gestionar la infraestructura necesaria.

¿Cómo se configura la CLI de Elastic Beanstalk?
Con las credenciales listas, sigue estos pasos para configurar la CLI:

Instala Elastic Beanstalk CLI siguiendo el enlace de instalación.
Ejecuta eb init y responde las preguntas sobre la región, el ID de acceso y la clave secreta.
Configura el nombre de la aplicación y la versión de Python.
Indica si utilizarás CodeCommit (en este caso, no, ya que se usa GitHub).
Configura una llave SSH para conectarte a los servidores.
¿Cómo se despliega la aplicación?
Crea un environment de producción con eb create coffee-shop-production.
El servicio creará la infraestructura necesaria, incluyendo instancias y configuraciones de seguridad.
Verifica el estado del environment con eb status.
¿Cómo se solucionan errores comunes durante el despliegue?
Configuración incorrecta del módulo WSGI: Configura el path correctamente en eb config.
Variable de entorno faltante: Crea la variable con eb setenv.
Error en ALLOWED_HOSTS de Django: Agrega el dominio correspondiente en el archivo de configuración de Django.
¿Cómo se gestionan archivos estáticos en Django?
Para asegurarte de que los archivos estáticos de Django se sirvan correctamente:

Ejecuta python manage.py collectstatic.
Configura el directorio de archivos estáticos en el archivo settings.py.

## Preguntas 

1.
¿Cuál es el comando para aplicar migraciones en Django?
python manage.py migrate

2.
¿Cómo defines una URL en Django?
urlpatterns = [ path('home/', views.home, name='home'), ]

3.
¿Qué archivo necesitas para definir un formulario en Django?
forms.py

4.
¿Cuál es el propósito de la función render en Django?
Renderizar una plantilla y devolver una respuesta HTTP

5.
¿Cómo configuras la base de datos en un proyecto Django?
En el archivo settings.py, en la sección DATABASES

6.
¿Cómo se crea un superusuario en Django?
python manage.py createsuperuser

7.
¿Cuál es el propósito de MEDIA_URL y MEDIA_ROOT en Django?
Para manejar archivos subidos por usuarios

8.
¿En qué archivo debes registrar una aplicación nueva un proyecto Django?
settings.py

9.
¿Cómo defines una relación Many-to-Many en un modelo de Django?
class MyModel(models.Model): related_model = models.ManyToManyField(RelatedModel)

9. ¿Cómo defines una relación Many-to-One en un modelo de Django?
class MyModel(models.Model): related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)

9. ¿Cómo defines una relación One-to-One en un modelo de Django?
class MyModel(models.Model): related_model = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)

10.
¿Qué comando se utiliza para crear migraciones en Django?
python manage.py makemigrations

11.
¿Para proteger una aplicación Django contra ataques de inyección SQL, qué medidas se deben tomar?
Usar consultas ORM de Django

12.
¿Cuál es la ventaja de usar vistas basadas en clases en lugar de vistas basadas en funciones en Django?
Reutilización de código y mayor organización

13.
¿Para manejar la autenticación de usuarios en Django, qué módulo es adecuado?
django.contrib.auth

14.
¿Qué patrón de diseño sigue Django para la separación de lógica y presentación?
Modelo-Vista-Template (MVT)

15.
¿Cómo puedes mejorar el rendimiento de una aplicación Django?
Usar cache y optimizar consultas de base de datos


16. 
¿Qué biblioteca se utiliza para trabajar con formularios en Django?

17. 
Qué archivo debes modificar para registrar un modelo en el panel de administración?
models.py
REPASAR 









