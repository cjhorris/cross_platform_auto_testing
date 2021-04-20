from behave import *

from pages.android.android_login_page import AndroidLoginPage
from pages.ios.ios_login_page import IOSLoginPage
from pages.web.web_login_page import WebLoginPage


@step('LoginPage initialize platform "{platform}"')
def login_page_initialize_platform(context, platform):
    context.login_page = {
        'ios': IOSLoginPage(),
        'android': AndroidLoginPage(),
        'web': WebLoginPage()
    }[platform]


@step('LoginPage I enter username "{username}"')
def login_page_enter_username(context, username):
    context.login_page.enter_username(username)


@step('LoginPage I enter password "{password}"')
def login_page_enter_password(context, password):
    context.login_page.enter_password(password)


@when("LoginPage I press login button")
def login_page_press_login_button(context):
    context.login_page.press_login_button()


@then("LoginPage I can login successfully")
def login_page_check_page_title(context):
    context.login_page.check_page_title("Landing Page")


@then('LoginPage I check error message "{error_message}"')
def login_page_check_error_message(context, error_message):
    context.login_page.check_error_message(error_message)


@then("LoginPage I can see submit button is disabled")
def login_page_check_submit_button_disabled(context):
    context.login_page.check_login_button_disabled()
