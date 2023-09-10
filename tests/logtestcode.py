# def test_go_to_login_email(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.go_to_login_email()
#
#
# def test_go_to_login_pass(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.go_to_login_pass()
#
#
# def test_go_to_login_button(browser):
#     page = LoginPage(browser, link)
#     page.open()
#     page.go_to_login_button()
#
#     time.sleep(1)
#     browser.save_screenshot('result6.png')

# def test_check_pets(browser):
#     test_go_to_login(browser)
#     link = 'http://34.141.58.52:8080/#/profile'
#     page = PetPage(browser, link)
#     page.open()
#     time.sleep(1)
#     # assert len(pets) == 4
#     browser.save_screenshot('result7.png')


# def test_add_new_pet_button(browser):
#     test_go_to_login(browser)
#     link = 'http://34.141.58.52:8080/#/profile'
#     page = PetPage(browser, link)
#     page.open()
#     page.add_new_pet_button()
#     time.sleep(1)
#     browser.save_screenshot('result8.png')