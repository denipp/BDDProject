from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Web(object):

    def __init__(self, driver):
        super(Web, self).__init__()
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
    def do_click(self,by_locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator)).click()
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator)).send_keys(text)
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return element.text
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool (element)
    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_is(title))
        return self.driver.title
    def switch_iframe(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it(by_locator))
    def switch_default_content(self):
        self.driver.switch_to.default_content()
    def dropdown(self, by_locator, value):
        dropdown = Select(WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(by_locator)))
        dropdown.select_by_value(value)





