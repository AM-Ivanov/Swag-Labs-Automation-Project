from pages.base_page import BasePage
from base.wd_setup import WebDriverSetup
from base.input_field_steps import InputFieldSteps


class AuthPage(BasePage):

    def __init__(self, driver, url='https://www.saucedemo.com/'):
        super().__init__(driver, url)
        self.elements = {
            'HEADER': '//div[@class="login_logo"]',
            'USERNAME_FIELD': '//input[@id="user-name"]',
            'PASSWORD_FIELD': '//input[@id="password"]',
            'LOGIN_BUTTON': '//input[@id="login-button"]',
        }
        self.failed_auth_elements = {'FAILED_LOGIN_BANNER': '//div[@class="error-message-container error"]',
                                     'FAILED_LOGIN_TEXT': '//h3[@data-test="error"]',
                                     'FAILED_LOGIN_BUTTON': '//button[@class="error-button"]',
                                     'FAILED_LOGIN_USERNAME_FIELD_ICON': '//input[@id="user-name"]/following-sibling::*['
                                                                         '@data-icon="times-circle"]',
                                     'FAILED_LOGIN_PASSWORD_FIELD_ICON': '//input[@id="password"]/following-sibling::*['
                                                                         '@data-icon="times-circle"]'}
