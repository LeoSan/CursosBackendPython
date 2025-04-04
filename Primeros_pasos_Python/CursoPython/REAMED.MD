## Curso Python 

> Lugar: Platzi 
> Fecha: 01 Abril 2025 
> Profesora: 

## Clase 1: Instalación Python 

# Instalación de Python en Windows y macOS

Esta guía te llevará a través del proceso de instalación de Python en sistemas operativos Windows y macOS.

## Instalación en Windows

**Paso 1: Descargar el Instalador de Python**

1.  Abre tu navegador web y ve al sitio oficial de Python: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2.  Busca la última versión estable de Python 3. Haz clic en el enlace correspondiente para descargar el instalador (generalmente un archivo `.exe`). Asegúrate de descargar la versión para Windows.

**Paso 2: Ejecutar el Instalador**

1.  Una vez que la descarga se complete, localiza el archivo `.exe` en tu carpeta de Descargas (o la ubicación donde guardaste el archivo).
2.  Haz doble clic en el archivo `.exe` para ejecutar el instalador.

**Paso 3: Configurar la Instalación**

1.  En la primera pantalla del instalador, asegúrate de marcar las siguientes casillas:
    * **"Add Python X.Y to PATH"** (donde X.Y es la versión de Python que estás instalando). Esto es crucial para poder ejecutar Python desde la línea de comandos.
    * **"Install launcher for all users (recommended)"** (opcional, pero recomendado).
2.  Haz clic en **"Install Now"** para iniciar la instalación con la configuración predeterminada, o en **"Customize installation"** si deseas cambiar la ubicación de instalación o instalar componentes específicos. Para la mayoría de los usuarios, "Install Now" es suficiente.

**Paso 4: Esperar la Finalización de la Instalación**

1.  Windows mostrará una barra de progreso mientras se instalan los componentes de Python. Espera a que el proceso se complete.

**Paso 5: Verificar la Instalación**

1.  Abre el **Símbolo del sistema** (puedes buscar "cmd" en el menú Inicio).
2.  Escribe el siguiente comando y presiona Enter:
    ```bash
    python --version
    ```
3.  Si Python se instaló correctamente, deberías ver la versión de Python que instalaste (por ejemplo, `Python 3.X.Y`).
4.  También puedes probar el intérprete de Python escribiendo `python` y presionando Enter. Esto abrirá la consola interactiva de Python (indicada por `>>>`). Para salir, escribe `exit()` y presiona Enter.

## Instalación en macOS

**Paso 1: Descargar el Instalador de Python**

1.  Abre tu navegador web y ve al sitio oficial de Python: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2.  Busca la última versión estable de Python 3. Haz clic en el enlace correspondiente para descargar el instalador (generalmente un archivo `.pkg`). Asegúrate de descargar la versión para macOS.

**Paso 2: Ejecutar el Instalador**

1.  Una vez que la descarga se complete, localiza el archivo `.pkg` en tu carpeta de Descargas (o la ubicación donde guardaste el archivo).
2.  Haz doble clic en el archivo `.pkg` para ejecutar el instalador.

**Paso 3: Seguir las Instrucciones del Instalador**

1.  macOS te guiará a través de una serie de pantallas. Lee cada una cuidadosamente y haz clic en **"Continuar"** (Continue).
2.  Se te pedirá que aceptes los términos de la licencia. Haz clic en **"Aceptar"** (Agree).
3.  Puedes elegir la ubicación de instalación o dejar la predeterminada. Haz clic en **"Instalar"** (Install).
4.  Es posible que se te pida tu contraseña de administrador para permitir la instalación. Ingresa tu contraseña y haz clic en **"Instalar Software"** (Install Software).

**Paso 4: Esperar la Finalización de la Instalación**

1.  macOS mostrará una barra de progreso mientras se instalan los componentes de Python. Espera a que el proceso se complete.
2.  Una vez finalizada la instalación, puedes cerrar la ventana del instalador.

**Paso 5: Verificar la Instalación**

1.  Abre la aplicación **Terminal** (puedes encontrarla en Aplicaciones > Utilidades o buscándola con Spotlight).
2.  Escribe el siguiente comando y presiona Enter:
    ```bash
    python3 --version
    ```
    * **Nota:** En macOS, la versión preinstalada de Python 2 todavía puede estar presente. Por eso, es importante usar `python3` para referirte a la versión 3 que acabas de instalar.
3.  Si Python 3 se instaló correctamente, deberías ver la versión de Python que instalaste (por ejemplo, `Python 3.X.Y`).
4.  También puedes probar el intérprete de Python 3 escribiendo `python3` y presionando Enter. Esto abrirá la consola interactiva de Python 3 (indicada por `>>>`). Para salir, escribe `exit()` y presiona Enter.


