from splinter import Browser
from selenium.webdriver.common.keys import Keys

executable_path = '/usr/local/bin/chromedriver'
browser = Browser('chrome', executable_path=executable_path, headless=False)

browser.visit('https://www.deakin.edu.au/')
search = browser.find_by_id('search-bar__input')
search.type('Hello World')
search.type(Keys.RETURN)


interest_area = browser.find_by_css(
    'div.module__interest-area-home-courses > ul > li'
)

for interest_area_li in interest_area:
    interest_area_a = interest_area_li.find_by_tag('a')
    print(interest_area_a.first['textContent'])
    print(interest_area_a.first['href'])

print('===================================')

links_found = browser.links.find_by_partial_href('/courses/find-a-course')
for link in links_found:
    print(link.text)
    print(link['textContent'])
    print(link['href'])
    print('-------')

browser.quit()
