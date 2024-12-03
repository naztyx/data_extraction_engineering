from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

import time

# from requests_html import AsyncHTMLSession, HTMLSession

import pandas as pd

url = 'https://www.fiba.basketball/en/events/fiba-u17-basketball-world-cup-2024/games/114355-CAN-EGY#shotChart'

driver = webdriver.Chrome(service=Service('C:\\chromedriver\\chromedriver.exe'))

driver.get(url)

#maximize the window
driver.maximize_window()
print(driver.title)
# Scroll to the middle of the page
time.sleep(3)
# driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
# time.sleep(2)
driver.execute_script("window.scrollTo(0, 650);")
time.sleep(5)

# Set zoom to 70%
# driver.execute_script("document.body.style.zoom = '-50';")
driver.execute_script("document.body.style.zoom='80%';")
time.sleep(4)
# Wait for the elements to be interactable

wait = WebDriverWait(driver, 10)

uncheck_home_all = driver.find_element(By.XPATH, '//*[@id="radix-:rb:-content-shotChart"]/div/div/div[1]/div/main/div/div[2]/div/div[4]/div[1]/div/label/span')
uncheck_home_all.click()

uncheck_away_all = driver.find_element(By.XPATH, '//*[@id="radix-:rb:-content-shotChart"]/div/div/div[1]/div/main/div/div/div/div[4]/div[2]/div/label/span')
uncheck_away_all.click()

time.sleep(5)

driver.quit()
