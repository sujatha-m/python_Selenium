import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
path =r"C:\Users\sujat\OneDrive\Desktop\test"
opts.add_experimental_option("prefs", {"download.default_directory": path, "safebrowsing.enabled": True})

driver = webdriver.Chrome(options=opts)

driver.get("https://www.python.org/downloads/")
driver.maximize_window()

driver.find_element("xpath", '(//a[text()="Download Python 3.12.0"])[3]').click()
time.sleep(2)
driver.close()