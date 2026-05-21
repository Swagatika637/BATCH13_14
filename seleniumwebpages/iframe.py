# iframe = frame inside a frame
# here in the practice page , except the white page everything there present is javascript
# when javascript execute in javascript_executer ,than the  javascript_executer will run an aapplication in the browser.
# iframe must have 2 things i.e 'id' and 'name'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#for seeing thw window in full size
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')


# switch to frame
driver.switch_to.frame('courses-iframe')

time.sleep(3)
click_course = driver.find_element(By.LINK_TEXT,'Courses')
# courses is the <a> tag thats why here link_text is used
click_course.click()

time.sleep(3)

# in iframe how to return to the main frame (switch to main frame)
driver.switch_to.default_content()

driver.close()


# INT Q. returning to main window in;
# tab : tab[0] here using indexing we return to the main window
# window : save the current window iin main window as main_window = driver.current_window_handle
# iframe : default_content()
