from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.Meetup.com")
driver.maximize_window()
time.sleep(3)
# WebDriverWait(driver,timeout=10).until("document_initialised")
print("get")


f_login = driver.find_element(By.ID,"login-link")
f_login.click()
# f_login.send_keys(Keys.ENTER)
time.sleep(3)
print("click to login")

# email
email = driver.find_element(By.ID,"email")
email.send_keys("nk.empiric@gmail.com")
time.sleep(3)

# password
s = driver.find_element(By.ID,"current-password")
s.send_keys("neha0409!@")
time.sleep(13)
s.send_keys(Keys.ENTER)
# s.click()

print("enterrrrrrrrrrrrr")
time.sleep(15)
print("sleep-15")
# submit
# submit = driver.find_element(By.NAME,"submitButton")
# submit.send_keys(Keys.ENTER)
# time.sleep(13)
# print("Logged in")


h = driver.find_element(By.NAME,"keywords")
h.send_keys("health")
h.send_keys(Keys.ENTER)
time.sleep(15)
print("search health")


# s = driver.find_element(By.ID,"location-search-submit")
# s.send_keys(Keys.ENTER)
# time.sleep(12)
# print("click login")

s = driver.find_element(By.ID,"event-card-in-search-results")
s.send_keys(Keys.ENTER)
time.sleep(10)
print("click login")
# neha0409!@
