# Curso de Python Profesional: Arquitectura de Proyectos, Entornos y PyPI🚀

> Domina las herramientas modernas de desarrollo en Python con proyectos prácticos. Aprende a escribir, probar y automatizar código profesional con Ruff, pytest, Mypy y GitHub Actions. Mejora tu flujo de trabajo con formateo automático, validaciones en tiempo real y despliegues eficientes que te preparan para entornos de producción reales.

| Detalle | Información |
| :--- | :--- |
| **Publicado el** | 22 Octubre 2025 |
| **Profesor** | Luis Martinez  |
| **Fecha de Inicio** | 29/12/2025  |
| **Fecha de Fin** | 31/12/2025  |
| **Enlace** | https://platzi.com/cursos/python-avanzado/  |



## CLASE 01:  Calidad, automatización y asincronía en Python profesional


¿Por qué calidad, automatización y asincronía en Python marcan la diferencia?
La diferencia no está en “hacerlo correr”, sino en construir software que resista el paso del tiempo. La calidad evita el caos de estilos y errores. La automatización libera tiempo de tareas repetitivas. La asincronía multiplica la eficiencia en operaciones de input y output con APIs y bases de datos.

Código que evoluciona sin romperse en cada cambio.
Equipos que hablan el mismo idioma técnico.
Menos fricción operativa y más foco en valor de negocio.
Mejor rendimiento cuando hay espera por I/O.
¿Qué reglas y herramientas garantizan el mismo idioma del equipo?
Imagina cinco personas editando un archivo sin reglas: sería un caos. La salida es estandarizar prácticas y exigirlas con herramientas que verifiquen cada cambio sin intervención manual.

¿Qué reglas alinean al equipo en Python?
PEP 8 para respetar reglas importantes del lenguaje.
Anotaciones de tipo para claridad y mantenimiento.
Tests unitarios para validar comportamientos de forma confiable.
¿Qué herramientas automatizan la calidad sin intervención?
Formateadores y linters para legibilidad y consistencia.
Recommit hooks para validar cada cambio antes de subir al repositorio.
GitHub Actions para ejecutar herramientas de calidad en cada push.
TaskRunners como Make para evitar recordar comandos largos.
¿Cómo desarrollar las habilidades clave y qué lograrás al finalizar?
El objetivo es ejecutar un pipeline de calidad sin fricción y dominar la asincronía para mejorar el rendimiento en I/O. Además, compartirás tu trabajo con la comunidad.

¿Cómo automatizar reglas y configurar un pipeline de calidad?
Automatizar tus reglas de desarrollo para que se verifiquen siempre.
Configurar un pipeline completo que valida la calidad sin intervención manual.
Integrar verificaciones en cada cambio y en cada push.
¿Cómo dominar la programación asincrónica y refactorizar I/O?
Dominar la programación asincrónica para optimizar operaciones que esperan respuesta.
Refactorizar código síncrono a asíncrono, mejorando drásticamente el rendimiento en tareas con APIs o bases de datos.
¿Cómo publicar en la comunidad y dar el salto profesional?
Publicar en la comunidad: tu primer aporte open source de Python en PyPI.
Consolidar disciplina, herramientas y práctica real para construir Python Profesional.


```PYTHON


```
## CLASE 02:  Configuración inicial del proyecto Platy News con Python


¿Qué es Platy News y qué lograrás con Python?
Platy News es una CLI que integra varias fuentes de información para buscar noticias y complementarlas con análisis de IA. Reúne conocimientos desde variables y ciclos hasta entornos virtuales, POO, typing y AsyncIO, guiándote hacia un trabajo más profesional y colaborativo.

