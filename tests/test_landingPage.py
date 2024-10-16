from models.stagingda import HomePage
import pytest

def test_launch(page):
    home = HomePage(page)
    home.navigate()
    home.launch()

def test_validate(page):
    home = HomePage(page)
    home.validate()