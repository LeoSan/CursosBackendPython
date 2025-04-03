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