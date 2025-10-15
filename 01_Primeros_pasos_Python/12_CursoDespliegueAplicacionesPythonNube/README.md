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

## Clase 12: Configuración de Certificados SSL con Certbot y Nginx

**¿Por qué es importante usar un certificado SSL?**

- En la actualidad, mantener la seguridad al visitar sitios web es fundamental. 
- Utilizar el puerto 80 con el protocolo HTTP ya no es seguro, razón por la cual la mayoría de los sitios han migrado al puerto 443 usando un certificado SSL. 
- Esto permite una conexión encriptada entre el navegador del usuario y el servidor, protegiendo la información contra posibles interceptaciones. 


**¿Cómo instalar Servbot y sus dependencias?**

1. Abre la terminal de tu servidor.

2. Ejecuta el siguiente comando para instalar Servbot y Python 3:

´sudo apt install certbot python3-certbot-nginx´

3. Una vez instalados, toma nota de todos los paquetes que se hayan instalado para futuras referencias.

**¿Cuál es el proceso para generar un certificado SSL?**

1. Ejecutamos el comando =>  ´sudo certbot --nginx´

2. Introduce un correo electrónico válido. Este se usará para notificaciones sobre la expiración del certificado o problemas de seguridad.

3. Acepta los términos y condiciones.

4. Decide si quieres notificar a Servbot una vez que tu certificado sea creado correctamente, lo cual es útil para estadísticas.

> PD: Es importante seleccionar el dominio correcto al que deseas aplicar el certificado. Si en tu servidor hay varios configurados, deberás elegir el adecuado. El sistema te mostrará los dominios disponibles para que selecciones el tuyo.

## Clase 13: Configuración de Servidor para Despliegue de Aplicaciones Django 

**¿Cómo configurar un servidor para clonar un repositorio de Python?**

Configurar un servidor para clonar un repositorio de Python es un paso crucial para el despliegue de aplicaciones web. Aquí te guiamos en la preparación de tu servidor para trabajar con proyectos en Python utilizando un repositorio alojado en una plataforma como GitHub, garantizando que tengas todo listo para ejecutar tu aplicación.



**Enlaces**
- https://platzi.com/cursos/deploying-python/72368-configuracion-de-servidores-web-y-aplicacion


**¿Qué pasos seguir para preparar el servidor?**

1. Clonación y Configuración de Carpetas:

    - Conéctate al servidor utilizando SSH con la llave generada previamente.
    - Crea un directorio seguro dentro del servidor para tus aplicaciones:
        ´sudo mkdir /srv/apps´
    - Asegúrate de que el usuario correcto tenga permisos sobre estas carpetas:
        ´sudo chown ubuntu:ubuntu /srv/apps´

**2. Clonar el Repositorio de Git:**
    - Usa el comando git clone para traer el repositorio al servidor. Recuerda especificar un nombre para la carpeta clonada:
        ´git clone <URL-del-repositorio> Django-basic-production´

    - Soluciona permisos si es necesario ajustando la propiedad de las carpetas.

**¿Cómo configurar un entorno virtual y dependencias?**
    
    1. Crear un entorno virtual y manejar las dependencias es clave para aislar el entorno de desarrollo y evitar conflictos entre proyectos.

    - Crear un entorno virtual:

    - Crea una carpeta para tus entornos virtuales y un entorno nuevo:
        - mkdir .envs
        - python3 -m venv .envs/Django-basic-production

    2. Instalar Dependencias:

    - Activa el entorno virtual:
    - source .envs/Django-basic-production/bin/activate

    3 Instala las dependencias listadas en requirements.txt:
    - pip install -r requirements.txt


**¿Cómo ejecutar y servir la aplicación de Django?**

    > Finalmente, una vez que la aplicación está configurada, es hora de servirla para que sea accesible.

    1. Configura el servidor de aplicaciones:

        - Instala y usa Gunicorn para servir tu aplicación:
            - pip install gunicorn

        - Ejecuta el servidor de aplicaciones:
            - gunicorn --bind 0.0.0.0:8000 config.wsgi:application

    2. Ajusta Grupos de Seguridad y Configura Host Permitidos:

    - Agrega las IPs en el archivo de configuración de Django (ALLOWED_HOSTS) y ajusta las reglas de seguridad de AWS para aceptar el puerto 8000.

## Clase 14: Configuración de UWSGI para Despliegue de Aplicaciones Python

**¿Cómo configurar nuestra aplicación Python utilizando UWSGI?**

Configurar una aplicación Python utilizando UWSGI es un proceso que te permitirá mejorar el manejo de recursos y asegurar la ejecución eficiente de tu servidor. Veamos cómo puedes realizar esta configuración.

