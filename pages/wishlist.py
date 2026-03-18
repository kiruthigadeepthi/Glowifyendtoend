from selenium.webdriver.common.by import By

class Wishlist:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://glowify-cosmetics-site.onrender.com/shop/category/lipsticks/"
    def load(self):
        self.driver.get(self.url)
    def wishlist(self):
        #self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/a/img").text
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/button[2]/i").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav/div/div/a").click()
        return self.driver.current_url