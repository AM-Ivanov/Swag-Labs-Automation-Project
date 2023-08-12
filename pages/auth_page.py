from pages.base_page import BasePage
from base.elements.button import Button
from base.elements.input_field import InputField
from base.elements.base_element import BaseElement


class AuthPage(BasePage):
    def __init__(self, driver, url='https://www.saucedemo.com/'):
        super().__init__(driver, url)
        # Basic elements
        self.HEADER = BaseElement('HEADER', '//div[@class="login_logo"]', self.driver)
        self.USERNAME_FIELD = InputField('USERNAME_FIELD', '//input[@id="user-name"]', self.driver)
        self.PASSWORD_FIELD = InputField('PASSWORD_FIELD', '//input[@id="password"]', self.driver)
        self.LOGIN_BUTTON = Button('LOGIN_BUTTON', '//input[@id="login-button"]', self.driver)
        self.basic_elements = (
            self.HEADER, self.USERNAME_FIELD, self.PASSWORD_FIELD, self.LOGIN_BUTTON)
        # Failed auth
        self.FAILED_LOGIN_BANNER = BaseElement(
            'FAILED_LOGIN_BANNER', '//div[@class="error-message-container error"]', self.driver)
        self.FAILED_LOGIN_TEXT = BaseElement(
            'FAILED_LOGIN_TEXT', '//div[@class="error-message-container error"]/h3[@data-test="error"]', self.driver)
        self.FAILED_LOGIN_BUTTON = Button('FAILED_LOGIN_BUTTON', '//button[@class="error-button"]', self.driver)
        self.FAILED_LOGIN_USERNAME_FIELD_ICON = BaseElement(
            'FAILED_LOGIN_USERNAME_FIELD_ICON',
            '//input[@id="user-name"]/following-sibling::*[@data-icon="times-circle"]', self.driver)
        self.FAILED_LOGIN_PASSWORD_FIELD_ICON = BaseElement(
            'FAILED_LOGIN_PASSWORD_FIELD_ICON',
            '//input[@id="password"]/following-sibling::*[@data-icon="times-circle"]', self.driver)
        self.failed_auth_elements = (
            self.FAILED_LOGIN_BANNER, self.FAILED_LOGIN_TEXT, self.FAILED_LOGIN_BUTTON,
            self.FAILED_LOGIN_USERNAME_FIELD_ICON, self.FAILED_LOGIN_PASSWORD_FIELD_ICON)