**¿Qué debemos instalar para comenzar?**
Primero, necesitamos conectarnos al servidor e instalar UWSGI. Ejecuta el siguiente comando en tu terminal para instalar UWSGI, junto con su plugin para Python:


```batch
sudo apt install uwsgi
sudo apt install uwsgi-plugin-python3
```
Este plugin es crucial ya que UWSGI admite múltiples tipos de aplicaciones, pero necesitamos especificar que vamos a trabajar con aplicaciones de Python.

**¿Cómo validar la instalación de UWSGI?**

Una vez instalado, valida que UWSGI esté funcionando correctamente ejecutando:
```batch
uwsgi
```

En este punto, debes ver todos los parámetros configurados por defecto, como el tamaño de memoria y el número de procesos que pueden ejecutarse.


**¿Cómo crear el archivo de configuración de UWSGI?**

- Dirígete al directorio de configuraciones de UWSGI ubicado generalmente en /etc/uwsgi. 
- Debes crear un archivo de configuración para tu aplicación:
- Crea el archivo de configuración en la carpeta apps-available usando vim o tu editor preferido:
- ´sudo vim /etc/uwsgi/apps-available/nombre-aplicacion-production.ini´
- En el archivo .ini, define las siguientes configuraciones:

```batch
[uwsgi]
module = config.wsgi:application
plugins = python3
socket = /tmp/nombre-aplicacion-production.sock
chdir = Ruta/absoluta/a/tu/proyecto
home = Ruta/entorno/virtual
env = DJANGO_SETTINGS_MODULE=configuracion.settings
master = true
processes = 4
module: Especifica el módulo Python que debe ejecutarse.
plugins: Indica que se usará el plugin de Python3.
socket: Define la comunicación entre UWSGI y Nginx.
chdir y home: Establecen el directorio de trabajo y el entorno virtual para tu aplicación.
env: Configura las variables de entorno necesarias para ejecutar la aplicación.
master: Habilita el proceso máster que supervisa otros procesos.
processes: Configura la cantidad de procesos que deseas ejecutar.

```

```batch
module = config.wsgi:application

plugins = python3

socket = /tmp/deployment-produccion.sock

chdir = /home/ubuntu/srv/apps/deployment-produccion

home = ../.envs/deployment-produccion

env = DJANGO\_SETTINGS\_MODULE=config.settings

master = true

processes = 4

```

**¿Cómo habilitar y validar que tu aplicación está en ejecución?**

- Para activar tu aplicación, crea un enlace simbólico en la carpeta apps-enabled:

´sudo ln -s /etc/uwsgi/apps-available/nombre-aplicacion-production.ini /etc/uwsgi/apps-enabled/´

- Verifica que tu aplicación esté corriendo correctamente:

- Reinicia UWSGI:
- ´sudo service uwsgi restart´

- Usa htop para monitorear los procesos:
- ´htop´

- Presiona F4 y filtra por uwsgi para ver los procesos activos. Deberías ver varios procesos, incluyendo el proceso máster.

- Confirma que el socket funciona verificando su existencia en /tmp:

´ls /tmp/´

- Y ahí lo tienes. Una vez que tu archivo de configuración esté activado y los enlaces simbólicos correctos, tu aplicación estará lista para manejar solicitudes mediante UWSGI y Nginx.

**¿Qué hacer si encuentras problemas?**
Si no ves los procesos en ejecución, puedes verificar con:

´sudo service uwsgi status´
- Asegúrate que no haya errores en los enlaces simbólicos o configuraciones incorrectas dentro del archivo .ini.



**Comandos**
- ´history | grep ln´ => Permite ver tu historial de los comando ejecutados 


## Clase 15: Configuración de Proxy Reverso con Nginx y UWSGI en Python

¿Cómo conectar un socket UWSGI con Nginx?
Conectar un socket de UWSGI con Nginx es un paso clave en el proceso de despliegue de aplicaciones en Python. UWSGI crea un archivo de socket que será utilizado por servicios como Nginx para mostrar la aplicación en un navegador web. Sin esta conexión, la aplicación no es accesible para los usuarios.

¿Qué es un proxy reverso?
El concepto de proxy reverso juega un papel fundamental aquí. Un proxy reverso es un servidor que se coloca delante de servidores web para dirigir las peticiones de los usuarios al servidor adecuado. En este caso, Nginx actúa como proxy reverso conectándose al socket y redirigiendo las solicitudes a UWSGI.

¿Cómo configurar Nginx?
Para conectar Nginx con UWSGI, sigue estos pasos:

Accede a la configuración de Nginx:

