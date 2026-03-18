from pages.searchbar import SearchBar
import pytest

@pytest.mark.parametrize("search_input,expected_url_part", [
    ("Lipsticks", "Lipsticks"),
    ("Perfume", "Perfume"),
    ("SkinCare","SkinCare")
])

def test_searchbar(driver,search_input,expected_url_part):
    search=SearchBar(driver)
    search.load()
    search.searchbar(search_input)
    assert expected_url_part in driver.current_url

