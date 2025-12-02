import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class EfficientTables(unittest.TestCase):
    
    def setUp(self):
        # Configuración del driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

    def test_sort_tables_efficiently(self):
        driver = self.driver
        
        # --- ENFOQUE EFICIENTE ---
        # En lugar de hacer una petición al navegador por CADA celda (lo cual es lento),
        # traemos filas completas y procesamos en memoria.

        # 1. Localizar la tabla específica
        table = driver.find_element(By.ID, "table1")

        # 2. Obtener TODAS las filas del cuerpo de la tabla de una sola vez
        # Esto es una sola llamada a Selenium que devuelve una lista de WebElements
        rows = table.find_elements(By.XPATH, ".//tbody/tr")

        table_data = []

        # 3. Iterar sobre las filas (procesamiento en Python, rápido)
        for row in rows:
            # Obtener todas las celdas de la fila actual
            cells = row.find_elements(By.TAG_NAME, "td")
            
            # Extraer el texto de cada celda y guardarlo en una lista
            # Esto usa comprensión de listas para ser más pythonico
            row_data = [cell.text for cell in cells]
            
            table_data.append(row_data)

        # Imprimir los datos extraídos
        # Nota: La estructura aquí es una lista de filas [[col1, col2...], [col1, col2...]]
        # A diferencia del ejemplo anterior que era lista de columnas.
        print("Datos extraídos eficientemente (Fila por Fila):")
        for row in table_data:
            print(row)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
