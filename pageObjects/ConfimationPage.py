from selenium.webdriver.common.by import By


class ConfirmationPage:
    country = (By.ID, 'country')
    countrysel = (By.LINK_TEXT, 'India')
    checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchasebtn = (By.XPATH, '//input[@class="btn btn-success btn-lg"]')
    successmsg = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')

    def __init__(self, driver):
        self.driver = driver

    def getcountry(self, countryname):
        self.driver.find_element(*ConfirmationPage.country).send_keys(countryname)
         #self.driver.find_element(By.ID, 'country')

    def selectcountry(self):
        self.driver.find_element(*ConfirmationPage.countrysel).click()
    # self.driver.find_element_by_link_text('India')

    def checkboxbtn(self):
        self.driver.find_element(*ConfirmationPage.checkbox).click()
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def getpurchasebtn(self):
        self.driver.find_element(*ConfirmationPage.purchasebtn).click()
    # self.driver.find_element(By.XPATH, '//input[@class="btn btn-success btn-lg"]')

    def get_successmsg(self):
        successtext = self.driver.find_element(*ConfirmationPage.successmsg).text
        return successtext
