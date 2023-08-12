from selenium.webdriver.chrome.webdriver import WebDriver
from base.elements.base_element import BaseElement


class InputField(BaseElement):
    def __init__(self, name, locator: str, driver: WebDriver, wait=3):
        super().__init__(name, locator, driver, wait)

    def enter_value(self, value):
        self.find()
        self.element.send_keys(value)
        assert self.element.get_attribute(
            'value') == str(
            value), f'Incorrect text in field. Expected "{value}", actually "{self.element.get_attribute("value")}".'

    def clear(self):
        self.find()
        self.element.clear()
        assert self.element.get_attribute('value') == '', f'Field is not empty.'

    def placeholder_equals(self, expected_value):
        self.find()
        assert self.element.get_attribute(
            'placeholder') == expected_value, f'Incorrect placeholder of the field. Expected "{expected_value}", \
                actually "{self.element.get_attribute("placeholder")}"'
