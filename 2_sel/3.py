from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.Meetup.com")
# driver.maximize_window()
# print("max window")
# driver.save_screenshot("sel.png")
print("ss")
print("IN meetup.com")
time.sleep(10)
# driver.close()
print("done")


# f_login = driver.find_element(By.ID,"login-link")
# f_login.click()
# # f_login.send_keys(Keys.ENTER)
# time.sleep(3)
# print("click to login")

# # email
# email = driver.find_element(By.ID,"email")
# email.send_keys("nk.empiric@gmail.com")
# time.sleep(3)

# # password
# s = driver.find_element(By.ID,"current-password")
# s.send_keys("neha0409!@")
# time.sleep(3)
# # s.send_keys(Keys.ENTER)
# s.submit()
# print("Logged In")
# time.sleep(15)

# # h = driver.find_element(By.NAME,"keywords")
# # h.send_keys("health")
# # h.send_keys(Keys.ENTER)
# # time.sleep(15)
# # print("search health")

# # s = driver.find_element(By.ID,"event-card-in-search-results")
# # s.send_keys(Keys.ENTER)
# # time.sleep(10)

# driver.find_element(By.CLASS_NAME,"DayPicker-Day").click()
# print("done")
# time.sleep(15)


d = driver.find_element(By.XPATH,'//*[@id="page"]/div[2]/main/div[1]/div[1]/div/div[1]/h1')
print("done")
time.sleep(15)
print(d.text)