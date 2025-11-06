# Curso de Unit Testing en Python
> Crea y automatiza pruebas unitarias en Python con UnitTest y PyTest. Organiza, parametriza, simula APIs externas, mide cobertura, usa mocks, datos dinámicos y aplica buenas prácticas para asegurar calidad en tus proyectos.

Inicio: 28-04-2025 
fin: 


## Notas mentales comandos 
- Debes estar dentoro del archivo raiz del proyecto no dentro de src y no dentro de tests 
-  python3 -m unittest -v -b tests.nombreTestPrueba =>  python3 -m unittest -v -b tests.test_api_client.py => Permite ejeucutar las pruebas programadas en el archivo correspondiente 
- python3 -m unittest -v -b tests.test_api_client.ApiClientTests.test_get_location_returns_side_effect  => Esta manera es de ejeuctar un metodo unico de test 

- python -m doctest => ´python3 -m doctest src/calculator.py´


- coverage run --source src -m unittest discover tests
- coverage report 
# Clase 1: Tipos de pruebas 
> Probar software no solo es una tarea técnica, es un proceso crítico que puede marcar la diferencia entre el éxito o el fracaso de un proyecto.

## ¿Qué tipos de pruebas son necesarias para asegurar la calidad del software?
- Pruebas unitarias: Se encargan de validar que cada componente pequeño del código funcione correctamente de manera aislada.
- Pruebas de integración: Verifican que los distintos componentes trabajen bien en conjunto, evitando problemas en la interacción de partes.
- Pruebas funcionales: Validan que el sistema en su totalidad funcione como se espera según los requisitos.
- Pruebas de rendimiento: Aseguran que el software sea rápido y eficiente, evaluando su comportamiento bajo diferentes condiciones de carga.
- Pruebas de aceptación: Determinan si el software cumple con las expectativas del usuario final.


## ¿Qué herramientas de testing ofrece Python?
- UnitTest: Permite crear pruebas unitarias de manera sencilla, asegurando que todas las partes del código realicen su función correctamente.
- PyTest: Facilita la creación de pruebas con una configuración avanzada para cubrir diferentes escenarios.
- DocTest: Integra pruebas directamente en los comentarios de las funciones, permitiendo validar el código mientras se mantiene la documentación.
- Coverage: Permite medir las lineas de código cuales no fueron validadas  
```python

```


# Clase 2: Pruebas Automatizadas y Unitarias con Python: Ahorra Tiempo y Evita Errores

- Testing Unitario: Verifica el correcto funcionamiento de unidades individuales de código, como funciones o métodos.

- Testing de Integración: Asegura que los diferentes módulos o componentes funcionen bien en conjunto.

- Testing de Sistema: Evalúa el sistema completo para asegurarse de que cumple con los requisitos especificados.

- Testing de Aceptación: Verifica que el software satisface las necesidades del usuario final.

- Testing de Regresión: Asegura que los cambios o actualizaciones no hayan introducido nuevos errores en funcionalidades ya existentes.

```python

def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 12


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product() 

```


# Clase 3 - 4: Estructura de Proyectos de Testing con Unit Test en Python
> > Las pruebas unitarias en Python son esenciales para asegurar el correcto funcionamiento del código. Utilizando la clase TestCase de la biblioteca UnitTest, podemos estructurar pruebas de manera eficiente y limpiar recursos una vez que se han ejecutado.



## ¿Cómo estructurar un proyecto de testing en Python?
1.  Separación de código y pruebas: Coloca el código fuente en una carpeta src y las pruebas en una carpeta test.

2. Entorno virtual: Crea un entorno virtual para aislar dependencias del proyecto. Esto se hace con python -m venv, lo que genera una carpeta con binarios y librerías solo para el proyecto. Ejemplo ´python3 -m venv venvtest´ para activar ´source venvtest/bin/activate´

3. Uso de gitignore: Añade un archivo .gitignore para evitar que el entorno virtual y otros archivos no deseados se suban al repositorio.