Aplicación de línea de comandos con comandos intuitivos en la terminal.
Búsqueda de noticias con múltiples fuentes: News API, The Guardian y OpenAI.
Análisis con IA integrado mediante un LLM.
Python 3.13 como requisito por el uso de typing avanzado.
Trabajo en equipo y mejora de un código legacy.
Pruebas unitarias con carpeta test para validar el proyecto.
¿Cómo clonar e instalar el proyecto paso a paso?
El proyecto se distribuye en un repositorio con readme que irás mejorando. La estructura incluye paquetes, módulos y la carpeta test con pruebas unitarias. Usarás Visual Studio Code para explorar el código y la terminal para ejecutar comandos.

¿Qué estructura tiene el repositorio y qué herramientas usarás?
README inicial que documenta requisitos y uso.
Paquetes y módulos organizados por funcionalidad.
test con pruebas unitarias para validar el comportamiento.
Visual Studio Code para editar y ejecutar.
Terminal para comandos del flujo de instalación.
¿Qué comandos ejecutar en la terminal?
Clonación con git clone usando el enlace SSH y apertura en VS Code.
git clone <URL-SSH>
cd <carpeta-del-repositorio>
code -r .
Creación del entorno virtual con el comando indicado y activación según tu sistema.
vvm
# luego activar con el comando que muestre vvm.
Instalación en modo editable para habilitar el comando platynews.
vpip install -e
Verificación rápida del comando (mostrará errores si faltan claves).
platynews
¿Cómo configurar API keys y ejecutar comandos con IA?
La configuración se hace con un archivo .env en la raíz del proyecto. Debes crear el archivo y pegar las API keys siguiendo el readme. Sin estas claves, platynews mostrará errores al iniciar.

¿Dónde crear y pegar las API keys en .env?
Crea el archivo .env según lo indicado en el readme.
Genera y copia la clave de News API desde tu cuenta y pégala en .env.
En OpenAI crea una nueva clave secreta y verifica que tienes saldo activo.
Regístrate en The Guardian como desarrollador, confirma el correo y copia la clave recibida a .env.
Guarda el archivo y vuelve a ejecutar platynews.
¿Cómo probar una consulta con guardian y LLM?
Abre el readme y toma un ejemplo de uso con un tema como “cambio climático”.
Ejecuta el comando para preguntar por las “principales causas” usando el source guardian.
Espera unos segundos para ver la lista de temas procesados por el LLM.
Si aparece la ayuda de uso en vez de errores, las API keys están bien configuradas.

Buenas prácticas:

Verifica el entorno virtual activo antes de instalar o ejecutar.
Mantén el readme actualizado con cada cambio.
Revisa la carpeta test para entender los unit tests del proyecto.


## CLASE 03: Configuración y uso de Ruf como formateador automático en Python
¿Cómo instalar y configurar Ruf con pyproject.toml?
Configurar Ruf desde el principio evita fricciones de estilo y facilita la colaboración. La instalación se hace en el entorno de desarrollo y queda registrada en el archivo de configuración del proyecto.

Abre la terminal en la carpeta del proyecto.
Agrega la dependencia al entorno de desarrollo con el gestor de paquetes.
V add --def Ruf
Verifica que en pyproject aparezca la dependencia en el grupo de desarrollo.
Ejecuta el formateo en el path actual.
root format .
Revisa los cambios: se reportan archivos reformateados y archivos sin cambios.
Ejemplo real: 20 archivos reformateados y 3 sin cambios.
Cambios típicos que verás:
Inserción de líneas en blanco para legibilidad.
Cambio de comillas simples a dobles o viceversa.
Alineación y espacios según PEP 8.
Idea clave: por defecto, Ruf aplica PEP 8 automáticamente. Si tu equipo usa otro estándar, configura las reglas en pyproject.toml para mantener consistencia.

¿Qué reglas PEP 8 aplica y cómo personalizarlas?
Ruf es un reemplazo de Black que formatea según PEP 8. Sin embargo, puedes ajustar el estilo para seguir reglas ya establecidas en tu proyecto, todo desde pyproject.toml dentro de la sección de configuración de la herramienta.

¿Cómo cambiar el estilo de comillas?
Si necesitas que las comillas sean simples, define el quote style en la configuración. Al volver a ejecutar el formateo, Ruf actualizará los archivos según la regla.

