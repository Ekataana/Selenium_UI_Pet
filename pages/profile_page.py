import time

from selenium.webdriver.common.devtools.v113 import browser

from .base_page import BasePage
from .locators import ProfilePageLocators, NewPetLocators, EditPetPage


class ProfilePage(BasePage):
    def create_new_pet(self):
        add_new_pet_button = self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON)
        add_new_pet_button.click()
        pet_name = self.browser.find_element(*NewPetLocators.PET_NAME)
        pet_name.send_keys('Baron')
        pet_type = self.browser.find_element(*NewPetLocators.PET_TYPE)
        pet_type.click()
        cat_pet_type = self.browser.find_element(*NewPetLocators.CAT_PET_TYPE)
        cat_pet_type.click()
        submit_button = self.browser.find_element(*NewPetLocators.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(3)
        pet_photo = self.browser.find_element(*NewPetLocators.UPLOAD_PET_PHOTO_BUTTON)
        pet_photo.click().send_keys(r"D:\STUDY\AQApython\Selenium_UI_Pet\baron.png")
        create_new_pet = self.browser.find_element(*NewPetLocators.FILE_UPLOAD_BUTTON)
        create_new_pet.click()
        time.sleep(2)
        browser.save_screenshot("result8.png")

    def edit_pet_info(self):
        edit_pet_button = self.browser.find_element(*ProfilePageLocators.EDIT_PET_BUTTON)
        edit_pet_button.click()
        edit_pet_age = self.browser.find_element(*EditPetPage.INPUT_AGE)
        edit_pet_age.send_keys('5')
        save_button = self.browser.find_element(*EditPetPage.SAVE_BUTTON)
        save_button.submit()
        browser.save_screenshot('result9.png')

    def delete_pet(self):
        delete_pet_button = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BUTTON)
        delete_pet_button.click()
        accept_pet_delete = self.browser.find_element(*ProfilePageLocators.PET_DELETE_ACCEPTION)
        accept_pet_delete.click()
        browser.save_screenshot('result10.png')



