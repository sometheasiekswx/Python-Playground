from selenium.webdriver.common.by import By
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.deakin.edu.au/")

key_dates_button = driver.find_element(
    By.XPATH, '//*[@id="main-content"]/div[2]/div/div/div/span[2]'
)
key_dates_button_css = driver.find_element(
    By.CSS_SELECTOR,
    '#main-content > div:nth-child(2) > div > div > div > span:nth-child(2)'
)
key_dates = key_dates_button.find_element(
    By.TAG_NAME, "a"
)
key_dates_css = key_dates_button_css.find_element(
    By.CSS_SELECTOR,
    'a'
)
print(key_dates.get_attribute("text").strip())
print(key_dates.get_attribute("href"))
print(key_dates_css.get_attribute("text").strip())
print(key_dates_css.get_attribute("href"))

print()

buttons = driver.find_elements(
    By.XPATH, '//*[@id="main-content"]/div[2]/div/div/div/span'
)
buttons_css = driver.find_elements(
    By.CSS_SELECTOR,
    '#main-content > div:nth-child(2) > div > div > div > span'
)
for button in buttons:
    key_dates = button.find_element(
        By.TAG_NAME, "a"
    )
    print(
        str(key_dates.get_attribute("text").strip()),
        type(str(key_dates.get_attribute("textContent").strip()))
    )
    print(key_dates.get_attribute("href"))
for button_css in buttons_css:
    key_dates = button_css.find_element(
        By.TAG_NAME, "a"
    )
    print(
        str(key_dates.get_attribute("text").strip()),
        type(str(key_dates.get_attribute("textContent").strip()))
    )
    print(key_dates.get_attribute("href"))

search_bar = driver.find_element_by_name("query")
print(search_bar.get_attribute("placeholder"))

print(
    driver.find_element_by_css_selector(
        "div.module__banner-title > h1"
    ).get_attribute("textContent")
)

print(
    driver.find_element(
        By.CSS_SELECTOR,
        "div.module__banner-title > h1"
    ).get_attribute("textContent")
)

print(
    driver.find_element_by_xpath(
        '//*[@id="main-content"]/div[1]/div[2]/div/div/div[1]/h1'
    ).get_attribute("textContent")
)

print(
    driver.find_element(
        By.XPATH,
        '//*[@id="main-content"]/div[1]/div[2]/div/div/div[1]/h1'
    ).get_attribute("textContent")
)

time.sleep(2)

driver.quit()