Usa la terminal para navegar a la carpeta de configuración de Nginx (/etc/nginx).
Ejecuta ls para listar los archivos y busca sites-available y sites-enabled.
Editar el archivo de configuración:

Con el comando cat, revisa el archivo en sites-available que corresponde a tu dominio.
Para hacer cambios, utiliza un editor como vim con privilegios de superusuario (sudo).
Modificar las configuraciones:

Borra las líneas temporales con el comando que duplica la tecla D (DD) en vim.
Incluye las nuevas configuraciones, como include y las configuraciones de UWSGI.
Usa uwsgi_pass con el protocolo unix para pasar el socket correcto a Nginx.
Asegúrate de finalizar cada línea con un punto y coma ;.
Validar y reiniciar Nginx:

Antes de reiniciar Nginx, valida los cambios con nginx -t para comprobar que la sintaxis es correcta.
Si es así, reinicia el servicio con sudo service nginx restart.
Con estos pasos, habrás conectado exitosamente tu dominio con la aplicación Python usando Nginx y UWSGI.

¿Cómo añadir salud de verificación con Nginx?
Un elemento crucial del despliegue es comprobar la salud del sistema. Aprende a crear un endpoint de verificación en Nginx para asegurar que los sistemas funcionan correctamente.

¿Por qué es importante un estado de verificación?
Cuando tienes varios procesos ejecutándose, como Nginx y UWSGI, uno de ellos puede fallar y causar un error 500 en tu sitio. Un endpoint de verificación te permitirá monitorizar y validar si al menos uno de los servicios está funcionando.

¿Cómo configurarlo?
Abre el archivo de configuración de Nginx:

Sigue los mismos pasos anteriores para acceder y editar el archivo de configuración.
Agrega una nueva locación:

Añade una sección location que apunte a un nuevo endpoint, por ejemplo, /status.
Configura lo que se mostrará cuando se acceda a este endpoint.
Revisa y reinicia:

Una vez configurado, guarda los cambios.
Valida la configuración de nuevo con nginx -t.
Si todo está correcto, reinicia el servicio de Nginx.


## Clase 16: Configuración de Logs en Nginx y UWSGI para Aplicaciones Python

**¿Por qué es crucial configurar logs en tus aplicaciones Python?**
Al desplegar nuestras aplicaciones Python, es normal que funcionen correctamente en un principio. Sin embargo, a medida que se realizan cambios o se presentan escenarios específicos, pueden surgir errores. Configurar logs detallados es esencial no solo para detectar fallas más fácilmente, sino también para agruparlos de acuerdo a la aplicación en ejecución, simplificando el proceso de diagnóstico y corrección. Los logs permiten identificar y resolver problemas de manera eficiente al proveer registros históricos de los eventos y errores que se presentan.

**¿Cómo estructurar logs en aplicaciones Django con Nginx y UWSGI?**
Para optimizar la gestión de logs, es importante agruparlos dentro de tus aplicaciones Django, alineados con servidores web como Nginx y gestores de aplicaciones como UWSGI. A continuación, se describe la metodología para alcanzar este objetivo:

1. Ramas Git y cambios en código:

	- Utiliza ramas como develop para crear y probar cambios antes de fusionarlos a main o producción.
	- Verifica y aplica migraciones o actualizaciones según los cambios realizados.

2. Revisar e instalar nuevas dependencias:

	- Activa el entorno virtual y ejecuta:
	- pip install -r requirements.txt
	- Reinicia el servicio de aplicación con:
	- sudo service uwsgi restart

3. Comprender la importancia de los logs:

	- Los logs fijan la base para identificar errores, especialmente detectando códigos de respuesta HTTP (como 400, 500, etc.) y sus causas subyacentes.

4. Estrategia para depuración y logs de seguridad:

	- Temporalmente habilita el modo de depuración en Django, pero ten cuidado de no dejarlo activo en producción, ya que expone información sensible como direcciones IP y detalles de configuración.
	- Al resolver el problema, desactiva el debug y verifica que las configuraciones vuelvan a su estado original para mantener la seguridad.

5. Agrupar y estructurar logs en Nginx:

	- Edita el archivo de configuración de Nginx (e.g., en /etc/nginx/sites-enabled/) para especificar ubicaciones de logs separados:
	- access_log /var/log/nginx/deploy_with_python_access.log;
	- error_log /var/log/nginx/deploy_with_python_error.log;
	- Verifica la configuración con:
	- sudo nginx -t
	- Reinicia Nginx para aplicar los cambios:
	- sudo service nginx restart

