from playwright.sync_api import Page, expect
from pages.homePage import HomePage  
#Homepage is class name
#homepage is python file inside pages folder
from pages.loginPage import LoginPage
import json
from utils.readingJson import readJsonData

def test_loginUsingValidCreds(page, home_page, login_page):
    home_page.launchTheAmazonBrowser()
    home_page.hoverOnAccount()
    home_page.clickOnSignInbtn()

    #code to handle the json file
    #with open(credentials) as f:
     #   testData = json.load(f)
    
    #print(testData)
    #print(testData["username"])
    #print(testData["password"])

    credentials = "testData\credentials.json"
    testData = readJsonData(credentials)

    login_page.enterEmailId(testData["username"])
    login_page.clickOnContinueBtn()
    login_page.enterPassword(testData["password"])
    login_page.clickOnContinueBtn()

