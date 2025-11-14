# Curso Práctico de Python: Creación de un CRUD🚀

1.
En el ejemplo de la clase, se agrega un objeto 'Libro' a una lista de usuarios. ¿Por qué el tipado de la lista como 'List[SolicitanteProtocol]' es un enfoque superior a simplemente esperar el error en tiempo de ejecución?
Porque 'Protocol' obliga a la clase 'Libro' a heredar automáticamente de 'SolicitanteProtocol'.

**Repasar**

2.
¿Cuál es el propósito principal de la Programación Orientada a Objetos (OOP) según se describe en la clase?
Construir sistemas informáticos que modelan o imitan entidades y procesos de la vida real.

3.
En el sistema de biblioteca presentado, ¿por qué es necesario que la clase `Estudiante` realice un 'override' del método `Solicitar libro` en lugar de simplemente usar el heredado de `Usuario`?
- Porque al hacer 'override' se asegura que los atributos `nombre` y `cédula` se hereden correctamente.
- Porque el método original en la clase `Usuario` está incompleto y no se puede utilizar directamente.
**Repasar**

4.
En la clase, al implementar por primera vez el método `__str__`, el instructor encuentra un `TypeError` que indica que el método devolvió un valor `NoneType`. ¿Cuál fue la causa exacta de este error y cómo se solucionó según lo explicado?
La f-string estaba mal formateada, utilizando la variable `libro` en lugar de `self` para acceder a los atributos.

**Repasar**

5.
En el contexto de la clase Libro, ¿cuál es la principal ventaja de implementar un método 'getter' como get_veces_prestado() para acceder al atributo privado __veces_prestado?
- Permite controlar el acceso a la información, pudiendo añadir lógica de validación o formato antes de devolver el valor, funcionando como el 'cajero' del ejemplo.

6.
En la clase `Libro`, ¿cuál es la diferencia fundamental entre el parámetro `titulo` y el atributo `self.titulo` dentro del método `__init__`?

- `titulo` contiene el valor de entrada y `self.titulo` lo almacena para que persista en el objeto.

7.
¿Cuál es el propósito principal de llamar a `super().__init__(nombre, cedula)` dentro del constructor de las clases `Estudiante` y `Profesor`?
- Invocar el constructor de la clase padre (`Usuario`) para que se encargue de inicializar los atributos `nombre` y `cédula`.

8.
¿Cuál es la principal ventaja de utilizar el `Context Manager` (`with open(...)`) para escribir en el archivo JSON dentro de la clase `Persistencia`?
Permite escribir líneas de código más cortas, ya que no es necesario importar la librería `os` para manejar rutas de archivos.

**Repasar**

9.
¿Cuál es el propósito principal de utilizar Clases Base Abstractas (ABC) en Python, según lo explicado en la clase?
- Establecer un 'contrato' que obliga a las subclases a implementar métodos específicos, garantizando una interfaz consistente.

10.
Si el método `libros_disponibles` se modificara para que la línea de retorno fuera `return libro` en lugar de `return libro.titulo`, ¿qué tipo de datos contendría la lista devuelta por el método?
- Una lista de objetos de la clase `Libro`.

11.
Si se invoca el método `libro.prestar()` sobre un objeto libro que ya fue prestado (es decir, su atributo `disponible` es `False`), ¿qué resultado se produciría según se describe en la clase Libro?
- Levantaría una excepción de tipo `LibroNoDisponibleError`.

12.
¿Cuál es el propósito principal de definir una clase como abstracta en Python mediante la herencia de ABC?
- Servir como una plantilla o "contrato" que obliga a las subclases a implementar una interfaz mínima de métodos.

13.
¿Qué acción específica realiza el método `buscar_usuario` de la clase `Biblioteca` cuando, después de recorrer toda la lista de usuarios, no encuentra una coincidencia con la cédula proporcionada?
- Lanza una excepción `UsuarioNoEncontradoError`.

14.
Al implementar el método `crear_no_disponible` con `@classmethod`, ¿por qué se utiliza el parámetro `cls` para crear la nueva instancia en lugar de invocar directamente a `Libro(...)`?
- Facilita la herencia, permitiendo que las subclases de `Libro` usen este método para crear instancias de su propio tipo específico.

15.
Dado que `TituloInválidoError` hereda de `biblioteca_error`, ¿qué ocurriría en el siguiente bloque de código si `funcion_que_falla()` lanza un `TituloInválidoError`? ```python try: funcion_que_falla() except biblioteca_error as e: print("Error de biblioteca detectado") except TituloInválidoError as e: print("Título inválido detectado") ```
- Se imprimirá "Título inválido detectado" porque es la excepción más específica que coincide.
**Repasar**

