import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del driver usando webdriver_manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        # Navegar a la sección de "Add/Remove Elements"
        driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()

    def test_add_remove(self):
        driver = self.driver

        # Solicitar al usuario cuántos elementos agregar y eliminar
        elements_added = int(input("How many elements will you add?: "))
        elements_removed = int(input("How many elements will you remove?: "))
        total_elements = elements_added - elements_removed

        # Localizar el botón para agregar elementos
        add_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/button')

        sleep(3) # Pausa para visualizar

        # Agregar elementos según la cantidad indicada
        for i in range(elements_added):
            add_button.click()

        # Eliminar elementos según la cantidad indicada
        for i in range(elements_removed):
            try:
                # Intentar localizar y hacer clic en el botón de eliminar (siempre el primero visible)
                delete_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                # Si no encuentra el botón (porque se acabaron), imprime mensaje y rompe el ciclo
                print("You're trying to delete more elements the existent")
                break

        # Verificar y mostrar cuántos elementos quedaron en pantalla
        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There 0 are elements on screen")

        sleep(3) # Pausa final para visualizar el resultado

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = "reportes", report_name = "add_remove_selements_test_report"))
