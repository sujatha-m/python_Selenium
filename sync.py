import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options)

driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\progress.html")
driver.maximize_window()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.implicitly_wait(30)
driver.find_element("xpath", '//button[text() = "Click Me"]').click()
driver.find_element("xpath", '//div[text()="100%"]')
print('Done!!!')

