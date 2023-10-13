import time
from selenium import webdriver

driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demowebshop.tricentis.com/")
# maximizing the window
driver.maximize_window()
time.sleep(2)
# driver.minimize_window()
# time.sleep(2)
# driver.fullscreen_window()

time.sleep(2)
# print(driver.get_window_size())   # {'width': 1366, 'height': 768}
# print(driver.get_window_position())  # {'x': -8, 'y': -8}
# print(driver.get_window_rect())

# driver.set_window_size(300, 200)
# driver.set_window_position(200, 300)
# driver.set_window_rect(100, 200, 300, 400)

# navigating in browser
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
# time.sleep(2)
# driver.close()  # close the current window

time.sleep(2)
driver.quit()   # close all the window