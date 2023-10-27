"""
# ctrl+shift+i
to automate low level interaction like mouse movements, mouse buttons, press keys

import actionchains class
create an object for Actionchain class
"""

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts= webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# driver.get("https://www.myntra.com/")
# driver.maximize_window()

act_obj = ActionChains(driver)
# link = driver.find_element("xpath", '//div[@class ="desktop-navLink"]//a[text() ="Men"]')
# act_obj.move_to_element(link).perform()
# time.sleep(2)

# profilelink
# profile = driver.find_element("xpath", '//span[text()="Profile"]')
# act_obj.move_to_element(profile).perform()
# time.sleep(2)
# ***********************************************************************************************************

# # double click and page down
# from selenium.webdriver.common.keys import Keys
# driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\demo.html")
# driver.maximize_window()
#
# button = driver.find_element("id", "double-click")
# act_obj.double_click(button).perform()
# act_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)

# ***********************************************************************************************************

# # drag and drop
# driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
# driver.maximize_window()
# drag =driver.find_element("xpath", '//div[@id="draggable"]')
# drop = driver.find_element("xpath",'//div[@id="droppable"]')
# act_obj.drag_and_drop(drag,drop).perform()
# time.sleep(4)
# ***********************************************************************************************************

# file upload
driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\demo.html")
driver.maximize_window()
path =r"C:\Users\sujat\OneDrive\Desktop\test"
driver.find_element("xpath", '//input[@type="file"]').send_keys(path)
time.sleep(10)

driver.close()