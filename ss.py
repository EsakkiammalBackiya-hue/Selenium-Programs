from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
driver_path="C:/Users/USER/Desktop/Selenium/chromedriver-win64/chromedriver.exe"
service=Service(driver_path)
driver=webdriver.Chrome(service=service)
driver.get("https://www.google.com")
time.sleep(3)
save_path="C:/Users/USER/Desktop/Selenium/screenshot.png"
folder=os.path.dirname(save_path)
if not os.path.exists(folder):
    os.makedirs(folder)
driver.save_screenshot(save_path)
print("Screenshot Saved Successfully at{save_path}")
driver.quit()