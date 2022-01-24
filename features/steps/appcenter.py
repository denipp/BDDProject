import time
import datetime

import allure
from behave import *
from selenium.webdriver.common.by import By

class Appcenter:
    @given(u'Open App Center homepage')
    def step_impl(context):
        context.web.open("https://apps.qiscus.com/en/")
    @when(u'User in homepage')
    def OpenWeb(context):
        context.web.is_visible((By.XPATH, '//h1[contains(text(),"Qiscus Apps")]'))
    @then(u'verify have add-ons in homepage')
    def VerifyHomepage(context):
        time.sleep(2)
        try:
            context.web.is_visible((By.CLASS_NAME, 'card-app-desc'))
        except:
            now = str(datetime.datetime.now())
            allure.attach(
            context.web.get_screenshot_as_png(),
            name="Fail - "+now, attachment_type=allure.attachment_type.PNG
            )
            assert False

    @when(u'in App Center homepage click contact us')
    def step_impl(context):
        try:
            time.sleep(2)
            context.web.do_click((By.XPATH, '//a[contains(text(),"Contact Us")]'))
        except:
            now = str(datetime.datetime.now())
            allure.attach(
                context.web.get_screenshot_as_png(),
                name="Fail - " + now, attachment_type=allure.attachment_type.PNG
            )
            assert False

    @then(u'verify if user in contact us page')
    def step_impl(context):
        try:
            time.sleep(5)
            context.web.is_visible((By.XPATH, '//h2[contains(text(),"Contact Sales")]'))

        except:
            now = str(datetime.datetime.now())
            allure.attach(
                context.web.get_screenshot_as_png(),
                name="Fail - " + now, attachment_type=allure.attachment_type.PNG
            )
            assert False
