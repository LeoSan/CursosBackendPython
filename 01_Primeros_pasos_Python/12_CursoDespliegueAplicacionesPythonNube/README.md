# Curso de Despliegue de Aplicaciones Python en la Nube

## Clase 1: 

> Despliega aplicaciones Python en la nube: configura servidores, DNS, bases de datos, dominios, certificados SSL, envía archivos estáticos, monitorea y automatiza despliegues usando herramientas como AWS, Nginx, UWSGI y Ansible.

- Profesor: Luis Martínez
- Fecha Inicio: 19/Junio/2025  
- Fecha Fin: 
- Guia : https://github.com/platzi/curso-flask/ 
- Curso Viejo -> https://platzi.com/clases/old/flask-19/ -> flask viejo curso 



## Clase 2: Conexión de Python con Servidores WEB: WSGI 

**Concepto**: 
- Cuando programamos en python en modo WEB este no retorna un HTML al servidor si no que retorna un tipo de OutPut basado en al protocolo WSGI
- WSGI : Es el standar que usan python tradicionarl reciben un request retorna un unico response y lo retorna al servidor 
- Ya python maneja ASG usa el asincronismo dentro de las aplicaciones de Python 

- *WSGI*: * Web Server Gateway Interface*, representa un estándar fundamental en el ecosistema de desarrollo web con Python. Se trata, en esencia, de una especificación que define la interacción entre los servidores web y las aplicaciones web escritas en Python
- *ASGI*: Asynchronous Server Gateway Interface, que es un estándar diseñado para facilitar la comunicación entre servidores web y aplicaciones web de manera asíncrona. 

*Librerias*
- Podemos Usar *Gunicorn* para darle el poder a python que pueda generar un request y response 

*Cuando Usarlo* 
- Tipo de Aplicación 
    - Si estas usando Django usas *WSGI*
    - Si estas usando APIREST puedes usar *ASGI*

- Uso comun 
    - *WSGI* aplicaciones web tradicionales 
    - *ASGI* aplicaciones web en tiempo real 

- Ejemplo de Servidores 
    - Gunicorn, uWSGI 
    - Uvicorn, Daphone   

- Framework 
    - Django, Flask
    - FASTAPI, Starlette, Django-ASGI 


## Clase 3: Versionamiento Semantico y Control de Versiones en Git 

**Concepto**: 
> Explicación logica de las veriones 
- Mayor Version: 1. :  
- Menor Version .0
- Path version: ..1

**Comandos**
- git tag: MNos genera una version de nuestra aplicación Ejemlo ´git tag -a v1.0.0 -m´
- Deja el mensaje con -m se aconseja primera version 

**Nota**: 
- El versionamiento segmantico siempre tienes que venir de una version estable 
- Se usa el Git Flow: Metodologia 
    - Main: Producción 
    - develop: Version estable para desarrollo 
    - feature/login: Requerimientos 
    - hotfix: en caso de un issue 

## Clase 4: Comando especiales para despliegue y configuración 

**Comandos**: 

- cd: moverme entre carpetas
- pwd: me indica saber donde estoy dentro del sistema  
- ssh -h: me permite usar unaconexion  usando internet para validar las conexiones  con servidores que estara  corriendo nuestro proyecto 
- git: maneja nuestro repo 
- curl -i url: me muestra ciertos valores web ´curl -i ww.google.com´
- dig : permite validar todos los permisos dns de un dominion ´dig ww.google.com´
- traceroute www.google.com: podemos ver las ip que se estan usando para conectar con el servidor final 
- vim: es un editor de texto  
- Buscar: primero abrimos el archivo vim nombre.txt luego /palabra podemos presionar la n de next para buscar la siguiente palabra podemos dar ESC y sin gurdar :q!

**Nota**:
- En configuración de servidores siempre usaremos terminal no tiene interfaz grafica
- siempre usaremos ssh para conectarnos a los servidores


