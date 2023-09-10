import time

from pages.main_page import MainPage

link = 'http://34.141.58.52:8080/#/'


def test_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result5m.png')


def test_go_to_register_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    browser.save_screenshot('result5ma.png')


def test_filter_by_pet_type(browser):
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_type()
    time.sleep(2)
    browser.save_screenshot('result6m.png')


def test_filter_by_pet_name(browser):
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_name()
    time.sleep(2)
    browser.save_screenshot('result7m.png')


def test_like_for_coco(browser):
    page = MainPage(browser, link)
    page.open()
    page.like_for_coco()
    time.sleep(2)
    browser.save_screenshot('result8m.png')