from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage(object):
    # El método __init__ es el constructor de la clase.
    # Recibe el 'driver' de Selenium para poder interactuar con el navegador.
    def __init__(self, driver):
        # Guardamos el driver en una variable "privada" (convención _nombre) para usarlo en otros métodos.
        self._driver = driver
        # Definimos la URL de la página que representa este objeto.
        self._url = 'https://google.com'
        # Definimos el localizador de la barra de búsqueda (su atributo 'name' es 'q').
        # Es buena práctica tener los localizadores como atributos para cambiarlos fácil si la web cambia.
        self.search_locator = 'q'

    # @property convierte un método en una propiedad de solo lectura.
    # Permite acceder a 'google_page.is_loaded' sin usar paréntesis ().
    @property 
    def is_loaded(self):
        # Esperamos explícitamente hasta 10 segundos a que el elemento de búsqueda esté presente.
        # Esto confirma que la página ha cargado correctamente los elementos esenciales.
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q')))
        return True

    # Esta propiedad nos permite obtener el texto que está escrito en el buscador.
    @property
    def keyword(self):
        # Buscamos el elemento del input por su nombre 'q'.
        input_field = self._driver.find_element(By.NAME, 'q')
        # Retornamos el valor actual del atributo 'value' del input.
        return input_field.get_attribute('value')

    # Método para navegar a la URL de la página.
    def open(self):
        self._driver.get(self._url)

    # Método para escribir un término en el buscador.
    # Abstrae la acción de "buscar el elemento y escribir".
    def type_search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.send_keys(keyword)

    # Método para enviar el formulario de búsqueda.
    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.submit()

    # Método de alto nivel que combina acciones más pequeñas.
    # Realiza una búsqueda completa: escribe y envía.
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()