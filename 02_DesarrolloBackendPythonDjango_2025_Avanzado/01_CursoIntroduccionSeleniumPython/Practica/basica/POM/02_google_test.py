import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Nota: Para que este import funcione, el archivo '01_google_page.py' debe renombrarse a 'google_page.py'
# o tener un nombre válido de módulo Python (sin empezar por números).
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    # @classmethod: Indica que este método se ejecuta una sola vez para toda la clase,
    # en lugar de ejecutarse antes de cada método de prueba individual.
    @classmethod
    def setUpClass(cls):
        # Inicializamos el driver de Chrome. Usamos ChromeDriverManager para gestionar el driver automáticamente.
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    # Este es el método de prueba. Debe comenzar con 'test_'.
    def test_search(self):
        # Instanciamos el Page Object 'GooglePage', pasándole el driver que configuramos.
        # Esto crea una capa de abstracción: el test no sabe de 'find_element', solo de acciones de negocio.
        google = GooglePage(self.driver)
        
        # Llamamos al método 'open' del Page Object para ir a Google.
        google.open()
        
        # Llamamos al método 'search' del Page Object para realizar una búsqueda completa.
        # Fíjate cómo el test se lee casi como lenguaje natural: "google open", "google search".
        google.search('Platzi')

        # Verificación (Assert):
        # Comprobamos que el texto en la barra de búsqueda (google.keyword) sea igual a 'Platzi'.
        self.assertEqual('Platzi', google.keyword)

    # @classmethod: Se ejecuta una vez al finalizar todas las pruebas de la clase.
    @classmethod
    def tearDownClass(cls):
        # Cerramos el navegador y terminamos la sesión del driver.
        cls.driver.quit()


if __name__ == "__main__":
    # Ejecutamos las pruebas con verbosity=2 para tener más detalles en la consola.
    unittest.main(verbosity=2)