import os
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from time import sleep

from dotenv import load_dotenv
load_dotenv()

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()   
   
    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--log-level=1')
        
        print (os.environ.get('SELENIUM_HEADLESS'))

    if options in options:
        chrome_options.add_argument(options)  

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = make_chrome_browser()
    browser.get('http://www.udemy.com.br')
    sleep(3)
    browser.quit()