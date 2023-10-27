"""
alert : small msg box which gives some kind of information for the user
1. simple alert : ok
2. confirm : ok / cancel
3. prompt ok / cancel / enter

we cannot inspect pop up

"""

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts= webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# driver.get("https://nxtgenaiacademy.com/alertandpopup")
# driver.maximize_window()

# # simple alert
# driver.find_element("xpath", '//button[@name="alertbox"]').click()
# alert_obj = driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.accept()
# time.sleep(2)

# # confirm
# driver.find_element("xpath", '//button[@name="confirmalertbox"]').click()
# alert_obj = driver.switch_to.alert
# # alert_obj.accept()
# # time.sleep(3)
# alert_obj.dismiss()
# time.sleep(3)

# #locating the element responsible for triggering the prompt
# driver.find_element("xpath", '//button[@name = "promptalertbox1234"]').click()
# alert_obj = driver.switch_to.alert
# # alert_obj.send_keys("yes")
# alert_obj.send_keys("No")
# alert_obj.accept()
# time.sleep(2)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

driver.find_element("xpath", '//input[@type="submit"]').click()
# driver.find_element("xpath",'//input[@class ="button-1 search-box-button"]').click()
time.sleep(2)
alert_obj = driver.switch_to.alert

print(alert_obj.text)
alert_obj.accept()
time.sleep(2)
driver.close()



