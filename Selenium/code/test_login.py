import pytest
from _pytest.fixtures import FixtureRequest
import time

from ui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait




class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        #self.LKPage\

        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass

class LoginPage(BasePage):
    url = 'https://park.vk.company/'

    def login(self, user, password):
        login_button = self.driver.find_element(*basic_locators.ParkVKLocators.LOGIN_BUTTON)
        login_button.click()

        github_oauth_link = self.driver.find_element(*basic_locators.ParkVKLocators.GITHUB_OAUTH_LINK)

        time.sleep(5)
        #WebDriverWait(self.driver, 10).until(EC.url_to_be('https://park.vk.company/feed/'))

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://park.vk.company/feed/'

    def __init__(self, driver):
        self.driver = driver

    def click_menu_item(self, item_name):
        menu_item = self.driver.find_element(By.LINK_TEXT, item_name)
        time.sleep(2)
        menu_item.click()


class TestLogin(BaseCase):
    authorize    = True

    def test_login(self, credentials):
        pass


class TestLK(BaseCase):

    def test_lk1(self):
        pass

    def test_lk2(self):
        pass

    def test_lk3(self):
        pass