16. ¿Por qué el atributo `limite_libros` se inicializa con el valor `3` en la clase `Estudiante`, mientras que en la clase `Profesor` se inicializa con `None`?
- Para implementar diferentes reglas de negocio: los estudiantes tienen un límite fijo de préstamos, mientras que los profesores no tienen límite.

17. El instructor refactoriza el método `cambiar_disponibilidad` en dos métodos más específicos: `prestar` y `devolver`. ¿Qué principio de diseño de software se ejemplifica principalmente con esta decisión?

18. ¿Cuáles son las dos condiciones que el método `buscarLibro` en la clase `Biblioteca` verifica para retornar exitosamente un objeto libro?
- Aumentar la claridad y especificidad del código, asignando a cada método una única responsabilidad bien definida.

19. ¿Cuál es el propósito principal de encapsular una llamada a una función dentro de un bloque `try`/`except` en Python, según lo explicado en la clase?

- Evitar que una excepción detenga la ejecución completa del programa, permitiendo manejar el error y continuar.


20. Si un desarrollador está creando un sistema para una tienda de mascotas, ¿cómo aplicaría el concepto de 'clase' según los principios de OOP explicados en la clase?

- Crearía una clase 'Animal' como un plano para definir las características comunes (nombre, especie, edad) de todas las mascotas.

21. En el proceso de refactorización, el profesor mueve el código de ejecución del archivo `Usuarios.py` al archivo `main.py`. ¿Cuál es el problema principal de tener código de ejecución dentro de un módulo que, según las buenas prácticas, solo debería definir clases?

- Viola el principio de responsabilidad única, ya que el módulo realizaría tanto la definición de clases como la ejecución de lógica de la aplicación.

22. Si un desarrollador se olvida de asignar un argumento a un atributo dentro del constructor, como en `def __init__(self, titulo, autor): self.titulo = titulo`, ¿cuál sería la consecuencia al intentar acceder a `mi_libro.autor` después de crear `mi_libro = Libro("El Principito", "Saint-Exupéry")`? 

- Se produciría un `TypeError` al momento de crear el objeto, porque no se usó el argumento `autor`.
**Repasar**

23. Al implementar la búsqueda de usuarios, ¿cuál es la razón principal para colocar el bloque `try/except` que maneja `UsuarioNoEncontradoError` en el archivo `main` en lugar de dentro del método `buscar_usuario`?
- Para separar la lógica de negocio (la búsqueda) del manejo de la interfaz de usuario (mostrar el error).


24. Considerando el 'problema del pingüino', donde un `Pingüino` hereda de una clase `Pajaro` que tiene un método `volar()`, ¿por qué la composición sería un mejor enfoque para modelar la relación entre un pájaro y su capacidad de volar?
- Permite que la capacidad de 'volar' sea un componente opcional que solo se asigna a los pájaros que realmente pueden hacerlo.

25. En una clase abstracta, ¿cuál es la diferencia clave entre un método que tiene una implementación (concreto) y uno marcado con @abstractmethod?
- El método concreto se hereda con su implementación, mientras que el abstracto solo impone una firma que la subclase debe implementar.

26. Un desarrollador quiere crear una función 'procesar_pagos' que acepte una lista de objetos de diferentes tipos ('TarjetaCredito', 'PayPal', 26 'TransferenciaBancaria'). ¿Cuál sería la implementación más robusta y moderna usando los conceptos de la clase para asegurar que todos los objetos tengan un método 'ejecutar_pago'?

- Definir un 'PagableProtocol' con un método 'ejecutar_pago' y anotar la lista como 'List[PagableProtocol]'.

27. ¿Cuál es el propósito de inicializar `self.libros = []` y `self.usuarios = []` dentro del constructor de la clase `Biblioteca`?

- Obligar a que cada biblioteca tenga siempre un catálogo y una lista de usuarios, aunque estén vacíos.
**Repasar**

28. Según lo demostrado en la clase, ¿qué componentes específicos del módulo `abc` son necesarios importar para crear y hacer cumplir una clase abstracta?
- La palabra clave `abstract` y la función `implements` para conectar la subclase.
**Repasar**

1.
Un desarrollador quiere crear una función 'procesar_pagos' que acepte una lista de objetos de diferentes tipos ('TarjetaCredito', 'PayPal', 'TransferenciaBancaria'). ¿Cuál sería la implementación más robusta y moderna usando los conceptos de la clase para asegurar que todos los objetos tengan un método 'ejecutar_pago'?
Definir un 'PagableProtocol' con un método 'ejecutar_pago' y anotar la lista como 'List[PagableProtocol]'.

2.
El instructor menciona que el patrón de OOP se aplica a bancos, ecommerce y plataformas gubernamentales. ¿Qué característica fundamental de OOP hace que este enfoque sea tan versátil en dominios tan diferentes?
La capacidad de abstraer y modelar cualquier entidad del mundo real (cliente, producto, transacción) como un objeto con atributos y comportamientos.

