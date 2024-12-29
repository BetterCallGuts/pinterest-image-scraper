from   bs4 import BeautifulSoup
from   login import   os, time
from  cleaner import  handle_divs, handle_link, init
import logging
from selenium import webdriver


url = os.environ.get("url")

def main():
    driver:webdriver  = init()
    logging.debug("Driver initialized")
    driver.implicitly_wait(5)
    for _ in range(int(os.environ.get("pages"))):
        

        soup:BeautifulSoup = BeautifulSoup(driver.page_source, "lxml")
        tables:list[BeautifulSoup] = soup.find_all("div",{"role" : "list"})
        result:list[str] = handle_divs(tables)
        time.sleep(5)

        for link in result:
            try:
                handle_link(link, driver)
            except Exception as e:
                logging.error(e)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.implicitly_wait(5)
        logging.debug("Scrolling")
    driver.quit()

if __name__ == "__main__":
    main()

