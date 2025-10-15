# Curso de Introducción a Selenium con Python

## Datos Clase: 

> Selenium es un framework de automatización de navegadores multilenguaje. Con él podrás simular las acciones de tus usuarios dentro de aplicaciones web con fines de testing, generar los reportes correspondientes, automatizar tareas repetitivas e incluso extraer datos de la web. Cualquier acción humana puede ser replicada y serás capaz de programarla.

- Publicado el 23 de junio de 2020
- Profesor: Hector Vega @TerragnigmArk 
- Fecha Inicio:15/10/2025 
- Fecha Fin: 

## Clase  01: Por qué aprender Selenium y qué verás 

> Requisitos 
- Python 
- HTML 
- Fundamentos de pruebas se software 
- 

## Clase  02: Curso de introducción a Selenium con Python 

## **Concepto**
> Es una herramienta para automatización de acciones en los diferentes navegadores 
> ¿Qué es selenium?: Es una suite de heramientas para automatización de navegadores.

## **Caracteristicas**
- Selenium es compatbile con los navegadores web más populares y algunos lenguajes de programación; Java, C#, Kotlin, Perl, Php, Python, Ruby, JavaScript.      []
- compactible con distintos lenguajes []
- No es una herramienta para testing pero se puede usar 
- No es una herramienta para Scraping pero se puede usar 
- El origen del nombre es por "Selenio", que es medicina para el envenenamiento por mercurio.
- Selenium NO es un software, sino una suite de distintos softwares

- America
- Inicio en el 2024 
- Creador Jason Huggins 
- Creo iun JavaScriptTestRunner despues llamado Selenium Core   

-- 
- Japon 
- Creador Chinya Katasani 
- Generó un Pluggin para Firefox [Facil de usar y mejor sin generar lineas de codigo]
- Llamado Selenium IDE [Capaz de grabar, repetir, importar y exportar automatizaciones]

-- 

- America 
- Creador Simon Stewart 
- crear el protocolo WebDriver utilizar una API de alto nivel.
- Ejecutar el comando en el navegador web 


## Selenium IDE
- Pros de Selenium IDE:
    - Excelente para iniciar en Testing y Pruebas unitarias
    - No requiere saber programar
    - Exporta scripts para Selenium RC y Selenium WebDriver
    - Genera reportes

- Contras de Selenium IDE:
    - Disponible solo para Firefox y Chrome
    - No sorporta DDT (Data Driven Testing)

## Selenium RC
- Pros de Selenium RC:
    - Soporte para:
    - Varias plataformas, navegadores y lenguajes
    - Operaciones lógicas y condicionales
    - DDT
    - Posee una API madura

- Selenium RC:
    - Complejo de instalar
    - Necesita de un servidor corriendo
    - Comandos redundants y ambigüos en su API
    - Navegación no tan realista

## Selenium WebDriver
- Pros de Selenium WebDriver:
    - Soporte para múltiples lenguajes
    - Fácil de instalar
    - Comunicación directa con el navegador
    - Interacción más realista

