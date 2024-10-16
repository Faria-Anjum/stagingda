from models.stagingda import HomePage, PrepaidInfoPage
import pytest

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    return page

def test_prepaid_visibility(page):
    home = HomePage(page)
    home.navigate()
    prepaid = PrepaidInfoPage(page)
    prepaid.prepaid_visibility()

def test_prepaid_check_know_details(page):
    home = HomePage(page)
    home.navigate()
    prepaid = PrepaidInfoPage(page)
    prepaid.prepaid_visibility()
    prepaid.prepaid_know_details

def test_prepaid_click_order_now(page):
    home = HomePage(page)
    home.navigate()
    prepaid = PrepaidInfoPage(page)
    prepaid.prepaid_visibility()
    prepaid.prepaid_order_now()