import time
import datetime
from selenium.webdriver.common.by import By
from web_source.web import Web
from selenium.webdriver.common.keys import Keys
import allure

class PublicCatalog(Web):

    WEB = "https://apps.qiscus.com/en/"
    TITLE_PUBLIC = (By.XPATH, '//h1[contains(text(),"Qiscus Apps")]')
    ADD_ONS = (By.CLASS_NAME, 'card-app-desc')
    CONTACT_US = (By.XPATH, '//a[contains(text(),"Contact Us")]')
    TITLE_CONTACT_US = (By.XPATH, '//h2[contains(text(),"Contact Sales")]')



    def __init__(self, driver):
        super(Web, self).__init__()
        self.driver = driver

    def open_public_catalog(self):
        self.open(self.WEB)
    def check_homepage(self):
        self.is_visible(self.TITLE_PUBLIC)
    def check_add_ons_homepage(self):
        self.is_visible(self.ADD_ONS)
    def click_contact_us(self):
        self.do_click(self.CONTACT_US)
    def check_contact_us(self):
        actual = self.get_element_text(self.TITLE_CONTACT_US)
        assert 'Sales' in actual

    def screenshot(self):
        now = str(datetime.datetime.now())
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Fail - " + now, attachment_type=allure.attachment_type.PNG
        )

