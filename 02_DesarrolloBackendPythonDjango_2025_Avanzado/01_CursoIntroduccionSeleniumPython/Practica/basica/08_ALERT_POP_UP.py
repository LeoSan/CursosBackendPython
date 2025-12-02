import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyunitreport import HTMLTestRunner

# unittest: Módulo estándar para pruebas.
# selenium: Librería para controlar el navegador.
# webdriver_manager: Instala automáticamente el driver de Chrome.
# pyunitreport: Genera reportes HTML.
class CompareProducts(unittest.TestCase):

    def setUp(self):
        # Configuración inicial antes de cada prueba
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30) # Espera implícita de 30 seg para encontrar elementos
        driver.maximize_window()   # Maximizar ventana
        driver.get("http://demo-store.seleniumacademy.com/") # Navegar a la URL del sitio de prueba

    def test_compare_products_removal_alert(self):
        driver = self.driver
        # 1. Buscar producto 'tee' (camisetas)
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()           # Limpiar campo por si tiene texto
        search_field.send_keys('tee')  # Escribir 'tee'
        search_field.submit()          # Enviar formulario (Enter)

        # 2. Interactuar para provocar la alerta
        driver.find_element(By.CLASS_NAME, 'link-compare').click() # Click en 'Add to Compare'
        driver.find_element(By.LINK_TEXT, 'Clear All').click()     # Click en 'Clear All' -> ESTO DISPARA LA ALERTA

        # 3. Manejo de la Alerta (Pop-up)
        alert = driver.switch_to.alert # Cambiar el foco del driver a la alerta
        alert_text = alert.text        # Obtener el texto de la alerta
        
        # Verificar que el texto de la alerta sea el esperado
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        
        alert.accept() # Aceptar la alerta (Click en OK)

    def tearDown(self):
        # Limpieza después de la prueba
        self.driver.implicitly_wait(3)
        self.driver.close() # Cerrar la ventana del navegador


if __name__ == "__main__":
	 unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'report_alerts'))