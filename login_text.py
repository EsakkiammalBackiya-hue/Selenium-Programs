from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("C:/Users/USER/Desktop/Selenium/login.html")
driver.find_element(By.ID,"username").send_keys("testuser")
driver.find_element(By.ID,"password").send_keys("12345")
time.sleep(5)
