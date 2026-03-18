import pytest
from pages.homepage import HomePage

@pytest.mark.parametrize("tab,expected_url_part", [
    ("Lipsticks", "lipsticks"),
    ("Skincare", "skincare"),
    ("Eye Makeup", "eye"),
    ("Hair care", "hair-care"),
    ("Nails", "nails"),
    ("Fragnance", "fragnance"),
    ("Offers", "offers"),
    ("About", "about"),
    ("Contact", "contact"),
])
def test_navigation_tabs(driver, tab, expected_url_part):
    homepage = HomePage(driver)
    homepage.load()
    current_url = homepage.select_tab(tab)
    assert expected_url_part in current_url.lower()