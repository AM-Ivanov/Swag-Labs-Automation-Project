from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)
        self.elements = {}

    def find_all_elements(self):
        self.driver.implicitly_wait(4)
        for element in self.elements:
            try:
                self.driver.find_element(By.XPATH, self.elements[element])
            except:
                print(f'Failed to find element "{element}"')