## Curso de Patrones de Diseño y SOLID en Python

## Clase 1: Patrones de Diseño y Principios SOLID en Python para Procesadores de Pago
> El mundo del desarrollo de software ha evolucionado considerablemente en las últimas décadas gracias a dos pilares fundamentales: los patrones de diseño, que llevan 30 años organizando el caos del código, y los principios SOLID, que llevan 20 años haciendo la vida de los programadores más sencilla. Juntos, permiten construir sistemas más mantenibles, escalables y flexibles. En este curso, aprenderemos a aplicar ambos conceptos mientras desarrollamos un procesador de pagos en Python, mejorando el código a lo largo del proceso para crear una solución robusta y eficiente.

## ¿Por qué es importante aprender patrones de diseño y principios SOLID?
Los patrones de diseño y los principios SOLID ofrecen soluciones probadas a problemas comunes en el desarrollo de software. Aunque llevan décadas en uso, siguen siendo esenciales porque:

- Mejoran la mantenibilidad del código.
- Aumentan la flexibilidad y escalabilidad.
- Facilitan la implementación de pruebas, tanto unitarias como de integración.
- Optimizan el rendimiento del código.
- Mejoran la experiencia de desarrollo, haciéndolo más claro y ordenado.

## ¿Cómo aplicaremos los patrones de diseño y los principios SOLID?
A lo largo del curso, trabajaremos sobre una base de código inicial que no cumple con ninguno de los principios SOLID ni sigue patrones de diseño. Esto nos permitirá ver, de manera práctica, cómo transformar el código paso a paso. Usaremos Python para construir un sistema de procesamiento de pagos, aplicando mejoras incrementales entre cada lección, las cuales servirán como retos para que los estudiantes reflexionen y discutan en la sección de comentarios.


## Analogía

Imagina que estás construyendo algo con bloques LEGO. Los principios SOLID son como las reglas para construir estructuras de LEGO que sean fuertes, fáciles de cambiar y reutilizar. Cada letra de SOLID representa una de estas reglas. 

´´´python


´´´


## Clase 2-3-4: Principio de Responsabilidad Única en Desarrollo de Software

> S - Single Responsibility Principle (Principio de Responsabilidad Única):

## concepto 

Establecido por Robert C. Martin. Este principio indica que una clase o función debe tener solo una razón para cambiar, lo que mejora la mantenibilidad y reduce la complejidad. Implementarlo no solo facilita las pruebas unitarias, sino que también incrementa la reutilización del código y disminuye el acoplamiento

## Analogía
Piensa en un bloque de LEGO que solo hace una cosa. Por ejemplo, un bloque rojo de 2x4 solo es rojo y tiene ese tamaño. No intenta ser también una rueda o una antena.
En programación, esto significa que cada parte de tu código (una clase, una función) debería tener una sola razón para cambiar. Si una clase hace demasiadas cosas, cualquier cambio en una de esas cosas podría obligarte a cambiar la clase entera, ¡incluso si las otras cosas no se vieron afectadas!

## Programación 

En programación, esto significa que cada parte de tu código (una clase, una función) debería tener una sola razón para cambiar. Si una clase hace demasiadas cosas, cualquier cambio en una de esas cosas podría obligarte a cambiar la clase entera, ¡incluso si las otras cosas no se vieron afectadas. 


## ¿Cómo saber cuándo aplicar el principio de responsabilidad única?
- Múltiples razones para cambiar: Si una clase o función tiene varias razones para ser modificada, es un buen indicio de que tiene más responsabilidades de las que debería.

- Alta complejidad y difícil mantenimiento: Si se encuentra complicado añadir nuevas funcionalidades o corregir errores, es probable que la falta de una clara definición de responsabilidades esté afectando el código.

- Dificultad para realizar pruebas unitarias: Si preparar una prueba implica mucho trabajo o configurar demasiados elementos, es señal de que el principio no se está siguiendo correctamente.

- Duplicación de código: Si una funcionalidad, como una validación, está replicada en varios lugares, se debería extraer a una única función y reutilizarla donde sea necesario.


´´´python


´´´


## Clase 5-6: Principio Abierto-Cerrado en Desarrollo de Software

> O - Open/Closed Principle (Principio de Abierto/Cerrado):

## Concepto 

El principio abierto-cerrado (Open-Closed Principle) es clave para mantener la flexibilidad y estabilidad en el desarrollo de software, permitiendo que el código sea ampliado sin ser modificado. Este principio garantiza que el software pueda evolucionar de manera eficiente sin afectar las funcionalidades ya probadas

## ¿Qué es el principio abierto-cerrado?
El principio abierto-cerrado establece que el software debe estar abierto para su extensión pero cerrado para su modificación

## ¿Cuáles son los beneficios de aplicarlo?
Menos errores: al no tocar el código existente, se minimizan los errores derivados de cambios imprevistos.
Actualizaciones más rápidas: la extensión del software se vuelve más ágil, lo que es crucial cuando hay cambios constantes de requisitos en las empresas.
Estabilidad del sistema: el código probado y validado permanece inalterado, lo que facilita el desarrollo de nuevas funcionalidades sin riesgos.

