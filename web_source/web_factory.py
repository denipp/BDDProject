from selenium import webdriver
from web_source.PublicCatalog import PublicCatalog


def get_web(browser):
    if browser == "chrome":
        return PublicCatalog(webdriver.Chrome())