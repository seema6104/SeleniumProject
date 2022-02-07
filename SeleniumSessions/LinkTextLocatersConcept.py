from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demoqa.com/links")

driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)

allLinks_element = driver.find_elements(By.TAG_NAME, 'a')
print(len(allLinks_element))
for ele in allLinks_element:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))
time.sleep(5)