![Ejemplo de Git Ignore para pyton ](/Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/04_CursoUnitTestingPython/practicas/test_001/.gitignore)



## ¿Cómo escribir y ejecutar pruebas con Unit Test?
Para escribir pruebas, sigue estas buenas prácticas:

1. Crea un archivo de pruebas, como test_calculator.py, y empieza importando Unit Test.
2. Define clases que hereden de unittest.TestCase.
3. Escribe métodos de prueba que validen funciones específicas usando assertEqual para verificar resultados.
4. Ejecuta las pruebas con ´python3 -m unittest discover -v -s tests ´  para que Unit Testing encuentre y ejecute las pruebas automáticamente. recuerda el comando discovery es para indicarle que pruebas va ser **usamos test que es el nombre del directorio**

```python

import unittest
from src.calculator import sum, subtract, multiplication, division

"""
Esta clase nos va a dar una serie de funcionalidades que nos van a permitir ver el progreso de 
las pruebas, qué prueba se ejecutó, qué prueba falló, por qué falló
"""
class CalculatorTest(unittest.TestCase):
    
    def test_sum(self):
        assert sum(2, 3) == 5
   
    def test_subtract(self):
        assert subtract(10, 5) == 5
   
    def test_multiplication(self):
        assert multiplication(2, 4) == 8
    
    def test_division(self):
        assert division(30, 2) == 15
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(30, 30)
```


# Clase 5: Pruebas Unitarias con Método Setup en Python
> El uso del método setup en los tests permite simplificar y evitar la duplicación de código en las pruebas. Al iniciar un test, setup se ejecuta automáticamente, preparando el entorno para cada prueba de forma eficiente. 

```python

   def setUp(self) -> None:
        self.account = BankAccount(balance=1000)# Esto nos permite ejecutar esta linea de prueba se usa para evitar duplicar codigo esto se hace porque esta linea se repite en varios bloques 


```


# Clase 6: Pruebas de Registro de Transacciones en Cuentas Bancarias
> El método teardown es esencial para asegurar que nuestras pruebas no interfieran entre sí, y se usa para limpiar cualquier recurso temporal al final de cada prueba


```python

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

```


# Clase 7: Métodos de Assert en UnitTest para Pruebas Efectivas
> UnitTest nos proporciona una amplia gama de métodos de aserción que mejoran la forma en que validamos nuestras pruebas.

- assertEqual(a, b): Verifica si a y b son iguales.
- assertNotEqual(a, b): Verifica si a y b no son iguales.
- assertTrue(x): Verifica si x es verdadero.
- assertFalse(x): Verifica si x es falso.
- assertIs(a, b): Verifica si a y b son el mismo objeto.
- assertIsNot(a, b): Verifica si a y b no son el mismo objeto.
- assertIsNone(x): Verifica si x es None.
- assertIsNotNone(x): Verifica si x no es None.
- assertIn(a, b): Verifica si a está en b (para contenedores como listas, tuplas,  diccionarios, conjuntos o cadenas).
- assertNotIn(a, b): Verifica si a no está en b.
- assertIsInstance(a, b): Verifica si a es una instancia de la clase b (o de una subclase).
- assertNotIsInstance(a, b): Verifica si a no es una instancia de la clase b.
- assertRaises(exc, fun, *args, **kwargs): Verifica que la llamada a fun(*args, **kwargs) lanza la excepción específica exc. También se puede usar como un administrador de contexto con la sintaxis with self.assertRaises(SomeException):.
- assertRaisesRegex(exc, r, fun, *args, **kwargs) (disponible desde Python 3.2): Similar a - - assertRaises, pero también verifica que el mensaje de la excepción coincida con la expresión regular r. También se puede usar como administrador de contexto.
- assertAlmostEqual(a, b, places=7, msg=None, delta=None): Verifica si a y b son aproximadamente iguales, considerando un número específico de lugares decimales (places, por defecto 7) o una diferencia máxima (delta).
- assertNotAlmostEqual(a, b, places=7, msg=None, delta=None): Verifica si a y b no son aproximadamente iguales.
- assertGreater(a, b): Verifica si a es mayor que b.
- assertGreaterEqual(a, b): Verifica si a es mayor o igual que b.
- assertLess(a, b): Verifica si a es menor que b.
- assertLessEqual(a, b): Verifica si a es menor o igual que b.
- assertRegex(text, regex) (disponible desde Python 3.1): Verifica si la cadena text coincide con la expresión regular regex.
- assertNotRegex(text, regex) (disponible desde Python 3.2): Verifica si la cadena text no coincide con la expresión regular regex.
- assertCountEqual(first, second) (disponible desde Python 3.2): Verifica si la secuencia first y la secuencia second contienen los mismos elementos, sin importar el orden.


