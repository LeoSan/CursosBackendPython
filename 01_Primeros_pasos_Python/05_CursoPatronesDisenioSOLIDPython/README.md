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
> Los patrones de diseño son soluciones reutilizables para problemas comunes en el desarrollo de software. Imagina los patrones de diseño como recetas culinarias: cada patrón es como una receta que se aplica en condiciones específicas para resolver un problema recurrente en la programación. Surgieron del libro "Design Patterns", escrito por cuatro autores conocidos como "La Banda de los Cuatro". Estos autores clasificaron 23 patrones en tres categorías distintas: creacionales, estructurales y de comportamiento. Al igual que los principios SOLID, los patrones de diseño facilitan la creación de un código más mantenible y reutilizable y ayudan a establecer un lenguaje común entre los desarrolladores.

## ¿Cuáles son los patrones de diseño creacionales?
Los patrones creacionales se centran en la creación de instancias de objetos, especialmente cuando una clase es compleja de instanciar debido a sus múltiples atributos o condiciones previas a su creación. Hay cinco patrones de diseño creacionales destacados:

- Singleton: Garantiza que una clase tenga solo una instancia y proporciona un punto de acceso global a ella.
- Factory Method: Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar.
- Abstract Factory: Ofrece una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas.
- Builder: Separa la construcción de un objeto complejo de su representación, permitiendo crear diferentes tipos de objetos con el mismo proceso.
- Prototype: Permite copiar instancias existentes sin depender de sus clases.

## ¿Qué son los patrones de diseño estructurales?
Los patrones de diseño estructurales están enfocados en la composición efectiva y escalable de clases y objetos. Proveen soluciones para estructurar tus clases de manera que maximicen la eficiencia y escalabilidad. Los siete patrones estructurales clave son:

- Adapter: Permite que interfases incompatibles trabajen juntas.
- Bridge: Desacopla una abstracción de su implementación para que ambas puedan variar independientemente.
- Composite: Permite componer objetos en estructuras de árbol para representar jerarquías parte-todo.
- Decorator: Añade nuevas funcionalidades a un objeto de manera dinámica.
- Facade: Simplifica la interfaz de un conjunto de clases.
- Flyweight: Usa compartición para soportar de manera eficiente grandes cantidades de objetos.
- Proxy: Proporciona un sustituto o marcador de posición para controlar el acceso a otros objetos.

## ¿Cómo ayudan los patrones de diseño de comportamiento?
Los patrones de diseño de comportamiento abordan la comunicación y asignación de responsabilidades entre objetos, facilitando la interacción entre clases de distintas naturalezas. Entre los 11 patrones de comportamiento propuestos, algunos de los más destacados son:

- Observer: Permite a un objeto notificar a otros objetos sobre cambios en su estado.
- Strategy: Define una familia de algoritmos, encapsula cada uno, y los hace intercambiables.
- Command: Encapsula una solicitud como un objeto, permitiendo parametrizar a los clientes con diferentes solicitudes.
- Iterator: Proporciona una manera de acceder secuencialmente a elementos de un objeto agregado sin exponer su representación subyacente.
- Mediator: Define un objeto que encapsula cómo interactúan un conjunto de objetos.
- State: Permite a un objeto alterar su comportamiento cuando su estado interno cambia.
- Visitor: Permite definir nuevas operaciones sobre objetos de una estructura objeto sin cambiar las clases de los elementos sobre los cuales opera.


´´´python


´´´

## Clase 8:
> 

## Notas mentales : 
- Hacer ejerciios en python para los siguientes patrones: 

- Patron de creación 
    - Siglentom
    - Factory 

- Patron de Estructural 
    - Adapter 
    - facade

- Patron Comportamiento 
    - Estrategy 
    - Observer

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

## Sección de  Preguntas 

1.
Si encuentras que una clase en tu proyecto de Python tiene múltiples razones para cambiar, ¿qué principio de diseño deberías aplicar para mejorar su estructura?
Aplicar el Principio de Inversión de Dependencias (DIP) para depender de abstracciones en lugar de concreciones.
REPASAR

2.
Si tienes una clase base 'Animal' con un método 'hacer_sonido', y una subclase 'Perro' que hereda de 'Animal', ¿qué debe garantizar la subclase 'Perro' para cumplir con el Principio de Sustitución de Liskov?
La subclase 'Perro' debe implementar 'hacer_sonido' sin cambiar su firma.

3.
Si una subclase requiere un parámetro adicional en un método que ya existe en la clase base, ¿qué principio de diseño se está violando?
Se está violando el Principio de Sustitución de Liskov.

