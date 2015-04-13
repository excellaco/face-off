# Helper methods to consolidate steps.py
def login(context, username, password):
    context.browser.find_element_by_name('signIn').click()
    context.browser.find_element_by_name('login').send_keys(username)
    context.browser.find_element_by_name('password').send_keys(password)
    context.browser.find_element_by_class_name('yj-btn').click()


def click_card(driver, index):
    driver.find_element_by_id('colleague' + str(index)).click()


def get_card(driver, index):
    return driver.find_element_by_id('colleague' + str(index))