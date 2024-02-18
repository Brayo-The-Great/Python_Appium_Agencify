import unittest
from time import sleep
from typing import Any, Dict
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    platformVersion='13.0',
    deviceName='OPPO CPH2473',
    language='en',
    locale='US',
    autoGrantPermissions='true',
    app=r'C:\Users\PC\Desktop\TESTAPKs\20350.apk'

)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_agencify_staging_app(self) -> None:
        self.user_login()

    def user_login(self):
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Login"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Email"]').send_keys(
            "eva.mutuku@agencify.insure")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Password"]').send_keys("123456789")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Login"]')
        el.click()
        self.driver.implicitly_wait(60)

        self.create_quote()

    def create_quote(self):
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='(//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/navigation_bar_item_icon_view"])[4]')
        el.click()
        self.driver.implicitly_wait(60)

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Motor Private"]')
        el.click()
        self.driver.implicitly_wait(60)

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="COMP"]')
        el.click()
        self.driver.implicitly_wait(60)

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[1]').send_keys(
            "KQA 324S")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[2]').send_keys(
            "3000000")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.view.View[1]/android.widget.EditText/android.widget.Button')
        el.click()
        self.driver.implicitly_wait(60)

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Sun, Feb 18"]')
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
        self.driver.implicitly_wait(30)

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Continue"]')
        el.click()
        self.driver.implicitly_wait(90)


if __name__ == '__main__':
    unittest.main()
