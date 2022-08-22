"""
For PageObject
"""
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Page object
    """
    LOCATOR_EMAIL = (By.CSS_SELECTOR, '[class="subheading mb-5"] a')

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://alexvorsa.github.io"

    def find_element(self, locator, time=10):
        """
        Find element with waiting
        """
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Find a few elements with waiting
        """
        try:
            return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
        except ValueError as error:
            logger.info(error)
            return None

    def go_to_site(self):
        """
        Go to site
        """
        return self.driver.get(self.base_url)

    def get_email(self):
        """
        Get email from page
        """
        _el = self.find_element(self.LOCATOR_EMAIL, time=2)
        return _el.text
        