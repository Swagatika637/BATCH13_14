from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #  i want to open chrome thats why webdriver.Chrome() is used.

driver.get('https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DApple')


tags = driver.find_element(By.TAG_NAME,value='a')  #this line is for finding the anchor tag <a>tag #find_element is used when a specific element is needed
print(tags) # it returns some elements, the anchor tag is used for all links on the page

tags = driver.find_elements(By.TAG_NAME,value='a') # find_elements is used when all elements were needed.
print(tags) #It returns elements in a list[]

print(len(tags)) #It will return the lengh of tags  INT Q. Give me the hyper link list in the page  you are working with  / how many times the API will hit?


for i in tags:     # It is used to count the tags in a webpage
    print(i.text)    #i= selenium element, .text is used to return value in english



#driver.quit() #to close the window , here that is the chrome. (using when multiple window is there)
driver.close() # close the current window



'''Difference between find_element and find elements ?'''

# web browser is the search engine , webpage :  what works inside the search engine


