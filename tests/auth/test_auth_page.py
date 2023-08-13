import pytest
from tests.fixtures import auth_page_fixture


@pytest.mark.basic_auth_tests
@pytest.mark.auth_layout_tests
class TestAuthPage:

    def test_basic_elements_are_present(self, auth_page_fixture):
        auth_page = auth_page_fixture[1]
        auth_page.elements_are_on_page(auth_page.basic_elements)

    def test_basic_elements_have_required_properties(self, auth_page_fixture):
        auth_page = auth_page_fixture[1]
        auth_page.HEADER.element_text_equals('Swag Labs')
        auth_page.HEADER.color_equals('black')
        auth_page.USERNAME_FIELD.placeholder_equals('Username')
        auth_page.PASSWORD_FIELD.placeholder_equals('Password')
        auth_page.LOGIN_BUTTON.button_name_is('Login')
        auth_page.LOGIN_BUTTON.color_equals('black')
        auth_page.LOGIN_BUTTON.background_color_equals('green')
