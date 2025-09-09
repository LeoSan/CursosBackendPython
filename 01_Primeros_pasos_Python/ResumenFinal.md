1.
¿Qué es la complejidad algorítmica?

Es la evaluación de recursos que toma un algoritmo para resolver un problema.

2.
¿Cuántas veces correrá el for loop en el siguiente caso?

def my_func(x):
    respuesta = 0
    for i in range(2000):
        respuesta += 1
    return respuesta
2000

3.
En el contexto del ordenamiento por inserción, ¿cuál de las siguientes afirmaciones describe correctamente el proceso de inserción de un nuevo elemento en la sublista ordenada?

Los elementos mayores al elemento que se está evaluando se mueven un lugar a la derecha para hacer espacio.

4.
Son algunas de las características de Python como lenguaje:
Sintaxis clara, escalable y de propósito general.
5.
Son las partes esenciales de una linked list:
Nodo, data, next, previous, head y tail.
6.
¿Qué ventaja tiene utilizar una linked list si de todos modos los nodos están creados de forma individual?
Nos permite tener un orden de sus datos, recorrerlos y agruparlos según nuestras necesidades.


7.
¿Cuál será el resultado del siguiente bloque de código?

a = {1,2}
b = {2,3}
print(a - b)
{2}
REPASAR 


8.
¿Qué es un entorno virtual?
La herramienta de Python para aislar o encapsular proyectos con sus propios paquetes y versiones sin afectar a otros proyectos y entornos virtuales.

9.
¿Con qué comando guardamos el nombre y versión de todos los paquetes de terceros en nuestro proyecto dentro de un archivo de texto?
pip3 freeze > requirements.txt
10.
¿Cuál es la sintaxis para añadir un parámetro a una ruta?
/movies/{id}
11.
¿Cómo se puede añadir un parámetro query a una ruta?
Solo poniéndolo como parámetro de una función
12.
¿Cuál es la clase que nos sirve para validar parámetros query?
Query
13.
¿Cuál es la forma correcta de importar un modelo en Django?
from myapp.models import MyModel
14.
¿Cómo defines una relación One-to-One en un modelo de Django?
class MyModel(models.Model): related_model = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
15.
¿Para manejar la autenticación de usuarios en Django, qué módulo es adecuado?

django.contrib.auth
16.
¿Cuál es la ventaja principal de automatizar las pruebas con Python?
Detectar errores más rápido y en mayor cantidad
17.
¿Qué método HTTP usamos para modificar un recurso en una vista de detalle en Django?
PUT
18.
Al realizar una eliminación de un recurso con DELETE en Django, ¿qué código de estado HTTP se debe devolver?
204 No Content
19.
¿Qué clase de permiso se debe usar en Django REST Framework para asegurar que un usuario esté autenticado antes de acceder a un endpoint?
IsAuthenticated
20.
¿Qué técnica puedes implementar en Django REST para limitar la cantidad de solicitudes que un usuario puede hacer en un período de tiempo?
Throttling
21.
Si necesitas agregar una nueva funcionalidad a un sistema sin modificar el código existente, ¿qué principio de diseño deberías aplicar?
El principio Open/Closed
22.
Al aplicar el principio de inversión de dependencias, ¿cuál es la principal ventaja de hacer que la clase de alto nivel dependa de interfaces en lugar de implementaciones concretas?
Facilita la modificación y prueba del código
23.
¿Qué patrón de diseño se debe aplicar para construir un objeto con múltiples configuraciones opcionales y cómo se implementaría en Python?
Se debe aplicar el patrón Builder, creando una clase Builder que contenga métodos para establecer cada atributo opcional y un método build para crear la instancia final.
24.
¿Qué comando en Git muestra el historial de commits de una rama?
`git log`
25.
¿Cuál de las siguientes opciones describe mejor la finalidad de un 'pull request' en GitHub?
Proponer cambios en el repositorio principal
26.
¿Qué archivo se suele usar en GitHub Pages para configurar el sitio?
`_config.yml`
27.
¿Qué método HTTP es más apropiado para crear un nuevo recurso en una API REST según las mejores prácticas?
POST

28.
¿Qué código de estado HTTP es más apropiado para indicar que un recurso ha sido actualizado exitosamente en FastAPI?
HTTP 200 OK
REPASAR

29.
Si necesitas crear un endpoint en FastAPI para suscribir un usuario a un plan específico, ¿qué método HTTP deberías utilizar?
POST
30.
¿Qué configuración asegura que las pruebas no modifiquen la base de datos de producción?
Usar una base de datos en memoria temporal y limpiar las tablas después de cada prueba.