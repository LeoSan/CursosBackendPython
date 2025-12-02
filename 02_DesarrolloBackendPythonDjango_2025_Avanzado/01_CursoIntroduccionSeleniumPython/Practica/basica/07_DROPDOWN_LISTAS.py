import unittest
from pyunitreport import HTMLTestRunner # para generar el reporte en html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Service es una clase que se encarga de abrir el navegador
from webdriver_manager.chrome import ChromeDriverManager # para que se abra el navegador
from selenium.webdriver.common.by import By # Clase moderna para buscar elementos
from selenium.webdriver.support.ui import Select # Clase para manejar listas desplegables

class LanguageOptions(unittest.TestCase):

    # Se ejecuta al inicio de cada test, abrir el navegador
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get(" http :// demo-store . seleniumacademy . com /") # <<--eliminar los espacios en la URL

    def test_select_language(self):
        exp_options = ["English", "French", "German"] # creamos una lista con las opciones esperadas
        act_options = [] # creamos una lista vacía para las opciones actuales
        # Asegúrate de que 'select_language' es un elemento 'select'
        # select_language = self.driver.find_element(By.ID, "select-language") # versión antigua
        select_language = Select(self.driver.find_element(By.ID, "select-language")) # Busca la lista desplegable de idiomas por su id

        # Ahora puedes acceder a 'options'
        options = select_language.options
        # self.assertEqual(3, len(select_language.find_elements(By.TAG_NAME, "option"))) # versión antigua
        self.assertEqual(3, len(options)) # Comprueba que haya 3 opciones en la lista desplegable

        # for option in select_language.find_elements(By.TAG_NAME, "option"): # versión antigua
        for option in select_language.options: # Recorre cada opción de la lista desplegable
            act_options.append(option.text) # Agrega el texto de la opción a la lista de opciones actuales, solo el texto, no el valor html

        self.assertEqual(exp_options, act_options) # Comprueba que las opciones de ambas listas esperadas sean iguales a las opciones actuales

        first_option = select_language.first_selected_option # Obtiene la opción seleccionada por defecto
        # self.assertEqual("English", select_language.first_selected_option.text)  # versión antigua
        self.assertEqual("English", first_option.text) # Comprueba que la opción seleccionada por defecto sea "English"

        select_language.select_by_visible_text("German") # Selecciona la opción "German" de la lista desplegable

        self.assertTrue("store=german" in self.driver.current_url) # Comprueba que la URL actual contenga "store=german"

        select_language = Select(self.driver.find_element(By.ID, "select-language")) 
        select_language.select_by_index(0) # Selecciona la primera opción de la lista desplegable

    # Se ejecuta al finalizar cada test, cerrar el navegador
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HTMLTestRunner(output="reportes", report_name="hello-world-report"),
        verbosity=2,
    )