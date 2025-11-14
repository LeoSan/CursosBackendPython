import unittest 
from pyunitreport import HTMLTestRunner 
from selenium import webdriver 

class HelloWorld(unittest.TestCase):
    
    # Preparación del entorno de prueba
    def setUp(self): 
        self.driver = webdriver.Chrome(executable_path=r'path/to/chromedriver') 
        driver = self.driver 
        driver.implicitly_wait(10) 
        driver.maximize_window() 
    
    # Caso de prueba
    def test_hello_world(self): 
        driver = self.driver 
        driver.get("https://www.google.com") 
        print("Hello World") 
    
    # Limpieza del entorno de prueba
    def tearDown(self): 
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report')) 