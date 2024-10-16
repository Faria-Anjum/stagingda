from models.stagingda import HomePage, PrepaidInfoPage, PrepaidPage
import pytest

def test_prepaid_type_number(page):
    home = HomePage(page)
    home.navigate()
    info = PrepaidInfoPage(page)
    info.prepaid_visibility()
    info.prepaid_order_now()
    prepaid = PrepaidPage(page)
    prepaid.type_msisdn(prepaid.number)

def test_prepaid_show_available(page):
    prepaid = PrepaidPage(page)
    prepaid.available_number()

def test_prepaid_show_unavailable(page):
    prepaid = PrepaidPage(page)
    prepaid.type_msisdn(prepaid.wrongNumber)
    prepaid.unavailable_number()

def test_prepaid_click_refresh(page):
    prepaid = PrepaidPage(page)
    prepaid.click_refresh()

def test_form_fillup(page):
    prepaid = PrepaidPage(page)
    prepaid.fill_customer_details()
    prepaid.select_home_delivery()

def test_delivery_time(page):
    prepaid = PrepaidPage(page)
    prepaid.select_delivery_time()

def test_collect_from_wic(page):
    prepaid = PrepaidPage(page)
    prepaid.select_nearest_wic()

def test_collect_from_store(page):
    prepaid = PrepaidPage(page)
    prepaid.select_nearest_store()

def test_checkout_online_payment(page):
    prepaid = PrepaidPage(page)
    prepaid.type_msisdn()
    prepaid.available_number()
    prepaid.select_available_number()
    prepaid.click_continue()