from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

# ----- 1 -----

# driver.get("https://www.w3schools.com/html/html_forms.asp")
# form = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/form')
# form_inputs = form.find_elements_by_tag_name("input")
# for form_input in form_inputs:
#     print("Input Text %s (%s)" % (
#         form_input.get_attribute("name"),
#         type(form_input.get_attribute("name"))
#     ))

# for form_input in form_inputs:
#     try:
#         form_input.clear()
#         form_input.send_keys("HEYYYYY BROTHERRRR!!!")
#     except:
#         pass
#         # form_input.click()

# ----- 2 -----

# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
# # driver.switch_to.frame("iframeResult")
# driver.switch_to_frame("iframeResult")

# --- 2.1 ---

# select = driver.find_element_by_id("cars")
# all_options = select.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()
#     time.sleep(0.2)

# --- 2.2 ---

# select = Select(driver.find_element_by_id("cars"))
# options = select.options
# for option in options:
#     option.click()
#     print("Value: {0} | Text {1}".format(
#         option.get_attribute("value"),
#         option.get_attribute("text")
#     ))
# select.select_by_index(1)
# time.sleep(0.2)
# select.select_by_visible_text("Saab")
# time.sleep(0.2)
# select.select_by_value("audi")
# time.sleep(0.2)
# select.select_by_index(0)
# time.sleep(0.2)

# ----- 3 -----

# driver.get("https://www.w3schools.com/tags/tag_select.asp")
# for i in range(5):
#     driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
# for handle in driver.window_handles:
#     driver.switch_to_window(handle)
#     time.sleep(0.2)

# ----- 4 -----

# driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
# driver.switch_to_frame("iframeResult")
# driver.find_element_by_xpath("/html/body/button").click()
# alert = driver.switch_to_alert()
# print(alert.text)
# alert.accept()

driver.get("https://www.codesdope.com/cpp-oop/")
for i in range(3):
    next = driver.find_element_by_link_text("Next")
    next_link = next.get_attribute("href")
    driver.get(next_link)
driver.back()
time.sleep(0.2)
driver.back()
time.sleep(0.2)
driver.forward()
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
    print()

time.sleep(2.5)
driver.quit()
