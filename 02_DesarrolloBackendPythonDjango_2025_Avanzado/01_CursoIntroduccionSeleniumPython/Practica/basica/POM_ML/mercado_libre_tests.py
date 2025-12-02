import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from mercado_libre_page import MercadoLibrePage

class MercadoLibreTests(unittest.TestCase):

    # setUpClass se ejecuta una sola vez antes de todos los tests de la clase.
    # Es más eficiente que setUp() si no necesitamos reiniciar el navegador en cada prueba.
    @classmethod  #Indica que este método se ejecuta una sola vez para toda la clase,
    # en lugar de ejecutarse antes de cada método de prueba individual.
    def setUpClass(cls):
        # Inicializamos el driver de Chrome usando webdriver_manager para gestión automática.
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    # Método de prueba principal. Define el flujo de usuario que queremos validar.
    def test_mercado_libre_flow(self):
        # 1. Instanciamos el Page Object pasándole el driver.
        # Esto conecta la lógica de la página con nuestro navegador actual.
        mercado_libre = MercadoLibrePage(self.driver)

        # 2. Navegamos a la página de inicio.
        mercado_libre.open()

        # 3. Seleccionamos el país (si aplica). 'CO' es el ID para Colombia.
        mercado_libre.select_country('CO')

        # 4. Realizamos la búsqueda del producto.
        # El test dice "busca esto", no "escribe en el input X y da click en Y".
        mercado_libre.search('playstation 4')

        # 5. Aplicamos filtros.
        # Observa lo legible que es: "filtrar por nuevo", "filtrar por Bogotá".
        mercado_libre.filter_by_new_condition()
        mercado_libre.filter_by_bogota_ubication()

        # 6. Ordenamos los resultados.
        mercado_libre.order_from_higher_price_to_lower_price()
        
        # 7. Extraemos datos.
        # Obtenemos los primeros 5 items ya procesados (nombre y precio).
        items = mercado_libre.get_first_five_items

        # 8. Imprimimos o validamos los resultados.
        print(items)
        # Aquí podrías agregar assertions, por ejemplo:
        # self.assertTrue(len(items) == 5)

    # tearDownClass se ejecuta al finalizar todos los tests.
    @classmethod
    def tearDownClass(cls):
        # Cerramos el navegador y liberamos recursos.
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)