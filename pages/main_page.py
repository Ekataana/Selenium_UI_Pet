import time

from selenium.webdriver import Keys

from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def go_to_register_page(self):
        register_button = self.browser.find_element(*MainPageLocators.REGISTER_BUTTON)
        register_button.click()

    def filter_by_pet_type(self):
        pet_type_filter = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_TYPE_BUTTON)
        pet_type_filter.click()
        pet_type_dog_filter = self.browser.find_element(*MainPageLocators.DOG_PET_TYPE_FILTER)
        pet_type_dog_filter.click()

    def filter_by_pet_name(self):
        pet_name_input = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name_input.send_keys('Rosi')
        pet_name_input.send_keys(Keys.RETURN)

    def like_for_coco(self):
        pet_name_input = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name_input.send_keys('Coco')
        pet_name_input.send_keys(Keys.RETURN)
        time.sleep(2)
        like_button = self.browser.find_element(*MainPageLocators.LIKE_FOR_PET_BUTTON)
        like_button.click()