- Constras de Selenium WebDriver:
    - No soporta nuevos navegadores tan rápido
    - No genera reportes o resultados de pruebas
    - Requiere de saber programar (Pero con Platzi esto no es desventaja (; )

## Selenium Grid:
    - Se utiliza junto a Selenium RC
    - Permite correr pruebas en paralelo
    - Conveniente para ahorrar tiempo


## Clase  03: Otras herramientas de testing y automatización

## Puppeteer

**Puppeteer** es una librería de Node.js que proporciona una API de alto nivel para controlar Chrome o Chromium a través del Protocolo DevTools. Es excelente para automatización centrada en Chrome/Chromium.

| Pros (Ventajas) | Contras (Desventajas) |
| :--- | :--- |
| **Integración con Chrome/Chromium:** Ofrece un control profundo y eficiente al estar desarrollado por Google. | **Soporte limitado de navegadores:** Se centra principalmente en Chrome y Chromium (soporte experimental o limitado para otros). |
| **Rendimiento y Velocidad:** Suele ser muy rápido y estable en el entorno Chrome. | **Solo soporta JavaScript/Node.js:** Los *scripts* de automatización deben escribirse en JavaScript o TypeScript. |
| **API Sencilla y Clara:** Su curva de aprendizaje es relativamente baja para desarrolladores familiarizados con Node.js. | **No es ideal para *cross-browser testing*:** La limitación de navegadores lo hace inadecuado para la cobertura total de navegadores. |
| **Casos de Uso Adicionales:** Ideal para *web scraping*, generación de PDFs y capturas de pantalla de páginas web. | **Requiere Node.js:** Es un requisito fundamental para su uso. |

***

## Cypress.io

**Cypress.io** es un *framework* de *front-end testing* que se ejecuta directamente en el navegador, en el mismo *loop* de ejecución que tu aplicación. Se enfoca en una experiencia de desarrollo y *debugging* superior.

| Pros (Ventajas) | Contras (Desventajas) |
| :--- | :--- |
| **Experiencia del Desarrollador (DX):** Fácil de configurar e instalar, con una API muy intuitiva. | **Soporte de Navegadores Limitado:** Aunque ha mejorado, tradicionalmente su soporte ha sido más limitado (principalmente Chrome, Edge, Firefox, Electron). |
| **Ejecución y *Debugging* Rápido:** Ejecuta pruebas directamente en el navegador, lo que permite depurar en tiempo real con sus DevTools. | **Solo soporta JavaScript/TypeScript:** Las pruebas deben escribirse en estos lenguajes. |
| **Auto-esperas (Automatic Waiting):** Maneja automáticamente elementos asíncronos y esperas, reduciendo la inestabilidad (*flakiness*) de las pruebas. | **No soporta múltiples pestañas/ventanas:** No puede interactuar con múltiples pestañas o navegadores simultáneamente (limitación arquitectónica). |
| **Capturas y Videos Integrados:** Genera capturas de pantalla y videos automáticamente al fallar las pruebas. | **No soporta automatización de aplicaciones móviles nativas.** |

***

## Selenium

**Selenium** (principalmente Selenium WebDriver) es un conjunto de herramientas de código abierto ampliamente reconocido para la automatización de navegadores.

| Pros (Ventajas) | Contras (Desventajas) |
| :--- | :--- |
| **Amplio Soporte de Navegadores:** Compatible con todos los principales navegadores (*cross-browser testing* exhaustivo). | **Curva de Aprendizaje Elevada:** Su configuración inicial es más compleja y requiere gestionar *drivers* y *bindings* de lenguaje. |
| **Soporte Multi-Lenguaje:** Permite escribir *scripts* en varios lenguajes (Java, Python, C#, JavaScript, Ruby, etc.). | **Necesidad de Herramientas Externas:** Carece de características integradas como informes, auto-esperas robustas o un *test runner* (*frameworks* de terceros son necesarios). |
| **Comunidad Grande y Activa:** Cuenta con una de las comunidades más grandes, lo que significa mucha documentación y soporte. | **Ejecución Lenta (relativa):** Al usar el protocolo **WebDriver**, la comunicación externa entre el *script* y el navegador puede ser más lenta. |
| **Escalabilidad (Selenium Grid):** Permite ejecutar pruebas en paralelo en múltiples máquinas y entornos simultáneamente. | **Mantenimiento Alto:** Las pruebas pueden ser frágiles y requieren más mantenimiento debido a la dependencia de selectores. |

--- 

 ¿Qué es Flakiness?

En el contexto de la automatización y el *testing* de *software*, el término **Flakiness** (inestabilidad o fragilidad de las pruebas) se refiere a la propiedad de una prueba automatizada de producir **resultados inconsistentes** (a veces pasa, a veces falla) **sin que haya habido ningún cambio en el código fuente** de la aplicación ni en el código de la prueba.

Una prueba que pasa el lunes y falla el martes (o en la siguiente ejecución) sin una causa clara y reproducible, se considera una **"Flaky Test"** (prueba inestable).

### Consecuencias del Flakiness:

* **Pérdida de Confianza:** El equipo deja de confiar en la *suite* de pruebas, ignorando las fallas porque "probablemente sea solo una prueba inestable".
* **Ralentización del CI/CD:** Interrumpe el flujo de Integración y Entrega Continua, ya que se requiere re-ejecutar las pruebas fallidas varias veces.
* **Pérdida de Tiempo:** Los desarrolladores y *testers* gastan tiempo valioso investigando fallas que no son *bugs* reales.

### Causas Comunes del Flakiness:

1.  **Problemas de Tiempo (Timing Issues):** El más común. La prueba intenta interactuar con un elemento o verificar un resultado antes de que la aplicación haya completado la operación asíncrona (como una llamada a una API, una animación o la carga del DOM).
2.  **Condiciones de Carrera (*Race Conditions*):** Cuando las pruebas se ejecutan en paralelo y compiten por un recurso compartido (ej. una entrada en la base de datos).
3.  **Dependencia del Orden de Ejecución:** Una prueba depende del estado o los datos que dejó una prueba anterior (lo que viola el principio de aislamiento).
4.  **Inestabilidad del Entorno:** Factores externos como latencia de red variable, lentitud del servidor de pruebas o entornos de prueba inconsistentes.

---

Aquí tienes un listado de conceptos relacionados que comparten la idea de una prueba que no cumple con su propósito de manera eficiente o confiable:

| Concepto Relacionado | Descripción | Relación con Flakiness |
| :--- | :--- | :--- |
| **Non-Deterministic Test** (*Prueba No Determinista*) | Es el nombre técnico para una **Flaky Test**. Se refiere a que la prueba no siempre produce el mismo resultado para el mismo código. | **Es la definición técnica de *Flakiness*.** |
| **Fragile Test** (*Prueba Frágil*) | Una prueba que falla ante cambios menores en la aplicación que no deberían afectar la funcionalidad (*ej. un pequeño cambio en el CSS*). | Es una causa común de *Flakiness*. Una prueba frágil a menudo se convierte en una *Flaky Test* cuando el entorno es inestable. |
| **Brittle Test** (*Prueba Quebradiza*) | Similar a Frágil. Una prueba que es difícil de mantener y que requiere constantes ajustes de código (ej. por usar selectores de UI muy específicos). | Su alto coste de mantenimiento y la facilidad con la que se rompe la hacen propensa a ser inestable. |
| **Slow Test** (*Prueba Lenta*) | Una prueba que tarda mucho tiempo en ejecutarse, generalmente debido a una alta complejidad, esperas fijas (*sleeps*) o interacciones excesivas. | No es Flaky, pero a menudo se vuelve Flaky. Las pruebas lentas amplifican los problemas de *timing* e inestabilidad del entorno, y son candidatas a ser deshabilitadas si se vuelven inestables. |
| **Order-Dependent (OD) Flakiness** | Un tipo específico de Flakiness donde la prueba solo falla cuando se ejecuta justo antes o justo después de otra prueba en particular. | Es una **causa raíz específica de Flakiness**, generalmente debido a recursos o estados compartidos no limpiados correctamente. |
| **Greedy Test** (*Prueba Codiciosa*) | Una prueba que consume demasiados recursos del sistema (memoria, CPU, red), lo que puede afectar a otras pruebas que se ejecutan en paralelo. | Puede **inducir Flakiness** en otras pruebas al causar escasez de recursos y ralentización inesperada en el entorno de ejecución. |

En resumen, cuando una prueba no es **determinista** (el resultado varía) o es demasiado **frágil** (se rompe fácilmente), se está enfrentando al gran problema de la **Flakiness**.



## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:
## Clase  0:



```Python

```


---
## **Resumen** 

