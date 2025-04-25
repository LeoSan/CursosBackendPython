# Curso de Python: PIP y Entornos Virtuales

> Trabaja profesionalmente con Python gestionando proyectos con PIP y entornos virtuales. Instala y contenediza aplicaciones en Docker, aprende a utilizar FastAPI para construir servidores web, y explora librerías como Pandas y Requests.

Nicolas Molina
@nicobytes
Colombian living in
Bolivia
Senior Software
Developer with +8 Years

## Clase 1: Python en tu propio entorno de desarrollo local

## Comandos básicos en la terminal, con esto iniciamos el proyecto:

- pwd: Indica en qué ubicación estamos
- mkdir: Crear una nueva carpeta
- ll: Lista de archivos
- cd: Nos permite abrir una carpeta
- clear: Nos permite despejar la terminal
- git init: Inicializar
- touch: Crear archivos

## Otros comandos

- rm: sirve para borrar archivos
- rmdir: sirve para borrar directorios
- mv: sirve para mover directorios
- df: indica el espacio en disco, el disponible, usado y total

```python

```


## Clase 2 - 3: Instalación en macOS
> 

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

## Clase 4: Python con VSCode
> Instalar librerias 

Solo recomendo una 
- python validado por microsoft 
- 
```python

```


## Clase 5: Python con Git y GitHub
> Creamos un proyecto en github y trabajar en repositorio 

## Pasos para crear un gitignore por proyecto en este caso python

- Paso 1: accedemos a esta pagina -> https://www.toptal.com/developers/gitignore
- Paso 2: Ingresamos los valores que necesitamos ignorar para este caso [windown Linux Macos Python]
- Paso 3: Esto nos genera un text ya con lo que se considera que se debe ingnorar para un proyecto Python
- Paso 4: Copia dicho txt, validamos si tenemos creado el archivo .gitignore en nuestro repo, si esta creado validalo si no generalo y pega lo que genero el portal web.  

```python



```

## Clase 6: Flujo de trabajo en Python
> 

El flujo de trabajo es:
1. creas un archivo.
2. lo pruebas
3. lo agregas a git
4. git add .
5. git commit -m
6. git pull origin main
7. git push origin main



## Clase 7: ¿Qué es pip?
> PIP es específico de Python y se utiliza para gestionar paquetes y módulos en proyectos de Python
> pip es un administrador de paquetes de Python que facilita la instalación y el mantenimiento de paquetes de software escritos en Python. Con pip, puedes instalar fácilmente paquetes de Python desde Internet, como las bibliotecas que necesitas para tu proyecto, y actualizarlos o desinstalarlos según sea necesario.

> Para utilizar pip, primero debes asegurarte de tener instalado Python en tu sistema. Luego, puedes instalar pip cancelado el siguiente comando en tu terminal:

python -m pip install pip

> Una vez que tienes pip instalado, puedes usar para instalar paquetes de Python obtuvo el siguiente comando:
pip install nombre-del-paquete


## Notas mentales 
- PIP es a Python como NPM es a JavaScript


## Enlace 
- https://pypi.org/project/pip/

Correr en la terminal los siguientes comandos

## comandos para recordar
- pip3 list 
- pip3 freeze
- pip install <paquete> => pip install matplotlib
- which python3




```python

import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.show()
    plt.close()

if __name__ == '__main__':
    generate_pie_chart()

```
## ejemplo Ejecutando el código 
![EjemploGrafica](../03_Curso_Python_PIP_Entornos_Virtuales/practica/pie.png)

## Clase 8: 
> Gráficas en Python con PIP

```python

import os


def create_folder(path, name_folder="logs"):
    path_to_create = os.path.join(path, name_folder)
    try:
        os.mkdir(path_to_create)
        print("Created successfully!")
    except Exception as err:
        print(f"It has occurred an unexpected error, details: {err}")

```


## Clase 9: ¿Qué es un ambiente virtual?
> Los entornos virtuales son una forma de crear un sistema operativo virtual dentro de otro sistema operativo. Esto permite a un usuario tener varios sistemas operativos diferentes en un mismo equipo físico, lo que puede ser muy útil en situaciones en las que es necesario utilizar diferentes aplicaciones o tecnologías que requieren entornos diferentes

## ¿Qué es un entorno virtual en Python?

Un entorno virtual (o ambiente virtual) en el contexto de Python es una herramienta que te permite crear un espacio aislado en tu sistema donde puedes instalar paquetes y dependencias de Python sin afectar el entorno global de Python en tu máquina.

## Beneficios de los entornos virtuales:

- Aislamiento: Cada entorno virtual es independiente y aísla las bibliotecas y paquetes que instalas en él.
- Gestión de dependencias: Facilita la especificación de dependencias necesarias para tu proyecto en un archivo requirements.txt.
- Evitar conflictos: Previene que las bibliotecas de un proyecto afecten a otros proyectos o al entorno global de Python.
- Limpieza y organización: Permite una gestión ordenada y eliminación de entornos virtuales no utilizados.

## Ventajas 

- Permiten utilizar varios sistemas operativos en un mismo equipo físico
- Permiten instalar y utilizar diferentes aplicaciones y tecnologías de manera segura, sin tener que hacer cambios permanentes en el sistema operativo principal
- Pueden ser fácilmente movidos o copiados, lo que significa que pueden ser utilizados en diferentes equipos o compartidos con otros usuarios
- También pueden ser fácilmente respaldados y restaurados en caso de que se produzca un problema, lo que puede ayudar a prevenir la pérdida de datos o el tiempo de inactividad
- Ofrecen una forma conveniente y segura de utilizar diferentes aplicaciones y tecnologías en un mismo equipo

# Notas mentales 
- Instalar a nivel global puede causar distintos problemas al momento de manejar diferentes proyectos, por ejemplo para algunos proyectos necesitaras otro tipo de version, libreria o modulos y para solucionar esto se creo un ambiente virtual en python el cual encapsula cada proyecto y no lo deja de forma compartida. 



```python

```

## Clase 10: Usando entornos virtuales en Python
> 


### Pasos para realizar un ambiente virtual

- Paso 1: Verificar donde esta python y pip
    - which python3
    - which pip3

- Paso 2: Si estas en linus o wsl debes instalar
    - sudo apt install -y python3-venv

- Paso 3: Poner cada proyecto en su propio ambiente, entrar en cada carpeta.
    - python3 -m venv env_name

- Passo 4: Activar el ambiente
    - source env_name/bin/activate

- Paso 5: Salir del ambiente virtual
    - deactivate

- Paso 6: Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
    - pip3 install matplotlib==3.5.0

- Paso 7: Verificar las instalaciones
    - pip3 freeze
- Paso 8: En caso que desees eliminar rm -r [env_name]

## Notas mentales 
- algo que debes recordar es que se genera un ambiente por cada carpeta de proyecto no es de manera global 
- Si tenemos en /Python/Proyecto1 ó /Python/Proyecto2 ó /Python/Proyecto3 debemos ejecutar el comando por cada carpeta 
- Ejemplo del comando python3 -m venv "env_name"
- luego lo activamos source "env_name"/bin/activate
- which python3
- which pip3
 

```python

```


## Clase 11: 
> 
```python

```

## Clase 12: 
> 
```python

```


## Clase 13: 
> 
```python

```

## Clase 14: 
> 
```python

```


## Clase 15: 
> 
```python

```

## Clase 16: 
> 
```python

```


## Clase 17: 
> 
```python

```

## Clase 18: 
> 
```python

```

## Clase 19: 
> 
```python

```


## Clase 20: 
> 
```python

```


