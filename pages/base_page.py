from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

    def elements_are_on_page(self, elements):
        self.driver.implicitly_wait(4)
        for element in elements:
            try:
                self.driver.find_element(By.XPATH, elements[element])
            except:
                print(f'Failed to find element "{element}"')