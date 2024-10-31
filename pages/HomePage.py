from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"  # Убедитесь, что URL корректен

    def open(self):
        """Открытие домашней страницы Insider"""
        print(f"Opening URL: {self.url}")  # Отладочная печать URL
        self.driver.get(self.url)

    def is_home_page_opened(self):
        """Проверка открытия главной страницы"""
        return "Insider" in self.driver.title
