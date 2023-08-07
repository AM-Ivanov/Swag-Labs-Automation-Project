from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from base.colors import colors


class BaseElement:
    def __init__(self, locator: str, driver: WebDriver):
        self.driver = driver
        self.locator = locator
        self.element = None # None because there is no need to find element when creating page class object

    def find(self):
        if self.element is None:
            self.element = self.driver.find_element(By.XPATH, self.locator)

    def element_text_equals(self, text):
        self.find()
        assert self.element.text == text, f'Incorrect element text. Expected {text}, actually {self.element.text}'

    def color_equals(self, color):
        self.find()
        assert self.element.value_of_css_property('color') == colors[
            color], f'Incorrect button color. Expected {colors[color]}, actually \
                    {self.element.value_of_css_property("color")}'

    def background_color_equals(self, color):
        self.find()
        assert self.element.value_of_css_property('background-color') == colors[
            color], f'Incorrect button color. Expected {colors[color]}, actually \
                    {self.element.value_of_css_property("background-color")}'
