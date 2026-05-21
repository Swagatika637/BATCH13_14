# How to scroll up and down
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/autocomplete/')
driver.maximize_window()

time.sleep(2)

# scrolldown using js
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')

# to use javascript which method of driver is used : execute_script
# go to the console_tab for executing on this url.

# taking screenshot from the point you are
# screenshot in selenium
driver.save_screenshot('screenshot1.png')

# taking ss by providing the path
driver.save_screenshot(r'C:\Users\HP\OneDrive\Desktop\screenshot1.png')
# to scroll window i write in the console tab :window.scrollTo(0,document.body.scrollHeight);


# [window : class][scrollTo : it is a function here used to scroll from start to end][0,document : x,y axis(these are the attribute/parameter )][body :to scroll the body of document ][scrollHeight : scroll till end(this is the object here till where we have to scroll )][';' :- in js every block should end with this.]
# scrollTo : it will scroll to which axis (x,y) you have provided.
# scrollUp : down to up, scrollby : up to down
# r' mode used because if any escape character is there it will remove that.

#In selenium if you don't provide the location , bydeafault it will save the screen shot file at where you are wrighting the program.
# why ss is neccessary : when there is an issue aries in ui testing , as a tester we have to give an evidence . That's why we take the ss to prove the issue in the automation script.
# when you take a screenshot of a picture , first it will create an empty file, and paste the ss there
# In python when we create an empty file it will reside in the bais
#screenshot file is always a png file.


time.sleep(3)
driver.close()

#jpg vs jpeg:  it depends on the picture resolution.

