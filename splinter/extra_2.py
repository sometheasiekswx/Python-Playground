from splinter import Browser
from time import sleep

browser = Browser(headless=True)
browser.visit(
    'https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default')

# browser.driver.save_screenshot('your_screenshot.png')

# screenshot = browser.screenshot(
#     '/Users/sometheasiek/Documents/PsychPress/Web Scraping/Splinter/your_screenshot_2', '.png')
# screenshot = browser.screenshot(
#     '/Users/sometheasiek/Documents/PsychPress/Web Scraping/Splinter/your_screenshot_3', '.png', full=True)
# browser.screenshot(
#     '/Users/sometheasiek/Documents/PsychPress/Web Scraping/Splinter/your_screenshot_4', '.png')

# html_snapshot = browser.html_snapshot(
#     '/Users/sometheasiek/Documents/PsychPress/Web Scraping/Splinter/your_screenshot.html')

# with browser.get_iframe('iframeResult') as iframe:
#     print(iframe.find_by_css('body > h1').text)
#     screenshot = iframe.find_by_css('body > h1').screenshot(
#         '/Users/sometheasiek/Documents/PsychPress/Web Scraping/Splinter/find_xpath_screenshot.png')
#     screenshot_path = iframe.find_by_css('body > h1').screenshot(
#         '/Users/sometheasiek/Documents/PsychPress/Web Scraping/Splinter/find_xpath_screenshot_2.png', full=True)

# browser.execute_script("alert(69);")

# alert = browser.get_alert()
# print(alert.text)
# alert.accept()


# browser.execute_script("alert(666); alert(42); alert(420);")

# with browser.get_alert() as alert:
#     print(alert.text)
#     alert.accept()

browser.quit()
