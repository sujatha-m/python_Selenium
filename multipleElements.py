
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=options)

driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\demo.html")
driver.maximize_window()

# elements = driver.find_elements("xpath",'//div[@class= "block block-category-navigation"]//a')
# print(elements)
#
# for element in elements:
#     print(element.text)
# time.sleep(2)

# listofFooterElements = driver.find_elements("xpath", '//div[@class ="footer-menu-wrapper"]//a')
#
# for element in listofFooterElements:
#     print(element.text)
# time.sleep(2)

#using xpath
# links = driver.find_elements("xpath","//a")
# print(len(links))
#
# #using tagname
# links = driver.find_elements("tag name","a")
# for link in links:
#     print(link.text)
#     print(link.get_property("href"))#gets all links
    # time.sleep(1)
# print(len(links))

# zip(*iterator)
# zip() used to combine two or more iterables into single iterable
words = ["hello", "hi", "welcome", "selenium", "python", "program", "how", "are", "you"]
text_boxes = driver.find_elements("name", "fname")
for text_boxes, word in zip(text_boxes, words):
    text_boxes.send_keys(word)
    time.sleep(2)

driver.close()