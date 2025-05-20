## Curso de Django Rest Framework
> Construye APIs seguras y escalables con Django REST Framework. Crea modelos, serializadores, endpoints, validaciones, autenticación, vistas y pruebas, usando las mejores prácticas del desarrollo web moderno.


## Clase 1: Creación de APIs con Django REST Framework
> 

## ¿Por qué las APIs son esenciales para las aplicaciones?
Las APIs conectan aplicaciones permitiendo que compartan información en tiempo real.
Sin APIs, no sería posible realizar tareas básicas como verificar tu ubicación o procesar pagos.
Permiten la comunicación eficiente entre servidores, fundamental para la funcionalidad de cualquier aplicación moderna.

## ¿Cómo facilita Django REST Framework la creación de APIs?
- Django REST Framework permite configurar y desplegar APIs sin necesidad de crear todo desde cero.
- Se encarga de la seguridad, la comunicación y la interacción con bases de datos, ofreciendo un enfoque escalable.
- Este framework se enfoca en la simplicidad y rapidez, haciendo que el desarrollo sea eficiente y sin complicaciones.

## ¿Qué hace a Django REST Framework adecuado tanto para principiantes como para expertos?
- Empresas de todos los tamaños, desde startups hasta grandes corporaciones, usan Django REST Framework debido a su versatilidad y facilidad de uso.
- No es necesario ser un experto para empezar a trabajar con él, lo que lo convierte en una opción accesible para cualquier desarrollador.
- Al utilizar Django REST Framework, puedes concentrarte en lo que realmente importa: crear experiencias digitales de calidad.

## ¿Qué beneficios ofrece Django REST Framework en la producción de APIs?
- Ahorra tiempo al evitar el desarrollo de funciones repetitivas y básicas.
- Integra funciones clave como autenticación, manejo de datos y seguridad de forma nativa.
- Facilita la escalabilidad, permitiendo que las aplicaciones crezcan sin problemas técnicos mayores.

```Python

```


## Clase 2: APIs y JSON: Comunicación entre Servidores y Aplicaciones Web
> Las APIs (Application Programming Interfaces) permiten que los computadores se comuniquen entre ellos de manera estructurada

## ¿Qué es el formato JSON y por qué es importante?
- JSON (JavaScript Object Notation) es el formato estándar para enviar y recibir datos a través de APIs.
- Permite almacenar y estructurar información como texto, arreglos y objetos.
- Por ejemplo, un usuario puede tener varios hobbies, y estos se almacenan en un arreglo dentro de un JSON.

## ¿Cómo se estructuran las APIs REST?
- REST (Representational State Transfer) es una arquitectura que define cómo deben enviarse los mensajes a través de HTTP usando JSON.
- Garantiza que las comunicaciones sean predecibles, lo que significa que las mismas solicitudes siempre producirán los mismos resultados.

## ¿Cuáles son los métodos principales de una API REST?
- GET: Se utiliza para obtener información. Puede devolver una lista de recursos o un recurso específico.
- POST: Permite crear nuevos recursos, como agregar un nuevo usuario.
- DELETE: Utilizado para eliminar un recurso existente.
- PUT y PATCH: Modifican la información de un recurso, ya sea un solo campo o todo el contenido.

```Python

```


## Clase 3: Creación de APIs con Django REST Framework
> 

## ¿Cómo instalar y configurar Django REST Framework?
- Paso 1: Primero, necesitas tener instalado Python. Confirma la instalación con el comando: python3 --version.
Crea un entorno virtual con: python3 -m venv venv, y actívalo con source venv/bin/activate (Linux/Mac) o consulta los recursos para hacerlo en Windows.

- Paso 2: Instala Django y Django REST Framework con: pip install django djangorestframework.

## ¿Cómo iniciar un proyecto con Django?
- Paso 3: Crea un nuevo proyecto usando el comando: django-admin startproject doctorapp . => el Punto Indica que cree el proyecto en el folder donde estoy actualmente 
Esto generará los archivos necesarios dentro de la carpeta donde estés trabajando.
- Paso 4: Agrega las librerías instaladas a un archivo requirements.txt con el comando: pip freeze > requirements.txt, lo cual es crucial para mantener control sobre las versiones que estás utilizando en tu proyecto.

## ¿Cómo integrar Django REST Framework en el proyecto?
- paso 5: Dentro del archivo settings.py, busca la configuración INSTALLED_APPS y agrega 'rest_framework'.
La documentación oficial de Django REST Framework proporciona detalles sobre su instalación y configuración, lo cual es una excelente fuente de referencia.

## ¿Qué extensiones son recomendables para mejorar el entorno de desarrollo?
Usa extensiones como “Python” y “Black” de Microsoft en tu editor para mejorar la experiencia de desarrollo.
La extensión de Python te permite realizar depuraciones fácilmente.
Black formatea tu código automáticamente conforme al estándar PEP8, ayudando a mantener un código limpio y consistente.

## ¿Cómo ejecutar el proyecto?
- Paso 6: Ejecuta el servidor de desarrollo con: python manage.py runserver. Esto te permite ver los cambios que realices en tiempo real.
Visita la URL generada para confirmar que Django se ha configurado correctamente.

```Python

```

## Clase 4: Django REST: Funcionalidades y Ventajas al Crear APIs
> 

