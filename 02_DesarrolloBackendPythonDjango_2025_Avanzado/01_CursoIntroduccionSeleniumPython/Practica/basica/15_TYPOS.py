import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Typos(unittest.TestCase):

    def setUp(self):
        # Configuración del driver con webdriver_manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Typos").click()

    def test_find_typos(self):
        driver = self.driver

        # Texto esperado correcto
        correct_text = "Sometimes you'll see a typo, other times you won't."
        found = False
        tries = 1

        # Bucle para refrescar la página hasta encontrar el texto correcto
        while not found:
            # Localizar el párrafo (es el tercer <p> dentro del div de contenido)
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            print(f"Intento {tries}: {text_to_check}")

            if text_to_check == correct_text:
                found = True # Si coincide, salimos del bucle
            else:
                tries += 1 # Si no, incrementamos intentos
                driver.refresh() # Y refrescamos la página

        self.assertEqual(found, True)

        print(f"It took {tries} tries to find the correct text")

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = "reportes", report_name = "typos_test_report"))
