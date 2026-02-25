
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import time


driver = webdriver.Chrome()


driver.get("https://www.geeksforgeeks.org/")

driver.maximize_window()

time.sleep(3)



searchIcon = driver.find_element(By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[2]")


time.sleep(3)


enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")

time.sleep(3)


enterText.send_keys("Data Structure")

time.sleep(3)

enterText.send_keys(Keys.RETURN)

time.sleep(30)