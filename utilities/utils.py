from selenium import webdriver

class Utils:
    @staticmethod
    def get_driver(browser_type="chrome"):
        #run driver based on requested browser
        if browser_type.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser_type.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            raise Exception(f"Unsupported browser: {browser_type}")
        driver.maximize_window()
        return driver

    @staticmethod
    def take_screenshot_on_failure(driver, filename="error.png"):

        try:
            driver.save_screenshot(filename)
            print(f"Screenshot saved as {filename}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
