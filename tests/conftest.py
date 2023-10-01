import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 110
    browser.config.window_height = 2300
    yield
    browser.quit()