## Clase 5: Uso de Variables de Entorno en Python con Archivos .env

**¿Cómo manejar variables de entorno y su importancia?**

Las variables de entorno son una herramienta poderosa que permite gestionar configuraciones que varían entre diferentes entornos, como local y producción, sin incorporar estos valores directamente en el código. Esta estrategia es esencial para mantener la seguridad y eficiencia en el desarrollo de software, eliminando la necesidad de modificaciones directas en el código fuente al cambiar de entorno.

**¿Qué son y cómo se crean las variables de entorno en Linux?**
- En Consola usamos el comando  ´export app_mode="local"´

**¿Cómo manejar las variables de entorno en Python?**

```python
import os

app_mode = os.environ.get('app_mode')
print(app_mode)

```
 
**¿Por qué es mejor usar archivos de configuración .env?**
- Podemos usar la libreroa dotenv =>  ´pip install python-dotenv´

```python
from dotenv import load_dotenv
import os

load_dotenv()

app_mode = os.getenv('APP_MODE')
secret = os.getenv('SECRET')
print(app_mode, secret)

```
**¿Cuáles son las mejores prácticas para utilizar archivos .env?**

- Seguridad: No incluyas archivos .env en los repositorios de código compartidos. Estos archivos pueden contener información sensible que no debería exponerse.

- Cohesión: Agrupa todas las configuraciones relacionadas en un único archivo. Esto facilita la gestión y el mantenimiento de las configuraciones en todos los entornos.

- Consistencia: Asegúrate de que todas las variables se definan de manera coherente y utilicen nombres descriptivos para su fácil identificación.

**Enlaces**
- https://share.doppler.com

## Clase 6: Elección y Configuración de Servidores en la Nube

**¿Qué son los servidores en la nube y cómo funcionan?**
Cuando escuchas que un servidor está "en la nube", realmente está ubicado en un centro de datos alrededor del mundo, como en Estados Unidos o Europa. 

**¿Cuáles son los recursos esenciales de un servidor?**

> Es importante conocer los tres recursos principales que componen un servidor, ya que impactan tanto en el rendimiento como en el costo del servicio.

- CPU (Unidad Central de Procesamiento): Encargada de procesar datos y ejecutar aplicaciones. Una CPU más potente generalmente implica un servidor más caro.

- Memoria RAM: Permite ejecutar varios procesos simultáneamente. Cuanta más RAM tenga un servidor, más procesos podrá manejar eficientemente.

- Almacenamiento: Existen diversos tipos de almacenamiento, como los discos SSD que son más rápidos al leer y escribir datos. Un ejemplo es el EBS de tipo GP3 de AWS.


## La Lección del "Costo Extra" en la Nube 💸

Los servicios en la nube son increíblemente flexibles en sus costos; puedes pagar solo por lo que usas. Pero aquí viene el punto clave:

Un bloque de código o una implementación mal optimizada podría costarnos unos centavos de más en cada ejecución. A simple vista, son detalles que no se notan.

Sin embargo, si tenemos un proyecto grande, con múltiples zonas de despliegue o bloques de código que, de manera eventual o masiva, disparan el uso de memoria, CPU y almacenamiento, esto genera un costo extra que no estaba previsto en el presupuesto.

Conclusión: Entender estos recursos no es solo tarea del equipo de DevOps. Cuando optimizas una consulta a la base de datos o reduces la carga de memoria de un endpoint, estás haciendo una contribución directa a la economía y sostenibilidad del proyecto. ¡Desarrollar eficientemente es desarrollar de forma rentable!

## Clase 7: Creación de Instancias en AWS: Paso a Paso para Principiantes

> nota ya tenemos cuenta aws 
> me falta una cuenata GPC
> Me falta Cuenta Oracle  => ofrece instancias gratuitas y con muy fáciles de configurar, y son gratutitas de por vida sin cobros

