import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner
from time import sleep


class Disappearing_elements(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        # Configurar el WebDriver y abrir la página web
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        # Navegar al sitio de pruebas "The Internet"
        driver.get('https://the-internet.herokuapp.com/')
        driver.implicitly_wait(3)
        driver.maximize_window()
        # Entrar a la sección de Elementos que Desaparecen
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()
       
    def test_name_elements(self):
        driver = self.driver
        
        # Lista para guardar los nombres de las opciones encontradas
        options = []
        # Sabemos que el menú debería tener 5 elementos en total (Home, About, Contact, Portfolio, Gallery)
        menu = 5
        tries = 1
        
        # Bucle: Seguir intentando hasta que encontremos las 5 opciones
        # La página a veces carga 4 y a veces 5 elementos aleatoriamente.
        while len(options) < 5:
            options.clear() # Limpiamos la lista en cada intento para empezar de cero
            
            # Iteramos del 1 al 5 para buscar cada elemento de la lista <li>
            for i in range(menu):
                try:
                    # Construimos el XPATH dinámicamente: li[1], li[2], etc.
                    option_name = driver.find_element(By.XPATH, (f"/html/body/div[2]/div/div/ul/li[{i + 1}]/a"))
                    options.append(option_name.text)   
                    print(options)
                except:
                    # Si falla (ej. el elemento 5 'Gallery' no está), capturamos la excepción
                    print(f"Option Number {i + 1} is Not FOUND")
                    tries += 1
                    driver.refresh() # Refrescamos la página para ver si esta vez aparecen todos
                    
        print(f"Finished in {tries} tries") #Para que en python me tome la variable debo colocar la f delante
        
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
            
if __name__ == "__main__":
    # Ejecutar las pruebas y generar el informe HTML
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='dynamic_element'))