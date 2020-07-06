from selenium import webdriver
from splinter import Browser

browser = Browser()
browser.visit(
    'https://splinter.readthedocs.io/en/latest/http-status-code-and-exception.html#')
print('Splinter:', browser, '|', 'Type:', type(browser))

browser.quit()

browser = webdriver.Firefox()
browser.get(
    "https://splinter.readthedocs.io/en/latest/http-status-code-and-exception.html#")
print('Splinter:', browser, '|', 'Type:', type(browser))

# print(browser.status_code.is_success())  # True
# print(browser.status_code == 200)  # True
# print(browser.status_code.code)  # 200

# try:
#     browser.visit('http://cobrateam.info/i-want-cookies')
# except HttpResponseError, e:
#     print "Oops, I failed with the status code %s and reason %s" % (
#         e.status_code, e.reason)

browser.quit()
