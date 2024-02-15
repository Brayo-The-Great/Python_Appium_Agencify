import unittest
from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    platformVersion='13.0',
    deviceName='OPPO CPH2473',
    language='en',
    locale='US',
    app=r'C:\Users\PC\Desktop\TESTAPKs\staging20348.apk'

)

appium_server_url = 'http://localhost:4723'

# driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_launch_app(self) -> None:
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, 'Agencify')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="insure.agencify.agencify:id/collapse_button"]')
        el.click()


if __name__ == '__main__':
        unittest.main()

# driver.quit()