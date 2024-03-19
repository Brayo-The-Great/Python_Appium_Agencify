import unittest
from time import sleep
from typing import Any, Dict
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
    platformVersion='13.0',
    deviceName='OPPO CPH2473',
    language='en',
    locale='US',
    autoGrantPermissions='true',
    app=r'C:\Users\PC\Desktop\TESTAPKs\staging20348.apk'

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

        el = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Login"]')))
        el.click()

        self.create_quote()

    def create_quote(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '(//android.widget.ImageView['
                       '@resource-id="insure.agencify.agencify:id/navigation_bar_item_icon_view'
                       '"])[4]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Motor Private"]')))
        el.click()

        el = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="COMP"]')))
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[1]').send_keys(
            "KQA 324S")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[2]').send_keys(
            "3000000")
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.view.View[''1]/android.widget'
                                            '.EditText/android.widget.Button')
        el.click()
        self.driver.implicitly_wait(60)

        current_date = datetime.now().strftime('%a, %d %b')  # Format like 'Wed, 28 Feb'
        xpath = f'//android.widget.TextView[@content-desc="{current_date}"]'
        el = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        el.click()

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()
        self.driver.implicitly_wait(30)

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Continue"]')
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Make"]'))).send_keys("BMW")
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.view.ViewGroup[@resource-id="insure.agencify.agencify:id/layoutInfo"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.AutoCompleteTextView[@resource-id="insure.agencify.agencify:id/model"]'))).send_keys(
            "X7")
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Body type"]'))).send_keys("STATION WAGON")
        el.click()

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

        el = WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(
            (By.XPATH, '(//android.widget.Button[@resource-id="insure.agencify.agencify:id/viewnext"])[1]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/buy"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.Button[@resource-id="insure.agencify.agencify:id/btn_close_dialog_amend_cover_date"]')))  # Got it dialogue pop up
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.Button[@resource-id="insure.agencify.agencify:id/addClien"]')))  # Select a client button
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.Button[@resource-id="insure.agencify.agencify:id/addClient"]')))  # New client button
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.ImageButton[@content-desc="Show drop-down menu"]')))  # Client Type button
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/firstName"]')))  # Individual button
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/firstName"]'))).send_keys(
            "QA")  # First Name

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/last_name"]'))).send_keys(
            "ONE")  # Last Name

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/mobile"]'))).send_keys(
            "0759404954")  # Mobile Number

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/id_no"]'))).send_keys(
            "64775697")  # National ID

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/pin"]'))).send_keys(
            "A865356896J")  # KRA PIN

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/email"]'))).send_keys(
            "waititubrian9@gmail.com")  # Email

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.RadioButton[@resource-id="insure.agencify.agencify:id/male"]')))  # Gender - Male
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.Button[@resource-id="insure.agencify.agencify:id/save_client"]')))  # Save button
        el.click()

        # user_input = input("Please enter the code sent to your phone number: ")
        # code = user_input  # Example code
        # if len(user_input) != 4:
        #     print("Error: The code should be exactly 4 characters long.")
        #     exit()
        #
        # print(f"Entering OTP: {code}")
        #
        # # Assuming this is the correct way to fetch the elements, adjust if needed
        # element1 = self.driver.find_element(By.XPATH,
        #                                     '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View')
        # element2 = self.driver.find_element(By.XPATH,
        #                                     '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View')
        # element3 = self.driver.find_element(By.XPATH,
        #                                     '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[3]/android.view.View')
        # element4 = self.driver.find_element(By.XPATH,
        #                                     '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[4]/android.view.View')
        #
        # # Sending the code to each input field
        # element1.send_keys(code[0])
        # # Add a short delay between entering each digit, adjust if needed
        # time.sleep(1)
        # element2.send_keys(code[1])
        # time.sleep(1)
        # element3.send_keys(code[2])
        # time.sleep(1)
        # element4.send_keys(code[3])



if __name__ == '__main__':
    unittest.main()
