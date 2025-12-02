import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

COLUMN_NUMBER = 5
ROW_NUMBER = 4

class Tables(unittest.TestCase):
    
    def setUp(self):
        # Configuración del driver con webdriver_manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        # Navegar a la sección de Tablas Ordenables
        driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

    def test_sort_tables(self):
        driver = self.driver

        # Crear una lista de listas vacías para almacenar los datos de cada columna.
        # COLUMN_NUMBER es 5, así que crea: [[], [], [], [], []]
        table_data = [[] for i in range(COLUMN_NUMBER)]
        print(table_data)

        # Iterar sobre cada columna (0 a 4)
        for i in range(COLUMN_NUMBER):
            # Obtener el encabezado de la columna actual
            # XPath dinámico: th[1], th[2], etc.
            header = driver.find_element(
                By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span'
            )
            # Agregar el texto del encabezado a la sublista correspondiente
            table_data[i].append(header.text)

            # Iterar sobre cada fila (0 a 3) para obtener los datos de esa columna
            for j in range(ROW_NUMBER):
                # Obtener el dato de la celda en la fila j+1 y columna i+1
                row_data = driver.find_element(
                    By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]'
                )
                # Agregar el dato a la sublista de la columna actual
                table_data[i].append(row_data.text)

        # Imprimir la estructura final de datos organizada por columnas
        print(table_data)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)