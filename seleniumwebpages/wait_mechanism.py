# Wait mechanism in Selenium is a way to make your script pause until a certain condition is met — like waiting for a web page or element to load — before continuing.
# There are three main types:
# Implicit Wait – wait a fixed amount of time for all elements.
# Explicit Wait – wait for a specific condition (like element visible or clickable).
# Fluent Wait – like explicit wait but with custom check intervals and ignored exceptions.
# Implecit wait is a common /global /universal mechanism . It waits a particular amount of time for every element. Implicit wait sets a default waiting time for the WebDriver to look for elements before throwing an exception.
# It applies globally to all element searches.
# Explicit wait : It is a conditional wait. Waits for a specific condition to be true before proceeding.
# Greenkart site :for practice wait mechanism (https://rahulshettyacademy.com/seleniumPractise/#/)

from selenium import webdriver
from selenium.webdriver.common.by import By
# for calling the explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# EC is the short form of expected_conditions
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
# It will wait for each element


driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

search_field = driver.find_element(By.XPATH,"//input[@type='search']")
search_field.send_keys('er')

# time.sleep(2)   If your web element is not after using the wait mechanism than here we have used this time.sleep
result = driver.find_elements(By.XPATH,"//div[@class='product']/div//button")
for i in result:
    i.click()
    # Here an error arises named as StaleElementReferenceException,

# clicking on the cart and than the proceed to checkout
cart_img_click = driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
check_out = driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# To enter some text on promo code after clicking on the proceed to checkout
text = driver.find_element(By.XPATH,"//input[@class='promoCode']")
text.send_keys('Abhi')
# to click on apply
apply = driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

# After applying in putting the wrong promocode it shows 'Invalid code' to fetch that code
# code = driver.find_element(By.XPATH,"//span[@class='promoInfo']")
# print(code.text)

# to wait webdriver we provide the driver for 15sec
wait = WebDriverWait(driver,15)
wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
# visibility_of_element_located : wait until the element is visible
# presence_of_element_located() : wait until the element is present
# wait.until : it means it will wait till the condition is satisfied , until is used to give the condition

time.sleep(3)
driver.close()