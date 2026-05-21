from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/droppable/')
driver.maximize_window()

time.sleep(2)

# Drag and Drop
# Int Q. IN real time scenario where you did the Drag up and Drag down.
# Ans : When we play a video.

# here we have to go to the frame because this is reside in the iframe body.
# Switch to the iframe that contains the draggable & droppable elements
iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(iframe)

wait = WebDriverWait(driver,15)

# Locate draggable and droppable elements
source = wait.until(EC.presence_of_element_located((By.ID,'draggable')))
target = wait.until(EC.presence_of_element_located((By.ID,'droppable')))

# Perform drag and drop
action = ActionChains(driver)
action.drag_and_drop(source,target).perform()

time.sleep(3)
driver.quit()
#In js there is no point to locate directly, so here axis is used. It will provide in the text file from the client side. developer provide the access in json file
# Here we have two points x, y . X = where to drag, y = where to drop. so do inspect on drag


# Select the next date june 15
# interact with keyboard help of selenium [cnt v, cnt c etc]