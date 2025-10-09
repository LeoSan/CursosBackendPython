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
    - hotfix: en caso de un sissue 

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

## Clase 10: 

## Clase 11: 

## Clase 12: 

## Clase 13: 

## Clase 14: 

## Clase 15: 

## Clase 16: 

## Clase 17: 

## Clase 18: 

## Clase 19: 

## Clase 20: 