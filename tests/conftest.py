from selene import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def setup():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 750
    browser.config.window_height = 1500
    browser.config.timeout = 6.0
    yield
    browser.quit()