[tool.ruf]
quote style = "single"
Efecto: cuando había comillas dobles, pasarán a comillas simples.
Úsalo solo si tu proyecto no seguirá PEP 8 por defecto en este aspecto.
¿Cómo excluir archivos con extend exclude?
Evita que se formatee código generado automáticamente por un framework agregando rutas a una lista de exclusiones. Crea una carpeta, por ejemplo: do not format, y añádela a la configuración.

[tool.ruf]
extend exclude = ["Platinus/do not format/"]
Crea un archivo .py dentro de esa ruta con comillas simples.
Ejecuta:
root format .
Resultado: ese archivo no se modifica.
Buenas prácticas de configuración: - Mantén un estándar único: si no es PEP 8, que sea el estándar del proyecto. - Controla cambios de estilo desde pyproject.toml para todo el equipo.

¿Qué buenas prácticas y flujo de trabajo recomiendan?
Adoptar Ruf de forma ordenada reduce conflictos en pull requests y acelera las revisiones.

Configura Ruf desde el inicio del proyecto para evitar divergencias de formato.
Integra Ruf format en hooks de pre-commit para validar antes de cada commit.
Define reglas consistentes en pyproject.toml y compártelas con todo el equipo.
Si necesitas volver a PEP 8 por defecto, revierte cambios de configuración y vuelve a formatear.


## CLASE 04: Configuración de MyPy para validación estática de tipos en Python

¿Qué es MyPy y por qué mejora la validación estática de tipos en Python?
MyPy permite encontrar incompatibilidades de tipos sin correr la aplicación. Con esto, el código se vuelve más robusto, fácil de mantener y confiable en equipos grandes. La clave: leer el error, entender el contexto y aplicar el tipado correcto.

Detecta errores antes de tiempo y evita bugs en producción.
Ayuda a documentar contratos de funciones y estructuras.
Acelera el refactor con confianza.
Permite reportes para ver cobertura de tipado por archivo.
¿Cómo instalar y ejecutar MyPy en Platzi News?
Primero se instala como dependencia de desarrollo y luego se ejecuta sobre el directorio de código fuente para ver los errores detectados.

¿Cómo instalar MyPy y los tipos para requests?
Instala MyPy como dev dependency.
v add --dev mypy
Si usas requests sin tipados, instala los stubs para eliminar el error de “Stub not installed”.
v add --dev types-requests
¿Cómo ejecutar el análisis y leer los errores de tipos?
Corre MyPy sobre el código fuente.
mypy src
Interpreta el resultado: archivo, dos puntos, número de línea y descripción del problema.
Ten en cuenta que versiones cambian y los mensajes pueden variar; lo importante es interpretar el tipo esperado vs. el recibido.
¿Cómo solucionar errores comunes y generar reportes HTML?
A continuación, ajustes reales de tipado, mejoras a parámetros y una forma de ignorar validaciones puntuales cuando conoces la intención del código.

¿Cómo tipar params compatibles en requests.get?
El error indica que params no coincide con la firma esperada. La causa: una clave como api_key con tipo desconocido. Solución: tipar el diccionario para que las llaves sean strings y los valores sean string o int.

Versión con typing clásico.
from typing import Union

params: dict[str, Union[str, int]] = {
    "query": query,
    "api_key": api_key,
}
Versión moderna y más legible (operador |).
params: dict[str, str | int] = {
    "query": query,
    "api_key": api_key,
}
Notas clave: - dict[str, …] tipa las llaves como strings. - str | int asegura compatibilidad con la firma de requests. - Quitar int mostrará un error inmediato si algún valor es entero.

Al volver a ejecutar MyPy, el error desaparece cuando el tipo es compatible.

¿Cómo ignorar validaciones puntuales con type: ignore?
Cuando la intención del código es válida pero choca con una regla, puedes ignorar solo esa línea con el motivo específico.

