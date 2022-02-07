from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.usertesting.com/platform?utm_source=mkto-fallback")
time.sleep(5)
request_Trial_Link= driver.find_element(By.XPATH, "//a[@class='btn']")
driver.execute_script("arguments[0].click();", request_Trial_Link)
first_name = driver.find_element(By.ID, "FirstName_0.23915351564377563")