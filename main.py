#############################################################################################################
#                                                                                                           #
#..........................................Imports and librarys.............................................#
#                                                                                                           #
#############################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import time
import requests
import json
from flask import Flask, request, Response, abort

from os import read
import time
import pytz
from types import SimpleNamespace
import selenium

from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
from datetime import date, datetime
import json
import math
from selenium.common.exceptions import StaleElementReferenceException


#############################################################################################################
#                                                                                                           #
#.....................................Driver Definations and Objects........................................#
#                                                                                                           #
#############################################################################################################


keyboard = Controller()

options = webdriver.FirefoxOptions()
options.headless = True
driver1 = webdriver.Firefox(
    executable_path="C:\Drivers\geckodriver.exe", options=options)
driver = webdriver.Firefox(
    executable_path="C:\Drivers\geckodriver.exe")

actions = webdriver.ActionChains(driver)
wait = WebDriverWait(driver, 25)

#############################################################################################################
#                                                                                                           #
#................................Login credentials for trading Platform.....................................#
#                                                                                                           #
#############################################################################################################


driver.get('https://kite.zerodha.com/')
driver.maximize_window()

driver.find_element(By.ID, 'password').send_keys("bvsailor87")
driver.find_element(By.ID, 'userid').send_keys("SB4984")
driver.find_element(By.CLASS_NAME, 'actions').click()


driver.implicitly_wait(50)
driver.find_element(By.ID, 'search-input')

print("kite page opened")

sec = driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]/div[1]")
print("hiu lulu")

print(sec.text)

#############################################################################################################
#                                                                                                           #
#................................Flask App and DaTA FETCHING through webhook................................#
#                                                                                                           #
#############################################################################################################


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data1 = json.loads(request.data)
        baselist = data1['stocks']
        list = tuple(map(str, baselist.split(',')))
        driver.find_element(
            By.ID, 'search-input').send_keys(list[0] + Keys.ENTER)

        # Tiker location

        wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, "info")))
        stop1 = driver.find_element(By.CLASS_NAME, "info")
        actions.move_to_element(stop1).click().perform()
        print("got it 1")
        # BUy Button
        wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#app span:nth-child(1) > button[type='button']")))
        stop2 = driver.find_element_by_css_selector(
            "#app span:nth-child(1) > button[type='button']")
        print("got it 2")
        actions.move_to_element(stop2).click().perform()

        ###

        # driver.find_element_by_xpath(
        #     "/html/body/div[1]/form/section/div[2]/div[1]/div/div[2]/label/span").click().perform()

        # Quantity element
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/div[2]/div[2]/div[2]/div[2]/div/div[1]/label").click()

        # Quantity input box
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/div[2]/div[2]/div[1]/div[1]/div/input").send_keys("2")
        # stop loss element
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/div[3]/div/div[2]/div[1]/label").click()

        # stoploss input box
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/div[3]/div/div[2]/div[2]/div/input").send_keys("-2")

        # Target element
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/div[3]/div/div[3]/div[1]/label/span[1]").click()

        # target input box
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/div[3]/div/div[3]/div[2]/div/input").send_keys("1.5")

        # submit order
        driver.find_element_by_xpath(
            "/html/body/div[1]/form/section/footer/div/div[2]/button[1]").click()

        #  lst = data1['stocks']
        # print(lst)
        # print(len(lst))
        print(list[0])
        print(len(list))
        # print(data1)
        # print(type(data1))
        # with open("memory.json", "r") as myfile:
        #     # reading = myfile.read()
        #     data2 = json.load(myfile)
        #     data2.append(data1)
        # with open("memory.json", "w") as file:
        #     json.dump(data2, file)
        # r = data2.append(data2)
        # myfile.write(r)
        # json.dump(data1, myfile)
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()

driver.find_element(By.ID, 'search-input').send_Keys(list[0])
