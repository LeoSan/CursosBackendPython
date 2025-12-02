import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # Importar el gestor de drivers
from selenium.webdriver.support import expected_conditions as EC # Importar condiciones esperadas
from selenium.webdriver.support.ui import WebDriverWait # Importar la clase para esperas explícitas


class ExplicitWaitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Configuración inicial que se ejecuta UNA VEZ para toda la clase
        # Usamos ChromeDriverManager para instalar/gestionar el driver automáticamente
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)

        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/') # Navegar a la URL
        driver.maximize_window() # Maximizar la ventana
        driver.implicitly_wait(3) # Espera implícita: Si un elemento no está, espera hasta 3 seg antes de fallar
    
    def test_account_link(self):
        # Prueba para verificar el dropdown de idioma y abrir el menú de cuenta
        
        # WebDriverWait: Espera explícita.
        # Espera hasta 10 segundos a que se cumpla la condición (lambda).
        # La lambda busca el elemento 'select-language' y verifica que tenga 3 opciones (length == '3').
        # Esto asegura que el dropdown de idiomas se haya cargado completamente.
        WebDriverWait(self.driver, 10).until(
                lambda s: s.find_element(By.ID, 'select-language').get_attribute('length') == '3'
        )
        
        # Espera hasta que el enlace 'ACCOUNT' sea visible en la página.
        account = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT'))
        )
        # Hace clic en 'ACCOUNT' para desplegar el menú.
        account.click()

    def test_create_new_customer(self):
        # Prueba para navegar a la creación de un nuevo cliente
        
        # Busca el elemento 'ACCOUNT' (aunque no lo usa aquí, sirve para verificar que sigue ahí)
        self.driver.find_element(By.LINK_TEXT, 'ACCOUNT')
        
        # Espera a que el enlace 'My Account' sea visible (aparece después de hacer click en ACCOUNT en el test anterior)
        my_account = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'My Account'))
        )
        # Hace clic en 'My Account'
        my_account.click()

        # Espera a que el botón 'CREATE AN ACCOUNT' sea "cliqueable" (visible y habilitado)
        create_account_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT'))
        )
        # Hace clic en el botón para crear cuenta
        create_account_button.click()

        # Espera hasta que el título de la página contenga 'Create New Customer Account'
        # Esto confirma que hemos llegado a la página correcta.
        WebDriverWait(self.driver, 10).until(
                EC.title_contains('Create New Customer Account')
        )

    @classmethod
    def tearDownClass(cls) -> None:
        # Cierra el navegador al finalizar todas las pruebas de la clase
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)