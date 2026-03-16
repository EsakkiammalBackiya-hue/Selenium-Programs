from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.LINK_TEXT,"Images").click()
time.sleep(10)