## clase 2: 

## Semántica y Sintaxis en Programación: Breve Descripción con Ejemplos

En programación, la **sintaxis** y la **semántica** son dos conceptos fundamentales que describen cómo se escribe y qué significa el código.

**Sintaxis:**

* Se refiere a las **reglas gramaticales** que definen la estructura correcta de un lenguaje de programación. Es como la ortografía y la gramática del lenguaje humano.
* Si la sintaxis es incorrecta, el compilador o intérprete **no podrá entender el código** y generará errores.
* Se centra en la **forma** en que se escriben los símbolos, las palabras clave y las estructuras del lenguaje.

**Ejemplo de Sintaxis (Python):**

```python
# Sintaxis correcta:
if edad > 18:
    print("Es mayor de edad")

# Sintaxis incorrecta (falta el colon al final del if):
# if edad > 18
#     print("Es mayor de edad") # Esto generará un error de sintaxis
```

**Semántica:**

* Se refiere al significado del código. Describe qué hace el programa cuando se ejecuta.
* Un código puede tener una sintaxis correcta pero una semántica incorrecta, lo que significa que el programa se ejecutará sin errores pero no hará lo que se esperaba.
* Se centra en la lógica y el comportamiento del programa.


## Clase 5: Manipulación de Cadenas de Texto en Python

**¿Cómo se definen las cadenas en Python?**
Para crear una cadena en Python, puedes utilizar comillas simples, dobles o triples. Por ejemplo:

```python
Comillas simples: name = 'Carli'
Comillas dobles: name = "Carli"
Comillas triples: name = '''    Carli''' -> si permite anexar espacios 
```

**¿Cómo se indexan las cadenas en Python?**
Las cadenas son colecciones ordenadas y accesibles por índices. Puedes acceder a un carácter específico utilizando corchetes:

```python
name = 'Carli'
print(name[0])  # Imprime 'C'
print(name[-1])  # Imprime 'i'
```

**¿Cómo se concatenan cadenas?**
Puedes concatenar cadenas utilizando el operador + y repetirlas con el operador *:

```python
first_name = 'Carli'
last_name = 'Florida'
full_name = first_name + ' ' + last_name
print(full_name)  # Imprime 'Carli Florida'

print(name * 5)  # Imprime 'CarliCarliCarliCarliCarli'
```

**metodos  definidas** 
- len()
- .count() 
- .capitalize()
- .title() 
- .swapcase() 
- .replace(,) 
- .split() 
- .strip() 
- .lstrip() 
- .rstrip() 
- .find()
- .index() 
- eval() # Este y el siguiente son super métodos
- .exec()

## Clasee 6: Enteros, Flotantes y Booleanos


**Tipos de datos**

- Enteros: Son todos los números enteros. Se representa con la palabra Integer (INT)
- Flotantes: Son todos los números decimales. Se representa con la palabra FLOAT
- Booleanos: Representa verdadero (true) o falso (false).


**¿Qué es un tipo de dato en Python?**
En Python, un tipo de dato se refiere a la clase de datos que una variable puede contener. Esto se puede verificar con la función type(), que devuelve la clase del valor contenido en la variable. Por ejemplo, type('Hello') devuelve class 'str', indicando que el dato es una cadena de texto.

**¿Cómo se utiliza la notación científica en Python?**
La notación científica se emplea para representar números muy grandes o muy pequeños de manera compacta. Por ejemplo, 1e6 representa 1,000,000 y 1e-6 representa 0.000001. Esta notación es útil en cálculos científicos y financieros, donde los números pueden variar significativamente en magnitud.

La notación cientifica (exponencial) se utiliza cuando tenemos números muy grandes o muy pequeños y se utiliza con la nomenclatura e o E.

Para comentar en Python se comienza el texto con # y automaticamente se coloca de color verde indicando que Python ignora esta sentencia.

El typecasting en Python se refiere a la conversión explícita de un tipo de dato a otro. Por curiosidad los invito a que lo intente.

Acá les comparto unos cuantos ejemplos:

```python
# Typecasting

print(float(2))
print(int(2.6))
print(int(True))
print(int(False))
print(bool(1))
print(float(True))
print(type("hello" == "world"))
```

## Clase 7: Todo lo que Debes Saber sobre print en Python

Esta información es Oro!

No haré resumen, pero si quizás los usos más importantes que te servirán a nivel laboral. :).

