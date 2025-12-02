import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class RegisterNewUserTests(unittest.TestCase):

    def setUp(self) -> None:
        # Configura el entorno de prueba antes de cada test
        # Inicializa el driver de Chrome usando webdriver_manager para gestionar la instalación del driver automáticamente
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        # Navega a la URL de la tienda de demostración
        driver.get("https://demo-store.seleniumacademy.com/")
        # Maximiza la ventana del navegador para asegurar que todos los elementos sean visibles
        driver.maximize_window()
        # Establece una espera implícita de 15 segundos para encontrar elementos si no aparecen de inmediato
        driver.implicitly_wait(15)

    def test_new_user(self):
        driver = self.driver
        # 1. Navegación hacia el formulario de registro
        # Busca y hace clic en el menú de 'Account' (Cuenta) usando XPATH
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        # Busca y hace clic en el enlace 'Log In' (Iniciar sesión)
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        # 2. Ir a crear cuenta
        # Define el XPATH del botón para crear una cuenta nueva
        account_button_xpath = '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span'
        # Encuentra el botón de crear cuenta
        create_account_button = driver.find_element(By.XPATH, account_button_xpath)

        # Verifica que el botón esté visible y habilitado antes de interactuar
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())

        # Hace clic en el botón para ir al formulario de registro
        create_account_button.click()

        # Verifica que el título de la página sea el esperado para confirmar que estamos en la página correcta
        self.assertEqual('Create New Customer Account', driver.title)

        # 3. Localizar elementos del formulario
        # Encuentra los campos del formulario por su ID
        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        news_letter_subscription = driver.find_element(By.ID, 'is_subscribed') # Checkbox de suscripción
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        # Encuentra el botón de enviar (Register) por XPATH
        submit_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span')

        # 4. Verificar estado de los campos
        # Crea una lista verificando si cada campo está habilitado (True/False)
        validate_form_list = [first_name.is_enabled(), last_name.is_enabled(), email_address.is_enabled(),
                              middle_name.is_enabled(), news_letter_subscription.is_enabled(),
                              password.is_enabled(), confirm_password.is_enabled(), submit_button.is_enabled()]

        # Verifica que TODOS los elementos de la lista sean True (todos los campos habilitados)
        self.assertTrue(all(validate_form_list))

        # 5. Llenar el formulario
        # Envía texto a cada campo correspondiente
        first_name.send_keys("NameTest")
        middle_name.send_keys("middleNameTest")
        last_name.send_keys("lastNameTest")
        email_address.send_keys("emailTest@testingmailk.com") # Nota: Usar un email único si se ejecuta varias veces
        password.send_keys("testPassword")
        confirm_password.send_keys("testPassword")
        
        # Envía el formulario haciendo clic en el botón de registro
        submit_button.click()

    def tearDown(self) -> None:
        # Cierra el navegador y finaliza la sesión de WebDriver al terminar la prueba
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)