1.
Tienes un set o conjunto de Python almacenado en la variable trips. ¿Cómo obtienes su cantidad de elementos?
len(trips)

2.
¿Cuál de las siguientes estructuras de datos nos permite ordenar sus elementos?
TUPLE 

3.
Dado el siguiente bloque de código:

def sum(a = 1, b = 0):
  return a + b
¿Cómo enviarías únicamente el valor de b para realizar la suma usando el valor por defecto de a?
sum(b=5)

4.
¿Qué herramienta nos permite trabajar con entornos virtuales en Python 3?
venv

5.
¿Con qué comando instalamos el paquete requests en su versión 2.27.1?
pip install requests==2.27.1

6.
¿De qué clase debe heredar un esquema de datos de Pydantic?
SchemaModel
REPASAR

7.
¿Cuál es la clase que nos sirve para validar parámetros query?
Param
REPASAR

8.
¿Qué parámetro puedes usar en la clase JSONResponse para enviar la información al cliente?
content

9.
¿Qué comando se utiliza para iniciar el servidor de desarrollo en Django?
python manage.py runserver

10.
¿Cómo defines una relación One-to-One en un modelo de Django?
class MyModel(models.Model): related_model = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)

11.
¿Para proteger una aplicación Django contra ataques de inyección SQL, qué medidas se deben tomar?
Usar consultas ORM de Django


12.
¿Qué middleware en Django se utiliza para habilitar la protección CSRF?
django.middleware.csrf.CsrfViewMiddleware


13.
¿Qué función se utiliza en una prueba unitaria para verificar que una excepción se lanza correctamente?
assertRaises()


14.
¿Cuál es el propósito principal del decorador @skip en una prueba unitaria?
Omitir temporalmente una prueba que aún no debe ejecutarse


15.
¿Cuál sería un buen nombre para una prueba de un método withdraw que reduce el saldo con un valor positivo?
test_withdraw_positive_amount_reduce_balance


16.
¿Qué debes agregar en settings.py para integrar Django REST Framework al proyecto?
Añadir 'djangorestframework' en INSTALLED_APPS
REPASAR

17.
¿Cómo aseguramos que los datos de una solicitud PUT sean válidos antes de guardar un recurso modificado en Django?
Usamos el método is_valid() del serializador


18.
¿Qué decorador debes usar en Python cuando necesitas un método que no dependa de ninguna instancia ni de la clase misma?
@property
REPASAR

19.
¿Cómo podrías aplicar el principio abierto/cerrado para añadir un nuevo método de notificación sin modificar el código existente?
Crear una nueva clase que implemente la interfaz de notificación y añadirla como opción en el servicio.


20.
Si decides implementar un nuevo validador en tu cadena de responsabilidad, ¿qué sería lo primero que deberías hacer para asegurar que funcione correctamente dentro del patrón?
Definir una interfaz o clase abstracta para los manejadores


21.
¿Qué comando en Git muestra el historial de commits de una rama?
`git log`


22.
Si quieres colaborar en un proyecto público de GitHub, ¿cuál es el primer paso recomendado?
Hacer un fork del repositorio en tu cuenta


23.
¿Qué representa `HEAD` en Git?
La referencia al commit actual en la rama activa


24.
Si deseas eliminar una rama local que ya no necesitas, ¿qué comando utilizas?
`git branch -d `


25.
Si necesitas relacionar múltiples clientes con múltiples planes en una base de datos usando FastAPI, ¿qué tipo de relación deberías implementar?
Relación muchos-a-muchos


26.
Si deseas implementar autenticación en un endpoint de FastAPI, ¿qué clase deberías usar para solicitar usuario y contraseña?
OAuth2PasswordBearer
REPASAR


27.
¿Qué clase base se usa para crear pruebas en Flask?
unittest.TestCase


28.
¿Cómo se define una ruta con parámetros dinámicos en Flask?
@app.route('/user/{id}')
REPASAR

29.
¿Qué configuración asegura que las pruebas no modifiquen la base de datos de producción?
Usar una base de datos en memoria temporal y limpiar las tablas después de cada prueba.


30.
Quieres validar que un campo 'código_postal' solo contenga números. ¿Dónde harías esta validación en tu modelo Pydantic?
En un método 'validate_codigo_postal' decorado con 'field_validator', usando métodos de string para validar contenido.


