from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")
time.sleep(4)
print("get")
get = driver.find_element(By.NAME,"q")
s = get.send_keys("git")
print("send key")
time.sleep(5)

enter = driver.find_element(By.NAME,"btnK")
# enter.click()
enter.submit()
# enter.send_keys(Keys.ENTER)
time.sleep(5)
print("enter")
driver.close()


