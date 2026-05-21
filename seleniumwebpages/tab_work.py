# Switch to window or switch to TAB
# Tab : creating a new page in the same bookmark, Window : creating an another bookmark in the same browser.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

time.sleep(2)
# open a new tab using is executer
driver.execute_script("window.open('')")

tabs = driver.window_handles
# window_handles is used to handle multiple tabs
driver.switch_to.window((tabs[1]))
# here it will switch to opened tab and here the index says which tab will switch.

driver.get('https://drive.google.com/drive/folders/1D1J8ZOAg3qf7gL0p37QQCT_H4D8dWmJQ')

time.sleep(3)
# return to main window
driver.switch_to.window(tabs[0])

print('back to main window')
time.sleep(3)

# driver.quit()   It is used to stop the window which is newly opened.

