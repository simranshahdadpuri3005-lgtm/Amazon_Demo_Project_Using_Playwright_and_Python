import nt
import os
from dotenv import load_dotenv
#load_dotenv()  reads the .env file and loads the environment variables

#one way to get data from command line is by using os.getenv
def test_getDataFromCommanLine():
    userName = os.getenv("userName")
    #using os.getenv, we are passing the username while execution 
    print("username passed from terminal is ", userName)
    password = os.getenv("password")
    print("password passed from terminal is ", password)


# To run this test, use the command:
# $env:userName="simran@test.com"; pytest -s

#to pass two values
# $env:userName="simran@gmail.com"
# $env:password="MySecretPassword"
# pytest -s

# or
# $env:userName="simran@gmail.com"; $env:password="MySecretPassword"; pytest -s

#we need to install pip install python-dotenv
#another way to get data from command line using dotenv module

def test_getDataFromEnvFile():
    load_dotenv(".env")   #loading the .env file
    userName = os.getenv("Amazon_username") #varaible name should be same as passed in the env file
    password = os.getenv("Amazon_password")
    print("username passed from env file is ", userName)
    print("password passed from env file is ", password)
   


