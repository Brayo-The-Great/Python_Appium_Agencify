import unittest
from time import sleep
from typing import Any, Dict
from datetime import datetime
from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
import time
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    platformVersion='14.0',
    deviceName='emulator-5554',
    language='en',
    locale='US',
    autoGrantPermissions='true',
    app=r'/Users/brianwaititumuraya/Documents/TESTAPKs/2.12.18.0staging.apk'

)

print(capabilities)

appium_server_url = 'http://127.0.0.1:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_agencify_staging_app(self) -> None:

        self.login_screen()

    def login_screen(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Login"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Email"]').send_keys(
            "brian.muraya@agencify.insure")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Password"]').send_keys("12345678")
        el.click()

        el = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Login"]')))
        el.click()

        self.get_quote_screen()

    def get_quote_screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '(//android.widget.ImageView['
                       '@resource-id="insure.agencify.agencify:id/navigation_bar_item_icon_view'
                       '"])[4]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Motor Private"]')))
        el.click()

        self.cover_type_screen()

    def cover_type_screen(self):
        el = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="COMP"]')))
        el.click()

        self.create_quote_screen()

    def create_quote_screen(self):
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[1]').send_keys(
            "KQA 324S")
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[2]').send_keys(
            "3000000")
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.view.View[''1]/android.widget'
                                            '.EditText/android.widget.Button')
        el.click()
        self.driver.implicitly_wait(60)

        # current_date = datetime.now().strftime('%a, %d %b')  # Format like 'Wed, 28 Feb'
        # xpath = f'//android.widget.TextView[@content-desc="{current_date}"]'
        # el = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        # el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
        self.driver.implicitly_wait(30)

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Continue"]')
        el.click()

        self.complete_information_screen()

    def complete_information_screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Make"]'))).send_keys("BMW")

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.view.ViewGroup[@resource-id="insure.agencify.agencify:id/layoutInfo"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.AutoCompleteTextView[@resource-id="insure.agencify.agencify:id/model"]'))).send_keys(
            "X7")

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Body type"]'))).send_keys("STATION WAGON")

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.view.ViewGroup[@resource-id="insure.agencify.agencify:id/layoutInfo"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '(//android.widget.ImageButton[@resource-id="insure.agencify.agencify:id/text_input_end_icon"])[4]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@text="2024"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="SET"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/next"]')))
        el.click()

        self.quote_comparison_screen()

    def quote_comparison_screen(self):
        el = WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(
            (By.XPATH, '(//android.widget.Button[@resource-id="insure.agencify.agencify:id/viewnext"])[1]')))
        el.click()

        self.quote_details_screen()

    def quote_details_screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/buy"]')))
        el.click()

        self.complete_schedules_details_screen()

    def complete_schedules_details_screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.Button[@resource-id="insure.agencify.agencify:id/btn_close_dialog_amend_cover_date"]')))  # Got it dialogue pop up
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.Button[@resource-id="insure.agencify.agencify:id/addClien"]')))  # Select a client button
        el.click()

        self.select_client_pullup_screen()

    def select_client_pullup_screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '(//android.widget.RadioButton[@resource-id="insure.agencify.agencify:id/radiobutton"])[3]')))
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Continue"]')
        el.click()

    if __name__ == '__main__':
        unittest.main()
