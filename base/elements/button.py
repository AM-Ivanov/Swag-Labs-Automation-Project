from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from base.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, name, locator: str, driver: WebDriver, wait=4):
        super().__init__(name, locator, driver, wait)

    def click(self):
        self.find()
        self.wait.until(ec.element_to_be_clickable(self.element))
        self.element.click()

    def button_name_is(self, name):
        self.find()
        assert self.element.get_attribute('value') == str(name), \
            f'Incorrect text in field. Expected "{name}", actually "{self.element.get_attribute("value")}".'
