from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MercadoLibrePage(object):
    # Constructor de la clase. Recibe el driver.
    # Nota: Evitar poner webdriver.Chrome() como valor por defecto, ya que abre un navegador al importar el archivo.
    def __init__(self, driver):
        self._driver = driver
        self._url = "https://mercadolibre.com"

    # Propiedad para verificar si la página ha cargado correctamente.
    # Espera a que la barra de búsqueda (name='q') esté presente.
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True

    # Propiedad que realiza el scraping de los primeros 5 artículos.
    @property
    def get_first_five_items(self):
        # Diccionario para guardar nombre y precio de los items.
        items_dict = {}

        # Esperamos a que la lista de resultados esté visible (usando un elemento común como el dropdown de ordenamiento).
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'andes-dropdown__trigger')))

        # Buscamos todos los contenedores de resultados de búsqueda.
        # Nota: 'ui-search-result__content-wrapper' es una clase común en ML, pero puede cambiar.
        items_elements = self._driver.find_elements(By.CLASS_NAME, 'ui-search-result__content-wrapper')

        # Iteramos sobre los elementos encontrados.
        for item_element in items_elements:
            # Buscamos el título dentro del elemento (tag 'a', atributo 'title').
            item_name = item_element.find_elements(By.TAG_NAME, 'a')[0].get_attribute('title')
            # Buscamos el precio dentro del elemento.
            item_price = item_element.find_element(By.CLASS_NAME, 'price-tag-fraction').text
            # Guardamos en el diccionario.
            items_dict[item_name] = item_price

            # Si ya tenemos 5 items, detenemos el bucle.
            if len(items_dict) == 5:
                break

        return items_dict

    # Método para escribir en el campo de búsqueda principal.
    def type_search(self, keyword):
        input_field = self._driver.find_element(By.CLASS_NAME, 'nav-search-input')
        input_field.send_keys(keyword)

    # Método para hacer clic en el botón de buscar (lupa).
    def click_submit(self):
        input_field = self._driver.find_element(By.CLASS_NAME, 'nav-search-btn')
        input_field.submit()

    # Método de negocio que encapsula la búsqueda completa.
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()

    # Método auxiliar para hacer clic en elementos difíciles.
    # A veces Selenium falla con .click() normal si hay elementos superpuestos.
    # Usar Javascript (execute_script) fuerza el clic directamente en el DOM.
    def click_custom(self, by_condition, by_value):
        location = self._driver.find_element(by_condition, by_value)
        self._driver.execute_script("arguments[0].click();", location)

    # Selecciona el país (ej: 'CO' para Colombia) en la landing page de ML.
    def select_country(self, country_id):
        self.click_custom(By.ID, country_id)

    # Filtra los resultados por condición "Nuevo".
    def filter_by_new_condition(self):
        # XPath específico para el filtro "Nuevo".
        xpath_value = '//*[@id="root-app"]/div/div[2]/aside/section/div[7]/ul/li[1]/a/span[1]'
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_value)))
        self.click_custom(By.XPATH, xpath_value)

    # Filtra los resultados por ubicación "Bogotá".
    def filter_by_bogota_ubication(self):
        # XPath específico para el filtro de ubicación.
        xpath_value = '//*[@id="root-app"]/div/div[2]/aside/section/div[11]/ul/li[1]/a/span[1]'
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_value)))
        self.click_custom(By.XPATH, xpath_value)

    # Abre el menú desplegable de ordenamiento ("Más relevantes", "Menor precio", etc).
    def expand_button_to_order(self):
        self.click_custom(By.CLASS_NAME, 'andes-dropdown__trigger')

    # Ordena los resultados de Mayor a Menor precio.
    def order_from_higher_price_to_lower_price(self):
        # Espera a que el botón de ordenamiento esté presente.
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'andes-dropdown__trigger')))
        # Despliega el menú.
        self.expand_button_to_order()
        # Hace clic en la opción específica (usando XPath).
        self.click_custom(By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_desc"]/div/div/span')

    # Navega a la URL inicial de Mercado Libre.
    def open(self):
        self._driver.get(self._url)
        self._driver.maximize_window()