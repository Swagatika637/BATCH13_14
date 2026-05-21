#Pop_up : A popup is a small window or message that appears on top of a webpage or app — usually to grab your attention, show information, or ask you to take an action (like clicking OK, filling a form, or closing it).
#Alert : An alert is a small popup message that appears in your browser, usually created with JavaScript. It can show information, ask for confirmation (OK/Cancel), or request input (a text box).You must interact with it (click OK or Cancel) before continuing to use the page.
# Both are using in javascript

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# Alert is a class used to interact with alert prompts. It contains methods for dismissing,accepting, inputting and getting text from alert prompts.
import time

driver =webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# Alert
name = driver.find_element(By.ID,'name')
name.send_keys('Abhilash')

alert_button = driver.find_element(By.ID,'alertbtn').click()
# At a single time multiple alerts can't come because system freez when an alert arise.

time.sleep(2)
alert = Alert(driver)
alert.accept()
# '''
# '''# Pop_up
name = driver.find_element(By.ID,'name')
name.send_keys('Abhilash')
pop_up_button = driver.find_element(By.ID,'confirmbtn').click()
alert = Alert(driver)
# It is used to handle the alert
# alert.accept()
# If you want to click on 'Ok'
# text_from_alert = alert.text
# print(text_from_alert)
# if you want to fetch the text from alert
alert.dismiss()
# If you want to 'cancel'

time.sleep(3)

driver.close()

