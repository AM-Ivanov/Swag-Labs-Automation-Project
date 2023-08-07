from tests.fixtures import auth_page_fixture
from pages.inventory_page import InventoryPage


class TestAuth:
    def test_auth_success(self, auth_page_fixture):
        driver, auth_page = auth_page_fixture[0], auth_page_fixture[1]
        auth_page.elements['USERNAME_FIELD'].enter_value('standard_user')
        auth_page.elements['PASSWORD_FIELD'].enter_value('secret_sauce')
        auth_page.elements['LOGIN_BUTTON'].click()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        inventory_page = InventoryPage(driver)
        checking_els = ('HEADER', 'MENU_BUTTON', 'CART_BUTTON')
        for el in checking_els:
            inventory_page.elements[el].find()


