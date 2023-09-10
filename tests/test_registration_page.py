from pages.registration_page import RegisterPage
import time

register_link = 'http://34.141.58.52:8080/#/register'


def test_go_to_register_new_user(browser):
    page = RegisterPage(browser, register_link)
    page.open()
    page.go_to_register_new_user_login()
    page.go_to_register_new_user_pass()
    page.go_to_register_new_user_pass_confirm()
    page.go_to_register_new_user_submit_button()
    time.sleep(1)
    browser.save_screenshot('result_r.png')