from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url="https://glowify-cosmetics-site.onrender.com/shop/category/lipsticks/"
    
    def load(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/a/h5").text

    def get_price(self):
        return self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/a/p[2]").text

    def add_to_cart(self):
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/button[1]/span").click()

    def go_to_cart(self):
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav/div/div/div[1]/a").click()
        return self.driver.current_url 