**¿Cómo supervisar los logs para un análisis eficaz?**
- Después de configurar los logs correctamente, es hora de realizar un seguimiento proactivo:


	1. Supervisión de logs dinámicos:
	- Puedes usar el comando tail para seguir los cambios en tiempo real en tus archivos de logs:
	- sudo tail -f /var/log/nginx/deploy_with_python_access.log

	2. Identificar y verificar peticiones y errores:
	- Usa los logs para ver las peticiones recibidas y verifica códigos de respuesta HTTP para detectar incidentes o confirmar una operación normal.

## Clase 17: Monitoreo de Errores en Django con Centry y Configuración de Logs

**¿Por qué es importante monitorear los errores en aplicaciones?**
Imagina tener que revisar constantemente los registros de errores para asegurarte de que tu aplicación esté funcionando correctamente. Sería una tarea ardua y poco práctica, ¿verdad? Por suerte, existen herramientas que automatizan este proceso, enviándonos alertas cuando algo anda mal. En esta guía, exploraremos cómo Centry, una herramienta poderosa y eficiente, nos ayuda a lograrlo.

**¿Cómo integrar Centry con un proyecto de Python?**
1. Creación de una cuenta en Centry
	- Para comenzar, necesitas crear una cuenta en Centry, la plataforma que nos permitirá monitorear automáticamente los errores de nuestra aplicación. Sigue estos pasos:
	- Visita la página web de Centry (centry.io).
	- Haz clic en el botón "Get Started".
	- Completa tus datos personales.
	- Selecciona la región donde deseas guardar tus datos (Europa o Estados Unidos, según prefieras).
	- Opcionalmente, suscríbete para recibir actualizaciones por correo y acepta los términos y condiciones.

2. Configuración de Centry en Django
	- Una vez que hayas creado tu cuenta, selecciona el framework de tu proyecto. En este caso, usaremos Django. Sigue los pasos descritos a continuación para configurar Centry:
	Configura el SDK: Esto te mostrará cómo instalar las dependencias necesarias.
	- Instala las dependencias en tu máquina local (o directamente en el servidor, si prefieres).
	- Activa el entorno virtual de tu proyecto.
	- Agrega la siguiente información al archivo settings.py al final del archivo:
```python 
	# Configuración de Centry
	SENTRY_DSN = 'tu_dsn_aquí' #esto lo podemos extraer de la pagina 

```	
	- Modifica el archivo urls.py para introducir un error intencionado que te permita comprobar la integración:
```python 
# Código en urls.py con error intencionado
def error_view(request):
    return 1 / 0
```	


**¿Cómo identificar y resolver errores usando Centry?**
- Después de configurar Centry, es momento de probar su eficacia. Intenta acceder a la URL que desencadenará el error intencionado. Deberías recibir un error de respuesta al cargar la página. Ahora, veamos los detalles del error en la plataforma de Centry.

1. Revisión y corrección de errores
	- Al acceder a Centry, verás que se registró el error recibido.
	- Haz clic en el error específico para ver detalles: URL, transacción, código de estado HTTP, entre otros.
	- Localiza el archivo y la línea donde ocurrió el error.
	- Corrige el error. En este caso, asegúrate de agregar una coma que falta en el archivo problemático.
	
	Gracias a Centry, no necesitas navegar por registros extensos para encontrar errores. La herramienta te ayudará a mantener la operatividad de tu aplicación de una manera simplificada.

**¿Cómo configurar alertas y administrar logs?**
	- Además de su capacidad para capturar errores, Centry ofrece funcionalidades de alerta y administración de logs que optimizan aún más la eficiencia del monitoreo de aplicaciones.

**Configuración de alertas**
	- Las alertas se pueden configurar para que se envíen directamente a tu correo electrónico.
	- Alternativamente, es posible integrarlas con sistemas de mensajería como Slack, garantizando que te mantengas informado en tiempo real.
	- Organización y gestión de logs

**Para evitar que los registros sean abrumadores, es conveniente organizarlos:**

Configura tu sistema de logs para agrupar registros por aplicación, fecha o día.
Edita el archivo de configuración de tu aplicación para incluir parámetros como log sucx y Demon Eyes. Esto permitirá que los archivos de log incluyan un número con cada cambio de día y se inicien con una marca de tiempo.

**ENLACE**
- https://sentry.io/welcome

## Clase 18: Configuración de Variables de Entorno en Servidor Django

**¿Cómo se configura el servidor y los archivos de aplicación de forma óptima?**
> Al configurar un servidor y modificar los archivos de una aplicación, es crucial asegurarse de que los cambios realizados cumplen con los estándares necesarios para la correcta operación en un entorno de producción. Esto implica gestionar modificaciones de manera estructurada, evitando prácticas poco recomendables, como cambiar archivos directamente en el servidor. Aprenderemos a manejar estos aspectos aprovechando herramientas como Git y archivos de entorno.

