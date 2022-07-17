from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class page_locators:
    LOCATOR_EMAIL = (By.CSS_SELECTOR, '[class="subheading mb-5"] a')
    
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://alexvorsa.github.io"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
        except:
            return None

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_email(self):
        el = self.find_element(page_locators.LOCATOR_EMAIL, time=2)
        return el.text