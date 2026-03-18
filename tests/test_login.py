from pages.login import LoginPage
   
def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("kiruthigasns16@gmail.com", "123456")
  

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("kiruthiga@gmail.com", "12345")
    assert "login" in driver.current_url
    