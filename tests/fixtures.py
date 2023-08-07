import pytest
from base.wd_setup import WebDriverSetup
from pages.auth_page import AuthPage


@pytest.fixture(scope="module")
def auth_page_fixture():
    driver = WebDriverSetup('Chrome', ['detach']).configure()
    auth_page = AuthPage(driver)
    yield driver, auth_page
    driver.quit()
