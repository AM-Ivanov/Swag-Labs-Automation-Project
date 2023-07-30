elements = {
    'HEADER': '//div[@class="login_logo"]',
    'USERNAME_FIELD': '//input[@id="user-name"]',
    'PASSWORD_FIELD': '//input[@id="password"]',
    'LOGIN_BUTTON': '//input[@id="login-button"]',
    'FAILED_LOGIN_BANNER': '//div[@class="error-message-container error"]',
    'FAILED_LOGIN_TEXT': '//h3[@data-test="error"]',
    'FAILED_LOGIN_BUTTON': '//button[@class="error-button"]',
    'FAILED_LOGIN_USERNAME_FIELD_ICON': '//input[@id="user-name"]/following-sibling::*[@data-icon="times-circle"]',
    'FAILED_LOGIN_PASSWORD_FIELD_ICON': '//input[@id="password"]/following-sibling::*[@data-icon="times-circle"]',
}

for element in elements:
    print(elements[element])
    print(element)
