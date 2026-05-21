from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# used to click on the openwindow
driver.find_element(By.ID,'openwindow').click()
# how to know which is the window (fetching the main window)
main_window = driver.current_window_handle
# to know how many windows are there
all_windows = driver.window_handles
# print(all_windows)    here we have 2 windows and it return the 2 windows in a list[]


# here looping is used to switch to the window you want
for i in all_windows:
    if i != main_window:
        # driver.switch_to.window(i)    it will open all window
        break
# to find the browser title
print(driver.title)
time.sleep(2)
driver.close()

driver.switch_to.window(main_window)
print(driver.title)
driver.quit()


