from splinter import Browser
from time import sleep


def fast_fill_by_javascript(browser, elem_class, text):
    """Fill text field with copy-paste, not by typing key by key.

    Otherwise you cannot type enter or tab.

    :param id: CSS id of the textarea element to fill
    """
    text = text.replace("\t", "\\t")
    text = text.replace("\n", "\\n")

    # Construct a JavaScript snippet that is executed on the browser sdie
    snippet = 'document.querySelector(".{0}").textContent = "{1}";'.format(
        elem_class, text)
    browser.execute_script(snippet)


browser = Browser()

browser.visit('https://www.deakin.edu.au/')
browser.execute_script("$('body').empty()")
print(browser.evaluate_script("4+4") == 8)

browser.visit(
    'https://www.deakin.edu.au/course/bachelor-artificial-intelligence')
title = browser.find_by_css('.module__banner-title > h1')

print("title['is_empty']:", title['is_empty'])
print("title.is_empty:", title.is_empty)
print("title['text']:", title['text'])
print("title.text:", title.text)
print("title['value']:", title['value'])
print("title.value:", title.value)

fast_fill_by_javascript(
    browser, 'course__section-heading', 'YAY!!!!!!!!!')
sleep(5)

browser.quit()