Sep: Te puede ayudar para la construcción de archivos planos en caso de que necesites que la salida tenga algún separador especial: Ej: print("Nunca", "pares", "de", "aprender", sep="; ")

```python
## Separadores 
print("manzana", "banana", "naranja", sep="-")
print(1, 2, 3, sep=", ")

## Especificar el final de línea (end):
## Por defecto, print() añade un salto de línea (\n) al final de la salida. Puedes cambiar este comportamiento utilizando el parámetro end.

print("Esto se imprime en", end=" ")
print("la misma línea.")

for i in range(5):
    print(i, end=", ")
print("fin")

## Usar cadenas formateadas (f-strings):
## Las f-strings (disponibles desde Python 3.6) son una forma concisa y legible de insertar expresiones dentro de cadenas de texto. Se definen prefijando la cadena con una f o F y colocando las expresiones entre llaves

nombre = "Carlos"
puntuacion = 95
print(f"El estudiante {nombre} obtuvo una puntuación de {puntuacion}.")
print(f"El doble de {puntuacion} es {puntuacion * 2}.")

# Usar el método .format():
# El método .format() también permite formatear cadenas, aunque es un poco más verboso que las f-strings.

nombre = "Laura"
profesion = "ingeniera"
print("Mi nombre es {} y soy {}.".format(nombre, profesion))
print("El número {0} al cuadrado es {1}.".format(5, 5**2)) # Usando índices
print("Nombre: {n}, Edad: {e}".format(n="Pedro", e=25)) # Usando nombres de clave

## combinaciones 

productos = ["manzana", "plátano", "uva"]
print("Lista de productos:", *productos, sep=", ", end=".\n¡Gracias!")
```

## Clase 8:  Operaciones Matemáticas en Python

En el mundo de la programación con Python, las operaciones matemáticas básicas como la suma, resta, multiplicación y división son fundamentales. Sin embargo, Python ofrece operaciones adicionales que expanden nuestras posibilidades.


PEMDAS es unaregla que indica el orden correcto de operaciones en una expresión matemática. Es una abreviación de las palabras en inglés "Parentheses" (paréntesis), "Exponents" (exponentes), "Multiplication" (multiplicación), "Division" (división), "Addition" (suma) y "Subtraction" (resta).

Gente corriganme si estoy mal, pero según yo recuerdo el acrónimo PEMDAS es:

P -> Paréntesis

E -> Exponenciación

M -> Multiplicación

D -> División

A -> Adición

S -> Sustracción

```python
#Operadores numéricos
a = 10
b = 10
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print("Parte entera de la división:", a // b)
print("Módulo:", a % b)
a /= 2
print(a)
operation_1  = 2 + 3 * 4
operation_2  = (2 + 3) * 4
print(operation_1)
print(operation_2)
operation_3 = (2+3) * (4**2)/ 8 - 1
print(operation_3)

a = 10
b = 3
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
```

## Clase 9 Operaciones de Entrada/Salida en Consola


En Python, cuando trabajamos con proyectos que requieren interacción del usuario, es común solicitar datos como correo o contraseña para ejecutar acciones específicas. Este mismo enfoque es útil para entender la función input.

**¿Cómo se recibe información del usuario en Python?**
Para recibir información del usuario desde la consola, creamos una variable y asignamos el resultado de la función input. Por ejemplo, para pedir el nombre del usuario:
```python
nombre = input("Ingrese su nombre: ")
print(nombre)
```
Al ejecutar este código, se habilita una sección para introducir información. Ingresamos un nombre, presionamos Enter y se imprime el valor guardado en la variable nombre.

**¿Qué ocurre si eliminamos la función print?**
Si eliminamos print y ejecutamos el código, el nombre ingresado no se mostrará en la consola:

nombre = input("Ingrese su nombre: ")
Para ver el resultado, es imprescindible usar print.

Podemos solicitar la edad del usuario creando una variable edad y utilizando input, luego imprimimos ambos valores:
```python
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(nombre)
print(edad)
```
Al ejecutar, ingresamos el nombre y la edad, y ambos valores se muestran en pantalla.

**¿Cuál es el tipo de dato devuelto por input?**
El resultado de input es siempre un string, incluso si ingresamos un número. Podemos verificar el tipo de dato usando type:

```python
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
print(type(name))
print(type(age))
```
Al ejecutar, se mostrará que ambos valores son de tipo str.

