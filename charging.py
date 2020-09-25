# probably want to create fake account to login with
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass

def login(driver, username, password):
    # get login page
    driver.get("https://secure07c.chase.com/web/auth/dashboard#/dashboard/overviewAccounts/overview/index")
    time.sleep(10) #TODO fix so it knows when page loaded

    driver.switch_to.frame("logonbox")

    # save email and password field elements
    username_field = driver.find_element_by_id('userId-text-input-field')
    # username_field = driver.find_element_by_xpath('//*[@id="userId-text-input-field"]')
    password_field = driver.find_element_by_id('password-text-input-field')
    # password_field = driver.find_element_by_xpath('//*[@id="password-text-input-field"]')
    

    # enter email and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)


if __name__ == "__main__":
    """
    If executed from command line, this script will parse an xml file and output the reformatted json object to a new file.
    """

    print('Please enter Chase username')
    username = input()

    password = getpass.getpass(prompt='Please enter Chase password\n')

    driver = webdriver.Chrome()
    try:
        login(driver, username, password)
    except:
        print('exception')
        print(username)


    # with open(output_filename, "w") as file:
    #     file.write(output)
