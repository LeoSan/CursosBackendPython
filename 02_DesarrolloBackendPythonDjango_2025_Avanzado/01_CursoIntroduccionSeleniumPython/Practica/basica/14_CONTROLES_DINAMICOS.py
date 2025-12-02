import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class DynamicControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración del driver usando ChromeDriverManager
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        # Navegar a la página de Controles Dinámicos
        driver.get('https://the-internet.herokuapp.com/dynamic_controls')
        driver.maximize_window()
        # Espera implícita: Selenium esperará hasta 15s si no encuentra un elemento inmediatamente
        driver.implicitly_wait(15)

    def test_remove_add_button(self):
        driver = self.driver
        
        # 1. Buscar y hacer clic en el botón "Remove"
        # Usamos XPATH para encontrar el botón que contiene el texto "Remove"
        remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button[contains(text(),"Remove")]')
        remove_button.click()
        
        # 2. Validar que el checkbox ha desaparecido
        # Esperamos a que aparezca el mensaje "It's gone!"
        # Nota: Gracias al implicitly_wait, el driver esperará a que el mensaje aparezca en el DOM
        self.validate_paragraph_text("It's gone!")

        # 3. Buscar y hacer clic en el botón "Add" (el botón cambia de texto/estado)
        button_add = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button[contains(text(),"Add")]')
        button_add.click()
        
        # 4. Validar que el checkbox ha vuelto
        self.validate_paragraph_text("It's back!")

        # 5. Volver a remover para dejar el estado limpio (opcional)
        # Nota: Aquí hay un riesgo si el botón tarda en cambiar de "Add" a "Remove"
        # En un escenario real, usaríamos WebDriverWait para esperar a que el botón sea cliqueable
        button_remove_again = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button[contains(text(),"Remove")]')
        button_remove_again.click()
        self.validate_paragraph_text("It's gone!")


    def test_enable_disable(self):
        driver = self.driver

        # 1. Buscar el botón de Habilitar/Deshabilitar
        enable_disable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
        
        # 2. Clic para Habilitar el input
        enable_disable_button.click()
        
        # Esperamos a que aparezca el mensaje de confirmación "It's enabled!"
        # Esto nos asegura que la acción asíncrona (barra de carga) ha terminado
        self.validate_paragraph_text("It's enabled!")

        # 3. Clic para Deshabilitar el input
        enable_disable_button.click()
        self.validate_paragraph_text("It's disabled!")
        
        # 4. Clic nuevamente para Habilitar
        enable_disable_button.click()
        self.validate_paragraph_text("It's enabled!")


    def validate_paragraph_text(self, expectedText):
        # Función auxiliar para verificar el mensaje de estado
        # Busca el elemento con id 'message' (que aparece dinámicamente)
        paragraph = self.driver.find_element(By.CSS_SELECTOR, '#message')
        paragraph_text = paragraph.text
        # Compara el texto obtenido con el esperado
        self.assertEqual(paragraph_text, expectedText)

    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador al finalizar
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=1)