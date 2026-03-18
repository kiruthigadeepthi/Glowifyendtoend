from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class SortPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://glowify-cosmetics-site.onrender.com/shop/category/lipsticks/"
        # Adjust locator to match actual HTML
        #self.sort_dropdown = (By.ID, "sortOptions")

    def load(self):
        self.driver.get(self.url)

    def select_sort_option(self, option_text):
        dropdown_element = self.driver.find_element(By.ID,"sortSelect")
        select = Select(dropdown_element)
        dropdown_element.click()
        time.sleep(1)
        select.select_by_visible_text(option_text)
        return option_text