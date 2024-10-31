from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, by_locator):

        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def click_element(self, by_locator):

        element = self.wait_for_element(by_locator)
        element.click()

    def type_text(self, by_locator, text):

        element = self.wait_for_element(by_locator)
        element.send_keys(text)

    def is_element_visible(self, by_locator):

        try:
            element = self.wait_for_element(by_locator)
            return element.is_displayed()
        except:
            return False

    def find_elements(self, by_locator):

        return self.driver.find_elements(*by_locator)
