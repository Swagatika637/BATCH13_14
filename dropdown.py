# There are two types of drop down (Selective, Auto suggestive)
'''
1. Selective dropdown : Where value is fixed, Tag name of a selective dropdown is 'Select'. It is static where options are fixed or options are available.
2. Auto-suggestive dropdown : It is dynamic, The options are not available .
'''


'''SELECTIVE DROPDOWN'''
#A check is made that the given element is, indeed, a SELECT tag. If it is not, then an UnexpectedTagNameException is thrown.
#INT.Q : If your select class is not interacring than what kid of error arises : UnexpectedTagNameException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
#
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
#
# driver = webdriver.Chrome()
# driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#
# # Select interacts with the 'options'
# select_locater = Select(driver.find_element(By.ID,value='dropdown-class-example'))
# There are 3 methods interacting with options; If the element is not selected than it is done by these three methods.
# select_locater.select_by_index(3)
# select_locater.select_by_value('option2')
# select_locater.select_by_visible_text('option1')
# select_locater.all_selected_options() : it is given for multiple choice, select the all otions and it depends on web page to web page
#
# select_locater.deselect_by_index(1)
# It works where multiple selectors are there.
# otherwise it shows 'NotImplementedError' shows , this error means The function you have implemented on a procedure which is not acceptable.

time.sleep(3)

driver.close()

'DOM : It is the representation of a web page. This the direct of some messages.'

select_by_index
select_by_value
select_by_visisble_text

'''AUTO SILECTIVE DROP DOWN'''
# It is a input box. After providing some text it will auto suggest some values and so that first we interact with the input-box and sends some values, whatever the value it will be show than we are interacting with the ul_tag - means the line tag


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

input_box = driver.find_element(By.ID,"autocomplete")
input_box.send_keys('ind')


# Xpath ://ul[@id='ui-id-1']/li :The Xpath is written here to find the li from the ul_tag.
values = driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li")
ul_tag = driver.find_element(By.XPATH,"//ul[@id='ui-id-1']")
values = ul_tag.find_elements(By.XPATH,"li")

for value in values:
    if value.text == 'India':
        value.click()


print(values)

time.sleep(3)
driver.close()


'''
Int. question : How the both dropdown works?
Both are the dropdown , selective dropdown is static where as The autosuggestive dropdown is dynamic
In selective dropdown the selenium provides  the select class where we interact the particular element , after the interaction the select class providing the methods i.e  #select_by_index
# select_by_value
# select_by_visisble_text , Based on these we select the static values

In autosuggestive dropdown has a input box , After providing text it will auto suggest  some values . So that first we interact with the input box and send some values , Whatever value it show than we are interacting with the ul_tag means whatever the line_tag is there . Within that we got the li_tag.
so that here, we are using the driver.findelement() to gather all the values  whatever the autosuggestive dropdown is showing than in the form of pythn for loop we interact with each element and check value.text() , we can convert the selenium object to python object . If it is matching than we will click(),    
'''