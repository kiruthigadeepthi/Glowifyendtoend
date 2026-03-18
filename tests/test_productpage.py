from pages.productpage import ProductPage
import time

def test_product_details_and_cart(driver):
    page = ProductPage(driver)
    page.load()

    # Verify product title and price are visible
    title = page.get_title()
    price = page.get_price()
    assert "Lipstick" in title
    assert "₹" in price

    # Add to cart and verify navigation
    page.add_to_cart()
    time.sleep(2)
    cart_url = page.go_to_cart()

    assert "cart" in cart_url.lower()