**Notas**
- En Amazon EC2 =>  "instancias EC2" para crear máquinas virtuales.
- En Amazon RDS =>  para Bases de datos 


Tambien podemos resaltar que GitHub nos permite tambien usar un mini servidor en la nube se le llama Automatización de Pruebas con GitHub Actions 🚀

> GitHub Actions es una herramienta de CI/CD integrada que automatiza el despliegue de tu proyecto Python.

Ventajas y Desventajas (Resumen)

- Ventajas 
    - Integración Nativa: Flujo de trabajo directo en GitHub.
    - Curva de Aprendizaje: El formato YAML y el debugging pueden ser complejos.
    - Gratis para Públicos: Ofrece una cuota generosa de minutos, ideal para proyectos de prueba.

- Desventajas

    - Límites de Ejecución: Los proyectos privados pueden agotar los minutos gratuitos, incurriendo en gastos.
    - Ecosistema: Amplio Marketplace de acciones preconstruidas (ej: setup-python).
    - Dependencia de GitHub: Si la plataforma falla, tu CI/CD se detiene.

## Pasos Mínimos para Desplegar (Esquema YAML)

- Crear archivo: Crear el archivo .github/workflows/despliegue.yml.
- Definir Disparador: Especificar que se ejecute al hacer push a una rama específica (main).
- Configurar Job: Usar un runner como runs-on: ubuntu-latest.
- Configurar Python: Usar la action actions/setup-python@v5.
- Instalar Dependencias: Ejecutar pip install -r requirements.txt.
- Desplegar: Ejecutar tu script de despliegue, usando Secrets de GitHub para las credenciales.

## Recomendaciones Anti-Cobro 💸

Para no agotar los minutos gratuitos:

- Limita Disparadores: No ejecutes el workflow en cada push a cualquier rama. Restringe las ejecuciones solo a ramas críticas (main) o permite la ejecución manual (workflow_dispatch).
- Usa Cache: Emplea la action actions/cache para guardar las dependencias de Python (el .venv). Esto evita reinstalar todo en cada ejecución y ahorra minutos de tiempo de cómputo.
- Monitorea tu Cuota: Revisa periódicamente el uso de tus minutos de Actions en la configuración de tu cuenta.

## Clase 8: Creación y Configuración de Instancias en AWS con Ubuntu

> Fuente : https://notebooklm.google.com/notebook/803f0206-582f-45c1-a531-970314713c26
> Fuente : https://aws.amazon.com/es/getting-started/hands-on/deploy-wordpress-with-amazon-rds/3

# ☁️ Pasos Detallados para Crear una Instancia EC2 en AWS

Este proceso te guía en la creación de una instancia EC2, ideal para entornos de prueba, aprovechando la capa gratuita de AWS.

## 📝 Paso 1. Elija una Amazon Machine Image (AMI)

Elige el "sistema operativo" de tu servidor.

1.  **Acceso a EC2:** Navega a la consola de AWS y dirígete al servicio **Amazon EC2**.
2.  **Iniciar el Asistente:** Haz clic en el botón azul **Lanzar instancia** para comenzar el proceso.
3.  **Selección de la AMI:** En la primera página, eliges la **Amazon Machine Image (AMI)**.
    * La AMI determina el *software* base, incluyendo el sistema operativo (Linux, Ubuntu, Windows, etc.).
    * **✅ Recomendación:** Selecciona la AMI de **Amazon Linux 2 (HVM)**, ya que es una opción muy popular y estable.

---

## ⚙️ Paso 2. Elija un Tipo de Instancia

Define el *hardware* de tu servidor (CPU, RAM, red).

1.  **Selección del Tipo:** Elige el tipo de instancia, que es la configuración específica de los recursos.
2.  **💰 Selección para Prueba:** Para evitar costos, selecciona el tipo de instancia **`t2.micro`**.
    * **Detalle *Free Tier*:** AWS permite ejecutar **750 horas al mes** de una instancia `t2.micro` dentro de la capa gratuita. ¡Perfecto para laboratorios!
