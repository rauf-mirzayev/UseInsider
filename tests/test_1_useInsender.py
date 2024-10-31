import pytest
from pages.HomePage import HomePage
from pages.CareersPage import CareersPage
from utilities.utils import Utils


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
    assert home_page.is_home_page_opened(), "Home page not opened"

    careers_page = CareersPage(driver)
    careers_page.navigate_to_careers()

    if not careers_page.are_sections_visible():
        Utils.take_screenshot_on_failure(driver, "careers_page_sections_not_visible.png")
        print("Careers page sections not visible. Screenshot taken.")
    assert careers_page.are_sections_visible(), "One or more sections on Careers page are not visible"