4.
Cuando una interfaz tiene demasiados métodos y no todas las clases que la implementan utilizan todos esos métodos, ¿qué acción deberías considerar para mejorar la cohesión y reducir el acoplamiento?
Segregar la interfaz en interfaces más pequeñas

5.
En un sistema donde los módulos de alto nivel dependen de los módulos de bajo nivel, ¿qué problema podrías enfrentar al intentar realizar cambios en el sistema?
Dificultades para intercambiar implementaciones sin afectar al sistema principal debido al alto acoplamiento.

6.
Si deseas implementar el principio de inversión de dependencias en un servicio de pagos, ¿qué patrón de diseño sería más adecuado para evitar que la clase de alto nivel dependa de la creación de clases de bajo nivel?
Patrón Strategy
Patrón Decorator
REPASAR

7.
Al aplicar el principio de inversión de dependencias, ¿cuál es la principal ventaja de hacer que la clase de alto nivel dependa de interfaces en lugar de implementaciones concretas?
Facilita la modificación y prueba del código

8.
¿Cómo podrías aplicar el principio de responsabilidad única para reestructurar un archivo de código que contiene múltiples clases relacionadas con el procesamiento de pagos?
Identificando y separando las clases en módulos específicos según su contexto y responsabilidad.

9.
¿Cuál sería el patrón de diseño más adecuado para simplificar la creación de instancias de objetos complejos en un sistema de gestión de usuarios?
Patrón de diseño creacional

10.
Si quisieras mejorar la comunicación entre diferentes clases en un sistema de reservas, ¿qué tipo de patrón de diseño deberías considerar?
Patrón de diseño de comportamiento

11.
¿En qué situaciones sería más beneficioso aplicar el patrón de diseño estrategia en lugar de estructuras condicionales tradicionales?
Cuando hay cambios frecuentes en los algoritmos o se necesita elegir dinámicamente entre diferentes soluciones.

12.
Si quisieras implementar un sistema de pagos que permita cambiar el método de procesamiento en tiempo de ejecución, ¿qué patrón de diseño sería el más adecuado?
El patrón de diseño estrategia, ya que permite intercambiar algoritmos de manera flexible.

13.
Al implementar el patrón estrategia, ¿cuál es la función principal de las interfaces o protocolos en Python?
Permitir que las clases de bajo nivel implementen diferentes algoritmos sin que la clase de alto nivel dependa de sus implementaciones específicas.

14.
Si estás diseñando un sistema de notificación que debe cambiar su comportamiento en función de la disponibilidad de información de contacto, ¿cómo implementarías el patrón de estrategia para seleccionar el notificador adecuado?
Implementando un método que permita cambiar el notificador en tiempo de ejecución según la información disponible.

15.
Si deseas agregar funcionalidades a un objeto en tiempo de ejecución sin modificar su estructura original, ¿cuál sería la mejor estrategia a seguir?
Utilizar el patrón decorador para añadir responsabilidades dinámicamente.

16.
Al aplicar el patrón decorador, ¿qué importancia tiene definir un protocolo para el servicio original y los decoradores?
Es crucial para asegurar que tanto el servicio original como los decoradores implementen la misma interfaz, permitiendo así una integración fluida.

17.
Si quisieras construir un objeto complejo en Python y deseas que su creación sea flexible y escalable, ¿qué patrón de diseño deberías aplicar?
Patrón Builder

18.
¿Qué patrón de diseño se debe aplicar para construir un objeto con múltiples configuraciones opcionales y cómo se implementaría en Python?
Se debe aplicar el patrón Builder, creando una clase Builder que contenga métodos para establecer cada atributo opcional y un método build para crear la instancia final.

19.
Si tuvieras que diseñar un sistema de notificación para un servicio de pagos, ¿qué componente del patrón Observer sería esencial para gestionar las suscripciones?
Una clase manager que maneje los listeners y sus notificaciones.

20.
¿Cómo implementarías un sistema que notifique a diferentes componentes sobre el estado de un pago (exitoso o fallido) utilizando el patrón Observer en Python?
Definiendo una interfaz de listener con un método notify y gestionando los listeners en un manager.

21.
En el contexto del patrón Observer, si un listener no está suscrito al manager, ¿qué sucederá cuando se notifique un evento de pago?
El manager lanzará un error al intentar notificar.
El evento se perderá y no se notificará a ningún listener.
REPASAR

22.
Si decides implementar un nuevo validador en tu cadena de responsabilidad, ¿qué sería lo primero que deberías hacer para asegurar que funcione correctamente dentro del patrón?
Definir una interfaz o clase abstracta para los manejadores

