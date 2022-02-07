from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(30)
driver.get("https://app.hubspot.com/login/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '#username').send_keeys("Riya123@yahoo.com")
driver.find_element(By.CSS_SELECTOR, '#password').send_keeys("Riya123@")
time.sleep(30)
print(driver.title)