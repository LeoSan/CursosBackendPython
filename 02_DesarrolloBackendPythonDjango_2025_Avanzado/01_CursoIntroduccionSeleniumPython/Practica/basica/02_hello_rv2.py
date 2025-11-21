import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
    
    def test_hello_world(self):
        self.driver.get('https://www.netflix.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'hello-world-report'))