settings = Settings()  # type: ignore[call-arg]
Buenas prácticas: - Usa comentarios de ignore solo cuando entiendas el mensaje. - Documenta el motivo con el código de error entre corchetes. - Evita ignorar bloques completos; sé específico a la línea.

¿Cómo corregir join cuando la lista no es de strings?
La función join requiere un iterable de strings. Si hay enteros mezclados, convierte cada elemento a string antes de unir.

msg = ", ".join(str(x) for x in missing_keys)
Garantiza que join reciba siempre lista de strings.
Evita errores del tipo “no se puede asignar al parámetro iterable[str]”.
Al limpiar y ejecutar de nuevo, MyPy puede mostrar el mensaje esperado:

Éxito: no hay issues encontrados en dieciséis archivos analizados.
¿Cómo generar un reporte HTML de cobertura de tipos?
Para compartir con el equipo qué archivos y líneas están tipados, genera un reporte HTML.

Instala la dependencia requerida.
v add --dev lxml
Genera el reporte en una carpeta.
mypy src --html-report mypy_report
Abre el index del reporte y revisa precisión por archivo y líneas tipadas.

## CLASE 05:  Configuración y uso de ruff para análisis estático en Python

¿Por qué usar ruff para análisis estático en Python?
Ruff permite detectar errores temprano y ahorrar tiempo. Integra revisión de estilo PEP 8, limpieza de imports y mejoras automáticas del código. Se configura en el archivo pyproject.toml, junto a otras herramientas como MyPy.

Es un formateador y un linter en uno solo.
Reemplaza PGLint y Flake ocho con reglas consolidadas.
Es ultrarrápido y apto para proyectos grandes.
¿Qué es un formatter y qué es un linter?
Un formatter (como ruff usado como formatter) “arregla” el estilo para cumplir PEP 8.
Un linter analiza el código fuente sin ejecutarlo para detectar errores de sintaxis, imports no usados y problemas potenciales.
Ejecuta cada uno así:

ruff format
ruff check
¿Cómo se configura ruff en pyproject.toml?
Define la configuración dentro de pyproject.toml.
Ajusta reglas según tu proyecto y, si quieres, agrúpalas con las de MyPy.
Mantén las reglas de lint juntas bajo la configuración de tool ruff para claridad.
¿Cómo ejecutar ruff, corregir y seleccionar reglas?
La práctica recomendada es correr ruff con frecuencia. Primero, inspecciona con check y, si hay errores arreglables, aplica fix.

ruff check
ruff check fix
Caso real: ruff reporta “diez errores”, de los cuales “ocho” son fixable. Con “check fix”, elimina imports no usados y aplica mejoras seguras. Quedan “dos errores” manuales, como variables definidas que nunca se usan.
Ruff evita borrar líneas que podrían cambiar el comportamiento; tú decides si eliminarlas.
¿Cómo activar rule selection e isort para ordenar imports?
Ruff permite ampliar la verificación con más reglas. Ejecuta todas para medir tu base de código:

ruff check select all
Ejemplo: aparecen “doscientos sesenta y seis” errores al activar más reglas. Esto muestra que ruff es altamente configurable y que, por defecto, usa un conjunto básico.
Desde la documentación, copia los “selects” recomendados: incluyen reglas de pycodestyles, pyflakes, pyupgrade y la “I” de isort para ordenar imports.
Tras configurar, usa “check fix” para que ruff elimine imports no usados y ordene los imports: primero los de Python, luego librerías externas y, al final, los locales. Separados por un enter, y dos enters antes del código.
¿Qué cambios automáticos y de estilo verás en el código?
Conversión de .format a “literal string” según la versión de Python: ruff sugiere el literal string por ser la práctica actual recomendada.
Límite de línea en 88 caracteres (PEP 8): divide donde sea seguro para mantener el código ejecutable. No partas expresiones críticas; busca el punto correcto para el salto.
Caso práctico: tras “catorce errores”, ruff arregla “siete” automáticamente. El resto requiere tu revisión.
¿Qué buenas prácticas fortalecen tu flujo con ruff?
Adoptar ruff desde el inicio eleva la calidad y agiliza revisiones. Integra su uso en tu ciclo de desarrollo.

