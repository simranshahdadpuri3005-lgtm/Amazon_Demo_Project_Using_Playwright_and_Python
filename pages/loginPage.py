from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page:Page): # page is default fixture by pytest
        self.page = page
        self.emailTextBox = page.locator("#ap_email_login")
        self.submitBtn = page.locator("input[type='submit']")
        self.passwordTextBox = page.locator("#ap_password")

    
    def enterEmailId(self, emailValue):
        self.emailTextBox.fill(emailValue)
        #fill function will clear the field and then enter the value

    def clickOnContinueBtn(self):
        self.submitBtn.click()

    def enterPassword(self, passwordValue):
        self.passwordTextBox.fill(passwordValue)



