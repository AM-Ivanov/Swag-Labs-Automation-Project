from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from base.error_texts import Errors
from base.colors import colors


class BaseElement:
    def __init__(self, name: str, locator: str, driver: WebDriver, wait=4):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.locator = locator
        self.name = name
        self.element = None  # None because there is no need to find element when creating page class object

    def find(self):
        if self.element is None:
            self.element = self.wait.until(ec.presence_of_element_located((By.XPATH, self.locator)))

    def is_presented(self):
        try:
            self.driver.find_element(By.XPATH, self.locator)
        except:
            return False
        return True

    def element_text_equals(self, text):
        self.find()
        assert self.element.text == text, f'Incorrect element text. Expected {text}, actually {self.element.text}'

    def color_equals(self, color):
        self.find()
        assert self.element.value_of_css_property('color') == colors[color], \
            Errors.validation_error.format('color', colors[color], self.element.value_of_css_property('color'))

    def background_color_equals(self, color):
        self.find()
        assert self.element.value_of_css_property('background-color') == colors[color], \
            Errors.validation_error.format('background-color', colors[color],
                                           self.element.value_of_css_property('background-color'))

    def border_color_equals(self, color):
        self.find()
        assert self.element.value_of_css_property('border-color') == colors[color], Errors.validation_error.format(
            'border-color', colors[color], self.element.value_of_css_property('border-color'))

    def border_bottom_color_equals(self, color):
        self.find()
        assert self.element.value_of_css_property('border-bottom-color') == colors[
            color], Errors.validation_error.format(
            'border-color', colors[color], self.element.value_of_css_property('border-bottom-color'))