https://ellibrodepython.com/python-testing
```python

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola") #Prueba igualdad

    def test_assert_true_or_false(self):
        self.assertTrue(True) # Prueba si el valor es verdadero
        self.assertFalse(False) # Prueba si el valor es falso

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )


```


# Clase 8: Decoradores de Unit Test para Saltar Pruebas y Detectar Fallos
> En el desarrollo de software, es común enfrentarse a situaciones donde las pruebas unitarias no pueden ejecutarse por cambios o desarrollos en curso. En estos casos, comentar el código de las pruebas no es la mejor práctica. Afortunadamente, Python y unittest ofrecen decoradores que nos permiten omitir pruebas temporalmente, sin comprometer el flujo de trabajo ni la integridad del proyecto. Aquí aprenderemos cómo usar decoradores como @skip, @skipIf y @expectedFailure para manejar estos casos de manera eficiente.

```python

    @unittest.skip("Trabjo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)

```

# Clase 9: 
> Cuando estamos desarrollando en Python, ejecutar todas las pruebas desde la terminal es común en entornos de desarrollo. Sin embargo, en producción o integración continua, este enfoque puede no ser ideal, especialmente cuando solo queremos ejecutar pruebas específicas o tener un mejor control sobre cómo organizamos y ejecutamos estas pruebas. Python y su módulo Unit Test nos ofrecen herramientas como las suites de pruebas para modularizar y seleccionar qué pruebas ejecutar

```python

```


# Clase 10: Formato de Nombres para Pruebas Unitarias en Python

## ¿Cómo definir el formato de los nombres de las pruebas?
Todos los tests deben agruparse en clases, cada una relacionada con una clase de tu proyecto. Por ejemplo, si tienes una clase llamada BankAccount, la clase de prueba debería llamarse BankAccountTest.
Cada prueba debe comenzar con test_, para que las herramientas de testing la identifiquen fácilmente.
El siguiente elemento en el nombre debe ser el método que estás probando. Si es un método deposit, el nombre sería test_deposit_.

## ¿Cómo estructurar el escenario de la prueba?
Después del método, añade el escenario. Esto se refiere a los valores o parámetros que usas en la prueba. Por ejemplo, en el caso de un valor positivo en un depósito, el escenario sería positive_amount.

## ¿Cómo describir el resultado esperado?
Para finalizar el nombre, indica el resultado esperado. Si el depósito incrementa el saldo, añade algo como increase_balance. Así, un nombre de prueba completo sería: test_deposit_positive_amount_increase_balance.

## ¿Por qué es útil este formato?
Permite a cualquier miembro del equipo entender el propósito de la prueba sin revisar el código completo.
Facilita el mantenimiento del código y el soporte, ya que con solo leer el nombre, se entiende el objetivo de la prueba.

## ¿Qué reto se propone para mejorar las pruebas actuales?
Refactoriza las pruebas que has creado, probando diferentes escenarios y resultados posibles.
Imagina nuevas circunstancias para probar el código.
Compara tus resultados con el proyecto refactorizado que estará disponible en la sección de recursos, y comparte tus ideas.

