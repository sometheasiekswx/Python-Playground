from splinter import Browser

executable_path = '/usr/local/bin/chromedriver'
browser = Browser('chrome', executable_path=executable_path, headless=False)

browser.visit('https://www.google.com/')
# browser = Browser(user_agent="Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)")
browser.visit('https://www.google.com/')
browser.fill('q', 'splinter - python acceptance testing for web applications')
browser.reload()
browser.fill('q', 'reddit')
print(browser.title)
print()
print(browser.html)
print()
# button = browser.find_by_name('btnK')
# button.click()
browser.find_by_name('btnK').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print "Yes, found it! :)"
else:
    print "No, didn't find it :("

if browser.is_element_present_by_css('#xjs > div > h1', 10):
    print "Yes, found it! :)"
else:
    print "No, didn't find it :("

browser.visit('http://cobrateam.info')
browser.visit('https://splinter.readthedocs.io')
print()
print(browser.html)
print()
browser.back()
print(browser.url)
browser.forward()
print(browser.url)

browser.quit()
