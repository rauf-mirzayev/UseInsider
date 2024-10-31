import pytest
from pages.JobPage import JobsPage
from utilities.utils import Utils


@pytest.fixture(params=["chrome"])
def setup(request):
    driver = Utils.get_driver(browser_type=request.param)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_2_qa_jobs_filtering_and_redirection(setup):
    driver = setup
    jobs_page = JobsPage(driver)

    try:
        #go to website
        jobs_page.go_to_quality_assurance_jobs()
        jobs_page.click_see_all_qa_jobs()  # Клик по кнопке "See all QA jobs"

        # apply filter
        jobs_page.apply_filters("Istanbul, Turkey", "Quality Assurance")
        assert jobs_page.verify_jobs("Istanbul, Turkey",
                                     "Quality Assurance"), "Jobs with the specified filters not found"

        # check viewrole redirection
        assert jobs_page.click_view_role(), "Redirection to Lever application page failed"

    except Exception as e:
        # take screenshot
        Utils.take_screenshot_on_failure(driver, "test_2_qa_jobs_filtering_and_redirection_failure.png")
        print(f"Exception occurred: {e}")
        raise  #one more execption for reprot
