from selenium import webdriver


driver = webdriver.Chrome()

driver.get("www.google.com")


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from web