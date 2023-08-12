from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

    @staticmethod
    def elements_are_on_page(elements):
        for element in elements:
            element.find()