3.  **Continuar:** Después de seleccionar `t2.micro`, haz clic en **Revisar y lanzar** para saltar las configuraciones avanzadas.

---

## 🛡️ Paso 3. Configure un Grupo de Seguridad

Define las reglas de red (el "cortafuegos") que controlan el tráfico.

Al llegar a la página de revisión, haz clic en el enlace **Editar grupos de seguridad**.

1.  **Configurar SSH (Acceso de Control):**
    * Debes permitir el tráfico **SSH** para poder conectarte de forma segura a la instancia y ejecutar comandos.
    * ⚠️ **Restringe el Origen:** Modifica la regla SSH existente para limitar el acceso solo a **tu dirección IP actual**. Esto es una práctica de seguridad esencial.
2.  **Configurar HTTP (Acceso Web):**
    * Añade una nueva regla para el tráfico **HTTP** (puerto 80) y permite el acceso desde **todas las direcciones IP** (`0.0.0.0/0`) para que los usuarios puedan ver tu sitio web (como WordPress).
    * Haga clic en **Agregar regla**, luego en el menú desplegable **Tipo** y selecciona **HTTP**.
3.  **Nombrar:** Asigna un nombre al Grupo de Seguridad (ej: **"wordpress"**) para facilitar su identificación.
4.  **Continuar:** Haz clic en el botón azul **Revisar y lanzar**.

---

## 🔑 Paso 4. Lance y Obtenga una Clave SSH

El último paso es lanzar y asegurar el acceso.

1.  **Lanzar la Instancia:** Haz clic en el botón azul **Lanzar**.
2.  **Configurar el Par de Claves:** Aparecerá un cuadro de diálogo para configurar el par de claves. Este archivo es la **llave digital** que usarás para conectar por SSH.
3.  **Creación y Descarga:**
    * Selecciona la opción **"Crear un nuevo par de claves"** y asígnale un nombre.
    * **¡Importante!** Haz clic en **Descargar par de claves** para guardar el archivo **`.pem`** en tu equipo. **Guárdalo de forma segura**, lo necesitarás después.
4.  **Lanzamiento Final:** Después de confirmar la descarga, haz clic en **Lanzar instancias**.

¡Felicidades! Tu instancia EC2 se estará creando. 🎉

## Clase 9: Conexión a Servidor mediante SSH y Llave .pem en Terminal Linux

> Podemos usar el comando ssh para acceder a la consola del servidor  

**Pasos**
- Paso 1: Podemos ejecutar ´ssh´ nos despliega las opciones 
![alt text](image.png)

- Paso 2: Podemos indentificarnos de la siguiente manera 
    - ´ssh -i [Nombre del archivo] [usuario]@[IP pública del servidor]´
    - Ejemplo ´ssh -i Python_server_Key.pem ubutun@34.202.113.209´ -> Este es del profesor
    - PD1: el PEM te lo genera al crear un servidor virtual 
    - PD2: ubutun@IP => lo podras ver en tu consonla web cuando generaste el servidor virtual  
![alt text](image-1.png)


- Paso 3: confirmamos la conexion 
![alt text](image-2.png)

- Paso 4: Regresamos al Paso 2 

- Paso 5: validar si estamos logueados 

![alt text](image-3.png)

- paso 6: podemos ver los procesos con htop

- paso 7: nos muestrad e amera logica los dorectorios df -h

- paso 8: who para indicar quien 


## Clase 10: Gestion de paquetes y configuraciones de servidores ubuntu 
**¿Qué es APT y cómo usarlo en Ubuntu?**
> APT es una herramienta esencial en cualquier servidor que corra sobre Ubuntu, ya que es el manejador predeterminado para la instalación y desinstalación de paquetes.

**Comandos Básicos Debian/Ubuntu** 
Ya te proporcioné una tabla en Markdown en mi respuesta anterior, pero ¡entiendo que quieres el formato más limpio posible!