```python

```


# Clase 11:  Pruebas de APIs en Python con Mocking y UnitTest SE LE LLAMA MOKEAR PRUEBAS A SERVIDORES 
> La simulación de servicios externos es crucial en proyectos de software para garantizar que las pruebas no dependan de APIs externas. Para lograrlo, utilizamos los Mocks, que permiten evitar las llamadas reales a servicios y, en cambio, retornan respuestas controladas en nuestras pruebas.

## ¿Qué es un Mock y cómo nos ayuda?
Un Mock es una herramienta que nos permite simular comportamientos de funciones o servicios externos. En lugar de ejecutar una llamada real a una API, podemos definir una respuesta predefinida, lo que permite:

Evitar depender de servicios externos en pruebas.
Acelerar la ejecución de las pruebas.
Controlar los resultados esperados.

## ¿Cómo integramos una API externa en Python?
Primero, se configura una función que recibe la IP del cliente y devuelve la ubicación mediante una API de terceros. Para hacer esto:

- Se instala la librería requests con ´pip3 install requests´.
- Si ya lo tenemos instaldo podemos generar un archivo rrequeriments.txt y aplicar el siguiente comando pip3 freeze | grep request > requeriments.txt
- Yo aplique este comando ' pip3 freeze | grep request > /Users/leonard/Documents/Dev/python/CursosBackendPython/01_Primeros_pasos_Python/04_CursoUnitTestingPython/practicas/test_001/requeriments.txt  '
- Se crea un archivo api_client.py donde conectamos con la API utilizando requests.get.
- Al recibir la respuesta, se convierte el resultado a JSON para obtener la información de país, ciudad y región.


```python

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")

```


# Clase 12: Simulación de Side Effects con Mock en Pruebas Unitarias
> Mock nos permite simular comportamientos variables, una herramienta útil cuando queremos probar cómo reacciona nuestro código ante diferentes escenarios sin modificar el entorno real. Uno de los usos más poderosos es el “side effect”, que nos ayuda a hacer que un método falle en un caso y funcione en otro. Esto es clave para manejar errores temporales, como en el caso de una API de pagos que rechaza una tarjeta incorrecta, pero acepta una correcta en un segundo intento.



```python
 @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI",
                },
            ),
        ]

        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

```

## ¿Qué métodos auxiliares facilita Mock?
Mock facilita métodos como raiseException, que lanza una excepción específica, y mock, que permite crear objetos personalizados. Estos objetos pueden tener parámetros configurables como status_code y devolver datos específicos al llamar métodos como JSON. Este tipo de pruebas es crucial para validar la resiliencia del software ante errores temporales.


# Clase 13: Simulación de Horarios para Pruebas Unitarias en Python **patching** 
> utilizando técnicas como el patch para simular situaciones específicas, como el control del horario de retiro en una cuenta bancaria. Esta habilidad es crucial cuando necesitamos validar restricciones temporales o cualquier otra lógica de negocio que dependa de factores externos, como el tiempo.

## **patching** 

Es una técnica comúnmente utilizada en las pruebas unitarias en Python para modificar temporalmente el comportamiento de un objeto o función durante la ejecución de las pruebas. Esto se hace principalmente para simular situaciones específicas o para evitar que el código real se ejecute, lo que permite que las pruebas sean más rápidas y controladas.

En Python, la biblioteca unittest.mock proporciona la función patch que se usa para este propósito. Aquí hay un desglose de cómo usar el patching:

### 1. Importar las Herramientas Necesarias
from unittest import TestCase
from unittest.mock import patch

### 2. Usar patch como Decorador
Puedes usar patch como un decorador para reemplazar un objeto o función durante la prueba.

```python

@patch('nombre_del_modulo.funcion_o_clase_a_mockear')
def test_mi_funcion(self, mock\_func):
    mock_func.return_value = 'valor simulado'
    resultado = mi_funcion_que_llama_a_mock_func()
    self.assertEqual(resultado, 'valor simulado')

```

