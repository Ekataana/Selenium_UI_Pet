from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):

    def go_to_register_new_user_login(self):
        login_data = self.browser.find_element(*RegisterPageLocators.LOGIN_NEW_USER)
        login_data.send_keys('bony666@gmail.com')

    def go_to_register_new_user_pass(self):
        password_data = self.browser.find_element(*RegisterPageLocators.PASSWORD_NEW_USER)
        password_data.send_keys('159753')

    def go_to_register_new_user_pass_confirm(self):
        confirm_pass = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        confirm_pass.send_keys('159753')

    def go_to_register_new_user_submit_button(self):
        submit_button = self.browser.find_element(*RegisterPageLocators.SUBMIT_BUTTON)
        submit_button.submit()
