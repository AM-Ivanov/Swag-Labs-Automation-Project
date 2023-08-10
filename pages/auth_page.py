from pages.base_page import BasePage
from base.elements.button import Button
from base.elements.input_field import InputField
from base.elements.base_element import BaseElement


class AuthPage(BasePage):

    def __init__(self, driver, url='https://www.saucedemo.com/'):
        super().__init__(driver, url)
        self.elements = {
            'HEADER': BaseElement('//div[@class="login_logo"]', self.driver),
            'USERNAME_FIELD': InputField('//input[@id="user-name"]', self.driver),
            'PASSWORD_FIELD': InputField('//input[@id="password"]', self.driver),
            'LOGIN_BUTTON': Button('//input[@id="login-button"]', self.driver),
        }
        self.failed_auth_elements = {
            'FAILED_LOGIN_BANNER': BaseElement('//div[@class="error-message-container error"]'
                                               , self.driver),
            'FAILED_LOGIN_TEXT': BaseElement('//div[@class="error-message-container error"]/h3[@data-test="error"]',
                                             self.driver),
            'FAILED_LOGIN_BUTTON': Button('//button[@class="error-button"]', self.driver),
            'FAILED_LOGIN_USERNAME_FIELD_ICON': BaseElement('//input[@id="user-name"] \
                                        /following-sibling::*[@data-icon="times-circle"]', self.driver),
            'FAILED_LOGIN_PASSWORD_FIELD_ICON': BaseElement('//input[@id="password"] \
                                        /following-sibling::*[@data-icon="times-circle"]', self.driver)
        }
