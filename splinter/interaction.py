from splinter import Browser
from time import sleep

executable_path = '/usr/local/bin/chromedriver'
driver = Browser(driver_name='chrome',
                 executable_path=executable_path, headless=False)

driver.visit(
    'https://splinter.readthedocs.io/en/latest/elements-in-the-page.html')
value = driver.find_by_tag('h1').value
print(value)
text = driver.find_by_tag('h1').text
print(text)
textContent = driver.find_by_tag('h1')['textContent']
print(textContent)

# driver.links.find_by_partial_text("Edit on GitHub").click()
driver.visit('https://handbook.monash.edu/current/units/MTH1010')

expand_all_script = "[].forEach.call(document.querySelectorAll('a.css-8lk6ln-SExpandAllButton.e1450wuy11'), function(expand) {expand.click();});"
driver.execute_script(expand_all_script)

sleep(5)

driver.quit()
