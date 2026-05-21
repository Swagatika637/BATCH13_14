# check how many product by a individual customer and price, product_name :- provide customer name?
# check the sell between 1st 15 days and last 15 days, compare growth and loss?
#provide a individual date, than give the total product, product sell and product owner name?


from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import json
# importing the json to read the data because it is store in the outside
driver = webdriver.Chrome()

file_path = os.path.abspath('ecom.html')

driver.get(file_path)

# json file handle in test data activities
with open('test_data.json','r') as file:
    data = file.read()
    expected_result = json.loads(data)
# To covert data from string to python data json.loads() has been used.
print(expected_result['row_count'])

# Q1. Total row count //
actual_total_rows = driver.find_elements(By.XPATH,'//tbody/tr')
assert expected_result['row_count'] == len(actual_total_rows)

 # Q2. check how many product buy a individual customer and price, product_name :- provide customer name?
name = 'Daya'
products = driver.find_elements(By.XPATH,f"//tr/td[text()='{name}']/following-sibling::td[2]")
print(len(products))
products_name = [i.text for i in products]
# '''list comprehension'''
print(products_name)
print(products)

# price
price = driver.find_elements(By.XPATH,f"//tr/td[text()='{name}']/following-sibling::td[4]")
all_price_list = [eval(i.text) for i in price]
# '''Here eval is used to convert as the data type need , means if it is in float/octal it will convert accordingly'''
print(sum(all_price_list))

# Q3.check the sell between 1st 15 days and last 15 days, compare growth and loss?

dates = driver.find_elements(By.XPATH,"//tr/td[4]")
for i in dates:
    dd = i.text[-2::]
#dd is for date
    print(dd)



time.sleep(3)
driver.close()