### 3. Usar patch como Context Manager

También puedes usar patch como un administrador de contexto, lo que te permite restaurar automáticamente el objeto original después de salir del bloque with.


```python
class MyTestCase(TestCase):

  

   def test_mi_funcion(self):

       with patch('nombre_del_modulo.funcion_a_mockear') as mock_func:

           mock_func.return_value = 'valor simulado'

           resultado = mi_funcion_que_llama_a_mock_func()

           self.assertEqual(resultado, 'valor simulado')

```

### 4. Parchear Métodos de Clases

Si necesitas parchear un método de una clase, también puedes hacerlo. Por ejemplo:

```python
class MiClase:

   def metodo(self):

       return 'valor real'



class MyTestCase(TestCase):

  

   @patch.object(MiClase, 'metodo')

   def test_metodo_mock(self, mock\_metodo):

       mock_metodo.return_value = 'valor simulado'

       instancia = MiClase()

       resultado = instancia.metodo()

       self.assertEqual(resultado, 'valor simulado')

```


### 5. Comportamiento de Llamadas

Puedes verificar cómo se ha llamado un objeto simulado:

```python
class MyTestCase(TestCase):

  
   @patch('nombre_del_modulo.funcion_a_mockear')

   def test_mi_funcion(self, mock_func):

       mi_funcion_que_llama_a_mock_func()

       mock_func.assert_called_once()

```




Usar patch es una excelente forma de escribir pruebas más efectivas y específicas al modificar comportamientos de manera temporal y controlada

# Clase 14: Parametrización de pruebas con SubTest en UnitTest 
> El uso de SubTest en UnitTest te permite optimizar tus pruebas evitando la duplicación de código. Imagina que necesitas probar un método con varios valores diferentes. Sin SubTest, tendrías que crear varias pruebas casi idénticas, lo que resulta ineficiente. SubTest permite parametrizar pruebas, lo que significa que puedes ejecutar la misma prueba con diferentes valores sin repetir el código.

## ¿Cómo evitar la duplicación de pruebas con SubTest?
Al utilizar SubTest, puedes definir todos los valores que deseas probar en una lista o diccionario. Luego, iteras sobre estos valores mediante un bucle for, ejecutando la misma prueba con cada conjunto de parámetros. Así, si es necesario modificar la prueba, solo tienes que hacer cambios en un único lugar.

## ¿Cómo implementar SubTest en un caso práctico?
Para ilustrarlo, se puede crear una prueba llamada test_deposit_various_values. En lugar de duplicar la prueba con diferentes valores de depósito, utilizas un diccionario que contiene los valores a probar y el resultado esperado. Después, recorres estos valores con SubTest usando la estructura with self.subTest(case=case) y ejecutas la prueba para cada valor del diccionario. Esto asegura que cada prueba sea independiente y evita sumar valores a la cuenta de manera incorrecta.

## ¿Cómo gestionar errores con SubTest?
SubTest también es útil para identificar errores específicos. Si una prueba falla con un conjunto particular de parámetros, SubTest te permite ver fácilmente qué valores causaron el fallo. Esto facilita mucho la corrección de errores, ya que puedes aislar rápidamente los casos problemáticos y corregirlos de manera eficiente


```python
    def test_deposit_multiple_ammounts (self):
        test_cases = [
            {"ammount":100, "expected": 1100}, 
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500},             
        ]

        for case in test_cases:
            with self.subTest(case=test_cases):
                self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])

```


# Clase 15: Pruebas de Código con Doctest en Python 
> El uso de Doctest es una herramienta poderosa que te permite escribir pruebas directamente en la documentación del código, lo que facilita que otros desarrolladores comprendan y verifiquen los resultados esperados. Además de los Unit Tests tradicionales, Doctest permite que tus comentarios sean interactivos, ofreciendo ejemplos funcionales que se ejecutan dentro del código de Python. Veamos cómo puedes utilizarlo de manera eficiente.

