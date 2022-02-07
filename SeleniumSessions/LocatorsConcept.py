from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
driver.find_element(By.ID, 'Form_submitForm_subdomain').send_keys('Naveen AutomationLab')
fullName = driver.find_element(By.ID, 'Form_submitForm_Name')
fullName.send_keys('Tina Mahajan')
time.sleep(3)
email = driver.find_element(By.ID, 'Form_submitForm_Email')
email.send_keys('TinaM345@gmail.com')
time.sleep(3)
phoneNum = driver.find_element(By.ID, 'Form_submitForm_Contact')
phoneNum.send_keys('5641232345')
time.sleep(3)
select_contry = Select(driver.find_elements(By.ID, 'Form_submitForm_Country'))
#print('Total country: ',len(select_contry))
select_contry.select_by_visible_text('Australia')
'''header_element = driver.find_elements(By.TAG_NAME, 'h1')
print(len(header_element))
time.sleep(5)
print("Header is : ", header_element.text) '''
allLinks_element = driver.find_elements(By.TAG_NAME, 'a')
print(len(allLinks_element))
for ele in allLinks_element:
    link_text = ele.text
    print(link_text)
time.sleep(5)
