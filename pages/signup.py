from selenium.webdriver.common.by import By
import time

class Signup:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://glowify-cosmetics-site.onrender.com/accounts/signup/"

    def load(self):
        self.driver.get(self.url)
    
    def signup(self,Name,email,password):
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/form/div[1]/input[1]").send_keys(Name)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/form/div[1]/input[2]").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/form/div[1]/div[1]/input").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/form/div[1]/button").click()
                                                                                                 
        
