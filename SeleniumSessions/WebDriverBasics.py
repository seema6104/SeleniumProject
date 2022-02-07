from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://www.google.com")

driver.find_element(By.NAME, 'q').send_keys("Naveen automation lab")
optionlist =driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li')
print(len(optionlist))

for ele in optionlist:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break

print(driver.title)
time.sleep(5)
driver.quit()