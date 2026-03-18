from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class SearchBar:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://glowify-cosmetics-site.onrender.com/"
    def load(self):
        self.driver.get(self.url)
    def searchbar(self,input):
        search_input=self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav/div/form/input")
        search_input.send_keys(input)
        search_input.send_keys(Keys.ENTER)

        time.sleep(2)
        
