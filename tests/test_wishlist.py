from pages.wishlist import Wishlist

def test_wishlist(driver):
    wish=Wishlist(driver)
    wish.load()
    wish.wishlist()
    assert "wishlist" in driver.current_url
    #assert product in driver.page_source