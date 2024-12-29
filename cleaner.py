import re
import time
from bs4 import BeautifulSoup
import requests
import os
from login import login_and_save_cookies
import logging
from selenium import webdriver


url = os.environ.get("url")


def init() -> webdriver :
    logging.basicConfig(filename='base.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
    os.makedirs("data", exist_ok=True)
    logging.debug("Made data folder")
    driver = login_and_save_cookies()
    driver.get(f"https://www.pinterest.com/search?q={os.environ.get('topic_')}")
    time.sleep(5)
    driver.implicitly_wait(5)
    logging.debug("Search page loaded")
    return driver


def sanitize_filename(filename:str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


def handle_divs(divs:list[BeautifulSoup]) -> list:
    result = []
    if divs:
        a = divs[0].find_all("a")
        for a_sinle in a:
            href:str = a_sinle.attrs.get("href")
            if href:
                if href.startswith("/pin/"):
                    href = url + href
                    result.append(href)
                
        return list(set(result))
    else:
        logging.error("No divs found")
        exit(1)

def handle_link(link:str, driver:webdriver.Chrome) -> None:
    driver.get(link)
    time.sleep(4)
    driver.implicitly_wait(5)
    soup_    = BeautifulSoup( driver.page_source, "lxml")
    div      = soup_.find("div",{"data-test-id" : "closeup-container"})
    if div:
        img      = div.find("img")
        if img:
            img_src = img.attrs.get("src")

            if img_src:
                h1 = soup_.find("h1")
                response = requests.get(img_src)
                with open(f"{os.path.join("data",sanitize_filename(h1.text))}.jpg", "wb") as file:
                    file.write(response.content)