import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #invokes Chrome browser

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Selenium provides locators such as  ID, Xpath , CSSSelector, Classname, name, linkText

driver.find_element(By.NAME,"email").send_keys("chefrodneyachery@gmail.com") # Enters the email I provided
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Python123#@!") # Enters the password I provided
driver.find_element(By.ID,"exampleCheck1").click() # Clicks the checkbox as requested by the line of code













































time.sleep(2)