Configúralo desde el inicio del proyecto para consistencia.
Ejecuta “run check” con regularidad, idealmente en cada commit. Con pre-commit podrás automatizarlo.
Combínalo con MyPy para tipos y PyTest para pruebas, logrando una suite completa de calidad de código.


## CLASE 06:  Configuración de pre-commit con Ruff y MyPy para validar código

¿Qué es pre-commit y cómo garantiza calidad en cada commit?
Pre-commit es un framework que simplifica la configuración de hooks que se ejecutan automáticamente cada vez que haces un commit. Al instalarlo y crear el archivo de configuración pre-commit.config.yml, puedes activar reglas como corrección de fin de archivo, eliminación de espacios en blanco y validación de YAML. Al correr pre-commit install, el hook se integra en la carpeta .git para que todo commit pase por estas comprobaciones.

¿Qué reglas básicas conviene activar?
end-of-file-fixer: asegura una línea vacía al final del archivo.
trailing-whitespace: elimina espacios en blanco innecesarios.
check-yaml: valida la sintaxis de archivos YAML.
¿Cómo instalar y configurar pre-commit con Ruff y MyPy?
Primero instala pre-commit como dependencia de desarrollo y valida que responde en la terminal. Si avisa que falta configuración, crea pre-commit.config.yml y añade tus reglas. Luego ejecuta pre-commit install: se activará el hook local.

Herramientas clave: Ruff como linter y formatter. MyPy como analizador estático de tipos.
Archivo de proyecto: pyproject.toml con la configuración de Ruff y reglas como Bandit.
Habilidad práctica: interpretar mensajes de error y corregirlos antes del commit.
# Instalar el hook en el repositorio
pre-commit install

# Flujo de trabajo básico
git status
git add .
git commit -m "mensaje"
Un ejemplo minimal de estructura para pre-commit.config.yml con las reglas mencionadas:

repos:
  - repo: ...
    rev: ...
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-yaml

  - repo: ...  # Integración de Ruff (Astral)
    rev: ...
    hooks:
      - id: ruff
      - id: ruff-format

  - repo: ...  # mirrors-mypy
    rev: "1.8.0"
    hooks:
      - id: mypy
¿Cómo probar la configuración con Ruff?
Genera un cambio que viole una regla: por ejemplo, una línea muy larga.
Ejecuta git add y git commit con un mensaje como “intento de commit malo”.
El primer commit puede instalar dependencias de hooks automáticamente.
Verás que Ruff bloquea el commit con el detalle del error: la línea supera el límite.
¿Cómo integrar MyPy en los hooks?
Añade mirrors-mypy con un ref que coincida con tu versión, por ejemplo: "1.8.0".
Guarda cambios y recuerda: si modificas pre-commit.config.yml, debes hacer git add de ese archivo para que el hook lo tenga en cuenta.
Reintenta el commit y confirma que MyPy ejecute sus comprobaciones.
¿Cómo validar, evitar errores y aplicar seguridad con Bandit?
Puedes necesitar terminar un commit urgente y omitir las verificaciones de estilo. En ese caso, usa la opción --no-verify al final del comando de commit. Úsala con responsabilidad.

git commit -m "mensaje urgente" --no-verify
Para seguridad, activa reglas de Bandit desde la configuración de Ruff en tu pyproject.toml. Un caso típico es la regla S307, que alerta sobre el uso inseguro de eval.

# Ejemplo inseguro: Bandit S307
user_input = input("Ingresa una expresión:")
resultado = eval(user_input)  # Inseguro: ejecución arbitraria de código
Al intentar el commit, pre-commit mostrará: “función insegura, considera cambiarla”.
Elimina el uso de eval y vuelve a ejecutar git add y git commit.
El commit pasará cuando el código cumpla las reglas activadas.
¿Qué buenas prácticas mejoran tu flujo?
Configúralo desde el inicio del proyecto para estándares consistentes.
Incluye solo herramientas esenciales para no ralentizar los commits.
Combínalo con continuous integration y continuous deployment para doble validación: local y remota.

