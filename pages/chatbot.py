from selenium.webdriver.common.by import By
import time

class ChatBot:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://glowify-cosmetics-site.onrender.com/"
    def load(self):
        self.driver.get(self.url)
    def chatbot(self,query):
        self.driver.find_element(By.XPATH,"/html/body/div[4]/img").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/input").send_keys(query)
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/button").click()
        time.sleep(2)
