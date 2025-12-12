# Curso de Estadística Computacional con Python🚀

> Domina la estadística computacional usando Python para analizar datos, realizar simulaciones y calcular probabilidades. Aprende a aplicar técnicas de inferencia estadística y a desarrollar simulaciones de Monte Carlo.

| Detalle | Información |
| :--- | :--- |
| **Publicado el** | 24 FEBRERO 2025 |
| **Profesor** | DAVID AROESTI  |
| **Fecha de Inicio** | 11/12/2025  |
| **Fecha de Fin** | 31/12/2025  |
| **Enlace** | https://platzi.com/cursos/programacion-estocastica/ |


---
<div align="center">
  <img src="image-2.png" alt="Global Certificate" width="50%" />
</div>


| Curso | Certificado |
| :--- | :---: |
| Curso de Estadística Computacional con Python | [Ver PDF](https://github.com/LeoSan/CursosBackendPython/blob/main/02_DesarrolloBackendPythonDjango_2025_Avanzado\05_CursoEstadisticaComputacionalPython\2025_CursoEstadisticaComputacionalPython_PLATZI.pdf) |

--- 

## CLASE 01: INTRODUCCIÓN 

**Objetivos**
● Aprender cuándo utilizar Programación
Dinámica y sus beneficios
● Entender la diferencia entre programas
deterministas y estocásticos
● Aprender a utilizar Programación Estocástica
● Aprender a crear simulaciones computacionales
válidas

## CLASE 02: Programación Dinámica: Optimización de Problemas con Memorización

> [El nombre] Programación Dinámica se escogió para esconder a patrocinadores gubernamentales el hecho que en realidad estaba haciendo Matemáticas. La frase Programación Dinámica es algo que ningún congresista puede oponerse. **Richard Bellman**


**PUNTOS CLAVES**

> Programación Dinámica
● Subestructura Óptima. Una solución global
óptima se puede encontrar al combinar
soluciones óptimas de subproblemas locales.
● Problemas empalmados. Una solución óptima
que involucra resolver el mismo problema en
varias ocasiones.


> Memoization
● La Memorización es una técnica para guardar
cómputos previos y evitar realizarlos
nuevamente.
● Normalmente se utiliza un diccionario, donde las
consultas se pueden hacer en O(1).
● Intercambia tiempo por espacio.


**¿Qué es la programación dinámica?**

La programación dinámica es un concepto indispensable en el mundo de las ciencias de la computación. A pesar de su nombre, el cual no refleja su verdadera esencia, es una técnica poderosa para optimizar ciertos tipos de problemas. La historia de su origen es peculiar: Richard Bellman acuñó este término en la década de 1950 para garantizar el financiamiento de sus investigaciones matemáticas, utilizando un nombre que sonara impresionante pero que, curiosamente, no está relacionado con el dinamismo. Sin embargo, su aplicación ha demostrado ser fundamental en la informática.

**¿Cómo funciona la programación dinámica?**

La programación dinámica se centra en problemas con una "subestructura óptima". Esto significa que la solución global óptima se puede alcanzar dividiendo el problema en partes más pequeñas, resolviendo cada una de manera óptima antes de combinarlas para obtener la solución total. Ejemplos de su aplicación incluyen:

- El problema del morral (Knapsack problem): Aquí se buscan soluciones óptimas en problemas cada vez más pequeños.

- La secuencia de Fibonacci: La solución se genera dividiendo el problema en partes más reducidas y encontrando soluciones para cada segmento menor.

- Las soluciones a estos problemas más pequeños se combinan para hallar una solución a la totalidad del problema.

**¿Qué es la memorización en programación dinámica?**

La memorización es crucial para hacer eficiente la programación dinámica. Se utiliza para evitar cálculos innecesarios al almacenar resultados de computaciones previas en una estructura de datos, como un diccionario, que nos permite acceder rápidamente a estos datos almacenados. He aquí algunos puntos clave sobre la memorización:

Optimización de tiempo: Al guardar los resultados en la memoria del sistema, se disminuyen significativamente los tiempos de cómputo.

Intercambio de tiempo por espacio: Este concepto es esencial en ciencias de la computación, donde al aumentar el uso del espacio de memoria, se reduce el tiempo necesario para la solución del problema.

Utilizando la memorización, se logra que los programas no repitan cálculos ya realizados, lo que resulta en la ejecución de programas mucho más rápidos y eficientes.

**¿Cuáles son las aplicaciones prácticas de la programación dinámica?**
La programación dinámica se aplica a una variedad de problemas, haciendo de su comprensión algo esencial para cualquier estudiante de informática. Con ejemplos amplios en algoritmos y optimización, continúa siendo un área fértil para el aprendizaje y la aplicación:

- Ordenación y búsqueda: Se utilizan técnicas para estructurar datos ordenadamente y búsquedas eficientes.

- Resolución de problemas matemáticos complejos: Desde la secuencia de Fibonacci hasta problemas de combinatoria, la programación dinámica ofrece formas eficientes de llegar a soluciones.

- Optimización de recursos: Eficiente en tareas de asignación de recursos y planificación.

- Aprovechar las técnicas de programación dinámica no solo refuerza la comprensión teórica, sino que potencia la capacidad de resolver problemas complejos de manera sistemática y optimizada.

**En conclusión, la programación dinámica y la memorización son conceptos que, aunque quizás intrincados en su origen, se revelan como herramientas esenciales en la caja de herramientas de cualquier ingeniero en informática. Su dominio abre puertas a la optimización de programas y algoritmos, culminando en soluciones eficientes e innovadoras. Continúa explorando estos conceptos para mejorar tu comprensión del fascinante mundo de las ciencias de la computación.**


![alt text](image.png)

## CLASE 03:  Optimización de Algoritmos con Programación Dinámica en Python


**¿Qué es la Programación Dinámica?**
La programación dinámica es una metodología de optimización que ahorra tiempo al intercambiar espacio. Utiliza la memorización para evitar cálculos repetidos al guardar los resultados de subproblemas que se pueden reutilizar. Esto es esencial en problemas donde hay muchas subestructuras comunes, como es el caso de la secuencia de Fibonacci.

**¿Cómo se implementa la secuencia de Fibonacci de forma recursiva?**
A pesar de ser sencilla de implementar, la solución recursiva a la secuencia de Fibonacci es ineficiente debido al cálculo repetido de los mismos subproblemas. El algoritmo recursivo es el siguiente:

```PYTHON

import sys
sys.setrecursionlimit(10002)

def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    n = int(input("Escoge un número: "))
    print(f"Fibonacci de {n} es {fibonacci_dinamico(n)}")    

```

> Recuerda programación algoritmica depende de la complegidad algoritmica ya que hay que saber a nivel de base que tipo de complejidad tiene el algoritmo.


**Dejo base de la complejidad algoritmica Complejidad Algorítmica (Big O Notation)**
![alt text](image-1.png)

"""
🟢 Zona Verde: P (Tiempo Polinómico - "Eficiente")
Estos son los algoritmos que las computadoras pueden resolver en un tiempo razonable, incluso con muchos datos.

- $O(1)$ - Constante: El mejor de todos. No importa si tienes 10 datos o 1 millón, toma el mismo tiempo.
Ejemplo: Acceder a un valor en un diccionario de Python o un array por su índice.

- $O(\log n)$ - Logarítmica: Muy rápido. El tiempo crece muy lentamente comparado con los datos.
Ejemplo: Búsqueda binaria (buscar una palabra en un diccionario físico abriendo por la mitad).

- $O(n)$ - Lineal: El tiempo crece proporcionalmente a los datos. Si duplicas los datos, duplicas el tiempo.
Ejemplo: Recorrer una lista con un bucle for simple.

- $O(n \log n)$: Un poco más lento que lineal, pero muy eficiente. Es el estándar para ordenar cosas.
Ejemplo: Los algoritmos de ordenamiento eficientes como Merge Sort o Quick Sort (lo que usa .sort() en Python).

- $O(n^2)$ - Cuadrática: El tiempo crece al cuadrado. Común en algoritmos "ingenuos".
Ejemplo: Un bucle for dentro de otro (bucles anidados). Común en ordenamiento burbuja.

- $O(n^3)$ y $O(n^k)$: Cúbica o Polinómica general. Bucles triples, cuádruples, etc. Sigue siendo "resoluble" (está en P), pero se vuelve lento rápido.


🔴 Zona Roja: NP (No Polinómico* / Intratable)
- Nota técnica: Aunque la imagen dice "NP", en este contexto visual se refiere a algoritmos que "No son Polinómicos" o que son Exponenciales/Factoriales. 
- Estos algoritmos son tan lentos que se vuelven inútiles si $n$ crece un poco (por ejemplo, si $n=100$, el programa podría tardar siglos).

- $O(2^n)$ - Exponencial: Por cada dato nuevo, el tiempo se duplica. Esto explota rapidísimo.
Ejemplo: Fibonacci Recursivo sin memoria (el que viste en tu README antes de optimizar). Calcular Fibonacci de 50 así podría tardar años.

- $O(n!)$ - Factorial: La peor pesadilla. Crece monstruosamente rápido.
Ejemplo: El problema del viajero (probar todas las rutas posibles entre ciudades). Si tienes 20 ciudades, es casi imposible de calcular a fuerza bruta.

""" 
## CLASE 04: Simulaciones con Caminos Aleatorios en Programación

**¿Cómo explicaron Einstein y el movimiento browniano esta teoría?**

Uno de los ejemplos más sorprendentes y fundamentales del uso de aleatoriedad es el movimiento browniano. En el siglo XIX, la mejora en los microscopios permitió observar comportamientos inesperados en partículas microscópicas que no podían ser explicados con el conocimiento de la época. Fue Albert Einstein el que explicó este fenómeno siendo un pionero en el uso de la aleatoriedad para entender cómo las moléculas de agua, al moverse aleatoriamente, impactan partículas de polen, generando lo que se conoce como movimiento browniano. Este descubrimiento le valió el Premio Nobel, no por su teoría de la relatividad, sino por este entendimiento profundo del comportamiento aleatorio a nivel molecular.

**¿Qué aplicaciones tienen los caminos aleatorios en las simulaciones?**
Los caminos aleatorios son la clave para crear simulaciones avanzadas y precisas en múltiples campos:

Simulación de partículas: Las simulaciones como la del humo, utilizan caminos aleatorios para modelar el comportamiento de millones de partículas. Mediante la definición de un comportamiento general, las partículas se mueven de manera aleatoria, reproduciendo el movimiento caótico del humo.

Unión de galaxias: A nivel macro, estas simulaciones ayudan a entender fenómenos astronómicos. Por ejemplo, la probable fusión de la galaxia Vía Láctea con Andrómeda es modelada usando caminos aleatorios, permitiendo prever el comportamiento de las estrellas y la gravedad involucradas.

Mercados financieros: En el ámbito económico, se utilizan para simular el comportamiento del mercado de valores, ayudando a predecir cómo las acciones pueden subir o bajar en el tiempo.

**¿Qué relación tienen con el arte y la tecnología?**
La aleatoriedad no se limita al ámbito científico, también se extiende a la creación artística:

Escultura de nube cuántica: Un ejemplo fascinante es el Quantum Cloud en Londres. Esta atracción turística utiliza caminos aleatorios computacionales para posicionar los elementos de la escultura, creando así una estructura singular que desafía las nociones tradicionales del arte.

```PYTHON


```
![alt text](image-3.png)

## CLASE 05: Camino Aleatorio en Programación Orientada a Objetos

**¿Qué es la programación dinámica y estocástica?**

La programación dinámica y estocástica es una técnica que se utiliza en el diseño de algoritmos para resolver problemas de optimización que se caracterizan por la incertidumbre y la necesidad de tomar decisiones secuenciales. Esta técnica es fundamental en la resolución de problemas en diversos campos como la ingeniería, la economía o las ciencias de la computación.

En este contexto, la profesora introduce un concepto interesante: el camino de borrachos. Descubramos cómo este concepto se materializa en un algoritmo de programación orientada a objetos.

**¿Cómo se implementa el camino de borrachos?**
El algoritmo del camino de borrachos se deriva de un problema que simula el movimiento aleatorio de un borracho que camina en un campo. Para entender cómo se desarrolla este concepto en programación, dividimos el problema en tres clases fundamentales:

Borracho: Un objeto que representa a una persona que se mueve de manera aleatoria.
Campo: Un objeto que define el entorno o mapa en el cual el borracho se mueve.
Coordenada: Un concepto abstracto que sirve para definir la posición dentro del campo.

**¿Cómo se representa a través de programación orientada a objetos?**
La programación orientada a objetos permite modelar el mundo real creando clases y objetos. En el caso del camino de borrachos, las clases mencionadas se configuran de la siguiente manera:

Borracho: Puede imaginarse como un individuo que se mueve dentro de las coordenadas de un campo. Además, se pueden extender sus características para definir comportamientos específicos, como un "borracho tradicional" que se mueve aleatoriamente a uno de los lados cardinales.

Campo: Funciona como un mapa y contiene las disposiciones de las coordenadas, permitiendo que el borracho se desplace dentro de él.

Coordenada: Es como un marcador que señala la posición actual del borracho dentro del campo, similar a un pin en Google Maps.

**¿Cómo se implementa el movimiento del borracho?**
El borracho se mueve aleatoriamente dentro del campo a través de movimientos en los ejes X e Y. Estos movimientos pueden ser:

Hacia la izquierda: decremento en el eje X.
Hacia la derecha: incremento en el eje X.
Hacia arriba: incremento en el eje Y.
Hacia abajo: decremento en el eje Y.
Aquí les presento un fragmento del código en Python:

class Borracho:
    def __init__(self):
        pass

    def mover(self):
        return random.choice([(1,0), (0,1), (-1,0), (0,-1)])

class Campo:
    def __init__(self):
        pass
¿Cómo se integran estas clases en la función principal?
Para concretar el comportamiento del borracho y sus desplazamientos, es necesario definir una función principal o main, un punto de entrada común en la mayoría de los lenguajes de programación:

if __name__ == '__main__':
    # Implementación del movimiento del borracho
    # Código para crear instancias de las clases e interactuar con ellas
El main se encarga de gestionar el flujo del programa: crear objetos, iniciar movimientos y registrar resultados. Se pueden implementar simulaciones para ver cómo varía la posición del borracho tras un número determinado de pasos.

¿Cómo se evalúan los resultados de las simulaciones?
En programación estocástica, ejecutar una simulación una sola vez no proporciona suficiente información debido a su componente aleatorio. Por ello, es necesario realizar múltiples simulaciones para obtener resultados promedio más fiables.

Simulaciones Múltiples: Es importante ejecutar varias simulaciones (por ejemplo, 100) para cada número de pasos definido, obteniendo así la media de las distancias recorridas.

Distancias Máxima y Mínima: Evaluar la distancia máxima y mínima alcanzada por el borracho en las distintas simulaciones proporciona insights sobre el comportamiento y alcance de los movimientos.


```PYTHON
import random

class Borracho:

    def __init__(self):
        self.posicion = [0,0]


    def camino_borrachos(self, pasos=0):
        direccion = random.choice(["derecha","izquierda","arriba","abajo"])
        for i in range(pasos):
            direccion = random.choice(["derecha", "izquierda", "arriba", "abajo"])
            if direccion == "izquierda":
                self.posicion[0] -= 1
            elif direccion == "derecha":
                self.posicion[0] += 1
            elif direccion == "arriba":
                self.posicion[1] += 1
            elif direccion == "abajo":
                self.posicion[1] -= 1
            else:
                return None
        return self.posicion

if __name__ == "__main__":
    borrachin = Borracho()
    direccion_final = borrachin.camino_borrachos(pasos=500)
    print(direccion_final)
    distancia_final = (direccion_final[0]**2+direccion_final[1]**2)**0.5
    print("La distancia final es: ",distancia_final)

```

![alt text](image-2.png)

## CLASE 06: 
```PYTHON


```


## CLASE 07: 

```PYTHON


```

## CLASE 08: 

```PYTHON


```

## CLASE 09: 
```PYTHON


```


## CLASE 10: 

```PYTHON


```

## CLASE 11: 

```PYTHON


```

## CLASE 12: 



```PYTHON


```


## CLASE 13: 
```PYTHON


```


## CLASE 14: 

```PYTHON


```

## CLASE 15: 

```PYTHON


```

## CLASE 16: 


```PYTHON


```
## CLASE 17: 
```PYTHON


```


## CLASE 18: 

```PYTHON


```

## CLASE 19: 

```PYTHON


```

## CLASE 20: 
```PYTHON


```