from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"

    def open(self):
        #open homepage
        print(f"Opening URL: {self.url}")
        self.driver.get(self.url)

    def is_home_page_opened(self):
        #check home page is opened
        return "Insider" in self.driver.title
