from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.jquery-az.com/jquery/demo.php?ex=48.0_1")
time.sleep(5)
dropDown_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Washington']").click()
