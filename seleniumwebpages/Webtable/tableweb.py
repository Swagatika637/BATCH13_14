from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
# os is the python module, It is used to give the absolute path

driver = webdriver.Chrome()

file_path = os.path.abspath('table.html')

driver.get(file_path)

expected_res = 5
# '''This is in the python module, the developer has gave this'''
thead = driver.find_elements(By.XPATH,'//thead/tr/th')

marks_index = 1
for i in thead:
    if i.text == 'Marks':
        break
    marks_index = marks_index+1
# print(marks_index)

marks = driver.find_elements(By.XPATH,f"//tbody/tr/td[{marks_index}]")

total_sum = 0
for mark in marks:
    total_sum = total_sum + int(mark.text)

print(total_sum)
count_of_candidates = driver.find_elements(By.XPATH,'//tbody/tr/td[1]')

actual_res = len(count_of_candidates)

# assertion#
assert expected_res == actual_res,'failed due to count mismach'
#
# verification
if expected_res == actual_res:
    print('Pass')
time.sleep(4)
driver.close()

'''
INT Q. The diff btw verification and assertion?
assertion : it using the "assert" keyword to compare between the expected result and actual result. If the expecte_res == actual_res than assertion keep moving, If they are not equal it will failed the condition and  rise the assertion error and it will not going for the next line.
verification : It is also used to check the compariosion between expectd result and actual result . Here the codition doesn't matter . whatever the conditionis , it will move forward. 
'''


#  creat a ecom webtable with more than 1000 rows where the datas will be 'Name, Address, Product_name, date, price, month'
# Total row count of the table?
#  check how many product by a individual customer and price, product_name :- provide customer name?
# check the sell between 1st 15 days and last 15 days, compare growth and loss?
#provide a individual date, than give the total product, product sell and product owner name?