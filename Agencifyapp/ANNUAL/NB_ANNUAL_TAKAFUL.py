import unittest
from datetime import time
import random
import string

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    platformVersion='14.0',
    deviceName='emulator-5554',
    language='en',
    locale='US',
    autoGrantPermissions='true',
    app=r'/Users/brianwaititumuraya/Documents/TESTAPKs/app (2).apk',
    enableMultiWindows=True,
    unicodeKeyboard=False,
    resetKeyboard=False

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

        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Password"]').send_keys("12345678")

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
        risk_id = self.generate_unique_sequence()
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[1]').send_keys(
            risk_id)
        el = self.driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.widget.ScrollView/android.widget.EditText[2]').send_keys(
            "2500000")
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
            (By.XPATH, '//*[@text="Make"]'))).send_keys("TOYOTA")

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.AutoCompleteTextView[@resource-id="insure.agencify.agencify:id/model"]'))).send_keys(
            "CROWN")

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Body type"]'))).send_keys("SEDAN")

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '(//android.widget.ImageButton[@resource-id="insure.agencify.agencify:id/text_input_end_icon"])[4]')))
        el.click()

        # self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="SET"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/next"]')))
        el.click()

        self.quote_comparison_screen()

    def quote_comparison_screen(self):
        el = WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(
            (By.XPATH, '(//android.widget.Button[@resource-id="insure.agencify.agencify:id/viewnext"])[2]')))
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
        search_xpath = '//android.widget.AutoCompleteTextView[@resource-id="insure.agencify.agencify:id/search_src_text"]'
        element = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, search_xpath)))
        element.click()
        action = ActionChains(self.driver)
        action.send_keys("mur").perform()

        el = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="QQ"]')))
        el.click()
        self.driver.hide_keyboard()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/link"]')))  # Continue Button
        el.click()

        self.Quote_Schedule_Screen()

    def Quote_Schedule_Screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Schedules"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Basic info"]')))
        el.click()

        self.Schedule_basic_info_screen()

    def Schedule_basic_info_screen(self):
        log_book_no = self.generate_random_string(10)  # Generating log book number
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/logBookNo"]'))).send_keys(
            log_book_no)  # Log book no

        chassis_no = self.generate_random_string(10)  # Generating chassis number
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/chassis"]'))).send_keys(
            chassis_no)  # Chassis no

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/colorTxt"]'))).send_keys(
            "Black")  # Color

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/sittingTxt"]'))).send_keys(
            "8")  # Sitting capacity

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/cubicTxt"]'))).send_keys(
            "2000")  # Cubic capacity

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.EditText[@resource-id="insure.agencify.agencify:id/yearReg"]')))  # Year of registration
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="SET"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/btnContinue"]')))  # Continue
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Save"]')))
        el.click()

        self.Valuer_Information_Screen()

    def Valuer_Information_Screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Valuer Information"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Head Office"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Continue"]')))
        el.click()

        self.Documents_Uploads_Screen()

    def Documents_Uploads_Screen(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Documents"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.FrameLayout[@resource-id="insure.agencify.agencify:id/nav_host_fragment"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[1]')))  # Driving License
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/btn_camera"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.FrameLayout[@resource-id="insure.agencify.agencify:id/nav_host_fragment"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[2]')))  # Logbook
        el.click()
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/btn_camera"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.FrameLayout[@resource-id="insure.agencify.agencify:id/nav_host_fragment"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[3]')))  # National ID
        el.click()
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/btn_camera"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')))
        el.click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.FrameLayout[@resource-id="insure.agencify.agencify:id/nav_host_fragment"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[3]')))  # Backside of National ID
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/btn_camera"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH,
             '//android.widget.FrameLayout[@resource-id="insure.agencify.agencify:id/nav_host_fragment"]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View[4]')))  # KRA PIN
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/btn_camera"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@content-desc="Shutter"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageButton[@content-desc="Done"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Continue"]')))
        el.click()

        self.Payment_Consent()

    def Payment_Consent(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Continue to payment"]')))
        el.click()

        element_xpath = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[1]/android.view.View'
        element = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element.click()
        action = ActionChains(self.driver)
        action.send_keys("1").perform()

        element_xpath = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[2]/android.view.View'
        element = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element.click()
        action = ActionChains(self.driver)
        action.send_keys("0").perform()

        element_xpath = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[3]/android.view.View'
        element = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element.click()
        action = ActionChains(self.driver)
        action.send_keys("1").perform()

        element_xpath = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[4]/android.view.View'
        element = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element.click()
        action = ActionChains(self.driver)
        action.send_keys("0").perform()

        self.Make_Payment()

    def Make_Payment(self):
        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@text="Continue"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.ImageView[@resource-id="insure.agencify.agencify:id/icShare"]')))
        el.click()

        el = WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="insure.agencify.agencify:id/pay"]')))
        el.click()

        # Set to store generated random strings

    generated_strings = set()

    # Set to store generated sequences
    existing_sequences = set()

    @staticmethod
    def generate_unique_sequence():
        while True:
            # Generate random characters
            first_letter = 'K'
            second_letter = random.choice(string.ascii_uppercase)
            third_letter = random.choice(string.ascii_uppercase)
            digits = ''.join(random.choices(string.digits, k=3))
            fourth_letter = random.choice(string.ascii_uppercase)

            sequence = f"{first_letter}{second_letter}{third_letter} {digits}{fourth_letter}"

            # Check if the generated sequence is unique
            if sequence not in TestAppium.existing_sequences:
                TestAppium.existing_sequences.add(sequence)
                return sequence

    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

    if __name__ == '__main__':
        unittest.main()
