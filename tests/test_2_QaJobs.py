import pytest
from pages.JobPage import JobsPage
from utilities.utils import Utils


def log_and_take_screenshot(driver, message, filename):
    #hrlper function to log a message and take a screenshot
    print(message)
    Utils.take_screenshot_on_failure(driver, filename)


@pytest.fixture(params=["chrome"])
def setup(request):
    driver = Utils.get_driver(browser_type=request.param)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_qa_jobs_filtering_and_redirection(setup):
    driver = setup
    jobs_page = JobsPage(driver)

    try:
        # Open QA jobs page and check URL
        jobs_page.go_to_quality_assurance_jobs()
        assert "quality-assurance" in driver.current_url, "Failed to load Quality Assurance Jobs page"

        # Log current URL
        print("Navigated to URL:", driver.current_url)

        # Apply filters
        jobs_page.click_see_all_qa_jobs()
        jobs_page.apply_filters("Istanbul, Turkey", "Quality Assurance")

        #Verify filtered jobs are displayed
        assert jobs_page.verify_jobs("Istanbul, Turkey", "Quality Assurance"), "Filtered jobs not found"

        #Redirection check for job details page
        assert jobs_page.click_view_role(), "Redirection to job application page failed"

        # Additional check for the application page URL
        assert "lever" in driver.current_url, "Application page URL does not contain 'lever'"

    except Exception as e:
        log_and_take_screenshot(driver, f"Exception occurred: {e}", "qa_jobs_filtering_redirection_failure.png")
        raise
