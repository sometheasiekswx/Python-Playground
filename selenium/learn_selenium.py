from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://www.python.org")
print("Before: ", driver.title)
assert "Python" in driver.title
print("After: ", driver.title)
elem = driver.find_element_by_name("q")
print("elem: ", elem)
elem.clear()
# elem.send_keys("pycon")
elem.send_keys("SWX Somethea Siek :D")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

time.sleep(2)
driver.close()
