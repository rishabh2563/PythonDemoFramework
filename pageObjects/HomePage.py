from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage():
    shop = (By.XPATH, '//a[text()="Shop"]')
    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    password = (By.XPATH, '//input[@id="exampleInputPassword1"]')
    checkbox = (By.XPATH, '//label[text()="Check me out if you Love IceCreams!"]')
    dropdown = (By.XPATH, '//select[@id="exampleFormControlSelect1"]')
    status = (By.XPATH, '//label[text()="Student"]')
    dob = (By.XPATH, '//input[@name="bday"]')
    submitbtn = (By.CSS_SELECTOR, 'input[type="submit"]')

    def __init__(self, driver):
        self.driver = driver

    def shopitem(self):
        self.driver.find_element(*HomePage.shop).click()

    # self.driver.find_element_by_xpath('//a[text()="Shop"]').click()

    def get_name(self, username):
        self.driver.find_element(*HomePage.name).send_keys(username)

    def get_email(self, email):
        self.driver.find_element(*HomePage.email).send_keys(email)

    def get_password(self, password):
        self.driver.find_element(*HomePage.password).send_keys(password)

    def get_checkbox(self):
        self.driver.find_element(*HomePage.checkbox).click()

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_status(self):
        return self.driver.find_element(*HomePage.status)

    def get_dob(self, dob):
        self.driver.find_element(*HomePage.dob).send_keys(dob)

    def get_submitbtn(self):
        self.driver.find_element(*HomePage.submitbtn).click()