## CLASE 07: Ejecución paralela de pruebas unitarias con pytest y coverage

¿Qué es pytest y por qué mejora tus pruebas unitarias?
Pytest es el estándar moderno en Python para pruebas unitarias. Es más simple de escribir, ofrece mejor reporte de errores y soporta plugins avanzados sin complicar la sintaxis. Lo mejor: puede ejecutar los unit tests existentes sin reescribirlos.

Pruebas unitarias: validan unidades pequeñas de código y documentan el comportamiento esperado.
Unit Test: biblioteca estándar tradicional; en el proyecto de Platzi News se usó para crear tests.
Pytest: ejecución sencilla, reporting claro y extensible mediante plugins.
¿Cómo instalar pytest como dependencia de desarrollo?
Ejecuta: v add --dev pytest.
Verás los paquetes instalados y cambios en pyproject con la versión de pytest.
¿Qué configuración básica necesita pytest?
En pyproject, agrega la sección de configuración: tool.pytest.ini_options.
Define las rutas de pruebas con testPaths y los patrones con python_files.
Expón la app con PYTHONPATH apuntando a SRC para que pytest encuentre tu código.
# pyproject.toml
[tool.pytest.ini_options]
testPaths = ["tests"]
python_files = ["test_*.py"]
¿Cómo medir cobertura con coverage y generar reportes útiles?
La métrica coverage indica qué porcentaje de tu código está cubierto por pruebas. Ayuda a priorizar dónde escribir nuevos tests y a visualizar líneas no ejercitadas.

Instala el plugin: v add --dev pytest-cov.
Ejecuta con parámetros de cobertura y reporte HTML.
pytest --cov=SRC --cov-report=html
Se genera la carpeta htmlcov con index.html y un resumen por archivo.
Ejemplo observado: 80 % de cobertura total. Archivos con 100 % están completos; otros muestran líneas sin probar.
Interpretación visual: líneas verdes aprobadas; líneas rojas sin pruebas que las ejecuten.
¿Qué decisiones tomar con el reporte de coverage?
Prioriza módulos en rojo con lógica crítica.
Agrega casos para ramas no cubiertas (condiciones, excepciones, bordes).
Repite la medición hasta alcanzar un nivel objetivo sostenible.
¿Cómo paralelizar pruebas con xdist y aplicar TDD en tu flujo?
La ejecución paralela con xdist usa múltiples núcleos para reducir drásticamente el tiempo de feedback. Esto incentiva ciclos rápidos y seguros, ideal al practicar TDD.

Instala el plugin: v add --dev pytest-xdist.
Ejecuta en paralelo con detección automática de núcleos.
pytest -n auto
Resultado observado: todas las pruebas en menos de un segundo usando 11 workers.
Agrega verbosidad para más detalle en la terminal: progreso, nodo, clase y método del test.
pytest -n auto --cov=SRC --cov-report=html -b -v
¿Por qué sumar Test Driven Development a esta configuración?
Test Driven Development te hace escribir el test antes del código.
Beneficios: diseño más claro, foco en requisitos y verificación continua al refactorizar.
Con pytest, coverage y xdist, el ciclo rojo–verde–refactor es ágil y confiable.
¿Qué otros plugins puedes explorar para tu contexto?
pytest-mock: crea mocks de dependencias fácilmente.
pytest-randomly: ejecuta en orden aleatorio para detectar dependencias entre tests.
La ecosistema de pytest incluye miles de plugins: elige el que resuelva tu necesidad específica

## CLASE 08: Configuración de GitHub Actions para CI/CD con Python

