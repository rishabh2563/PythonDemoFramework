import allure
from selenium.webdriver.support.select import Select
from Utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage


class Testone(BaseClass):
    @allure.step("Fill the datails in form")
    def test_form_filling(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        homepage.get_name("Rishabh")
        homepage.get_email("rt42@email.com")
        homepage.get_password("Test@321")
        homepage.get_checkbox()
        sel = Select(homepage.get_dropdown())
        sel.select_by_visible_text("Male")
        homepage.get_status().click()
        homepage.get_dob("12/10/1996")
        homepage.get_submitbtn()
        homepage.shopitem()

    @allure.step("Adding item to cart and purchasing it!")
    def test_shop_items(self):
        log = self.getlogger()
        log.info("getting all card titles")
        checkout = CheckoutPage(self.driver)
        products = checkout.checkout()
        for product in products:
            productname = product.text
            log.info(productname)
            if productname == "Blackberry":
                checkout.addtocart()
        checkout.checkoutbtn()
        confirmpage = checkout.checkoutsuccessbtn()
        log.info("Entering country name as IND")
        confirmpage.getcountry("Ind")
        self.verifyelementpresence("India")
        confirmpage.selectcountry()
        confirmpage.checkboxbtn()
        confirmpage.getpurchasebtn()
        log.info("Text recieved from application is" + confirmpage.get_successmsg())
        assert "Thank you! Yourhjsdahashsahjsadk" in confirmpage.get_successmsg()
