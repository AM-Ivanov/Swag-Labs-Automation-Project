from selenium import webdriver
from selenium.webdriver.common.by import By


class InputSteps:
    def __init__(self, driver):
        self.driver = driver

    def enter_value(self, element, value):
        element = self.driver.find_element(By.XPATH, element)
        element.send_keys(value)
        assert element.get_attribute('value') == value, f'Wrong text in field. Expected "{value}", actually "{element.text}".'

    def clear_field(self, element):
        element = self.driver.find_element(By.XPATH, element)
        element.clear()
        assert element.get_attribute('value') == '', f'Field is not empty.'
