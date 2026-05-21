''''#webdriver (This is a module from the Selenium library that provides all the browser drivers (like Chrome, Firefox, Edge, etc.)
#browser --- search engine(chrome, Firefox, safari, edge, chromium)

from selenium import webdriver
from selenium.webdriver.common.by import By # to find the element  importing here the By class
import time

driver = webdriver.Chrome()   # This is a class that launches a new Google Chrome browser window.
 #Driver =  This is the object that represents the Chrome browser session. You use it to control the browser (e.g., open a website, click a button, fill a form).

#get method-- hit the url
driver.get('https://www.facebook.com/')  # Here i call the webdriver, an d than in webdriver i called search engine , and than search engine get the url


 #locator is present in By class, so by using By. ID or By. NAME we find the elements.

email = driver.find_element(By.ID,value='email')   #ID is the unique value , here email is the value of id
email.send_keys('abhilash@gmail.com')   # send_keys is used to send the text in text box.

password = driver.find_element(By.ID,value='pass')
password.send_keys('abcd@12')

submit = driver.find_element(By.NAME,value='login')
submit.click()

time.sleep(5)  #it takes time in milliseconds


driver.quit()  # it is used to close the driver



# locater :  It locates the elements , It is used to identify . There are 8 locaters in selenium.
# 1. id
# 2. name
# 3. class name
# 4. tag name
# 5. css selector
# 6. xpath
# 7. link text
# 8. partial link text'''


# Sign in

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/r.php?locale=en_GB')

first_name = driver.find_element(By.NAME, value='firstname')
first_name.send_keys('Swagatika')

sur_name = driver.find_element(By.NAME, value='lastname')
sur_name.send_keys('Pradhan')

male = driver.find_element(By.XPATH, value='//div/span/span[2]/label/input').click()
#finding the location of male using Absolute XPath


time.sleep(3)



driver.quit()