3.
¿Cuál es la diferencia clave en la lógica del método `Solicitar libro` sobrescrito entre la clase `Profesor` y la clase `Estudiante`?
La clase `Estudiante` tiene un límite de libros en sus atributos, pero la clase `Profesor` no.

**Repasar**

4.
Un desarrollador nota que el contador 'veces_prestado' de la clase Libro está siendo modificado incorrectamente desde fuera de la clase. Según las prácticas de encapsulación explicadas, ¿cuál es la solución más robusta para evitar este problema?
Renombrar el atributo a '__veces_prestado' y crear métodos públicos 'get_veces_prestado()' y 'set_veces_prestado()' para controlar su acceso y modificación.

5.
Si un desarrollador crea una lista de objetos `Libro` y luego ejecuta `print(mi_lista_de_libros)`, pero en la consola ve una salida como `[<__main__.Libro object at 0x...>, ...]`, ¿cuál es la inferencia más lógica sobre el estado de la clase `Libro`?
La clase `Libro` no tiene implementado el método `__str__` (ni `__repr__`), por lo que Python utiliza su representación de objeto por defecto.

6.
Un `estudiante` tiene `limite_libros = 3` y ya ha solicitado 3 libros. Si se llama al 'Reto' e implementa un método `devolverLibro('Python básico')`, y luego se vuelve a llamar a `estudiante.solicitarLibro('Nuevo libro de IA')`, ¿cuál sería el resultado esperado de esta última llamada?
La solicitud sería rechazada con el mensaje de 'Límite alcanzado', porque el límite de 3 libros ya se usó.
**Repasar**

7.
¿Cuál es el propósito principal de usar los parámetros `ensure_ascii=False` e `indent` al llamar a `json.dump()` en Python para guardar los datos de la biblioteca?
Para generar un archivo JSON que sea legible para humanos y que soporte correctamente caracteres especiales del español como tildes y eñes.

8.
¿Mediante qué mecanismo específico el módulo `abc` de Python se asegura de que una subclase cumpla con el 'contrato' de la clase base abstracta en tiempo de ejecución?
Usando el decorador `@abstractmethod`, que impide la instanciación de cualquier subclase que no haya implementado los métodos marcados.

9.
Si en la clase `Biblioteca` se eliminara la línea `self.libros = []` de su método constructor, ¿cuál sería la consecuencia más directa al intentar ejecutar el método `libros_disponibles`?
El programa fallaría con un `AttributeError` porque la instancia de `Biblioteca` no tendría el atributo `libros`.

10.
Se tiene un sistema con una clase `Auto` diseñada con composición, de modo que `Auto` 'tiene un' `Motor`. Si en el futuro se necesita ofrecer autos con `MotorElectrico` o `MotorDeCombustion`, ¿qué ventaja clave proporciona la composición en este escenario?
Permite intercambiar el componente `Motor` por diferentes tipos, siempre que cumplan con la misma interfaz, sin alterar la clase `Auto`.

11.
Un estudiante A presta con éxito "La Metamorfosis". Inmediatamente, el estudiante B intenta buscar el mismo libro por su título. ¿Qué sucederá durante la ejecución del método `biblioteca.buscarLibro()` para el estudiante B?
El método lanzará `LibroNoDisponibleError` porque `libro.prestar()` cambió el atributo `disponible` a `False`.

12.
Un desarrollador está trabajando en `main.py` y escribe `biblioteca = Biblioteca()`. El editor de código subraya `Biblioteca` con un error 'no definida'. Basado en la estructura del proyecto refactorizado en la clase, ¿cuál es la causa más probable de este error y cómo se soluciona?
Falta la sentencia `import Biblioteca` o similar al inicio del archivo `main.py`, que es necesaria para que Python conozca la clase definida en otro módulo.

13.
¿Qué acción específica realiza el método `buscar_usuario` de la clase `Biblioteca` cuando, después de recorrer toda la lista de usuarios, no encuentra una coincidencia con la cédula proporcionada?
Lanza una excepción `UsuarioNoEncontradoError`.

14.
Si una subclase hereda de una clase abstracta pero no implementa todos sus métodos marcados con @abstractmethod, ¿en qué momento específico falla el programa?
El programa se ejecuta, pero se produce un AttributeError al llamar al método no implementado.
**Repasar**

15.
¿Por qué se considera una mejor práctica crear una excepción personalizada como `biblioteca_error` en lugar de simplemente usar una genérica como `ValueError`?
Permite capturar errores específicos de la lógica de la aplicación, haciendo el código más expresivo y evitando ocultar otros errores inesperados del mismo tipo genérico.
