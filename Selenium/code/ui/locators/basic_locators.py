from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass

class ParkVKLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.nav__button__menu>a')
    GITHUB_OAUTH_LINK = (By.CSS_SELECTOR, 'a.social-link[href="/social/login/github/"]')
    

    