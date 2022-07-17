import pytest

from tests.helper.base_app import BasePage


def test_get_url(browser):
    """
    """
    page = BasePage(browser)
    page.go_to_site()

    assert True, ''
