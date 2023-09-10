import time
from pages.login_page import LoginPage

login_link = 'http://34.141.58.52:8080/#/login'


def test_go_to_login(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.go_to_login_email()
    page.go_to_login_pass()
    page.go_to_login_button()
    time.sleep(1)
    browser.save_screenshot('result6.png')


# def test_go_to_register_page(browser):
#     page = LoginPage(browser, login_link)
#     page.open()
#     page.go_to_register_page()
#     time.sleep(1)
#     browser.save_screenshot('result6a.png')
