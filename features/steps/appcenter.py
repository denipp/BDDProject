import time
import datetime

import allure
from behave import *
from selenium.webdriver.common.by import By
from web_source.PublicCatalog import PublicCatalog

class Appcenter(PublicCatalog):
    @given(u'Open App Center homepage')
    def step_impl(context):
        context.web.open_public_catalog()
    @when(u'User in homepage')
    def OpenWeb(context):
        context.web.check_homepage()
    @then(u'verify have add-ons in homepage')
    def VerifyHomepage(context):
        time.sleep(2)
        try:
            context.web.check_add_ons_homepage()
        except:
            context.web.screenshot()
            assert False

    @when(u'in App Center homepage click contact us')
    def step_impl(context):
        try:
            time.sleep(2)
            context.web.click_contact_us()
        except:
            context.web.screenshot()
            assert False

    @then(u'verify if user in contact us page')
    def step_impl(context):
        try:
            time.sleep(5)
            context.web.check_contact_us()

        except:
            context.web.screenshot()
            assert False
