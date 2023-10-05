from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a')
    FILTER_BY_PET_TYPE_BUTTON = (By.ID, 'typesSelector')
    DOG_PET_TYPE_FILTER = (By.ID, 'pv_id_2_0')
    FILTER_BY_PET_NAME = (By.ID, 'petName')
    LIKE_FOR_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div/div/div[3]/div[2]/span[1]/i')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="pv_id_2_content"]/div/form/div[3]/button/span[2]')
    MENUBAR_BUTTON = (By.CLASS_NAME, 'p-menubar-button')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a')


class RegisterPageLocators:
    LOGIN_NEW_USER = (By.XPATH, '//*[@id="login"]')
    PASSWORD_NEW_USER = (By.XPATH, '//*[@id="password"]/input')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="confirm_password"]/input')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div[1]/main/fieldset/div/div/form/div[4]/button')


class ProfilePageLocators:
    BARON_PET = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:nth-child(1) > div')
    ROSI_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[2]/div')
    LUCKY_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[3]/div')
    BELLIS_PET = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[4]/div')
    ADD_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    EDIT_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
    DELETE_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[5]/div/div[2]/button[2]')
    PET_DELETE_ACCEPTION = (By.CLASS_NAME, 'p-button p-component p-confirm-popup-accept p-button-sm')


class NewPetLocators:
    PET_NAME = (By.CSS_SELECTOR, 'document.querySelector("#name")')
    PET_TYPE = (By.XPATH, '//*[@id="pv_id_18"]/div/span')
    CAT_PET_TYPE = (By.ID, 'pv_id_18_1')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    UPLOAD_PET_PHOTO_BUTTON = (By.CLASS_NAME, 'p-button p-component p-fileupload-choose')
    FILE_UPLOAD_BUTTON = (By.CLASS_NAME, 'p-button p-component p-fileupload-choose p-fileupload-choose-selected')


class EditPetPage:
    INPUT_AGE = (By.CSS_SELECTOR, "#age > input")
    SAVE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')
