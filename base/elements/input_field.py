from selenium.webdriver.chrome.webdriver import WebDriver
from base.elements.base_element import BaseElement
from base.colors import colors
from base.error_texts import Errors


class InputField(BaseElement):
    def __init__(self, locator: str, driver: WebDriver):
        super().__init__(locator, driver)

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

    def border_color_equals(self, color):
        self.find()
        if self.element.value_of_css_property('border-color'):
            assert str(self.element.value_of_css_property('border-color')) == colors[color], \
                Errors.validation_error.format('border-color', colors[color],
                                               self.element.value_of_css_property('border-color'))
        elif str(self.element.value_of_css_property('border-bottom-color')):
            assert self.element.value_of_css_property('border-color-bottom') == colors[color], \
                Errors.validation_error.format('border-color-bottom', colors[color],
                                               self.element.value_of_css_property('border-color-bottom'))
