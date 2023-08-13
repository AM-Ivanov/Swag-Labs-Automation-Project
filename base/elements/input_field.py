from selenium.webdriver.chrome.webdriver import WebDriver
from base.elements.base_element import BaseElement
from base.error_texts import Errors


class InputField(BaseElement):
    def __init__(self, name, locator: str, driver: WebDriver, wait=3):
        super().__init__(name, locator, driver, wait)

    def enter_value(self, value):
        self.find()
        self.element.send_keys(value)
        assert self.element.get_attribute('value') == str(value), \
            Errors.common_error.format('text in field', value, self.element.get_attribute("value"))

    def clear(self):
        self.find()
        self.element.clear()
        assert self.element.get_attribute('value') == '', f'Field is not empty.'

    def placeholder_equals(self, value):
        self.find()
        assert self.element.get_attribute('placeholder') == value, Errors.common_error.format(
            'placeholder of the field', value, self.element.get_attribute("placeholder"))
