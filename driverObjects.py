from selenium import webdriver
driver = webdriver.Chrome()

# if session is closed automatically , then use this snippet

opx = webdriver.ChromeOptions()
opx.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")