## Analogía

Imagina que puedes añadir nuevas funcionalidades a tu construcción de LEGO sin tener que desmontar las partes que ya funcionan. Puedes agregar más bloques sin tocar los que ya están bien colocados

## En programación 

En programación, esto significa que tus módulos (clases, funciones) deberían estar abiertos para la extensión (puedes añadirles nuevas funcionalidades) pero cerrados para la modificación (no deberías tener que cambiar su código existente para hacer algo nuevo). Esto se logra a menudo usando interfaces o clases abstractas.




´´´python


´´´

## Clase 7 - 8: Principio de Sustitución de Liskov en Desarrollo de Software

> L - Liskov Substitution Principle (Principio de Sustitución de Liskov):

## Concepto 

Es clave para garantizar la coherencia y la interoperabilidad en sistemas orientados a objetos. Propone que las subclases deben ser intercambiables con sus clases base sin alterar el comportamiento esperado



## ¿Cómo se aplican las subclases en LSP?
Las subclases deben respetar el contrato de la clase base. Esto significa que:

- No se puede cambiar la firma de los métodos.
- No se deben agregar nuevos atributos que afecten la funcionalidad de los métodos existentes.
- La interfaz y los tipos deben mantenerse compatibles.

## Analogía 
Piensa en diferentes tipos de bloques de LEGO que encajan en el mismo lugar. Por ejemplo, un bloque rojo de 2x2 y un bloque azul de 2x2 ambos encajan en el mismo espacio sin causar problemas.

## En programación 
En programación, esto significa que si tienes una clase padre (como "Vehículo") y clases hijas (como "Coche" y "Bicicleta"), puedes usar cualquiera de las clases hijas en cualquier lugar donde esperabas la clase padre, y todo debería seguir funcionando correctamente. Si intentas usar una bicicleta donde esperabas un coche y falla (por ejemplo, intentas acelerar con un pedal que no existe), estás violando este principio.


## ¿Cuáles son los beneficios del principio de sustitución?
Reutilización del código: Las clases que cumplen con LSP pueden ser utilizadas en diferentes contextos sin modificaciones.
Compatibilidad de interfaces: Facilita que las clases puedan interactuar de forma coherente sin errores inesperados.
Reducción de errores en tiempo de ejecución: El código se mantiene predecible y coherente, disminuyendo la posibilidad de fallos imprevistos.


´´´python


´´´

## Clase 9 - 10:
> I - Interface Segregation Principle (Principio de Segregación de la Interfaz):


## Concepto 

Es clave en la construcción de software flexible y modular. Su enfoque evita que las clases dependan de interfaces que no necesitan, promoviendo la cohesión y disminuyendo el acoplamiento.

## ¿Qué establece el principio de segregación de interfaces?
Este principio dice que los clientes no deben depender de interfaces que no utilizan. En el caso de una impresora multifuncional, por ejemplo, esta debería implementar interfaces para imprimir y escanear por separado. Si solo imprime, no necesita la capacidad de escaneo, y viceversa.

## Analogía 
Imagina que tienes diferentes herramientas para construir con LEGO. No todas las herramientas son útiles para todos los tipos de bloques. Una herramienta para unir bloques grandes no te servirá para colocar piezas pequeñas.

## En programación 

En programación, esto significa que es mejor tener muchas interfaces pequeñas y específicas para diferentes propósitos, en lugar de una interfaz grande que obligue a las clases a implementar métodos que no necesitan. Si una clase solo necesita una o dos de las muchas funciones de una interfaz grande, no debería verse obligada a implementar las demás.

´´´python


´´´

## Clase 11 - 12 - 13 :
> D - Dependency Inversion Principle (Principio de Inversión de Dependencias):
## Concepto 
Es uno de los pilares en la construcción de software robusto, ya que busca disminuir la dependencia entre módulos de alto y bajo nivel, mejorando la flexibilidad y testabilidad del código. Este principio establece que tanto los módulos de alto como de bajo nivel deben depender de abstracciones, no de implementaciones concretas.

## Analogía
Imagina que en lugar de que un bloque específico se conecte directamente a otro bloque específico, ambos se conectan a una placa base estándar. Esto hace que sea más fácil cambiar los bloques individuales sin afectar la conexión general.

## En Programación 
En programación, esto significa que tus módulos de alto nivel (las partes importantes de tu aplicación) no deberían depender directamente de los módulos de bajo nivel (los detalles de implementación). Ambos deberían depender de abstracciones (interfaces o clases abstractas). Esto hace que tu código sea más flexible y fácil de probar, ya que puedes reemplazar los módulos de bajo nivel con diferentes implementaciones sin cambiar los módulos de alto nivel.



´´´python


´´´

## Clase 14: Introducción a los Patrones de Diseño de Software
> 

´´´python


´´´

## Clase 8:
> 

´´´python


´´´

## Clase 9:
> 

´´´python


´´´

## Clase 10:
> 

´´´python


´´´