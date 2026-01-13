import pytest
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.account = page.locator("#nav-link-accountList")
        self.signInbtn = page.locator("#nav-flyout-ya-signin")
    
    def hoverOnAccount(self):
        self.account.hover()

    def clickOnSignInbtn(self):
        self.account.wait_for()
        self.signInbtn.click()


    def launchTheAmazonBrowser(self):
        self.page.goto("https://www.amazon.in/")
        self.account.wait_for(timeout=40000)

    def searchForProduct(self, value):
        self.searchTab.fill(value)
        self.searchBtn.click()
    
        