## ¿Qué es Doctest y cómo se usa?
Doctest es una librería que está incluida en Python y que permite crear pruebas en los comentarios del código. Esto lo hace práctico ya que puedes escribir pruebas de manera muy similar a una sesión interactiva de Python. Solo debes añadir los ejemplos dentro de los comentarios y ejecutarlos con el comando python -m doctest.

## Comando 
- python3 -m doctest src/calculator.py
```python

```


# Clase 16:Generación de Datos de Prueba con la Librería Faker 
> Generar datos de prueba puede ser una tarea tediosa, pero con la librería Faker, este proceso se simplifica enormemente. Faker nos permite crear datos aleatorios como nombres, correos electrónicos y otros atributos de manera eficiente para validar la compatibilidad de nuestro código con diversas entradas. A continuación, exploramos cómo aprovechar Faker en pruebas automatizadas y cómo integrar la librería en nuestro proyecto.


## ¿Cómo instalar Faker y qué ventajas ofrece?
Para empezar a utilizar Faker, simplemente debemos instalarla a través de la terminal con el comando:

- pip install faker

## enlace 
- https://pypi.org/project/Faker/
- https://faker.readthedocs.io/en/master/

```python

    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def test_user_creation(self):
        name_generated = self.faker.name()
        email_generated = self.faker.email()
        user = User(name=name_generated, email=email_generated)
        self.assertEqual(user.name, name_generated)
        self.assertEqual(user.email, email_generated)

    def test_user_with_multiple_accounts(self):
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_account(account=bank_account)

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value)


```


# Clase 17: Cobertura de Código en Python con Coverage: Instalación y Uso

> En los proyectos grandes de software, resulta difícil identificar qué partes del código están correctamente probadas y cuáles no lo están. Por ello, es esencial usar herramientas como Coverage, que nos permite analizar qué porciones de nuestro código han sido ejecutadas durante las pruebas y cuáles no. Esto facilita la detección de áreas que necesitan cobertura adicional.

## ¿Qué es Coverage y cómo funciona?
Coverage es una herramienta que se ejecuta junto a las pruebas y captura un reporte sobre qué partes del código han sido probadas. Una vez finalizado el proceso, genera un informe detallado que indica qué porcentaje del código está cubierto. De esta manera, puedes identificar qué secciones de código necesitan nuevas pruebas.

## ¿Cómo instalar y utilizar Coverage?
Para instalar Coverage en un proyecto Python, sigue los siguientes pasos:

Abre la terminal e instala la herramienta con pip install coverage.
Después, usa pip freeze | grep coverage para agregar la librería a tu archivo de requirements.
Una vez instalada, ejecuta el comando coverage run -m unittest discover -s tests, que corre las pruebas en la carpeta tests

## Comandos 
- coverage run --source src -m unittest discover tests
- coverage report 
- coverage html

```python


```


# Clase 18: Integración Continua con GitHub Actions para Pruebas Automatizadas 
> Integrar una suite de pruebas en un sistema de Continuous Integration (CI) es clave para automatizar el proceso de verificación de cambios en el código. En este caso, usaremos GitHub Actions para correr nuestras pruebas de manera automática cada vez que haya un cambio en el repositorio, asegurándonos de que el código esté siempre funcionando correctamente.

## ¿Cómo configurar tu primera GitHub Action?
Primero, accede a la pestaña de “Actions” dentro de tu repositorio en GitHub. Ahí encontrarás un Marketplace con varias opciones. Busca “Python” y selecciona la Action “Python Application”. Esta configuración correrá pruebas automáticamente cada vez que haya un push o un pull request hacia la rama “Main”.

## ¿Qué pasos incluye el workflow de pruebas?
Clonación del repositorio: El workflow comienza clonando tu código, similar a un git clone.
Configuración de Python: Utiliza la versión 3.10 de Python, asegurando compatibilidad con el código del proyecto.
Instalación de dependencias: Ejecuta las instalaciones de las librerías listadas en el archivo requirements.txt, por ejemplo, Faker y Coverage.
Modificación del comando de pruebas: En lugar de utilizar un test genérico, el comando se cambia a python -m unittest discover test, adaptado a las pruebas unitarias del proyecto.

