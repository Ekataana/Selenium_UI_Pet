from pages.profile_page import ProfilePage
import time

link = 'http://34.141.58.52:8080/#/profile'


def test_create_new_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.create_new_pet()
    time.sleep(2)


def test_edit_pet_info(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.edit_pet_info()
    time.sleep(2)


def test_delete_pet(browser):
    page = ProfilePage(browser, link)
    page.open()
    page.delete_pet()