**¿Cómo utilizamos Git para gestionar los cambios?**
> Al realizar cambios en un servidor, es vital utilizar una herramienta de control de versiones como Git para mantener un seguimiento de las modificaciones. Para esto se puede:

Realizar un git status para verificar los archivos modificados.
Utilizar git diff para observar específicamente qué partes del archivo han cambiado, por ejemplo, cambios en allow host o instalación de sentry.
Trabajar siempre desde una rama de desarrollo (por ejemplo, develop) para gestionar cambios y pruebas.

**¿Qué son y cómo manejamos las variables de entorno?**
Las variables de entorno son claves fundamentales para la configuración de una aplicación. En proyectos como los realizados con Django, algunos ejemplos cruciales incluyen:

SECRET_KEY: Clave utilizada para encriptar datos.
DEBUG: Para mostrar detalles de errores en el navegador.
SENTRY_DSN: Clave para configurar Sentry, herramienta de monitoreo de errores.
ALLOWED_HOSTS: Lista de dominios permitidos para la aplicación.
DATABASE_URL: URL para la configuración de la base de datos.

**¿Cómo configuro las variables de entorno adecuadamente?**
Configurar las variables de entorno es un paso esencial para asegurar que la aplicación sea segura y funcione correctamente. Sigamos estos pasos:

Creación de un archivo .env: Utilizando un editor como Vim, crea un archivo .env donde añadirás las variables de entorno.
vim .env
Copiar y pegar valores: Añade valores como SENTRY_DSN desde tu cuenta Sentry, el host permitido desde la documentación, y otros valores necesarios:
SENTRY_DSN=<tu_valor_dsn_aquí>
ALLOWED_HOSTS=deploymentbit.python.local
Reinicio del servidor: Para que los cambios surtan efecto, reinicia el servidor UWSGI con:
sudo service uwsgi restart

## Clase 19: Instalación y Configuración de PostgreSQL en Ubuntu para Django

**¿Cómo instalar y configurar PostgreSQL en un servidor Ubuntu?**

Instalar y configurar PostgreSQL en un servidor Ubuntu es una habilidad esencial para desarrolladores que desean manejar bases de datos de manera eficaz y segura. El proceso no solo implica la instalación del motor de bases de datos, sino también la creación de usuarios y bases de datos, así como la conexión de estas a un proyecto Django. Aprende a hacerlo siguiendo estos pasos detallados.

**¿Cuáles son los pasos para instalar PostgreSQL?**
Actualizar la lista de paquetes:

Conéctate a tu servidor usando el comando SSH y la clave de identificación.
Ejecuta el siguiente comando para actualizar la lista de paquetes disponibles:
sudo apt update
Instalar PostgreSQL:

Después de actualizar la lista de paquetes, instala PostgreSQL usando:
sudo apt install postgresql
Asegúrate de verificar que el servicio esté activo:
sudo service postgresql status


**¿Cómo crear un usuario y una base de datos en PostgreSQL?**

Una vez instalado PostgreSQL, es crucial crear un usuario y una base de datos que puedas conectar a tu aplicación.

1. Conectar a la consola de PostgreSQL:

- Cambia al usuario postgres para gestionar la base de datos:
- ´sudo -i -u postgres´
- Ingresa al gestor de bases de datos:
- ´psql´

2. Crear un nuevo usuario:

- Ejecuta el comando para crear un usuario:
- CREATE USER usuario_platzi WITH PASSWORD 'paz';

3. Crear una base de datos:

- Crea una nueva base de datos y establece al usuario como propietario:
- CREATE DATABASE dv_platzi OWNER usuario_platzi;
- Lista todas las bases de datos para verificar la creación:
- ´\l´

**¿Cómo conectar Django a PostgreSQL?**

Para conectar tu proyecto de Django con la base de datos PostgreSQL, es necesario revisar y ajustar la configuración del archivo .env.

Configurar la URL de la base de datos:

- Abre el archivo .env de tu aplicación y especifica la variable DATABASE_URL como sigue:
- DATABASE_URL=postgresql://usuario_platzi:paz@localhost:5432/dv_platzi

- Activar el entorno virtual y migrar:

- Activa el entorno virtual de tu proyecto:
- source venv/bin/activate
- Ejecuta las migraciones de Django para confirmar que todo está configurado correctamente:
- python manage.py migrate
- Las tablas deben crearse correctamente en la base de datos.

## Clase 20: Configuración de Instancias RDS en AWS para Bases de Datos