## ¿Cómo verificar si el workflow fue exitoso?
Una vez configurado el archivo y hecho el commit, puedes ver el progreso de la ejecución en la pestaña de “Actions”. Si todo salió bien, aparecerá un checkmark verde indicando que las pruebas pasaron exitosamente.

[Video](../04_CursoUnitTestingPython/info/video_001.mov)


# Clase 19: 
> Python ofrece una gran variedad de herramientas, y una de las más útiles para pruebas automatizadas es PyTest. PyTest mejora considerablemente la experiencia del desarrollador al permitir escribir y ejecutar pruebas de manera más eficiente. En esta guía veremos cómo instalar PyTest, crear pruebas parametrizadas y ejecutar un ejemplo básico. 

- Pytest es ideal si buscas una herramienta flexible, con una sintaxis más limpia y una comunidad activa que ofrece muchos plugins.

- Unittest es una buena opción si prefieres una herramienta integrada en la biblioteca estándar de Python y una estructura más clásica.

```python

@pytest.fixture
def account():
    return BankAccount()


@patch("src.BankAccount.datetime")
def test_withdraw_off_business_days_fails(mock_datetime, account):
    mock_datetime.now.return_value.hour = 9
    mock_datetime.now.return_value.weekday.return_value = 6
    with pytest.raises(OutOfScheduleError):
        account.withdraw(1000)

def test_divide_zero():
    with pytest.raises(ValueError,match="No se puede dividir entre 0"):
        c.divide(4,0)

```


# Clase 20: 
> Las herramientas de inteligencia artificial han revolucionado la forma en que desarrollamos software, simplificando tareas como la creación de pruebas unitarias. Estas herramientas permiten generar pruebas más rápido y con mayor precisión, ahorrando tiempo y reduciendo errores. A continuación, exploramos algunas herramientas clave que todo desarrollador debería conocer.

## ¿Qué es GitHub Copilot y cómo puede ayudarte a escribir pruebas?
GitHub Copilot es una extensión que puedes instalar en tu editor de código. Con ella, puedes chatear, darle contexto sobre tu código y pedirle que genere pruebas unitarias. Esta herramienta se integra directamente en el flujo de trabajo del desarrollador, lo que facilita la creación de pruebas con pocos comandos. Al escribir un prompt claro, como “create a test that doesn’t allow the deposit to be negative”, Copilot genera automáticamente el código de la prueba, optimizando el proceso de TDD (desarrollo guiado por pruebas).

## Beneficios de usar GitHub Copilot:
Ahorra tiempo generando pruebas automáticamente.
Mejora la precisión al sugerir código basado en grandes bases de datos de proyectos.
Facilita la integración en editores populares como Visual Studio Code.


## ¿Qué ofrece Supermaven y cómo se compara con otras herramientas?
Supermaven es una herramienta similar que permite integrar la API de ChatGPT directamente en tu editor de código. Con esta integración, puedes utilizar las capacidades de ChatGPT para generar y modificar pruebas en tiempo real. Lo interesante de Supermaven es que utiliza la misma suscripción de ChatGPT, lo que lo convierte en una opción versátil y eficiente para desarrolladores que ya usan esta IA.

## Características destacadas de Supermaven:
- Compatibilidad con múltiples editores de código.
- Capacidad para modificar pruebas según el contexto que le proporciones.
- Soporte para autocompletar código y optimizar la generación de pruebas unitarias.

## ¿Cómo usar ChatGPT para generar y modificar pruebas?
ChatGPT es otra herramienta clave para generar pruebas. Al darle contexto sobre el código, como la clase BankAccount, puedes solicitar que modifique o cree pruebas unitarias parametrizadas, lo que simplifica aún más el proceso de validación. Esta interacción con la IA facilita la generación de pruebas más completas, incluyendo distintos casos de prueba como depósitos positivos y negativos.

