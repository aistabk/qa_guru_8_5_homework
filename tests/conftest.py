import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.timeout = 8.0
    browser.config.window_width = 600
    browser.config.window_height = 1900
    yield
    browser.quit()
