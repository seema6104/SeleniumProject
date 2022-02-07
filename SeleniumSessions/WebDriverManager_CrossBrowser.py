from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName= "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari
else:
    print("Please pass the correct browser " + browserName)

driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys('naveenanimation30@gmail.com')
time.sleep(3)
driver.find_element(By.ID, 'password').send_keys('Test@12345')
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)

time.sleep(10)



