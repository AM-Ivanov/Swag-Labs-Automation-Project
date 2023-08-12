from pages.base_page import BasePage
from base.elements.button import Button
from base.elements.base_element import BaseElement


class InventoryPage(BasePage):

    def __init__(self, driver, url='https://www.saucedemo.com/inventory.html'):
        super().__init__(driver, url)
        self.HEADER = BaseElement('HEADER', '//div[@class="app_logo"]', self.driver)
        self.MENU_BUTTON = Button('MENU_BUTTON', '//button[@id="react-burger-menu-btn"]', self.driver)
        self.CART_BUTTON = Button('CART_BUTTON', '//a[@class="shopping_cart_link"]', self.driver)
        self.elements = (
            self.HEADER, self.MENU_BUTTON, self.CART_BUTTON
        )
