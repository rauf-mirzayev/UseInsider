from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.BasePage import BasePage
import time


class JobsPage(BasePage):
    # locators
    qa_jobs_url = "https://useinsider.com/careers/quality-assurance/"
    see_all_qa_jobs_button = (By.LINK_TEXT, "See all QA jobs")
    location_dropdown = (By.ID, "select2-filter-by-location-container")
    location_search_input = (By.XPATH, "//input[@class='select2-search__field']")
    location_result = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='Istanbul, Turkey']")
    department_dropdown = (By.ID, "department")
    job_list = (By.CLASS_NAME, "job-listing")
    view_role_button = (By.LINK_TEXT, "View Role")

    def go_to_quality_assurance_jobs(self):
        #open requested page
        self.driver.get(self.qa_jobs_url)
        assert "quality-assurance" in self.driver.current_url, "Failed to load Quality Assurance Jobs page"

    def click_see_all_qa_jobs(self):

        self.click_element(self.see_all_qa_jobs_button)

    def apply_filters(self, location, department):


        # open dropdown
        self.click_element(self.location_dropdown)
        time.sleep(1)  #pause for list of countries


        self.type_text(self.location_search_input, "Istanbul")


        self.click_element(self.location_result)

        #select dept
        department_select = Select(self.wait_for_element(self.department_dropdown))
        department_select.select_by_visible_text(department)

    def verify_jobs(self, location, department):
        #vacancy checking
        jobs = self.find_elements(self.job_list)
        return all(location in job.text and department in job.text for job in jobs)

    def click_view_role(self):

        self.click_element(self.view_role_button)
        return "lever" in self.driver.current_url