## Proceso de uso de ChatGPT para pruebas:
- Proporciona el contexto del código.
- Pide que modifique o cree una prueba específica.
- Analiza y ejecuta el código generado para verificar su funcionalidad.

## ¿Cuáles son las precauciones al usar herramientas de inteligencia artificial para pruebas?
Es crucial recordar que, aunque estas herramientas son extremadamente útiles, no debes copiar y pegar código sin antes revisarlo. La IA utiliza grandes bases de datos de código, algunos de los cuales pueden contener errores o prácticas no recomendadas. Es importante que valides siempre el código generado antes de implementarlo en producción.

## Consejos para un uso adecuado:
- Revisa cuidadosamente cada sugerencia antes de integrarla a tu código.
- Asegúrate de que las pruebas cubran todos los casos posibles.
- Ajusta el código generado según las mejores prácticas de tu equipo o proyecto.

## ¿Qué otras buenas prácticas debes seguir al escribir pruebas unitarias?
Además de usar herramientas de IA, existen otras buenas prácticas que debes tener en cuenta al desarrollar pruebas unitarias:

Agrupa las pruebas por funcionalidad o clase.
Utiliza herramientas como coverage para verificar qué partes del código no han sido probadas.
Borra los comentarios generados automáticamente para mantener el código limpio.

## Lista de recursos útiles:
- Documentación de GitHub Copilot -> https://docs.github.com/es/copilot
- Supermaven API para ChatGPT     -> https://supermaven.com/
- Tutorial sobre TDD (Desarrollo Guiado por Pruebas)

[Video](../04_CursoUnitTestingPython/info/video_001.mov)


## Preguntas 

1.
¿Qué tipo de prueba se debe realizar para validar el correcto funcionamiento de componentes individuales del código?
Pruebas unitarias

2.
Si un sistema comienza a fallar cuando diferentes componentes interactúan, ¿qué tipo de prueba no fue efectiva?
Pruebas de integración

3.
Para verificar si el software cumple las expectativas del usuario final, ¿qué prueba debe realizarse?
Pruebas de aceptación

4.
¿Cómo puedes asegurarte de que todas las líneas de código están siendo cubiertas en las pruebas?
Utilizando Coverage

5.
¿Cuál es la ventaja principal de automatizar las pruebas con Python?
Detectar errores más rápido y en mayor cantidad

6.
¿Qué método en TestCase se utiliza para preparar los recursos antes de cada prueba?
setUp()

7.
¿Qué función se utiliza en una prueba unitaria para verificar que una excepción se lanza correctamente?
assertRaises()

8.
¿Qué comando se usa para obtener una salida más detallada al ejecutar las pruebas unitarias?
pytest -v

9.
¿Cuál es el propósito principal del método assertEqual en UnitTest?
Verificar que dos valores son iguales.

10.
¿Qué método utilizarías para comprobar si una variable es True?
assertTrue

11.
¿Qué método sería adecuado para verificar si un valor está dentro de una lista en UnitTest?
assertIn

12.
¿Cuál es el propósito principal del decorador @skip en una prueba unitaria?
Omitir temporalmente una prueba que aún no debe ejecutarse

13.
¿Cuál sería un buen nombre para una prueba de un método withdraw que reduce el saldo con un valor positivo?
test_withdraw_positive_amount_reduce_balance

14.
¿Cómo puedes ejecutar las pruebas de Doctest en un archivo Python?
Usando el comando python -m doctest nombre_archivo.py

15.
Si quieres analizar qué partes de tu código no han sido probadas, ¿qué deberías hacer?
Revisar el reporte HTML de Coverage

16. 
En una prueba unitaria con Python, si una función devuelve 5 pero se esperaba 7, ¿cómo se detectaría el error?
Usando assert para comparar el resultado esperado con el real

