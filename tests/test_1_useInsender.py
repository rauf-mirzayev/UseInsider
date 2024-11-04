import pytest
from pages.HomePage import HomePage
from pages.CareersPage import CareersPage
from utilities.utils import Utils


def log_and_take_screenshot(driver, message, filename):
    #Helper function to log a message and take a screenshot
    print(message)
    Utils.take_screenshot_on_failure(driver, filename)


@pytest.fixture(params=["chrome"])
def setup(request):
    driver = Utils.get_driver(browser_type=request.param)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_careers_page_sections(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.open()

    # Additional check for page title
    assert "Insider" in driver.title, "Home page title does not contain 'Insider'"

    # Check that home page is open and screenshot if failed
    if not home_page.is_home_page_opened():
        log_and_take_screenshot(driver, "Home page not opened", "home_page_not_opened.png")
    assert home_page.is_home_page_opened(), "Home page not opened"

    careers_page = CareersPage(driver)
    careers_page.navigate_to_careers()

    # Additional check for Careers page URL
    assert "careers" in driver.current_url, "URL does not contain 'careers' after navigation"

    # Log and screenshot if sections are not visible
    if not careers_page.are_sections_visible():
        log_and_take_screenshot(driver, "Careers page sections not visible", "careers_page_sections_not_visible.png")
    assert careers_page.are_sections_visible(), "One or more sections on Careers page are not visible"
