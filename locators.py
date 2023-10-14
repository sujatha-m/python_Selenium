import time

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

# name, id, class name, css selector, xpath, tag name, link text, partial link text

# # using classname
# driver.find_element("class name", "ico-register").click()
#
# # using id
# driver.find_element("id", "small-searchterms").send_keys("Notebooks")
# time.sleep(2)

# # using name(locator name, locator Value)
# driver.find_element("name", "q").send_keys("mobile")
# time.sleep(2)

# # link text
# driver.find_element("link text", "Register").click()
# time.sleep(2)

# # partial link text
# driver.find_element("partial link text", "Reg").click()
# time.sleep(2)

# driver.find_element("id", "small-searchterms").send_keys("Notebooks")
# driver.find_element("name","q").clear()
# time.sleep(2)

# driver.find_element("css selector",'a[class="ico-register"]').click()
# time.sleep(2)

driver.find_element("css selector",'input[id="newsletter-email"]').send_keys("abc@gmail.com")
time.sleep(2)

driver.find_element("css selector", 'input[type="text"]').send_keys("hello")

driver.close()