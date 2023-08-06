from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, locator: str, driver: WebDriver, wait=4):
        super().__init__(locator, driver)
        self.wait = WebDriverWait(driver, wait)

    def click(self):
        self._find()
        self.wait.until(ec.element_to_be_clickable(self.element))
        self.element.click()

    def button_name_is(self, name):
        self._find()
        assert self.element.get_attribute('value') == str(name), \
            f'Incorrect text in field. Expected "{name}", actually "{self.element.get_attribute("value")}".'
