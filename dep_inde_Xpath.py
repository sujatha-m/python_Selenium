# dep-ind elements xpath

"""
1. Identify the dependent and independent element
2. write the xpath exp for independent element
3. traverse back until common parent of both dep and independent element is obtained(/..)
4. write the xpath exp for dependent element
"""

import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= opts)
driver.get("C:\\Users\sujat\PycharmProjects\python_Selenium\HTMLfiles\demo.html")
driver.maximize_window()

# driver.find_element("xpath", '//td[text()="Java"]/..//input[@type="checkbox"]').click()
# time.sleep(2)
# driver.find_element("xpath",'//td[text()="JavaScript"]/..//input[@type="checkbox"]').click()
# time.sleep(2)

languages = ["Java", "Ruby", "Perl", "Python", "C#", "JavaScript"]
# for language in languages:
#     driver.find_element("xpath", f'//td[text()="{language}"]/..//input[@type="checkbox"]').click()
#     time.sleep(2)

#checking by reverse order
for language in languages[::-1]:
    driver.find_element("xpath",f'//td[text() ="{language}"]/..//input[@type="checkbox"]').click()
    time.sleep(2)

# driver.get("https://www.python.org/downloads/")
# driver.maximize_window()
# driver.find_element("xpath", '//a[text( )="Python 3.9.8"]/../..//a[text( )="Release Notes"]').click()
# time.sleep(2)

driver.close()