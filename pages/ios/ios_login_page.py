from abc import ABC

from appium import webdriver

from pages.login_page import LoginPage

USERNAME_FIELD = "ios_username"
PASSWORD_FIELD = "ios_password"
ERROR_MESSAGE = "ios_error_message"
LOGIN_BUTTON = "ios_login_button"


class IOSLoginPage(LoginPage, ABC):

    def __init__(self):
        desired_caps = {
            "deviceName": "iPhone XR",
            "platformName": "iOS",
            "version": "12.1",
            "app": "https://testingbot.com/appium/sample.ipa",
            "realDevice": True
        }

        self.driver = webdriver.Remote("https://key:secret@hub.testingbot.com/wd/hub", desired_caps)

    def enter_username(self, username):
        self.driver.find_element(by="id", value=USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by="id", value=PASSWORD_FIELD).send_keys(password)

    def press_login_button(self):
        self.driver.find_element(by="id", value=LOGIN_BUTTON).click()

    def check_error_message(self, expected_error_message):
        actual_error_message = self.driver.find_element(by="id", value=ERROR_MESSAGE).text
        assert actual_error_message == expected_error_message, "Error message check error"

    def check_page_title(self, expected_page_title):
        actual_page_title = self.driver.title
        assert actual_page_title == expected_page_title, "Page title check error"

    def check_login_button_disabled(self):
        is_enabled = self.driver.find_element(by="id", value=LOGIN_BUTTON).is_enabled()
        assert not is_enabled, "login button assert fail"
