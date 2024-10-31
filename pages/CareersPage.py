from selenium.webdriver.common.by import By
from utilities.BasePage import BasePage

class CareersPage(BasePage):
    company_menu = (By.LINK_TEXT, "Company")
    careers_button = (By.LINK_TEXT, "Careers")
    locations_block = (By.XPATH, "//section[contains(., 'Locations')]")
    teams_block = (By.XPATH, "//section[contains(., 'Teams')]")
    life_block = (By.XPATH, "//section[contains(., 'Life at Insider')]")

    def navigate_to_careers(self):
        #go to careers through menu
        self.click_element(self.company_menu)
        self.click_element(self.careers_button)

    def are_sections_visible(self):
        #visibility checkings
        return (self.is_element_visible(self.locations_block) and
                self.is_element_visible(self.teams_block) and
                self.is_element_visible(self.life_block))
