import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\demo.html")
driver.maximize_window()

elements =driver.find_element("id", "multiple_cars")
select_obj = Select(elements)

#select obj is preference is based on priority 1.by value,2.by visible text, 3. index
select_obj.select_by_index(3)
time.sleep(2)
select_obj.select_by_visible_text("BMW")
time.sleep(2)
select_obj.select_by_value("aud")
time.sleep(2)

# print(select_obj.first_selected_option.text)

# print(select_obj.is_multiple)
# #deselecting all options
# select_obj.deselect_all()
# time.sleep(2)

# #getting the text of all the options
# all_options = select_obj.options
# for option in all_options:
#     print(option.text)

# #printing first selected option
# print(select_obj.first_selected_option.text)

#getting all the selected options
selected_options = select_obj.all_selected_options
for option in selected_options:
    print(option.text)


driver.close()