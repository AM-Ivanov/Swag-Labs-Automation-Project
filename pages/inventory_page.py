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
            # 'PRODUCTS_TITLE':
            #     BaseElement('//div[@class="header_secondary_container"]/span[@class="title"]', self.driver),
            # # тут надо написать класс под выпадающие списки
            # 'SORT_BUTTON': Button('//select[@class="product_sort_container"]', self.driver),
            # # тут тоже подумать, как лучше реализовать
            # 'ITEM_WIDGET': BaseElement('//div[@class="app_logo"]', self.driver),
            # # добавить класс картинок
            # 'ITEM_IMG': BaseElement('((//div[@class="inventory_item_img"])[1]', self.driver),
            # 'ITEM_TITLE': BaseElement('(//div[@class="inventory_item_name"])[1]', self.driver),
            # 'ITEM_DESC': BaseElement('(//div[@class="inventory_item_desc"])[1]', self.driver),
            # 'ITEM_PRICE': BaseElement('(//div[@class="inventory_item_price"])[1]', self.driver),
            # 'ITEM_ADD_BUTTON': Button('(//button[@id="add-to-cart-sauce-labs-backpack"])[1]', self.driver)
        }