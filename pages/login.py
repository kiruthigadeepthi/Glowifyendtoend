from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://glowify-cosmetics-site.onrender.com/accounts/login/"
        # Locators
    def load(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
