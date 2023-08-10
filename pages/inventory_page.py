from pages.base_page import BasePage
from base.elements.button import Button
from base.elements.input_field import InputField
from base.elements.base_element import BaseElement


class InventoryPage(BasePage):

    def __init__(self, driver, url='https://www.saucedemo.com/inventory.html'):
        super().__init__(driver, url)
        self.elements = {
            'HEADER': BaseElement('//div[@class="app_logo"]', self.driver),
            'MENU_BUTTON': Button('//button[@id="react-burger-menu-btn"]', self.driver),
            'CART_BUTTON': Button('//a[@class="shopping_cart_link"]', self.driver),
        }
