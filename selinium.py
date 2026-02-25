from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://books.toscrape.com")

time.sleep(30)