from models.stagingda import HomePage
import pytest

def test_trackOrderVisibility(page):
    home = HomePage(page)
    home.navigate()
    home.order_visibility()

def test_trackOrderFunctionality(page):
    home = HomePage(page)
    home.order_functionality()