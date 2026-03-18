from selenium.webdriver.common.by import By
from pages.productpage import ProductPage
import time
from selenium.webdriver.common.action_chains import ActionChains


class CartPage:
    def __init__(self,driver):
        self.driver = driver;
        self.url="https://glowify-cosmetics-site.onrender.com/shop/cart/"
    def load(self):
        self.driver.get(self.url)
    def checkout(self):
        action=ActionChains(self.driver)
        checkout=self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/a/span")
        action.double_click(checkout).perform()
        time.sleep(2)
        return self.driver.current_url