**¿Cómo se convierte el tipo de dato (casting)?**
Si queremos que la edad sea un número entero en lugar de un string, usamos el casting:
```python
age = int(input("Ingrese su edad: "))
#Ejecutamos y verificamos que age ahora es un entero. También podemos convertir a otros tipos de datos, como flotantes:

age = float(input("Ingrese su edad: "))
```
**¿Qué sucede si ingresamos un dato inesperado?**
Si el código espera un entero, pero ingresamos un string, se produce un ValueError. Es importante manejar el tipo de datos correctamente para evitar errores


## Clase 10: Lista 

Una lista en Python es una colección ordenada de elementos que puede contener elementos de diferentes tipos (enteros, flotantes, cadenas, etc.). Las listas son mutables, lo que significa que sus elementos se pueden cambiar después de que se ha creado la lista.


```python

# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos
print("\nAcceso a elementos")
print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# Modificar elementos
print("\nModificar elementos")
lista_numeros[0] = 10
print("Lista de números modificada:", lista_numeros)

# Agregar y eliminar elementos
print("\nAgregar y eliminar elementos")
lista_numeros.append(6)
print("Lista después de append:", lista_numeros)
lista_numeros.insert(2, 99)
print("Lista después de insert:", lista_numeros)
lista_numeros.remove(99)
print("Lista después de remove:", lista_numeros)
ultimo = lista_numeros.pop()
print("Elemento eliminado con pop:", ultimo)
print("Lista después de pop:", lista_numeros)
elemento = lista_numeros.pop(1)
print("Elemento eliminado en la posición 1:", elemento)
print("Lista después de eliminar en la posición 1:", lista_numeros)

# Operaciones básicas
print("\nOperaciones básicas")
lista_concatenada = lista_numeros + lista_mixta
print("Lista concatenada:", lista_concatenada)
lista_repetida = lista_numeros * 2
print("Lista repetida:", lista_repetida)
print("¿Está 3 en la lista?", 3 in lista_numeros)
print("Longitud de la lista:", len(lista_numeros))

# Iteración sobre los elementos de una lista
print("\nIteración sobre elementos de la lista")
for elemento in lista_numeros:
    print(elemento)

# Salida final
print("\nGracias por utilizar el programa de listas. ¡Hasta la próxima!")
```

## Clase 11:  Método slice

Cuando asignamos una lista a una nueva variable, por ejemplo, B = A, no estamos creando una copia independiente. Ambas variables apuntan al mismo espacio de memoria. Así, cualquier cambio en A se reflejará en B.

¿Cómo evitar que dos listas apunten al mismo espacio de memoria?
Para evitar que dos variables apunten al mismo espacio de memoria, debemos crear una copia superficial de la lista original usando slicing. Por ejemplo:

Crear una lista A con números del 1 al 5.
Asignar B = A y luego imprimir ambas listas muestra que ambas son idénticas.
Eliminar un elemento de A también lo elimina de B


```python

a = [1,2,3,4]
b = a

print(id(a))
print(id(b)) ## Imprimer mismo espacio de memoria asignado si alteras b se altera a 

#Para esto podemos aplicar slice o copy 

#Ejemplo Slice 
c = a[:]
c = a.copy()
print(id(c))

# Lista de ejemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplos de slicing
sublista1 = lista[2:5]
sublista2 = lista[:4]
sublista3 = lista[5:]
sublista4 = lista[::2]
sublista5 = lista[1:7:2]

# Slicing con índices negativos
sublista6 = lista[-5:]
sublista7 = lista[:-5]
sublista8 = lista[-8:-2:2]

```

## Notas 

- validar espacio de memorai print(id(a))

**¿Por qué es importante entender la asignación de memoria en listas?**
En Python, a diferencia de otros lenguajes, podemos almacenar diferentes tipos de datos en una colección. Entender cómo funciona la memoria es crucial para evitar errores en el código, especialmente en aplicaciones del mundo laboral.


## Clase Listas de más dimensiones y Tuplas

Las matrices en Python son una herramienta poderosa que permite organizar datos en listas de listas, facilitando su manejo y manipulación.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for row in matrix:
    for element in row:
        print(element)

```

**¿Cuál es la diferencia entre matrices y tuplas?**
A diferencia de las matrices, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. Las tuplas se utilizan para almacenar datos que no deben cambiar.

```python
# Ejemplo de tupla:
numbers = (1, 2, 3)
# Intentar modificar una tupla genera un error:
numbers[0] = 10  # Genera TypeError: 'tuple' object does not support item assignment


```

## Notas Mentales 
- Recuerda Leo, existen Listas, Diccionarios y Tuplas
- Las Listas [] es un conjunto de datos distintos ordenados o no ordenados 
- Los diccionarios [] es un conjunto variado de datos solo que tiene un key para indentificarlos 
- Las Tuplas () es un conjunto de datos inmutble 
