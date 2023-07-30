from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from base.colors import colors


class InputFieldSteps:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_value(self, element, value):
        element: WebElement = self.driver.find_element(By.XPATH, element)
        element.send_keys(value)
        assert element.get_attribute(
            'value') == str(value), f'Wrong text in field. Expected "{value}", actually "{element.get_attribute("value")}".'

    def clear_field(self, element):
        element: WebElement = self.driver.find_element(By.XPATH, element)
        element.clear()
        assert element.get_attribute('value') == '', f'Field is not empty.'

    def field_border_color_equal(self, element, color):
        element: WebElement = self.driver.find_element(By.XPATH, element)
        if element.value_of_css_property('border'):
            assert element.value_of_css_property('border-color') == colors[color], f'Incorrect border color. \
                Expected "{colors[color]}", actually "{element.value_of_css_property("border-color")}"'
        elif element.value_of_css_property('border-bottom'):
            assert element.value_of_css_property('border-color-bottom') == colors[color], f'Incorrect border color. \
                Expected "{colors[color]}", actually "{element.value_of_css_property("border-color-bottom")}"'