Aquí tienes la misma información de validación y complemento de comandos en una tabla Markdown concisa, lista para copiar y pegar:

---

## Comandos Esenciales de Linux y Desarrollo

| Comando | Propósito Validado y Complementado |
| :--- | :--- |
| `sudo apt update` | **Actualiza el índice local de paquetes disponibles** (el catálogo de software), **no instala** software. |
| `apt list --upgradable` | Muestra una lista de todos los **paquetes instalados** que tienen una versión más reciente disponible para ser descargada. |
| `sudo apt upgrade` | **Descarga e instala** las versiones más recientes de los paquetes listados, aplicando mejoras y correcciones. |
| `sudo apt install nginx` | Instala **NGINX**, un servidor web. En desarrollo, actúa como **proxy inverso** o servidor de archivos estáticos delante de tu aplicación Python. |
| `sudo service nginx status` | Verifica el **estado actual del servicio NGINX** (activo, inactivo, fallido). *Alternativa moderna:* `sudo systemctl status nginx`. |
| `sudo service nginx restart` | **Reinicia el servicio NGINX.** Necesario después de modificar su configuración. *Alternativa moderna:* `sudo systemctl restart nginx`. |
| `sudo apt install git` | Instala **Git**, el sistema de **control de versiones distribuido** fundamental para el desarrollo de software y la colaboración. |
| `sudo nginx -t` | Valida cambios en nginx |
| `ls -lah` | valida link simbolicos  |


## Clase 11: Configuración de DNS y NginX para aplicaciones web en Django 

> NginX: Nos permite configurar nuestro propio servidor seguiremos algunas buenas practicas pero antes se debe explicar los directorios para un mejor entendimiento: 
**Conceptos**
- En Ubuntu al instalar ngix encontraremos los files system en el Directorio ´/etc/ngix´
![Directorio Nginx ](image-4.png)

- Dicho directorio se divide en: 

/etc/nginx/
├── conf.d/             # Fragmentos de configuración incluidos automáticamente (ej. proxy, caché)
├── fastcgi.conf        # Archivo principal de configuración de FastCGI
├── fastcgi_params      # Parámetros estándar para FastCGI (usado con PHP)
├── mime.types          # Definiciones de tipos MIME para el manejo de archivos
├── nginx.conf          # Archivo de configuración global y principal de Nginx
├── proxy_params        # Parámetros estándar para configuraciones de proxy inverso
├── scgi_params         # Parámetros para el protocolo SCGI
├── sites-available/    # Configuraciones completas de sitios web disponibles (inactivos por defecto)
├── sites-enabled/      # Enlaces simbólicos a sitios activos en sites-available/
├── snippets/           # Bloques de configuración reutilizables (ej. ajustes SSL)
├── uwsgi_params        # Parámetros para el protocolo uWSGI (usado con Python)
├── modules-available/  # Módulos dinámicos disponibles para cargar
└── modules-enabled/    # Enlaces simbólicos a los módulos dinámicos activos



