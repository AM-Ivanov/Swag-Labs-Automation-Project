from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

    def elements_are_on_page(self, elements):
        self.driver.implicitly_wait(4)
        for name in elements:
            try:
                elements[name].find()
            except:
                print(f'Failed to find element "{name}"') # тут надо пофиксить принт, возвращает не пойми что