## ¿Cómo reutiliza Django REST las funcionalidades de Django?
Django REST reutiliza varias de las funcionalidades principales de Django, lo que permite un flujo de trabajo más sencillo:

- ORM de Django: DRF usa el Object-Relational Mapping (ORM) de Django para manejar modelos y realizar consultas a la base de datos sin escribir SQL.

- Sistema de URLs: Mejora el sistema de URLs de Django con un sistema de routers que crea automáticamente rutas de acceso a los recursos, simplificando la configuración de enrutamiento.

- Vistas basadas en clases: DRF extiende las vistas de Django con un nuevo concepto llamado Viewsets, que agrupa funcionalidades como listar, crear, actualizar y borrar dentro de una sola clase.

## ¿Qué añade Django REST para facilitar la creación de APIs?
Además de aprovechar la estructura de Django, Django REST agrega funcionalidades clave que hacen más fácil el desarrollo de APIs:

- Serializadores: Permiten transformar objetos Python a JSON y viceversa, facilitando la creación de APIs basadas en los modelos de Django sin tener que duplicar la información.

- Viewsets: Agrupan varias acciones en una sola clase, simplificando el código y reduciendo redundancias. Además, permiten manejar acciones según el método HTTP utilizado.

- Mejoras en seguridad: Gracias a la integración con Django, se pueden utilizar todas las configuraciones de seguridad como middleware y permisos.

- Compatibilidad con Django Admin: Permite seguir administrando la información de la aplicación a través de la interfaz administrativa de Django.

## ¿Cómo optimiza Django REST el desarrollo de APIs?
DRF optimiza varios aspectos del desarrollo de APIs al ofrecer herramientas que simplifican tareas comunes:

- Enrutamiento automático de URLs a través de routers.
- Serialización eficiente de datos basados en modelos Django, evitando la duplicación de lógica.
- Manejo de vistas más flexible con Viewsets que agrupan múltiples funcionalidades.
- Continuidad con las funcionalidades de seguridad y administración de Django, sin necesidad de configuraciones adicionales.

## Qué añade Django RF para desarrollar API's

Django REST agrega funcionalidades clave que hacen más fácil el desarrollo de APIs robustas, escalables y fácil de mantener:

- Estructura del Proyecto: Crea una carpeta api/ en tu app para organizar serializers, views y routers.
- Serializers: Usa ModelSerializer para simplificar la creación de serializers y validar datos.
- Vistas y Rutas: Utiliza vistas basadas en clases y routers para manejar operaciones CRUD de manera eficiente.
- Autenticación y Permisos: Configura el sistema de autenticación y establece permisos adecuados para controlar el acceso.
- Throttling: Implementa throttling para proteger tu API y garantizar acceso justo.
- Documentación: Genera documentación interactiva con herramientas como Swagger o Redoc.
- Pruebas: Escribe pruebas automatizadas usando APITestCase para asegurar el correcto funcionamiento de la API.
- Versionado: Considera implementar un esquema de versionado para manejar cambios futuros.
- Manejo de Errores: Utiliza las excepciones de DRF para ofrecer respuestas coherentes en caso de errores.

ORM: Permite interactuar con la base de datos utilizando objetos Python en lugar de consultas SQL.
Serializers: Convierten datos complejos (como objetos de modelos) en formatos como JSON y viceversa.
ViewSets: Agrupan las operaciones CRUD en una sola clase para simplificar el manejo de vistas en APIs.

## Clase 5: Modelos y Serializadores en Django para DoctorApp
> Pasos para genear modelos en tu APIs

- Paso 01: Generar los comandos para crear los modelos, recueda por cada ajuste debes correr los ultimos dos comandos 
```Python
- python3 manage.py startapp patients
- python3 manage.py startapp doctors
- python3 manage.py startapp bookings
- python manage.py makemigrations
- python manage.py migrate
```

- Paso 02: Registramos las apps creadas en el ´settings.py´ 

```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'patients',
    'doctors',
    'bookings',
]
```
- Paso 03: Este paso es generar el modelo.py 


- Paso 04: Este paso es generar el serializers.py => Recuerda los serializadores nos permiten convertir un modelo a Json y viceversa 

- Paso 04:

- Paso 05: 

- Paso 06:

- Paso 07:

```Python
- python3 manage.py startapp patients
- python3 manage.py startapp doctors
- python3 manage.py startapp bookings
- python manage.py makemigrations
- python manage.py migrate


```


## Clase 6: Uso de Serializadores en Vistas con Django REST Framework
> Pasos para Poblar las tablas 

## Pasos 
- Paso 1: pip install django-seed psycopg -> Instalar django-seed 
- Paso 2: 
```Python
    INSTALLED_APPS = [

    ....

    "django_seed",

    ]
```
- Paso 3: ´python manage.py seed patients --number=10´ => 
- Paso 4: 

{
"id":11,
"first_name":"Leonard",
"last_name":"Cuenca",
"date_of_birth":"2025-01-20",
"contact_number":"1",
"email":"cuenca623@gmail.com",
"address":"Calle 3434 con Calle 234",
"medical_history":"Reposo"
}

## Clase 7: 
> 

```Python

```


## Clase 8: 
> 

```Python

```


## Clase 9: 
> 

```Python

```


## Clase 10: 
> 

```Python

```


## Clase 11: 
> 

```Python

```


## Clase 12: 
> 

```Python

```


