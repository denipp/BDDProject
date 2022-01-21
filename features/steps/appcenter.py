import time
import datetime

import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Appcenter:
    @given(u'Launch Chrome Browser')
    def step_impl(context):
        context.driver = webdriver.Chrome()
    @then(u'Open App Center homepage')
    def OpenWeb(context):
        context.driver.get("https://apps.qiscus.com/en/")

    @then(u'verify have add-ons in homepage')
    def VerifyHomepage(context):
        time.sleep(2)
        try:
            WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-app-desc')))
        except:
            now = str(datetime.datetime.now())
            allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Fail - "+now, attachment_type=allure.attachment_type.PNG
            )
            assert False

    @when(u'in App Center homepage click contact us')
    def step_impl(context):
        try:
            WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Contact Us")]'))).click()
        except:
            now = str(datetime.datetime.now())
            allure.attach(context.driver.get_screenshot_as_png(),name="Fail - " + now, attachment_type=allure.attachment_type.PNG)
            assert False

    @then(u'verify if user in contact us page')
    def step_impl(context):

        try:
            WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Contact Sales")]'))).click()
        except:
            now = str(datetime.datetime.now())
            allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Fail - " + now, attachment_type=allure.attachment_type.PNG
            )
            assert False
