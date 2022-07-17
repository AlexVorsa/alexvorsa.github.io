"""
Basic tests
"""
from tests.helper.base_app import BasePage

def test_get_url(browser):
    """
    Get URL
    """
    page = BasePage(browser)
    page.go_to_site()

    assert True, ''

def test_email(browser):
    """
    Check email
    """
    page = BasePage(browser)
    page.go_to_site()

    assert page.get_email() == "ALEKSANDR.VORSA@YANDEX.RU", 'Unexpected email address'
