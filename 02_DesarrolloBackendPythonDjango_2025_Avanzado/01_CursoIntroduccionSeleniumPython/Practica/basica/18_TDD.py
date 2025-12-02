import csv
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
# Importamos las herramientas para DDT (Data Driven Testing)
from ddt import ddt, data, unpack


# Función auxiliar para leer datos del archivo CSV
def get_data(file_name):
    rows = []
    # Abrimos el archivo CSV en modo lectura ('r')
    data_file = open(file_name, 'r')
    # Creamos un objeto lector para interpretar el formato CSV
    reader = csv.reader(data_file)
    # next() salta la primera línea del archivo (los encabezados) para no usarlos como datos
    next(reader, None)

    # Iteramos sobre cada fila restante en el archivo
    for row in reader:
        rows.append(row)
    return rows

# @ddt: Decorador de clase obligatorio para habilitar Data Driven Testing en unittest
@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializamos el driver de Chrome usando webdriver_manager
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        # Navegamos al sitio de pruebas (Demo Store)
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        # Espera implícita para dar tiempo a que carguen los elementos
        driver.implicitly_wait(15)

    # @data: Inyecta los datos al test. 
    # *get_data(...): El asterisco 'desempaqueta' la lista de filas que devuelve la función.
    # @unpack: Toma cada fila (ej: ['music', '5']) y la separa en argumentos individuales para el método.
    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_dtt(self, search_value, expected_count):
        driver = self.driver

        # Localizamos la barra de búsqueda por su atributo 'name'
        search_field = driver.find_element(By.NAME, 'q')
        # Limpiamos el campo por si tiene texto previo
        search_field.clear()
        # Escribimos el término de búsqueda (search_value) que viene del CSV
        search_field.send_keys(search_value)
        # Enviamos el formulario (equivalente a presionar Enter)
        search_field.submit()

        # Buscamos todos los elementos que coincidan con el XPATH de los productos
        # Esto nos devuelve una lista de elementos encontrados
        products = driver.find_elements(By.XPATH, "//h2[@class='product-name']/a")

        # Convertimos el valor esperado a entero (desde el CSV viene como texto)
        expected_count = int(expected_count)

        if expected_count > 0:
            # Caso 1: Esperamos encontrar productos
            # Verificamos que la cantidad encontrada (len(products)) sea igual a la esperada
            self.assertEqual(expected_count, len(products), f"Expected {expected_count} products, but found {len(products)} products.")
        else:
            # Caso 2: No esperamos encontrar productos (expected_count es 0)
            # Verificamos que la lista de productos esté vacía
            self.assertTrue(len(products) == 0, "Expected no products, but found products.")

    @classmethod
    def tearDownClass(cls):
        # Cerramos el navegador al finalizar todas las pruebas de la clase
        cls.driver.quit()

if __name__ == "__main__":
    # Ejecutamos las pruebas y generamos el reporte HTML
    unittest.main(testRunner=HTMLTestRunner(output='reportes', report_name='search_csv_ddt'), verbosity=2)