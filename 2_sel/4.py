import urllib.request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#  get the source to download a img


driver.get("https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fmax%2F1400%2F1*HJpcblBvD8MpqAEZZXWVgg.png&imgrefurl=https%3A%2F%2Fmedium.com%2F%40moungpeter%2Fhow-to-automate-downloading-files-using-python-selenium-and-headless-chrome-9014f0cdd196&tbnid=nkiMwp6r7z9iHM&vet=12ahUKEwiNwuHjjtD7AhXYjtgFHX2fCW0QMygAegUIARC9AQ..i&docid=ok_G4d9EbJzWdM&w=1400&h=786&q=download%20image%20with%20selenium%20python&ved=2ahUKEwiNwuHjjtD7AhXYjtgFHX2fCW0QMygAegUIARC9AQ")

time.sleep(4)

img = driver.find_element(By.ID,"imi")
# img = driver.find_element(By.XPATH,"//img[@role='presentation'")
# img = driver.find_element(By.XPATH,"//img[@class='bg he hf c'")
print("find elemnt")
src = img.get_attribute('src')
print(src, "get attr------------")
# urllib.request.urlretrieve(src, 'd.png')
# data = urllib.request.urlopen(src)
# print("download img")


with open('dow.png','wb') as file:

    file.write(img.screenshot_as_png)