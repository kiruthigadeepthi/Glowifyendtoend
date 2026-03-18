import time
from pages.login import LoginPage
from pages.productpage import ProductPage
from pages.cartpage import CartPage
from pages.homepage import HomePage
from pages.checkout_page import CheckoutPage


def test_checkout_flow(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("kiruthigasns16@gmail.com", "123456")

    shop_tab=HomePage(driver)
    shop_tab.select_tab("Lipsticks")
    assert "lipsticks" in driver.current_url

    productpage = ProductPage(driver)
    productpage.add_to_cart()
    assert "Satin Glow Lipstick" in driver.page_source
    productpage.go_to_cart()
    
    time.sleep(3)
    cartpage = CartPage(driver)
    #cartpage.load()
    cartpage.checkout()
    assert "checkout" in driver.current_url

    checkoutpage=CheckoutPage(driver)
    checkoutpage.shipping("Kiruthiga","Ajith","9597840780","abc","xyz city","TN","625435")

    #pay=PaymentPage(driver)
    #pay.payment("5500 6700 0000 1002","03/32","765")