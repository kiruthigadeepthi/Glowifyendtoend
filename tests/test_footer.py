import pytest
from pages.footer import FooterSection

@pytest.mark.parametrize("links,expected_url",[
    ("Privacy Policy","privacy"),
    ("Terms & Conditions","terms")
])

def test_footertabs(driver,links,expected_url):
    footer=FooterSection(driver)
    footer.load()
    footer.footer(links)
    assert expected_url in driver.current_url
def test_facebook(driver):
    footer=FooterSection(driver)
    footer.load()
    footer.facebook()
    assert "facebook" in driver.current_url
def test_instagram(driver):
    footer=FooterSection(driver)
    footer.load()
    footer.instagram()
    assert "instagram" in driver.current_url