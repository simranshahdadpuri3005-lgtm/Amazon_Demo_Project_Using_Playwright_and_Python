import pytest
from playwright.sync_api import sync_playwright
from pages.homePage import HomePage
from pages.loginPage import LoginPage

# we are overriding the page to see the execution clearly by explicitly providing the steps
# we are just redeclare the page fixture and how it should behave

@pytest.fixture(scope="session")
def page():    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5000)
        page = browser.new_page()
        yield page
        browser.close()


#creation of objects in conftest will help in reducing the object creation again and again for test cases
@pytest.fixture()
def home_page(page):
    home_page = HomePage(page)
    #after creation of this object, constructor will automatically triggered
    return home_page

@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page


