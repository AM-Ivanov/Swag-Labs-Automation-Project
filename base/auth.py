import time
from selenium.webdriver.common.by import By


class auth:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'
        self.users = {'standart': 'standard_user', 'locked': 'locked_out_user', 'problem': 'problem_user',
                      'glitch': 'performance_glitch_user'}
        self.pass_for_all = 'secret_sauce'
        self.driver.get(self.base_url)
        self.login_field = self.driver.find_element(By.XPATH, '//input[@id="user-name"]')
        self.pass_field = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

    def succes_auth(self):
        self.login_field.send_keys(self.users['standart'])
        self.pass_field.send_keys(self.pass_for_all)
        self.login_button.click()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', f'Current page has unexpected URL: {self.driver.current_url}.'
        assert self.driver.find_element(By.XPATH,
                                        '//span[@class="title"]').text == 'Products', 'Unexpected page header.'

    def locked_user_auth(self):
        self.login_field.send_keys(self.users['locked'])
        self.pass_field.send_keys(self.pass_for_all)
        self.login_button.click()
        assert self.driver.current_url == 'https://www.saucedemo.com/', f'Current page has unexpected URL: {self.driver.current_url}.'
        assert self.driver.find_element(By.XPATH,
                                        '//div[@class="login_logo"]').text == 'Swag Labs', 'Unexpected page header.'
        locked_user_auth_error = self.driver.find_element(By.XPATH, '//div[@class = "error-message-container error"]')
        assert locked_user_auth_error.text == 'Epic sadface: Sorry, this user has been locked out.', 'Incorrect error message.'

    def problem_user_auth(self):
        self.login_field.send_keys(self.users['problem'])
        self.pass_field.send_keys(self.pass_for_all)
        self.login_button.click()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', f'Current page has unexpected URL: {self.driver.current_url}.'
        assert self.driver.find_element(By.XPATH,
                                        '//span[@class="title"]').text == 'Products', 'Unexpected page header.'
        first_item_img = self.driver.find_element(By.XPATH, '//img[@class= "inventory_item_img"][1]')
        assert first_item_img.get_attribute(
            'src') == 'https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg', 'Problem user sees unbugged product images.'

    def performance_glitch_user_auth(self):
        self.login_field.send_keys(self.users['glitch'])
        self.pass_field.send_keys(self.pass_for_all)
        self.login_button.click()
        time.sleep(5)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', f'Current page has unexpected URL: {self.driver.current_url}.'
        assert self.driver.find_element(By.XPATH,
                                        '//span[@class="title"]').text == 'Products', 'Unexpected page header.'
