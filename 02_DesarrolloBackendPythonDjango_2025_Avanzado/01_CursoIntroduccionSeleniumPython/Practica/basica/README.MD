## Practica básica Primer Paso Selenium 

- Paso 0: Crea un ambiente virtual
    - `lsb_release -a` 
    - `sudo apt update`     -> Linux
    - `sudo apt -y upgrade` -> Linux 
    - `sudo apt-get install python3.8-venv` -> Linux 
    - `py -m venv venv` -> Creamos 
    - `venv\scripts\activate` -> activamos en windows 
    - `source venv/bin/activate` -> activamos en linux 

> [!NOTE]
> si en linux no se te activa el entorno de trabajo recuerda que son permisos debes ejecutar los siguientes pasos 


    - Paso 0: `rm -rf ./venv`                -> Eliminar en caso el entorno viejo 
    - Paso 1: `python3 -m venv venv`         -> Crear el entorno de nuevo
    - Paso 2: `chmod +x ./venv/bin/activate` -> Generar  permiso 
    - Paso 3: Funciona en Bach => `source ./venv/bin/activate` ó Shell Zsh => `. ./venv/bin/activate`   -> Activar entorno
    - Paso 4: Deberia verse así `(venv) istemas@GlenaCNP-Leonard:~/proyectos/CursoSelenium/practicas/basica$ `


- Paso 1: Validamos version de Python se trabaja mucho mejor con la version 3.8 
    - python3 --version 
    - pip3 --version

- Paso 2: Instalamos Selenium  
    -  `pip3 install selenium` 

- Paso 3: Instalamos libreria report 
    - `pip3 install pyunitre`

- Paso 4: podemos generar un archivo con 
    - `touch requirements.txt` 
    - pasar lo que tenemos instalado  `pip3 freeze > requirements.txt`
    - y ejecutar en proximo proyectos `pip install -r requirements.txt`


## CONFUGURACIÓN DE PRUEBAS 
- Debemos crear la estructura basica para una prueba  

```python
import unittest 
from pyunitreport import HTMLTestRunner 
from selenium import webdriver 

class HelloWorld(unittest.TestCase):
    
    # Preparación del entorno de prueba
    def setUp(self): 
        self.driver = webdriver.Chrome(executable_path=r'path/to/chromedriver') 
        driver = self.driver 
        driver.implicitly_wait(10) 
        driver.maximize_window() 
    
    # Caso de prueba
    def test_hello_world(self): 
        driver = self.driver 
        driver.get("https://www.google.com") 
        print("Hello World") 
    
    # Limpieza del entorno de prueba
    def tearDown(self): 
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report')) 
```