| Archivo/Directorio | Propósito Principal |
| :--- | :--- |
| **`nginx.conf`** | **Archivo de Configuración Principal.** Contiene las directivas globales que definen el funcionamiento de Nginx (configuración de *worker processes*, módulos, la ruta a los archivos de log, y la inclusión de otros archivos). |
| **`conf.d`** | **Fragmentos de Configuración Adicionales.** Directorio utilizado para alojar pequeños archivos de configuración (`.conf`) que son automáticamente incluidos por el archivo principal `nginx.conf`. Se usa comúnmente para configuraciones de proxy, caché o *snippets* específicos. |
| **`sites-available`** | **Configuraciones de Sitios Web Disponibles.** Contiene los archivos de configuración completos para cada sitio web o aplicación que podrías alojar. Estos archivos *no están activos* hasta que se crea un enlace simbólico en `sites-enabled`. |
| **`sites-enabled`** | **Configuraciones de Sitios Web Activas.** Contiene **enlaces simbólicos** que apuntan a los archivos dentro de `sites-available`. Solo las configuraciones listadas aquí son cargadas por Nginx y están activas. |
| **`snippets`** | **Fragmentos Reutilizables.** Directorio para guardar pequeños bloques de configuración que se repiten y pueden ser incluidos fácilmente en múltiples archivos de configuración de sitios (ej. ajustes de SSL, configuración de *caching* común, etc.). |
| **`fastcgi_params`** | **Parámetros de FastCGI.** Contiene un conjunto de parámetros que se pasan al proceso *backend* FastCGI (típicamente usado para ejecutar PHP). |
| **`fastcgi.conf`** | **Configuración de FastCGI.** Archivo que incluye los `fastcgi_params` y añade directivas específicas de FastCGI. |
| **`proxy_params`** | **Parámetros de Proxy.** Contiene directivas (generalmente encabezados HTTP) que se pasan a un servidor *backend* cuando Nginx actúa como un proxy inverso (que es su uso más común). |
| **`scgi_params`** | **Parámetros de SCGI.** Similar a FastCGI, contiene parámetros para el protocolo SCGI, menos común que FastCGI. |
| **`uwsgi_params`** | **Parámetros de uWSGI.** Similar a FastCGI, contiene parámetros para el protocolo uWSGI, comúnmente usado para aplicaciones Python. |
| **`mime.types`** | **Tipos MIME.** Define la correlación entre las extensiones de archivos y su correspondiente tipo MIME para que Nginx sepa cómo servir correctamente cada tipo de archivo al navegador. |
| **`modules-available`** | **Módulos Dinámicos Disponibles.** Directorio que contiene módulos de Nginx que están disponibles para ser cargados, pero no están activos por defecto. |
| **`modules-enabled`** | **Módulos Dinámicos Activos.** Contiene enlaces simbólicos a los módulos en `modules-available` que han sido activados para su uso en la configuración actual. |
| **`koi-utf`, `koi-win`, `win-utf`** | **Mapas de Codificación de Caracteres.** Archivos de soporte para la conversión de codificación de caracteres, principalmente relacionados con idiomas del este de Europa. |

**Pasos**
- Paso 1: Debemos ingresar al directorio ´sites-available´ como lo indica la explicación aqui podremos crear todos los config que necesitamos por cada proyecto para este caso de la clase creamos un ejemplo llamado deployment paso 2. 
- Paso 2: podemos crear el archivo: 'sudo vim deploywithpython.com.conf' 
- Paso 3: En el archivo creado podemos generar las especificaciones del servicio [Aqui me toca investigar ya que esto es basico]

```batch

server {
    listen 80;
    server_name deployewithpython.com;
    location / {
        return 200 'Hola desde el archivo the conf';
        add_header Content-Type text/plain;
    }
}

```
    - Queda de esta manera
![alt text](image-5.png)

- Paso 4: luego de crear el conf, debemos habilitar esa configuracion para eso nos recorremos al siguiente directorio que se llama ´sites-enabled´ = cd sites-enabled
    - Debemos crear un link simbolico lo podemos crear de la siguiente manera: 
    - ´sudo ln -s ../sites-available/deploywithpython.com.conf .´ link simbolico funciona de la siguiente manera ´sudo ln -s [Lugar Origen] [Lugar Destino]´ en este caso el [.] es root
    - Validar si quedo de manera correcta ls -lah

- Paso 5: Podemos usar el comando para validar si los cambios estan correctos 
    - ´sudo nginx -t´
    - ´sudo service nginx restart´ cada vez que hacemos cambios hay que reiniciar

## Clase 12: 

## Clase 13: 

## Clase 14: 

## Clase 15: 

## Clase 16: 

## Clase 17: 

## Clase 18: 

## Clase 19: 

## Clase 20: 