23.
Al diseñar un sistema que valide información antes de procesar un pago, ¿qué patrón de diseño sería más efectivo para manejar múltiples validaciones de manera ordenada?
Cadena de Responsabilidades

24.
Si deseas mejorar la mantenibilidad de tu código en Python, ¿qué principio SOLID deberías aplicar para asegurar que una clase tenga una única responsabilidad?
Principio de Responsabilidad Única (SRP)

25.
Si necesitas que tu código sea flexible y fácil de extender, ¿cuál de los principios SOLID te ayudaría a evitar dependencias rígidas entre clases?
Principio Abierto/Cerrado (OCP)
Principio de Sustitución de Liskov (LSP)
REPASAR 

26. 
Al implementar el patrón Observer, ¿qué método es crucial en la interfaz listener para recibir actualizaciones de eventos?
Un método update que reciba un evento como parámetro.

27.
Al reestructurar un código que implementa el principio de inversión de dependencias, ¿qué deberías considerar al definir las clases de alto y bajo nivel?
Asegurarte de que las clases de alto nivel dependan de interfaces y no de implementaciones concretas.

28. 
¿En qué situaciones sería más beneficioso implementar el patrón Observer en un sistema de eventos?
Cuando un cambio en un objeto debe notificar a múltiples objetos interesados.

29.
Al implementar el método build en un Builder, ¿qué validaciones son necesarias para asegurar que se puede crear la instancia del servicio de pagos?
Es necesario validar que todos los atributos requeridos estén presentes y no sean None antes de crear la instancia del servicio de pagos.

30. 
Si necesitas agregar una nueva funcionalidad a un sistema sin modificar el código existente, ¿qué principio de diseño deberías aplicar?
El principio Open/Closed

31. 
Si tienes una clase que implementa múltiples comportamientos, como imprimir y escanear, pero solo necesitas uno de ellos, ¿qué principio de diseño deberías aplicar para evitar que la clase esté obligada a implementar métodos innecesarios?
Principio de Segregación de Interfaces (ISP)


32. 
Si tienes un objeto base y deseas extender su funcionalidad mediante decoradores, ¿cuál es el primer paso que debes realizar?
Definir una interfaz o clase abstracta que describa el comportamiento del objeto base.

33. 
Al diseñar un sistema de procesamiento de pagos, ¿qué patrón de diseño sería más adecuado para permitir la adición de nuevos métodos de pago sin modificar el código existente?
Patrón de Estrategia

34. 
Si decides modificar una interfaz que afecta a muchas clases, ¿qué principio de diseño te ayudaría a minimizar el impacto de esos cambios en el resto del sistema?
Principio de Inversión de Dependencias (DIP)

35. 
¿Cómo podrías aplicar el principio abierto/cerrado para añadir un nuevo método de notificación sin modificar el código existente?
Añadir el nuevo método de notificación dentro de la clase existente de notificación por email.
REPASAR 


36.
Cuando se necesita combinar múltiples comportamientos de forma flexible en un objeto, ¿qué patrón de diseño es más adecuado?
El patrón decorador, ya que permite componer comportamientos adicionales.

37. 
Si decides usar el patrón Builder para crear un objeto, ¿qué aspecto es crucial para asegurar que el proceso de construcción sea efectivo?
Usar un solo método para crear el objeto
REPASAR 

38. 
Si estás diseñando un sistema de notificaciones y quieres que sea fácil de mantener y escalar, ¿cómo aplicarías el principio de inversión de dependencias para lograrlo?
Definiendo una interfaz para los notificadores y haciendo que el gestor de notificaciones dependa de esta interfaz en lugar de las implementaciones concretas.

39. 
Si quisieras mejorar la mantenibilidad de un sistema, ¿qué técnica de reestructuración sería más efectiva al aplicar los principios SOLID?
Dividir el código en módulos que representen contextos específicos como validaciones, notificaciones y lógica de negocios

40. 
Al implementar el patrón Builder, ¿cuál es la principal ventaja que obtienes en comparación con un constructor tradicional?
Mayor flexibilidad en la creación de objetos

41. 
¿Qué patrón de diseño sería más adecuado implementar para crear un sistema de procesamiento de pagos que permita elegir entre diferentes pasarelas de pago según la situación?
Patrón Strategy

42. 
¿Qué problema surge si una clase no cumple con el principio de sustitución de Liskov en un sistema de notificaciones?
Las clases no son intercambiables, lo que puede causar errores en tiempo de ejecución.