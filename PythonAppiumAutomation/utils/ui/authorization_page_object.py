import time
from typing import Final

from utils.ui.main_page_object import MainPageObject


class AuthorizationPageObject(MainPageObject):
    login_button: Final = "xpath://body/div[4]/div[2]/a[text() = 'Log in']"
    login_input: Final = "css:input[name='wpName']"
    password_input: Final = "css:input[name='wpPassword']"
    submit_button: Final = "css:button#wpLoginAttempt"

    def __init__(self, driver):
        super().__init__(driver)

    def click_auth_button(self):
        self.wait_for_element_present(
            locator=self.login_button,
            error_message="Cannot find auth button"
        )
        time.sleep(1)
        self.wait_for_element_and_click(
            locator=self.login_button,
            error_message="Cannot find and click auth button"
        )

    def enter_login_data(self, login, password):
        self.wait_for_element_and_send_keys(
            locator=self.login_input,
            value=login,
            error_message="Cannot find and put login to the login input."
        )

        self.wait_for_element_and_send_keys(
            locator=self.password_input,
            value=password,
            error_message="Cannot find and put password to the password input."
        )

    def submit_form(self):
        self.wait_for_element_and_click(
            locator=self.submit_button,
            error_message="Cannot find and click auth button.",
            timeout_in_sec=15
        )
