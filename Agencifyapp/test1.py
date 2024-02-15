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
    app=r'C:\Users\PC\Desktop\TESTAPKs\20350.apk'

)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))



class TestAppium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def wait(self):
        driver.implicitly_wait(50)
        wait = WebDriverWait(self.driver, 60, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                                    NoSuchElementException])
        el = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.android.permission-controller:id"
                                                                     "/permission_allow_button")))

    def test_launch_app(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Agencify')
        el.click()

    def click_collapse_button(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                      value='//insure.agencify.agencify:id/collapse_button')
        el.click()

    def click_login_btn(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//androidx.compose.ui.platform.ComposeView/android.view.View/android'
                                            '.view.View/android.view.View[2]/android.widget.Button]')
        el.click()


driver.quit()