**¿Cómo configurar una instancia de base de datos en AWS?**
Configurar una instancia de base de datos en Amazon Web Services (AWS) es esencial para desplegar aplicaciones en producción sin preocuparse por las tareas manuales que normalmente implicarían mucho esfuerzo, como los backups y las actualizaciones. AWS proporciona un servicio llamado RDS (Relational Database Service), el cual facilita estos procesos. A continuación, te guiaré paso a paso por la configuración de una instancia de base de datos en AWS.

**¿Qué es el servicio RDS de AWS?**
RDS es un servicio de base de datos administrada que ayuda a las aplicaciones a operar sin la sobrecarga de gestionar datacenters, servidores, y servicios de actualización. Algunas funcionalidades claves de RDS incluyen:

- Automatización de copias de seguridad y actualizaciones: Reduce el trabajo manual y asegura que la base de datos esté al día.
- Escalabilidad: Permite ajustar los recursos según las necesidades de tu aplicación.
- Alta disponibilidad: Proporciona replicación de datos y failover automático en distintas zonas de disponibilidad.

**¿Cómo acceder y crear una instancia en RDS?**
Para comenzar, primero inicia sesión en la consola de AWS y sigue estos pasos:

En el dashboard de servicios de AWS, busca "RDS" y haz clic en él.
Haz clic en "DB Instances" y selecciona "Create Database".
Elige la opción "Standard create" para tener control sobre la configuración.
Aquí se pueden seleccionar diferentes motores de base de datos, como PostgreSQL. Opta por "Aurora" si se requiere este tipo específico de base de datos.

- Selecciona: Estándar create.
- Elige el motor: PostgreSQL.
- Versión: Deja la versión por defecto.

**¿Qué configuración inicial es necesaria para la instancia?**
A continuación, decide el entorno y los recursos para tu base de datos:

Entorno Productivo vs. Dev/Test: Escoge el entorno basado en el tráfico y el rendimiento esperado. Las instancias productivas son más robustas y garantizan alta disponibilidad.
Nombre del DB: Asigna un nombre significativo, como "platzi_database".
Usuario y llaves de encriptación: Utiliza "Postgres" como usuario por defecto y opta por dejar las llaves de encriptación predeterminadas para proteger los datos.

**¿Cómo configurar almacenamiento y seguridad?**
La optimización de E/S es vital para el rendimiento:

Almacenamiento: Elige "EO optimized" si buscas mejorar la entrada-salida (I/O).
Conectividad: Configura el acceso solo desde una instancia EC2.
Esto último es crucial, ya que, para mejorar la seguridad, se debe restringir el acceso a la base de datos desde ciertas IPs y servidores. De este modo, aunque se tenga conocimiento del usuario y contraseña, la base de datos no estará accesible públicamente.

¿Cómo conectar desde una instancia EC2?
Tras completar la configuración inicial y una vez que la base de datos esté disponible, sigue estos pasos para conectarte desde una instancia EC2 usando PostgreSQL:

psql -h <host_endpoint> -U Postgres -d Postgres
Para obtener el <host_endpoint>, dirígete al detalle de la base de datos en el dashboard de AWS RDS. A continuación, ingresar la contraseña solicitada.

**¿Cuáles son los próximos pasos?**
Una vez conectado, es posible crear estructuras adicionales en la base de datos o ejecutar migraciones:

Crear una nueva base de datos:
CREATE DATABASE rds_platzi OWNER Postgres;
Modificar el archivo de configuración: Edita el archivo .env para reflejar esta nueva conexión y confirma que las migraciones ejecuten correctamente.
Finalmente, un ejercicio recomendado es eliminar el PostgreSQL instalado en tu servidor web tradicional. Esto no solo reduce la carga del servidor web, sino que también optimiza el rendimiento y la eficacia de tu entorno de producción al manejar la base de datos través de RDS de AWS.

Configurar instancias a través de AWS RDS no solo asegura integridad y disponibilidad de los datos, sino que además permite centrar esfuerzos en el desarrollo de tu aplicación. ¡Sigue explorando y optimizando tus habilidades en AWS!

## Clase 21: Configuración de Archivos Estáticos en Django y Nginx

**¿Cómo podemos configurar archivos estáticos en Django y Nginx?**

Los archivos estáticos, como imágenes, CSS y JavaScript, son fundamentales para el correcto funcionamiento de una aplicación web, haciéndola más rápida y atractiva al usuario. En esta guía, exploraremos cómo configurar estos archivos con Django y Nginx, garantizando su correcta implementación y resolución de errores comunes.

**¿Cómo lidiar con un error 404 al cargar archivos estáticos?**
Si al intentar acceder a tu aplicación de Django en el entorno de administración observas un diseño pobre y detectas un error 404 en URLs que intentan acceder a archivos estáticos, es probable que el problema esté en la configuración de tu servidor para manejar dichos archivos. Aquí te sugerimos un enfoque:

Verifica la configuración de almacenamiento:

Asegúrate de que tu aplicación no está intentando utilizar un servicio de almacenamiento de terceros, como Amazon S3, si no está configurado.
En el código de configuración, revisa la sección relacionada con STATIC_URL y STATIC_ROOT. Estos deben estar dirigidos correctamente a las carpetas en el servidor.
Generar archivos estáticos:

**Utiliza el comando collectstatic de Django para recopilar todos los archivos estáticos en la carpeta configurada:**

- ´python manage.py collectstatic´

Asegúrate de que la carpeta generada es accesible por tu servidor web.

**¿Cómo configurar Nginx para servir archivos estáticos?**
Una vez que los archivos estáticos estén correctamente recopilados, el siguiente paso es configurar Nginx para servirlos. Sigue estos pasos para hacerlo:

Editar la configuración de Nginx:

Accede al archivo de configuración de Nginx (por ejemplo, etc/nginx/sites-enabled/tu_sitio) y añade una nueva location para servir los archivos estáticos.
location /static/ {
    alias /ruta/completa/a/tu/static/files/;
}
Validar y reiniciar Nginx:

Después de guardar tus cambios, siempre valida la configuración:
sudo nginx -t
Corrige cualquier error, como asegurarte de que todas las instrucciones terminen con un punto y coma.
Finalmente, reinicia Nginx para aplicar los cambios:
sudo service nginx restart

**¿Qué otros aspectos considerar para optimizar los archivos estáticos?**

El servir archivos estáticos desde Nginx es eficiente, pero considera reducir carga en el servidor usando servicios externos:

Usa Amazon S3: Al integrarlo, puedes reducir las solicitudes directas a tu servidor.
Configura el archivo .env para utilizar S3 si decides hacerlo.


## Clase 22:  Automatización de Deployments con Ansible y GitHub Actions

¿Cómo automatizar despliegues con Ansible?
¿Alguna vez has sentido estrés al tratar de recordar todos los comandos necesarios para un despliegue cada vez que un desarrollador introduce un cambio? Aquí te presento una herramienta que podría resolver muchos de tus problemas: Ansible. Ansible te permite automatizar todo el proceso de despliegue mediante un archivo YAML, simplificando significativamente la gestión de tus servidores y aplicaciones.

**¿Cómo instalar y configurar Ansible?**
1. Iniciar con Ansible es sencillo. El primer paso es instalarlo en tu máquina local. Para eso, simplemente abre la terminal y ejecuta el siguiente comando:
	- pip install ansible
	- https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html

Una vez que Ansible esté instalado, el siguiente paso es configurar un archivo llamado hosts. 
Este archivo define todos los servidores a los que deseas hacer el despliegue. Puedes agregar varios hosts y aplicaciones. Por ejemplo:

[webservers]
192.168.1.1 ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/.ssh/my_ssh_key
Aquí defines la IP de tu servidor, la llave de acceso y el usuario.

**¿Qué es un playbook y cómo se crea?**
Un playbook en Ansible es un conjunto de tareas que se ejecutan en los servidores definidos en tu archivo de hosts. 
Crear un playbook te permite especificar qué deseas hacer con tus servidores. Por ejemplo, ¿quieres actualizar los paquetes? Aquí tienes un ejemplo básico:

---
- name: Despliegue básico
  hosts: webservers
  become: yes

  tasks:
    - name: Actualizar paquetes APT
      apt:
        update_cache: yes


Para ejecutar este playbook y realizar las tareas en tu servidor, utiliza el siguiente comando en la consola:

- ansible-playbook -i hosts deploy.yml


**¿Cómo instalar paquetes y clonar repositorios con Ansible?
Ansible te da la flexibilidad de hacer tareas más complejas, como instalar paquetes o clonar repositorios. Puedes modificar tu playbook para que también realice estas tareas:

- name: Instalar paquetes necesarios
  apt:
    name: 
      - nginx
      - git
    state: present

- name: Clonar repo
  git:
    repo: 'git@github.com:usuario/proyecto.git'
    dest: '/ruta/destino'
    version: 'feature/calculator_divide'
    key_file: '~/.ssh/my_ssh_key'

Cuando ejecutas el playbook nuevamente, Ansible verifica si los paquetes están presentes. Si no lo están, los instala. Además, clona el repositorio en la versión especificada, asegurándose de que tu aplicación esté siempre actualizada.


**RESUMEN DEL CURSO** 
1.
¿Cuál protocolo deberías usar para manejar múltiples solicitudes simultáneas en una aplicación Python moderna?
ASGI

