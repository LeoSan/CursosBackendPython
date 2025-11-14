
#assertions.py
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AssertionsTest(unittest.TestCase):

	@classmethod
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("Platzi decía que el sitio no era seguro.com")

	def test_search_field(self):
		print('Searching the search bar')
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	
	def test_language_option(self):
		print('Searching the Select language dropdown')
		self.assertTrue(self.is_element_present(By.ID, 'iselect-language'))

	@classmethod
	def tearDown(self):
		self.driver.quit()

	def	is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException(): 
			self.driver.close()
			return False
		return True



#searchtests.py

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SearchTests(unittest.TestCase):

	@classmethod
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("Platzi no dejo poner el URL :c")

	def test_search_tee(self):
		driver = self.driver
		search_field = driver.find_element(By.NAME, "q")
		search_field.clear() 
		search_field.clear()
		
		search_field.send_keys('tee')
		search_field.submit()
		
	def test_search_salt_shaker(self):
		driver = self.driver
		search_field = driver.find_element(By.NAME, "q")
		search_field.clear() 
		search_field.send_keys('salt shaker')
		search_field.submit()

		#Searching by XPATH -> $x('//div[@class = "product-info"]/h2[@class="product-name"]/a/text()').map(x => x.wholeText) or $x('//div[@class = "product-info"]/h2/a/text()').map(x => x.wholeText)
		# REMEMBER: "h2" could also be replaced by "text-fill"
		products = driver.find_elements(By.XPATH, '//div[@class = "product-info"]/h2[@class="product-name"]/a')                                       
		self.assertEqual(1, len(products))


	@classmethod
	def tearDown(self):
		self.driver.quit()







# smoketests.py
from unittest import TestLoader, TestSuite
from assertions import AssertionsTest
from searchtests import SearchTests
from HtmlTestRunner import HTMLTestRunner

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#contruimos la suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])


# Aquí generamos nuestros reportes
kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": True
    }


runner = HTMLTestRunner(**kwargs)

runner.run(smoke_test)         