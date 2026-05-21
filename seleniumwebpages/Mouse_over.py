#Mouse_over : "Mouse over" just means move your mouse pointer on top of something (but don’t click).
#Hoverpoint : some function is there who sense the mouse operations with in the range. without any click or interpretation they can provide the result.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# ActionChains is a tool in Selenium that lets you control the mouse and keyboard in a browser.

import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#  to find the location of hover_element
hover_element = driver.find_element(By.ID,'mousehover')

action = ActionChains(driver)
# action handles the driver, move_to_element = this function is used to interaction with hover_element

time.sleep(3)
action.move_to_element(hover_element).perform()


# to click on top
driver.find_element(By.XPATH,'//a[text()="Top"]')
# here we have to write the Xpath

time.sleep(2)
driver.close()
