import pytest
from tests.fixtures import auth_page_fixture
from pages.inventory_page import InventoryPage
from base.error_texts import Errors


@pytest.mark.functional_auth_tests
class TestAuth:
    @pytest.mark.basic_auth_tests
    def test_successfull_auth(self, auth_page_fixture):
        driver, auth_page = auth_page_fixture[0], auth_page_fixture[1]
        auth_page.USERNAME_FIELD.enter_value('standard_user')
        auth_page.PASSWORD_FIELD.enter_value('secret_sauce')
        auth_page.LOGIN_BUTTON.click()
        inventory_page = InventoryPage(driver)
        assert driver.current_url == inventory_page.url
        inventory_page.elements_are_on_page(inventory_page.elements)

    @pytest.mark.negative_auth_tests
    def test_unsuccessfull_auth_with_correct_login_incorrect_password(self, auth_page_fixture):
        driver, auth_page = auth_page_fixture[0], auth_page_fixture[1]
        auth_page.USERNAME_FIELD.enter_value('standard_user')
        auth_page.PASSWORD_FIELD.enter_value('secret')
        auth_page.LOGIN_BUTTON.click()
        assert driver.current_url == auth_page.url
        auth_page.elements_are_on_page(auth_page.failed_auth_elements)
        auth_page.USERNAME_FIELD.border_bottom_color_equals('red')
        auth_page.PASSWORD_FIELD.border_bottom_color_equals('red')
        auth_page.FAILED_LOGIN_USERNAME_FIELD_ICON.color_equals('red')
        auth_page.FAILED_LOGIN_PASSWORD_FIELD_ICON.color_equals('red')
        auth_page.FAILED_LOGIN_BANNER.background_color_equals('red')
        auth_page.FAILED_LOGIN_TEXT.element_text_equals(
            'Epic sadface: Username and password do not match any user in this service')
        auth_page.FAILED_LOGIN_BUTTON.click()
        for elem in auth_page.failed_auth_elements:
            assert elem.is_presented() is False, Errors.element_presence_error.format(elem.name, 'is')
