from selenium.webdriver.common.by import By
import pytest
import time

class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver
    def shipping(self,first_name,last_name,Mob_number,address,city,state,pincode):
        self.driver.find_element(By.NAME,"first_name").send_keys(first_name)
        time.sleep(1)
        self.driver.find_element(By.NAME,"last_name").send_keys(last_name)
        time.sleep(1)
        self.driver.find_element(By.NAME,"mobile").send_keys(Mob_number)
        time.sleep(1)
        self.driver.find_element(By.NAME,"address").send_keys(address)
        time.sleep(1)
        self.driver.find_element(By.NAME,"city").send_keys(city)
        time.sleep(1)
        self.driver.find_element(By.NAME,"state").send_keys(state)
        time.sleep(1)
        self.driver.find_element(By.NAME,"pincode").send_keys(pincode)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/form/button").click()
        time.sleep(3)
    def payment(self,card_number,expirydate,cvv):
        card=self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div")
        card.send_keys(card_number)
        Expirydate=self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div/div[4]/div/form/div[1]/div[2]/label[1]/input")
        Expirydate.send_keys(expirydate)
        CVV=self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div/div[4]/div/form/div[1]/div[2]/label[2]/input")
        CVV.send_keys(cvv)
        self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[3]/div[2]/div/div[2]/button").click()