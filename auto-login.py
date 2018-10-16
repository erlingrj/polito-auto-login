#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib import request
import time
import sys

USERNAME = "Wirte your username here"
PASSWORD = "Write your password here"


def connect_to_polito(username, password, options):
    try:
        driver = webdriver.Chrome(options = options)
    except:
        raise RuntimeError(sys.exc_info()[0])

    try:
        driver.get("https://wifiauth.polito.it/fs/customwebauth/login.html")
        usr_element = driver.find_element_by_name("username")
        pwrd_element = driver.find_element_by_name("password")
        login_button = driver.find_element_by_id("btnAccedi")


        usr_element.clear()
        pwrd_element.clear()

        usr_element.send_keys(username)
        pwrd_element.send_keys(password)

        login_button.click()

    except:
        raise RuntimeWarning("You are not connected to the Polito WIFI")
    
    
    driver.quit()


def check_internet_connection():
    try:
        request.urlopen("https://www.polito.it/", timeout=1)
        return True;
    except:
        print("Could not detect internet connection")
        return False


def main(*args, **kwargs):
    options = Options()
    options.add_argument('--headless')

    while True:
        if not check_internet_connection():
            connect_to_polito(USERNAME, PASSWORD, options)
        
        time.sleep(3)

if __name__ == '__main__':
    main()
