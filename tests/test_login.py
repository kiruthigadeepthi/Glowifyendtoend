from pages.login import LoginPage


def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("kiruthigasns16@gmail.com", "123456")
    
    driver.save_screenshot("screenshots/valid_login.png")
    assert driver.current_url=="https://glowify-cosmetics-site.onrender.com/"
    
  

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("kiruthiga@gmail.com", "12345")
    driver.save_screenshot("screenshots/invalid_login.png")
    assert "login" in driver.current_url
    