¿Cómo configurar GitHub Actions para CI/CD en Python con ruff, mypy y pytest?
La integración continua ejecuta pruebas y validaciones automáticamente al integrar cambios con frecuencia. La entrega continua va más allá automatizando el despliegue. Con Actions, puedes crear un workflow que corra en cada push y en cada pull request hacia ramas clave.

Problema común: funciona local, falla en otro entorno por configuraciones o dependencias distintas.
Solución: automatizar validaciones de estilo con ruff, tipado estático con mypy y pruebas unitarias con pytest.
Beneficio: calidad consistente y detección temprana de errores.
¿Qué eventos disparan el workflow y cómo ahorrar minutos?
Define cuándo corre la Action con la llave on. Se recomienda limitar a ramas críticas para optimizar minutos.

Ejecutar en push solo en branches main y develop.
Ejecutar en pull request únicamente hacia main.
Repos públicos: gratis. Repos privados: 2000 minutos gratis; adminístralos y evita validar ramas WIP.
Ejemplo de disparadores y estructura mínima:

ame: Code style

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  python:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      # - name: Instalar UV
      #   run: <comando de instalación de UV>
      - name: ruff check
        run: V run ruff check
      - name: ruff format
        run: V run ruff format
      - name: mypy
        run: V run mypy src
      - name: pytest
        run: V run pytest -n auto
¿Qué pasos y comandos ejecuta el pipeline?
En el job se usa Ubuntu automáticamente. Los pasos típicos incluyen:

Checkout del repositorio.
Instalar UV para ejecutar comandos de Python.
ruff check: valida reglas de estilo y errores como E501 (línea muy larga).
ruff format: formatea el código automáticamente.
mypy src: analiza tipos solo en la carpeta src.
pytest -n auto: ejecuta pruebas aprovechando múltiples núcleos.
¿Cómo corregir fallos de estilo y tipado en la pipeline?
Si falla ruff por E501 (línea muy larga), corrige el archivo y valida con un flujo de git ordenado.

git pull para traer cambios recientes.
Crear rama: git switch -c fixed-pep8.
Editar el archivo, por ejemplo quitando el comentario que rompe PEP8.
git add y git commit (pasa validaciones de pre-commit).
git push y abrir el pull request.
Verifica en la pestaña Actions que los checks corren en el PR.
Cuando ruff y mypy pasen, puede fallar pytest si faltan variables de entorno como un API key. Los tests no deben usar claves reales; solo comprobar que existen.

¿Cómo inyectar variables de entorno seguras en pytest?
Agrega env en el paso de pytest con valores falsos, suficientes para que los tests encuentren las variables.

- name: pytest
  env:
    # define las variables usadas en tu .env con valores NO reales
    API_KEY: "this is not a API key"
    # API_SECRET: "this is not a API key"
    # PROJECT_ID: "dummy"
  run: V run pytest -n auto
Haz commit y push de la actualización del workflow.
Revisa el PR: ruff, mypy y pytest deben pasar en segundos.
¿Qué buenas prácticas fortalecen tu CI/CD con GitHub Actions?
Adopta hábitos que mantengan tu flujo estable y rápido.

Crear el workflow desde la pestaña Actions y partir de ejemplos oficiales de las librerías.
Usar actions reusables desde la documentación de cada herramienta para mayor flexibilidad.
Considerar la funcionalidad de cache disponible en la action de ruff para mejorar tiempos.
Nombrar el workflow (por ejemplo, Code style) para identificar los checks fácilmente.
Limitar on a main y develop, y pull requests hacia main, para cuidar minutos.
Ejecutar pytest con -n auto para paralelizar pruebas.
Mantener variables sensibles fuera del repo; usar valores dummy en env del workflow.

## CLASE 09: 



## CLASE 10: 



## CLASE 11: 



## CLASE 12: 






## CLASE 13: 



## CLASE 14: 



## CLASE 15: 



## CLASE 16: 



## CLASE 17: 



## CLASE 18: 



## CLASE 19: 



## CLASE 20: 
