import pytest
from pages.sorting import SortPage
import time

@pytest.mark.parametrize("option_text", [
    ("Top Rated"),
    ("Price Low → High"),
    ("Price High → Low"),
    ("Best Discount"),
])
def test_sort_dropdown(driver, option_text):
    page = SortPage(driver)
    page.load()
    current = page.select_sort_option(option_text)
    time.sleep(2)
    assert current == option_text