2.
¿Cuál es la mejor práctica para manejar un error crítico en producción utilizando Git?
Crear una rama hotfix desde la rama master para corregir el error y luego fusionar los cambios de vuelta a master y develop.

3.
¿Cómo se debe incrementar la versión de una aplicación en Git si se han agregado nuevas funcionalidades sin romper la compatibilidad?
Incrementar el número menor en el versionamiento semántico.

4.
Si deseas editar un archivo de configuración en un servidor sin interfaz gráfica, ¿qué editor de texto deberías usar?
Vim

5.
¿Cuál es la mejor manera de manejar variables sensibles en una aplicación Python para evitar que se suban al repositorio?
Usar un archivo .env y no subirlo al repositorio

6.
¿Qué tipo de almacenamiento deberías elegir para mejorar la velocidad de acceso a los archivos de tu aplicación en un servidor?
Un SSD de tipo gp3.

7.
¿Cuál es el primer paso para crear una instancia virtual en AWS?
Seleccionar el sistema operativo de la instancia.
**REPASAR**

8.
Si deseas minimizar costos al usar instancias en AWS, ¿qué deberías hacer?
Utilizar el plan Free Tier y monitorear el uso.

9.
Si necesitas instalar un nuevo paquete en un servidor Ubuntu, ¿qué herramienta deberías utilizar?
apt

10.
¿Qué comando deberías usar para actualizar la lista de paquetes disponibles en un servidor Ubuntu?
sudo apt upgrade
**REPASAR**

11.
Si deseas verificar si un servicio está corriendo en tu servidor, ¿qué comando deberías ejecutar?
sudo service nginx status

12.
¿Qué puerto deberías usar para asegurar que tu sitio web esté utilizando HTTPS?
443


13.
Si necesitas verificar que tu aplicación Python está corriendo correctamente en el servidor, ¿qué comando podrías usar?
Htop para ver la lista de procesos en ejecución.


14.
¿Qué paso es crucial para asegurar que uWSGI pueda ejecutar una aplicación Python correctamente en un servidor?
Crear un link simbólico correcto desde apps available a apps enabled.


15.
¿Cuál es el propósito de usar un Proxy Reverso en Nginx al desplegar una aplicación WSGI?
Permitir que las solicitudes web se redirijan al socket de la aplicación.


16.
¿Cuál es la mejor práctica para manejar errores en una aplicación Python desplegada en producción?
Configurar logs separados para cada aplicación


17.
¿Por qué es importante no habilitar el modo debug en producción en una aplicación Django?
Porque expone información sensible del servidor


18.
¿Cuál es la ventaja principal de integrar Sentry en un proyecto de Python?
Permite detectar y notificar errores automáticamente sin revisar manualmente los logs.


19.
Si deseas recibir alertas de errores en tiempo real, ¿qué configuración adicional podrías implementar con Sentry?
Configurar alertas para que lleguen a un sistema de mensajería.


20.
¿Qué método es más eficiente para organizar los logs de una aplicación web?
Agrupar los logs por aplicación y fecha.


21.
¿Cuál es la mejor práctica para manejar las claves secretas en un proyecto Django en un entorno de producción?
Utilizar variables de entorno para almacenar las claves secretas.


22.
¿Qué comando se debe usar para aplicar los cambios realizados en el archivo de configuración de variables de entorno en el servidor?
python manage.py runserver
**REPASAR**

23.
Si deseas crear un nuevo usuario en PostgreSQL, ¿qué comando deberías usar?
CREATE USER nombre_usuario WITH PASSWORD 'contraseña';


24.
¿Cuál es la principal ventaja de utilizar Amazon RDS para gestionar bases de datos en producción?
Automatización de copias de seguridad y actualizaciones.


25.
Al crear una base de datos en Amazon RDS, ¿qué opción deberías elegir para un entorno de pruebas con bajo costo?
Seleccionar el Free Tier con una instancia de 2 CPUs y 1 GB de RAM.


26.
¿Cuál es la mejor práctica para manejar archivos estáticos en una aplicación Django en producción?
Utilizar un servicio como S3 para almacenar y servir los archivos estáticos.


27.
¿Qué comando de Django se utiliza para recopilar archivos estáticos en un solo lugar?
collectstatic


28.
¿Qué configuración en Nginx permite servir archivos estáticos correctamente en Django?
Configurar una location con alias apuntando a la carpeta de archivos estáticos.


29.
¿Cuál es la ventaja principal de usar Ansible para el despliegue de aplicaciones en múltiples servidores?
Automatiza el proceso de despliegue, reduciendo errores humanos.


30.
Si necesitas actualizar paquetes en un servidor usando Ansible, ¿qué módulo deberías utilizar?
El módulo 'apt' para sistemas basados en Debian.