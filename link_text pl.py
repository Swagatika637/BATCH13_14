from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

#to interact with hyper link
# driver.find_element(By.ID,value='u_0_6_IZ').click()  #It will give NosuchElement Error because we can't click any hyperlink through ID.


#for that we use partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,value='Forgotten password').click()
 
time.sleep(5)
driver.close()


#LINK_TEXT : It is used when all the details were given . It takes the text only but the exact text . If there will be some mistake in the text it will return an error . for example: Instead of 'forget password' if you give 'forget' or 'forget passwor' it will retuen an error.
#PARTIAL_LINK_TEXT :It is used when complete information is not there. It also takes the text. It will work even  if the matching value is given  For example: Instead of 'forget password' just give 'password' it will work.

# Both are used for the <a> tag, The hyper link.