from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(10)

# ******************** FIND SEARCH ******************************
a = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
print("find search")
# SEND KEY
a.send_keys("OnePlus Nord CE 2 Lite")
a.send_keys(Keys.ENTER)
print("enter key preesed")     
time.sleep(5)

# ******************** CLICK TO FIRSTELEMENT ******************************
driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a').click()
print("clicked to first element ")
time.sleep(20)

# ******************** SCRAPING DETAILS ******************************
# PRICE
# # a = driver.find_element(By.XPATH,'//div[@class="celwidget"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')
# # driver.find_element(By.XPATH,'//table[@class="a-lineitem a-align-top"]/tbody/tr[2]/td[2]/span[1]/span[1]')
# driver.find_element(By.XPATH,'//div[@id="centerCol"]/div[10]/div[2]/div/table/tbody/tr[2]/td/span[1]/span[1]')
WebDriverWait(driver, 40).until(ec.presence_of_element_located((By.XPATH,'//div[@id="centerCol"]/div[10]/div[2]/div/table/tbody/tr[2]/td/span[1]/span[1]')))
print("find price")
time.sleep(5)

# DETAILS
# driver.find_element(By.XPATH,'//table[@class="a-normal a-spacing-micro"]/tbody')
# b = WebDriverWait(driver,30).until(ec.presence_of_element_located((By.XPATH,'//table[@class="a-normal a-spacing-micro"]/tbody')))
# print("found details ")
# time.sleep(7)