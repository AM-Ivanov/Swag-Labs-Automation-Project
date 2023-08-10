from tests.fixtures import auth_page_fixture
from pages.inventory_page import InventoryPage


class TestAuth:
    def test_successfull_auth(self, auth_page_fixture):
        driver, auth_page = auth_page_fixture[0], auth_page_fixture[1]
        auth_page.elements['USERNAME_FIELD'].enter_value('standard_user')
        auth_page.elements['PASSWORD_FIELD'].enter_value('secret_sauce')
        auth_page.elements['LOGIN_BUTTON'].click()
        inventory_page = InventoryPage(driver)
        assert driver.current_url == inventory_page.url
        inventory_page.elements_are_on_page(inventory_page.elements)

    def test_unsuccessfull_auth_with_correct_login_incorrect_password(self, auth_page_fixture):
        driver, auth_page = auth_page_fixture[0], auth_page_fixture[1]
        auth_page.elements['USERNAME_FIELD'].enter_value('standard_user')
        auth_page.elements['PASSWORD_FIELD'].enter_value('secret')
        auth_page.elements['LOGIN_BUTTON'].click()
        assert driver.current_url == auth_page.url
        auth_page.elements_are_on_page(auth_page.failed_auth_elements)
        auth_page.elements['USERNAME_FIELD'].border_color_equals('red')
        auth_page.elements['PASSWORD_FIELD'].border_color_equals('red')
        auth_page.failed_auth_elements['FAILED_LOGIN_USERNAME_FIELD_ICON'].color_equals('red')
        auth_page.failed_auth_elements['FAILED_LOGIN_PASSWORD_FIELD_ICON'].color_equals('red')
        auth_page.failed_auth_elements['FAILED_LOGIN_BANNER'].background_color_equals('red')
        auth_page.failed_auth_elements['FAILED_LOGIN_TEXT'].element_text_equals('Epic sadface: Password is required')
        auth_page.failed_auth_elements['FAILED_LOGIN_BUTTON'].click()
        for elem in auth_page.failed_auth_elements.keys():
            assert auth_page.failed_auth_elements[
                       elem].is_presented() is False, f"Element {elem} didn't disappear from the page like expected."
