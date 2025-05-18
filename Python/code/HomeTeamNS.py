"""
Web Automation

From terminal(base): % conda activate py39
> pip install selenium

> brew install --cask chromedriver
"""

import time

import telepot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Browser Configuration (DO NOT EDIT)
BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
DRIVR_PATH = "/opt/homebrew/Caskroom/chromedriver/119.0.6045.105/chromedriver-mac-arm64/chromedriver"

service = Service(DRIVR_PATH)
options = webdriver.ChromeOptions()
options.binary_location = BRAVE_PATH
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)
###########################################################

# Auto-Fill Configuration:
URL = "https://safra-carpark.hometeamns.sg/public/validation"

IU = 715903797
CC_NO = 1111740147381006

NAME = "Joseph Gan"
MOBILE_NO = 97107958
SAFRA_ID = "A200287379"
VEHICLE_NO = "FBQ5939X"
############################################################

browser.get(URL)

IU_xpath = browser.find_element("xpath", '//*[@id="input-15"]')
IU_xpath.send_keys(IU)

CC_xpath = browser.find_element("xpath", '//*[@id="input-19"]')
CC_xpath.send_keys(CC_NO)

CheckStatus_xpath = browser.find_element(
    "xpath", '//*[@id="app"]/div/div[1]/div[2]/div[4]/div/button/span'
)
CheckStatus_xpath.click()

time.sleep(1)

try:
    ExistsRegistration = browser.find_element("css selector", ".v-alert__content")
except:
    ExistsRegistration = None
############################################################

# Notification Configurations:
TELEGRAMTOKEN = "6373995454:AAESQybFEJpPxsg9EDkKFi1a66kTk3AkFu4"
RECIEVER_ID = 260562811

bot = telepot.Bot(TELEGRAMTOKEN)

# Validate Registration Status: If registration does not exist proceed with registration otherwise terminate
if ExistsRegistration:
    bot.sendMessage(RECIEVER_ID, ExistsRegistration.text)
else:
    NAME_xpath = browser.find_element("xpath", '//*[@id="input-33"]')
    NAME_xpath.send_keys(NAME)

    MOBILE_xpath = browser.find_element("xpath", '//*[@id="input-37"]')
    MOBILE_xpath.send_keys(MOBILE_NO)

    SAFRA_ID_xpath = browser.find_element("xpath", '//*[@id="input-41"]')
    SAFRA_ID_xpath.send_keys(SAFRA_ID)

    VEHICLE_NO_xpath = browser.find_element("xpath", '//*[@id="input-45"]')
    VEHICLE_NO_xpath.send_keys(VEHICLE_NO)

    CheckTermsCondition_xpath = browser.find_element(
        "xpath",
        '//*[@id="app"]/div[1]/div[1]/div[2]/form/div[9]/div/div/div/div[1]/div/div',
    )
    CheckTermsCondition_xpath.click()

    Continue_xpath = browser.find_element(
        "xpath", '//*[@id="app"]/div[1]/div[1]/div[2]/form/div[10]/div/button/span'
    )
    Continue_xpath.click()

    time.sleep(1)

    SuccessRegistation = browser.find_element("css selector", ".v-alert__content")
    bot.sendMessage(RECIEVER_ID, SuccessRegistation.text)

browser.quit()
