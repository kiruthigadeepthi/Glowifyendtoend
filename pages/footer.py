from selenium.webdriver.common.by import By
import time
class FooterSection:
    def __init__(self,driver):
        self.driver=driver
        self.url="https://glowify-cosmetics-site.onrender.com/"

    def load(self):
        self.driver.get(self.url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def footer(self,link):
        self.driver.find_element(By.LINK_TEXT,link).click()
        time.sleep(2)
        return self.driver.current_url
    def facebook(self):
        fb_icon=self.driver.find_element(By.XPATH,"/html/body/footer/div[2]/div/div[4]/div/a[1]/i")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", fb_icon)
        fb_icon.click()
        
    def instagram(self):
        insta_icon=self.driver.find_element(By.XPATH,"/html/body/footer/div[2]/div/div[4]/div/a[2]/i")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", insta_icon)
        insta_icon.click()
        