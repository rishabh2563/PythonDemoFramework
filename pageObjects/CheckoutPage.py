from selenium.webdriver.common.by import By

from pageObjects.ConfimationPage import ConfirmationPage


class CheckoutPage:
    products = (By.XPATH, '//div[@class="card h-100"]//h4//a')
    cartbtn = (By.XPATH, '//div[@class="card h-100"]//div/button')
    checkbtn = (By.XPATH, '//a[contains(text(),"Checkout")]')
    coutscsbtn = (By.XPATH, '//button[contains(text(),"Checkout")]')

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        return self.driver.find_elements(*CheckoutPage.products)
        # products = self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]//h4//a')

    def addtocart(self):
        return self.driver.find_element(*CheckoutPage.cartbtn)

    # self.driver.find_element(By.XPATH, '//div[@class="card h-100"]//div/button')

    def checkoutbtn(self):
        self.driver.find_element(*CheckoutPage.checkbtn).click()

    #  self.driver.find_element(By.XPATH, '//a[contains(text(),"Checkout")]')

    def checkoutsuccessbtn(self):
        self.driver.find_element(*CheckoutPage.coutscsbtn).click()
        confirmpage = ConfirmationPage(self.driver)
        return confirmpage
    # self.driver.find_element(By.XPATH, '//button[contains(text(),"Checkout")]')


