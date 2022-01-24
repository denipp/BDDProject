from selenium import webdriver
from web_source.web import Web



def browser_chrome(context, timeout=30):
    browser = webdriver.Chrome()
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()