# Select
"""
All the list box methods are implemented using select class
import select class, pass the web element (list box) as a argument
3 different methods
1. select_item_by_visible_text
2. select_item_by_index
3. select_by_value

"""

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\demo.html")
driver.maximize_window()

elements = driver.find_element("id", "standard_cars")
select_obj = Select(elements)

# Selecting the obj by index
# select_obj.select_by_index(2)
# time.sleep(2)
# select_obj.select_by_index(6)
# time.sleep(2)

# Selecting the obj by visible_text
# select_obj.select_by_visible_text("Honda")
# time.sleep(2)
# select_obj.select_by_visible_text("BMW")
# time.sleep(2)

#selecting the obj by value
# select_obj.select_by_value("for")
# time.sleep(2)
# select_obj.select_by_value("hda")
# time.sleep(2)

# is_multiple is a function, return boolean
# print(select_obj.is_multiple)

# # getting all the options
# all_options = select_obj.options
#
# # printing all the text from options web element
#
# for option in all_options:
#     print(option.text)

# # selecting all the options one by one using index
# all_options = select_obj.options     # options is a parameter
# for i in range(len(all_options)):   # range(0, 10)
#     select_obj.select_by_index(i)
#     print(all_options[i].text)
#     time.sleep(1)

# # selecting all the options one by one using visible_text
# all_options = select_obj.options # list of web elements of options
# options = [option.text for option in all_options]
# print(options)
# for text in options:
#     select_obj.select_by_visible_text(text)
#     time.sleep(2)

# selecting all the options one by one using value
all_options = select_obj.options

values = [option.get_attribute("value") for option in all_options]
print(values)

for value in values:
    select_obj.select_by_value(value)
    time.sleep(1)

driver.close()

#select by index
# select by visible text
#select by value