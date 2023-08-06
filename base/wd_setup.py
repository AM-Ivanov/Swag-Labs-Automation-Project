from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class WebDriverSetup:
    def __init__(self, browser, required_options=None):
        self.browser = browser
        self.required_options = required_options

    def configure(self) -> WebDriver:
        options_browsers_dict = {'Chrome': [webdriver.ChromeOptions(), webdriver.Chrome],
                                 'Firefox': [webdriver.FirefoxOptions(), webdriver.Firefox],
                                 'Edge': [webdriver.EdgeOptions(), webdriver.Edge],
                                 'Ie': [webdriver.IeOptions(), webdriver.Ie]}
        if self.required_options:
            options = options_browsers_dict[self.browser][0]
            [options.add_experimental_option(option, True) for option in self.required_options]
            return options_browsers_dict[self.browser][1](options=options)
        else:
            return options_browsers_dict[self.browser][1]()
