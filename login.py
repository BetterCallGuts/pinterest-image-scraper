from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time
import os
from dotenv import load_dotenv
import logging

load_dotenv()

url = os.environ.get("url")

def login_and_save_cookies():
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    logging.debug("Driver initialized")
    driver.get(url)  
    logging.debug("Page loaded")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[2]/button').click()
    driver.implicitly_wait(5)

    driver.find_element(By.NAME, "id").send_keys(os.environ.get("email_")) 
    driver.find_element(By.NAME, "password").send_keys(os.environ.get("password_"))
    driver.find_element(By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[1]/form/div[7]/button').click()
    logging.debug("Login complete")
    driver.implicitly_wait(5)


    with open("cookies.json", "w") as file:
        json.dump(driver.get_cookies(), file)
    print("Cookies saved to cookies.json")

    return driver

def load_cookies_into_session(session, filename):
    logging.debug("Loading cookies")
    with open(filename, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
    logging.debug("Cookies loaded")
