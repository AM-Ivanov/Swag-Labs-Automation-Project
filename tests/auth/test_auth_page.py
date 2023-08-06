from tests.fixtures import auth_page_fixture


class TestAuthPage:

    def test_base_elements_are_present(self, auth_page_fixture):
        auth_page = auth_page_fixture
        auth_page.elements_are_on_page(auth_page.elements)

    def test_base_elements_have_required_properties(self, auth_page_fixture):
        auth_page = auth_page_fixture
        auth_page.elements['HEADER'].element_text_equals('Swag Labs')
        auth_page.elements['HEADER'].color_equals('black')
        auth_page.elements['USERNAME_FIELD'].placeholder_equals('Username')
        auth_page.elements['PASSWORD_FIELD'].placeholder_equals('Password')
        auth_page.elements['LOGIN_BUTTON'].button_name_is('Login')
        auth_page.elements['LOGIN_BUTTON'].color_equals('black')
        auth_page.elements['LOGIN_BUTTON'].background_color_equals('green')
