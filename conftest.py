import pytest

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page