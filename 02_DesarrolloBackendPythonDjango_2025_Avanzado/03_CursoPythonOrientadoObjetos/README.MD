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
Porque al hacer 'override' se asegura que los atributos `nombre` y `cédula` se hereden correctamente.

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